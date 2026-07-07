import type { ReactNode } from "react";

interface SectionCardProps {
  title?: string;
  eyebrow?: string;
  children: ReactNode;
  className?: string;
}

export function SectionCard({ title, eyebrow, children, className = "" }: SectionCardProps) {
  return (
    <section
      className={`rounded-3xl border border-slate-200 bg-white/90 p-6 shadow-sm shadow-slate-200/70 ${className}`}
    >
      {(eyebrow || title) && (
        <div className="mb-5">
          {eyebrow && (
            <p className="mb-2 text-xs font-bold uppercase tracking-[0.25em] text-blue-600">
              {eyebrow}
            </p>
          )}
          {title && <h2 className="text-2xl font-bold tracking-tight text-slate-950">{title}</h2>}
        </div>
      )}
      {children}
    </section>
  );
}
