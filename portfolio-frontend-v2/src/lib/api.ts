import type { ApiErrorResponse, HealthResponse, PredictionResponse } from "../types/api";
import { API_BASE_URL } from "./constants";

function buildApiUrl(path: string) {
  return `${API_BASE_URL}${path}`;
}

async function parseApiError(response: Response): Promise<string> {
  try {
    const data = (await response.json()) as ApiErrorResponse;

    if (typeof data.detail === "string") {
      return data.detail;
    }

    if (Array.isArray(data.detail) && data.detail.length > 0) {
      return data.detail
        .map((item) => item.msg || JSON.stringify(item))
        .join(", ");
    }

    if (data.message) {
      return data.message;
    }

    return `API request failed with status ${response.status}`;
  } catch {
    return `API request failed with status ${response.status}`;
  }
}

export async function getHealth(): Promise<HealthResponse> {
  let response: Response;

  try {
    response = await fetch(buildApiUrl("/api/v1/health"));
  } catch {
    throw new Error(
      "Network failure while checking backend health. Check the backend URL and CORS configuration.",
    );
  }

  if (!response.ok) {
    throw new Error(await parseApiError(response));
  }

  return response.json() as Promise<HealthResponse>;
}

export async function predictImage(file: File): Promise<PredictionResponse> {
  const formData = new FormData();
  formData.append("file", file);

  let response: Response;

  try {
    response = await fetch(buildApiUrl("/api/v1/predict"), {
      method: "POST",
      body: formData,
    });
  } catch {
    throw new Error(
      "Network failure while calling the prediction API. Check your backend URL, internet connection, and CORS settings.",
    );
  }

  if (!response.ok) {
    throw new Error(await parseApiError(response));
  }

  return response.json() as Promise<PredictionResponse>;
}
