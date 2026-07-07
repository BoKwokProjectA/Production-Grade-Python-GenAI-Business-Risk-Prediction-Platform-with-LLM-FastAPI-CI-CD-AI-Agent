import { Disclaimer } from "./components/Disclaimer";
import { Footer } from "./components/Footer";
import { Header } from "./components/Header";
import { HealthCheck } from "./components/HealthCheck";
import { Hero } from "./components/Hero";
import { LinksPanel } from "./components/LinksPanel";
import { PredictionUploader } from "./components/PredictionUploader";

function App() {
  return (
    <div className="min-h-screen bg-slate-50">
      <Header />
      <main>
        <Hero />

        <div className="mx-auto grid max-w-7xl gap-8 px-5 pb-16">
          <PredictionUploader />
          <HealthCheck />
          <LinksPanel />
          <Disclaimer />
        </div>
      </main>
      <Footer />
    </div>
  );
}

export default App;
