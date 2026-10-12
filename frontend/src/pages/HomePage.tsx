import { useEffect, useState } from "react";
import SightingCard from "../components/SightingCard";
import type { SightingApiResponse } from "../types";

export default function HomePage() {
  const [sightings, setSightings] = useState<SightingApiResponse[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const controller = new AbortController();

    async function loadSightings() {
      try {
        const response = await fetch(
          // "http://127.0.0.1:8000/api/sightings/",
          "/api/sightings",
          { signal: controller.signal }
        );

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
    <div className="home">
      <section className="intro">
        <h1>Sight Seeking</h1>
        <p>
          Spotted something worth exploring? Share it so others can find it too.
        </p>
      </section>

      <div className="add-sighting">
        <h2>Add a New Sighting</h2>
        <p>Share your wildlife encounters with the community!</p>
        <button onClick={() => console.log("Add Sighting clicked")}>
          Add Sighting!
        </button>
      </div>

      <div className="home-layout">
        <section>
          <h2>Recent Sightings</h2>

          {loading && <p>Loading sightings...</p>}

          {error && <p>Unable to load sightings: {error}</p>}

          {!loading && !error && sightings.length === 0 && (
            <p>No sightings available yet.</p>
          )}

          {!loading &&
            !error &&
            sightings.map((s) => (
              <SightingCard key={s.id} sighting={s} />
            ))}
        </section>

        <aside className="map-placeholder">Map coming soon</aside>
      </div>
    </div>
  );
}