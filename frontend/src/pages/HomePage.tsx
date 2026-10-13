import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import SightingCard from "../components/SightingCard";
import type { SightingApiResponse } from "../types";

export default function HomePage() {
  const navigate = useNavigate();

  const [sightings, setSightings] = useState<SightingApiResponse[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const controller = new AbortController();

    async function loadSightings() {
      try {
        const response = await fetch("/api/sightings", {
          signal: controller.signal,
        });

        if (!response.ok) {
          throw new Error("Failed to load sightings");
        }

        const data: SightingApiResponse[] = await response.json();
        setSightings(data);
      } catch (err) {
        if (controller.signal.aborted) return;

        setError(
          err instanceof Error ? err.message : "Something went wrong"
        );
      } finally {
        if (!controller.signal.aborted) {
          setLoading(false);
        }
      }
    }

    loadSightings();

    return () => controller.abort();
  }, []);

  return (
    <main className="home">
      <section className="hero">
        <div className="hero-content">
          <p className="eyebrow">Explore. Discover. Share.</p>

          <h1>Find wildlife worth exploring.</h1>

          <p className="hero-text">
            Sight Seeking helps nature enthusiasts discover wildlife sightings,
            explore species, and share their own encounters with the community.
          </p>

          <div className="hero-actions">
            <button
              className="primary-button"
              onClick={() => navigate("/report")}
            >
              Report a Sighting
            </button>

            <button className="secondary-button">
              Explore Sightings
            </button>
          </div>
        </div>

        <div className="hero-panel card">
          <h3>Community Snapshot</h3>

          <div className="stat-grid">
            <div className="stat-item">
              <span className="stat-number">{sightings.length}</span>
              <span className="stat-label">Sightings</span>
            </div>

            <div className="stat-item">
              <span className="stat-number">40</span>
              <span className="stat-label">Species</span>
            </div>

            <div className="stat-item">
              <span className="stat-number">18</span>
              <span className="stat-label">Regions</span>
            </div>

            <div className="stat-item">
              <span className="stat-number">15</span>
              <span className="stat-label">Habitats</span>
            </div>
          </div>
        </div>
      </section>

      <section className="section-block">
        <div className="section-heading">
          <div>
            <p className="eyebrow">Latest Activity</p>
            <h2>Recent Sightings</h2>
          </div>

          <button className="text-button">
            View All Sightings
          </button>
        </div>

        {loading && (
          <div className="status-card card">
            <p>Loading sightings...</p>
          </div>
        )}

        {error && (
          <div className="status-card card">
            <p>Unable to load sightings: {error}</p>
          </div>
        )}

        {!loading && !error && sightings.length === 0 && (
          <div className="status-card card">
            <h3>No sightings yet</h3>
            <p>
              Add the first wildlife sighting to start building the community
              field guide.
            </p>
          </div>
        )}

        {!loading && !error && sightings.length > 0 && (
          <div className="sightings-grid">
            {sightings.slice(0, 6).map((sighting) => (
              <SightingCard
                key={sighting.id}
                sighting={sighting}
              />
            ))}
          </div>
        )}
      </section>

      <section className="dashboard-grid section-block">
        <div className="map-card card">
          <div className="section-heading">
            <div>
              <p className="eyebrow">Explore Nearby</p>
              <h2>Wildlife Map</h2>
            </div>
          </div>

          <div className="map-placeholder">
            <span>Interactive map coming soon</span>
          </div>
        </div>

        <div className="quick-guide card">
          <p className="eyebrow">Field Guide</p>
          <h2>Start Exploring</h2>

          <div className="guide-links">
            <button>Browse Species</button>
            <button>Find Wildlife</button>
            <button>View Hunting Seasons</button>
          </div>
        </div>
      </section>
    </main>
  );
}