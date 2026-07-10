#!/usr/bin/env bash

# Azure Container Apps deployment command record
# Project: AI Medical Image Risk Prediction Portfolio API
# Safe for GitHub: no real secrets are stored in this file.

LOCATION="uksouth"
RG="rg-isic-aca-demo-uks"
ACR_NAME="isicapiacrhp7lku"
APP_NAME="isic-api-azure"
ENV_NAME="aca-env-isic-demo-uks"
LOG_WORKSPACE="law-isic-aca-demo-uks"
IDENTITY_NAME="id-isic-aca-pull"
IMAGE_NAME="isic-api"
IMAGE_TAG="azure-demo-v2"

ACR_LOGIN_SERVER=$(az acr show \
  --name "$ACR_NAME" \
  --resource-group "$RG" \
  --query loginServer \
  -o tsv)

IDENTITY_ID=$(az identity show \
  --name "$IDENTITY_NAME" \
  --resource-group "$RG" \
  --query id \
  -o tsv)

FULL_IMAGE_NAME="$ACR_LOGIN_SERVER/$IMAGE_NAME:$IMAGE_TAG"

# Secrets must be supplied at runtime only.
SECRET_KEY="<set-at-runtime-not-committed>"
POWER_AUTOMATE_URL="<set-at-runtime-not-committed>"

# Check Azure account and existing resources.
az account show --output table

az group show \
  --name "$RG" \
  --output table

az acr show \
  --name "$ACR_NAME" \
  --resource-group "$RG" \
  --output table

az acr repository show-tags \
  --name "$ACR_NAME" \
  --repository "$IMAGE_NAME" \
  --output table

az identity show \
  --name "$IDENTITY_NAME" \
  --resource-group "$RG" \
  --query "{name:name, location:location, principalId:principalId}" \
  --output table

az containerapp env show \
  --name "$ENV_NAME" \
  --resource-group "$RG" \
  --query "{name:name, location:location, provisioningState:properties.provisioningState}" \
  --output table

# Container App update command used after rebuilding azure-demo-v2.
az containerapp update \
  --name "$APP_NAME" \
  --resource-group "$RG" \
  --image "$FULL_IMAGE_NAME" \
  --cpu 2.0 \
  --memory 4.0Gi \
  --min-replicas 0 \
  --max-replicas 1

# Endpoint checks.
AZURE_URL="https://isic-api-azure.livelybeach-7ed547b8.uksouth.azurecontainerapps.io"

curl -i "$AZURE_URL/"
curl -I "$AZURE_URL/docs"
curl -i "$AZURE_URL/openapi.json"
curl -i "$AZURE_URL/api/v1/health"
curl -i -X POST "$AZURE_URL/api/v1/chat" \
  -H "Content-Type: application/json" \
  -d '{"question":"How does the ensemble inference engine work?"}'

# Predict endpoint requires a local test image.
# Example:
# TEST_IMAGE="path/to/test_image.jpg"
# curl -i -X POST "$AZURE_URL/api/v1/predict" \
#   -F "file=@${TEST_IMAGE};type=image/jpeg"
