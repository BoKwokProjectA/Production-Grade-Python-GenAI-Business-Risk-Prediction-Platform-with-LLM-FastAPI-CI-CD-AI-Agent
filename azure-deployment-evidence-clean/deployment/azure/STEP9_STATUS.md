# Step 9 Azure Endpoint Test Status

Azure Container App:
- isic-api-azure

Azure URL:
- https://isic-api-azure.livelybeach-7ed547b8.uksouth.azurecontainerapps.io

Current result:
- /api/v1/health returned HTTP 200
- Uvicorn is now running successfully
- Previous issue  was fixed by rebuilding and deploying image tag azure-demo-v2

Still required before README main URL update:
- /
- /docs
- /openapi.json
- /api/v1/chat
- /api/v1/predict

GCP Cloud Run remains unchanged.
README has not been updated yet.
