import { ArrowRight, Brain, Cloud, ShieldCheck } from "lucide-react";
import { PROJECT_LINKS } from "../lib/constants";

export function Hero() {
  return (
    <section id="top" className="relative overflow-hidden px-5 py-16 sm:py-20 lg:py-24">
      <div className="absolute inset-0 -z-10 bg-[radial-gradient(circle_at_top_left,_rgba(37,99,235,0.16),_transparent_34%),radial-gradient(circle_at_top_right,_rgba(14,165,233,0.18),_transparent_32%)]" />

      <div className="mx-auto grid max-w-7xl items-center gap-10 lg:grid-cols-[1.05fr_0.95fr]">
        <div>
          <div className="mb-5 inline-flex items-center gap-2 rounded-full border border-blue-100 bg-blue-50 px-4 py-2 text-sm font-semibold text-blue-700">
            <ShieldCheck size={16} />
            Educational AI platform with safety boundaries
          </div>

          <h1 className="max-w-4xl text-4xl font-black tracking-tight text-slate-950 sm:text-5xl lg:text-6xl">
            Full-stack AI risk prediction platform.
          </h1>

          <p className="mt-6 max-w-2xl text-lg leading-8 text-slate-600">
            A polished React + TypeScript frontend for a deployed FastAPI backend.
            Upload an image, call the production API, and display a structured risk
            prediction response with clear governance boundaries.
          </p>

          <div className="mt-8 flex flex-col gap-3 sm:flex-row">
            <a
              href="#predict"
              className="inline-flex items-center justify-center gap-2 rounded-2xl bg-blue-600 px-6 py-3 text-sm font-bold text-white shadow-lg shadow-blue-600/25 hover:bg-blue-700"
            >
              Try risk scoring
              <ArrowRight size={17} />
            </a>
            <a
              href={PROJECT_LINKS.swaggerDocs}
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center justify-center rounded-2xl border border-slate-200 bg-white px-6 py-3 text-sm font-bold text-slate-700 shadow-sm hover:border-blue-200 hover:text-blue-700"
            >
              Open Swagger docs
            </a>
          </div>
        </div>

        <div className="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-2xl shadow-slate-200/80">
          <div className="grid gap-4">
            <div className="rounded-3xl bg-slate-950 p-5 text-white">
              <div className="mb-6 flex items-center justify-between">
                <span className="rounded-full bg-emerald-400/15 px-3 py-1 text-xs font-bold text-emerald-300">
                  Live API Ready
                </span>
                <Cloud size={22} className="text-blue-300" />
              </div>
              <p className="text-sm text-slate-300">Backend endpoint</p>
              <p className="mt-2 break-all text-sm font-semibold text-white">
                {PROJECT_LINKS.backendApi}
              </p>
            </div>

            <div className="grid gap-4 sm:grid-cols-2">
              <div className="rounded-3xl border border-slate-100 bg-slate-50 p-5">
                <Brain className="mb-4 text-blue-600" size={28} />
                <p className="text-sm font-bold text-slate-950">ConvNeXt + EVA-02</p>
                <p className="mt-2 text-sm leading-6 text-slate-600">
                  Backend ensemble returns a risk label and confidence score.
                </p>
              </div>
              <div className="rounded-3xl border border-slate-100 bg-slate-50 p-5">
                <ShieldCheck className="mb-4 text-blue-600" size={28} />
                <p className="text-sm font-bold text-slate-950">Governance scoped</p>
                <p className="mt-2 text-sm leading-6 text-slate-600">
                  Clear disclaimer and no automated decision-making claims.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
