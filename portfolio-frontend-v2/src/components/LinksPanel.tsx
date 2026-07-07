import { ExternalLink } from "lucide-react";
import { PROJECT_LINKS } from "../lib/constants";
import { SectionCard } from "./SectionCard";

const links = [
  {
    label: "Live scoring API",
    href: PROJECT_LINKS.backendApi,
    description: "Primary deployed FastAPI service powering the platform.",
  },
  {
    label: "Swagger docs",
    href: PROJECT_LINKS.swaggerDocs,
    description: "Interactive backend API documentation.",
  },
  {
    label: "OpenAPI schema",
    href: PROJECT_LINKS.openApiSchema,
    description: "Machine-readable backend schema.",
  },
  {
    label: "GitHub repository placeholder",
    href: PROJECT_LINKS.githubRepo,
    description: "Replace this with your frontend or monorepo GitHub URL.",
  },
  {
    label: "Frontend live demo placeholder",
    href: PROJECT_LINKS.frontendDemo,
    description: "Replace this with your final Vercel deployment URL.",
  },
];

export function LinksPanel() {
  return (
    <SectionCard eyebrow="Portfolio links" title="Platform resources" className="scroll-mt-24">
      <div id="links" className="grid gap-4 md:grid-cols-2">
        {links.map((link) => (
          <a
            key={link.label}
            href={link.href}
            target="_blank"
            rel="noreferrer"
            className="group rounded-3xl border border-slate-200 bg-slate-50 p-5 transition hover:border-blue-200 hover:bg-blue-50/50"
          >
            <div className="flex items-center justify-between gap-4">
              <p className="font-black text-slate-950 group-hover:text-blue-700">{link.label}</p>
              <ExternalLink size={18} className="shrink-0 text-slate-400 group-hover:text-blue-600" />
            </div>
            <p className="mt-2 text-sm leading-6 text-slate-600">{link.description}</p>
            <p className="mt-3 break-all text-xs font-semibold text-slate-400">{link.href}</p>
          </a>
        ))}
      </div>
    </SectionCard>
  );
}
