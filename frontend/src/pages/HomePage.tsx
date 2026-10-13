import { useEffect, useState, type FormEvent } from "react";
import SightingCard from "../components/SightingCard";
import {
  SIGHTING_TYPE_LABELS,
  type SightingApiResponse,
  type SightingType,
} from "../types";

type AddSightingFormProps = {
  onAdd: (sightingType: SightingType, notes: string, dateTime: Date) => void;
};

// Demo-only form: entries are kept in page state and never sent to the database.
function AddSightingForm({ onAdd }: AddSightingFormProps) {
  const [sightingType, setSightingType] = useState<SightingType>("ANIMAL");
  const [notes, setNotes] = useState("");
  const [dateTime, setDateTime] = useState("");

  const handleAddSighting = (e: FormEvent) => {
    e.preventDefault();
    if (!notes.trim()) return;

    // Fall back to "now" if the user leaves the date blank.
    onAdd(sightingType, notes.trim(), dateTime ? new Date(dateTime) : new Date());

    setNotes("");
    setDateTime("");
  };

  return (
    <form className="add-sighting-form" onSubmit={handleAddSighting}>
      <select
        value={sightingType}
        onChange={(e) => setSightingType(e.target.value as SightingType)}
      >
        {Object.entries(SIGHTING_TYPE_LABELS).map(([value, label]) => (
          <option key={value} value={value}>
            {label}
          </option>
        ))}
      </select>
      <textarea
        placeholder="Notes (e.g. Brown pelican diving near the pier)"
        value={notes}
        onChange={(e) => setNotes(e.target.value)}
        required
      />
      <input
        type="datetime-local"
        value={dateTime}
        onChange={(e) => setDateTime(e.target.value)}
      />
      <button type="submit">Add Sighting!</button>
    </form>
  );
}

export default function HomePage() {
  const [sightings, setSightings] = useState<SightingApiResponse[]>([]);
  // Sightings entered on this page; kept separate so the API load can't overwrite them.
  const [addedSightings, setAddedSightings] = useState<SightingApiResponse[]>([]);
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

  const handleAddSighting = (
    sightingType: SightingType,
    notes: string,
    dateTime: Date
  ) => {
    const newSighting: SightingApiResponse = {
      id: Date.now(), // temporary unique id; the database would assign a real one
      user_id: 0,
      sighting_type: sightingType,
      timestamp: dateTime.toISOString(),
      description: notes,
      locationLongitude: 0,
      locationLatitude: 0,
    };

    // Newest entries go on top of the list.
    setAddedSightings((prev) => [newSighting, ...prev]);
  };

  const allSightings = [...addedSightings, ...sightings];

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
        <AddSightingForm onAdd={handleAddSighting} />
      </div>

      <div className="home-layout">
        <section>
          <h2>Recent Sightings</h2>

          {loading && <p>Loading sightings...</p>}

          {error && <p>Unable to load sightings: {error}</p>}

          {!loading && allSightings.length === 0 && (
            <p>No sightings available yet.</p>
          )}

          {allSightings.map((s) => (
            <SightingCard key={s.id} sighting={s} />
          ))}
        </section>

        <aside className="map-placeholder">Map coming soon</aside>
      </div>
    </div>
  );
}