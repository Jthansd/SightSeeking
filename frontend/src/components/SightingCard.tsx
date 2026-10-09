import type { Sighting } from "../types";

type Props = { sighting: Sighting };

export default function SightingCard({ sighting }: Props) {
  return (
    <div style={{ border: "4px solid #ccc", padding: 8, margin: "8px 0", borderRadius: 4 }}>
      <h3>{sighting.species}</h3>
      <p>{sighting.location} · {sighting.date}</p>
    </div>
  );
}