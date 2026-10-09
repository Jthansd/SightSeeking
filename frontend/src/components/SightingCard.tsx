import { SIGHTING_TYPE_LABELS, type Sighting } from "../types";

import "./SightingCard.css";

type Props = { sighting: Sighting };

export default function SightingCard({ sighting }: Props) {
  const when = new Date(sighting.observed_at ?? sighting.timestamp).toLocaleString();

  return (
    <div className="card">
      <span className="tag">{SIGHTING_TYPE_LABELS[sighting.sighting_type]}</span>
      <p>{sighting.description}</p>
      {sighting.sighting_type === "ANIMAL" && <p>Count: {sighting.animal_count}</p>}
      <small>{when}</small>
    </div>
  );
}