import { useEffect, useMemo, useState } from "react";
import { ImagePlus, Loader2, UploadCloud, XCircle } from "lucide-react";
import { predictImage } from "../lib/api";
import {
  ACCEPTED_IMAGE_TYPES,
  MAX_UPLOAD_SIZE_BYTES,
  MAX_UPLOAD_SIZE_MB,
} from "../lib/constants";
import type { PredictionResponse } from "../types/api";
import { PredictionResult } from "./PredictionResult";
import { SectionCard } from "./SectionCard";

function validateFile(file: File | null): string | null {
  if (!file) {
    return "Please select an image file before running prediction.";
  }

  if (!ACCEPTED_IMAGE_TYPES.includes(file.type)) {
    return "Unsupported upload. Please use a JPEG, PNG, or WebP image.";
  }

  if (file.size > MAX_UPLOAD_SIZE_BYTES) {
    return `File is too large. Please upload an image under ${MAX_UPLOAD_SIZE_MB} MB.`;
  }

  return null;
}

export function PredictionUploader() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [result, setResult] = useState<PredictionResponse | null>(null);
  const [error, setError] = useState<string>("");
  const [isLoading, setIsLoading] = useState(false);

  const previewUrl = useMemo(() => {
    if (!selectedFile) return "";
    return URL.createObjectURL(selectedFile);
  }, [selectedFile]);

  useEffect(() => {
    return () => {
      if (previewUrl) URL.revokeObjectURL(previewUrl);
    };
  }, [previewUrl]);

  function handleFileChange(event: React.ChangeEvent<HTMLInputElement>) {
    const file = event.target.files?.[0] || null;

    setSelectedFile(file);
    setResult(null);

    const validationError = validateFile(file);
    setError(validationError || "");
  }

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

    const validationError = validateFile(selectedFile);

    if (validationError) {
      setError(validationError);
      return;
    }

    setIsLoading(true);
    setError("");
    setResult(null);

    try {
      const prediction = await predictImage(selectedFile as File);
      setResult(prediction);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Unexpected prediction failure.");
    } finally {
      setIsLoading(false);
    }
  }

  function handleClear() {
    setSelectedFile(null);
    setResult(null);
    setError("");
  }

  return (
    <SectionCard
      eyebrow="Live API demo"
      title="Upload an image and call the risk scoring endpoint"
      className="scroll-mt-24"
    >
      <form id="predict" onSubmit={handleSubmit} className="grid gap-6 lg:grid-cols-[0.9fr_1.1fr]">
        <div>
          <label
            htmlFor="image-upload"
            className="flex min-h-72 cursor-pointer flex-col items-center justify-center rounded-3xl border-2 border-dashed border-slate-300 bg-slate-50 px-6 py-8 text-center transition hover:border-blue-300 hover:bg-blue-50/60"
          >
            {previewUrl ? (
              <img
                src={previewUrl}
                alt="Selected upload preview"
                className="mb-4 h-44 w-full rounded-2xl object-cover"
              />
            ) : (
              <div className="mb-4 flex h-16 w-16 items-center justify-center rounded-3xl bg-blue-100 text-blue-700">
                <ImagePlus size={30} />
              </div>
            )}

            <p className="text-base font-bold text-slate-950">
              {selectedFile ? selectedFile.name : "Choose an image for risk scoring"}
            </p>
            <p className="mt-2 max-w-sm text-sm leading-6 text-slate-500">
              Accepted formats: JPEG, PNG, WebP. Maximum recommended size: {MAX_UPLOAD_SIZE_MB} MB.
            </p>

            <input
              id="image-upload"
              type="file"
              accept={ACCEPTED_IMAGE_TYPES.join(",")}
              onChange={handleFileChange}
              className="sr-only"
            />
          </label>

          {selectedFile && (
            <button
              type="button"
              onClick={handleClear}
              className="mt-3 inline-flex items-center gap-2 text-sm font-semibold text-slate-500 hover:text-rose-600"
            >
              <XCircle size={16} />
              Clear selected image
            </button>
          )}
        </div>

        <div className="flex flex-col justify-between rounded-3xl border border-slate-200 bg-white p-5">
          <div>
            <h3 className="text-lg font-black text-slate-950">Prediction workflow</h3>
            <ol className="mt-4 space-y-3 text-sm leading-6 text-slate-600">
              <li>
                <span className="font-bold text-slate-950">1.</span> Select a supported image file for scoring.
              </li>
              <li>
                <span className="font-bold text-slate-950">2.</span> Frontend sends multipart form-data to{" "}
                <code className="rounded bg-slate-100 px-1">/api/v1/predict</code>.
              </li>
              <li>
                <span className="font-bold text-slate-950">3.</span> Backend returns label,
                probability score, model version, timestamp, and uploaded image ID.
              </li>
            </ol>

            {error && (
              <div className="mt-5 rounded-2xl border border-rose-200 bg-rose-50 p-4 text-sm font-medium leading-6 text-rose-700">
                {error}
              </div>
            )}
          </div>

          <button
            type="submit"
            disabled={isLoading}
            className="mt-6 inline-flex w-full items-center justify-center gap-2 rounded-2xl bg-blue-600 px-6 py-3 text-sm font-black text-white shadow-lg shadow-blue-600/25 transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {isLoading ? (
              <>
                <Loader2 className="animate-spin" size={18} />
                Running prediction...
              </>
            ) : (
              <>
                <UploadCloud size={18} />
                Run prediction
              </>
            )}
          </button>
        </div>
      </form>

      {result && selectedFile && (
        <PredictionResult result={result} imageName={selectedFile.name} />
      )}
    </SectionCard>
  );
}
