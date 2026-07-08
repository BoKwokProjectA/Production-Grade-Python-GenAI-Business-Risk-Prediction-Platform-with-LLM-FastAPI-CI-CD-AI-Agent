export const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL?.replace(/\/$/, "") || "http://localhost:8000";

export const PROJECT_LINKS = {
  backendApi: API_BASE_URL,
  swaggerDocs: `${API_BASE_URL}/docs`,
  openApiSchema: `${API_BASE_URL}/openapi.json`,
  githubRepo: "https://github.com/BoKwokProjectA/Production-Grade-Python-GenAI-Business-Risk-Prediction-Platform-with-LLM-FastAPI-CI-CD-AI-Agent",
  frontendDemo: "https://production-grade-python-gen-ai-busi.vercel.app",
};

export const ACCEPTED_IMAGE_TYPES = ["image/jpeg", "image/png", "image/webp"];

export const MAX_UPLOAD_SIZE_MB = 10;
export const MAX_UPLOAD_SIZE_BYTES = MAX_UPLOAD_SIZE_MB * 1024 * 1024;
