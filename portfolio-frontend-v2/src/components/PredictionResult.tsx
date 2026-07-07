import type { PredictionResponse } from "../types/api";

interface PredictionResultProps {
  result: PredictionResponse;
  imageName: string;
}

function formatProbability(probability: number) {
  return `${(probability * 100).toFixed(2)}%`;
}

function formatDate(timestamp: string) {
  const date = new Date(timestamp);

  if (Number.isNaN(date.getTime())) {
    return timestamp;
  }

  return date.toLocaleString();
}

export function PredictionResult({ result, imageName }: PredictionResultProps) {
  const normalizedPrediction = result.prediction.toLowerCase();
  const isMalignant = normalizedPrediction.includes("malignant");

  return (
    <div className="mt-6 rounded-3xl border border-slate-200 bg-slate-50 p-5">
      <div className="mb-4 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <p className="text-sm font-semibold text-slate-500">Risk scoring result</p>
          <h3 className="mt-1 text-2xl font-black text-slate-950">
            {isMalignant ? "Higher-risk label" : "Lower-risk label"}
          </h3>
        </div>

        <span
          className={`inline-flex w-fit rounded-full px-4 py-2 text-sm font-black uppercase tracking-wide ${
            isMalignant
              ? "bg-rose-100 text-rose-700"
              : "bg-emerald-100 text-emerald-700"
          }`}
        >
          {result.prediction}
        </span>
      </div>

      <div className="mb-5">
        <div className="mb-2 flex items-center justify-between text-sm">
          <span className="font-semibold text-slate-600">Risk score</span>
          <span className="font-black text-slate-950">{formatProbability(result.probability)}</span>
        </div>
        <div className="h-3 overflow-hidden rounded-full bg-white">
          <div
            className={`h-full rounded-full ${isMalignant ? "bg-rose-500" : "bg-emerald-500"}`}
            style={{ width: `${Math.min(Math.max(result.probability * 100, 0), 100)}%` }}
          />
        </div>
      </div>

      <dl className="grid gap-3 text-sm sm:grid-cols-2">
        <div className="rounded-2xl bg-white p-4">
          <dt className="font-semibold text-slate-500">Uploaded file name</dt>
          <dd className="mt-1 break-all font-bold text-slate-950">{imageName}</dd>
        </div>
        <div className="rounded-2xl bg-white p-4">
          <dt className="font-semibold text-slate-500">Backend file ID</dt>
          <dd className="mt-1 break-all font-bold text-slate-950">{result.isic_id}</dd>
        </div>
        <div className="rounded-2xl bg-white p-4">
          <dt className="font-semibold text-slate-500">Model version</dt>
          <dd className="mt-1 font-bold text-slate-950">{result.model_version}</dd>
        </div>
        <div className="rounded-2xl bg-white p-4">
          <dt className="font-semibold text-slate-500">Timestamp</dt>
          <dd className="mt-1 font-bold text-slate-950">{formatDate(result.timestamp)}</dd>
        </div>
      </dl>

      <p className="mt-4 text-xs leading-5 text-slate-500">
        This is a model output from a portfolio API. It is not a professional assessment or automated decision.
      </p>
    </div>
  );
}
