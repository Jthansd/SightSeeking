import {
  SIGHTING_TYPE_LABELS,
  type Sighting,
  type SightingApiResponse,
} from "../types";

import "./SightingCard.css";

type Props = {
  sighting: Sighting | SightingApiResponse;
};

export default function SightingCard({ sighting }: Props) {
  const when = new Date(
    ("observed_at" in sighting ? sighting.observed_at : null) ??
      sighting.timestamp
  ).toLocaleString();

  return (
    <div className="card">
      <span className="tag">
        {SIGHTING_TYPE_LABELS[sighting.sighting_type]}
      </span>

      <p>{sighting.description}</p>

      {sighting.sighting_type === "ANIMAL" &&
        "animal_count" in sighting &&
        sighting.animal_count != null && (
          <p>Count: {sighting.animal_count}</p>
        )}

      <small>{when}</small>
    </div>
  );
}