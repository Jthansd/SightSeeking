import { useState } from "react";
import SightingCard from "./components/SightingCard";
import type { Sighting } from "./types";

const starterSightings: Sighting[] = [
  { id: 1, species: "Red-tailed Hawk", location: "Balboa Park", date: "2026-10-01" },
  { id: 2, species: "Coyote", location: "Mission Trails", date: "2026-10-03" },
];

export default function App() {
  const [sightings, setSightings] = useState<Sighting[]>(starterSightings);
  const [species, setSpecies] = useState("");

  function addSighting() {
    if (species.trim() === "") return;
    const newSighting: Sighting = {
      id: Date.now(),
      species: species,
      location: "Unknown",
      date: new Date().toLocaleDateString(),
    };
    setSightings([newSighting, ...sightings]);   // build a new array; don't push into the old one
    setSpecies("");
  }

  return (
    <div style={{ maxWidth: 600, margin: "0 auto", padding: 16 }}>
      <h1>Wildlife Tracker</h1>

      <input
        value={species}
        onChange={(e) => setSpecies(e.target.value)}
        placeholder="What did you see?"
      />
      <button onClick={addSighting}>Add</button>

      {sightings.map((s) => (
        <SightingCard key={s.id} sighting={s} />
      ))}
    </div>
  );
}