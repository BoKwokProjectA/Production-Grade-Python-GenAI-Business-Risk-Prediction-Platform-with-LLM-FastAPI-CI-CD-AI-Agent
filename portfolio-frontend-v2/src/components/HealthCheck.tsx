import { useEffect, useState } from "react";
import { CheckCircle2, Loader2, RefreshCw, ServerCrash } from "lucide-react";
import { getHealth } from "../lib/api";
import type { HealthResponse } from "../types/api";
import { SectionCard } from "./SectionCard";

export function HealthCheck() {
  const [health, setHealth] = useState<HealthResponse | null>(null);
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  async function loadHealth() {
    setIsLoading(true);
    setError("");

    try {
      const data = await getHealth();
      setHealth(data);
    } catch (err) {
      setHealth(null);
      setError(err instanceof Error ? err.message : "Unable to check backend health.");
    } finally {
      setIsLoading(false);
    }
  }

  useEffect(() => {
    void loadHealth();
  }, []);

  const isHealthy = health?.status?.toLowerCase().includes("healthy") || health?.status === "ok";

  return (
    <SectionCard eyebrow="Backend status" title="Production API health check" className="scroll-mt-24">
      <div id="health" className="grid gap-5 lg:grid-cols-[1fr_auto] lg:items-center">
        <div className="flex items-start gap-4">
          <div
            className={`flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl ${
              error
                ? "bg-rose-100 text-rose-700"
                : isHealthy
                  ? "bg-emerald-100 text-emerald-700"
                  : "bg-slate-100 text-slate-600"
            }`}
          >
            {isLoading ? (
              <Loader2 className="animate-spin" size={24} />
            ) : error ? (
              <ServerCrash size={24} />
            ) : (
              <CheckCircle2 size={24} />
            )}
          </div>

          <div>
            <p className="text-lg font-black text-slate-950">
              {error
                ? "Backend health check failed"
                : health
                  ? `Status: ${health.status}`
                  : "Checking backend..."}
            </p>
            <p className="mt-2 text-sm leading-6 text-slate-600">
              This section calls <code className="rounded bg-slate-100 px-1">GET /api/v1/health</code>{" "}
              from the configured deployed backend.
            </p>

            {error && (
              <p className="mt-3 rounded-2xl border border-rose-200 bg-rose-50 p-3 text-sm font-medium text-rose-700">
                {error}
              </p>
            )}
          </div>
        </div>

        <button
          type="button"
          onClick={loadHealth}
          disabled={isLoading}
          className="inline-flex items-center justify-center gap-2 rounded-2xl border border-slate-200 bg-white px-5 py-3 text-sm font-bold text-slate-700 shadow-sm transition hover:border-blue-200 hover:text-blue-700 disabled:opacity-60"
        >
          <RefreshCw size={16} className={isLoading ? "animate-spin" : ""} />
          Refresh
        </button>
      </div>

      {health && (
        <dl className="mt-6 grid gap-3 text-sm sm:grid-cols-3">
          <div className="rounded-2xl bg-slate-50 p-4">
            <dt className="font-semibold text-slate-500">API version</dt>
            <dd className="mt-1 font-black text-slate-950">{health.api_version || "Not returned"}</dd>
          </div>
          <div className="rounded-2xl bg-slate-50 p-4">
            <dt className="font-semibold text-slate-500">Model version</dt>
            <dd className="mt-1 font-black text-slate-950">
              {health.model_version || "Not returned"}
            </dd>
          </div>
          <div className="rounded-2xl bg-slate-50 p-4">
            <dt className="font-semibold text-slate-500">Service</dt>
            <dd className="mt-1 font-black text-slate-950">{health.service || "FastAPI backend"}</dd>
          </div>
        </dl>
      )}
    </SectionCard>
  );
}
