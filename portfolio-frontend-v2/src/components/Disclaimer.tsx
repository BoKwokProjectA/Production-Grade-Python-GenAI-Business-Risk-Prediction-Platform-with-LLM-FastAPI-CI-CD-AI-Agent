import { AlertTriangle } from "lucide-react";
import { SectionCard } from "./SectionCard";

export function Disclaimer() {
  return (
    <SectionCard
      eyebrow="Safety and governance"
      title="Educational AI engineering portfolio only"
      className="scroll-mt-24 border-amber-200 bg-amber-50/80"
    >
      <div id="disclaimer" className="flex gap-4">
        <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-amber-100 text-amber-700">
          <AlertTriangle size={24} />
        </div>
        <div className="space-y-3 text-sm leading-7 text-amber-950">
          <p>This project is an educational and job-application portfolio implementation of a full-stack AI risk scoring platform.</p>
          <p>
            It is not a regulated product, clinical decision-support system, or automated decision-making system.
            Outputs are for technical demonstration only and should not be used for real-world decisions without qualified human review, validation, and appropriate governance controls.
          </p>
          <p>
            
          </p>
        </div>
      </div>
    </SectionCard>
  );
}
