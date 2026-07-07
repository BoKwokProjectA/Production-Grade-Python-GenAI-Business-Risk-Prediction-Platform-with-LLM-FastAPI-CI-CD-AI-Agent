export type PredictionLabel = "benign" | "malignant" | "Benign" | "Malignant" | string;

export interface PredictionResponse {
  isic_id: string;
  probability: number;
  prediction: PredictionLabel;
  model_version: string;
  timestamp: string;
}

export interface HealthResponse {
  status: string;
  model_version?: string;
  api_version?: string;
  service?: string;
  timestamp?: string;
  [key: string]: unknown;
}

export interface ApiErrorResponse {
  detail?: string | { msg?: string }[] | Record<string, unknown>;
  message?: string;
}
