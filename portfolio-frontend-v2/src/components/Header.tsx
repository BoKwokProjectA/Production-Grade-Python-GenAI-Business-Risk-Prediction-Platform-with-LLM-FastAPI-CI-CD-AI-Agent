import { Activity } from "lucide-react";
import { PROJECT_LINKS } from "../lib/constants";

export function Header() {
  return (
    <header className="sticky top-0 z-40 border-b border-white/60 bg-white/80 backdrop-blur-xl">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-5 py-4">
        <a href="#top" className="flex items-center gap-3">
          <div className="flex h-10 w-10 items-center justify-center rounded-2xl bg-blue-600 text-white shadow-lg shadow-blue-600/25">
            <Activity size={21} />
          </div>
          <div>
            <p className="text-sm font-bold leading-tight text-slate-950">AI Risk Platform</p>
            <p className="text-xs text-slate-500">Portfolio Frontend v2</p>
          </div>
        </a>

        <nav className="hidden items-center gap-7 text-sm font-medium text-slate-600 md:flex">
          <a className="hover:text-blue-700" href="#predict">Predict</a>
          <a className="hover:text-blue-700" href="#health">Health</a>
          <a className="hover:text-blue-700" href="#links">Links</a>
          <a className="hover:text-blue-700" href="#disclaimer">Disclaimer</a>
        </nav>

        <a
          href={PROJECT_LINKS.githubRepo}
          target="_blank"
          rel="noreferrer"
          className="inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white px-4 py-2 text-sm font-semibold text-slate-700 shadow-sm hover:border-blue-200 hover:text-blue-700"
        >
          <span>GitHub</span>
        </a>
      </div>
    </header>
  );
}
