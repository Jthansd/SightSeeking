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
  const observedAt =
    "observed_at" in sighting && sighting.observed_at
      ? sighting.observed_at
      : sighting.timestamp;

  const when = observedAt
    ? new Date(observedAt).toLocaleString()
    : "Unknown date";

  const commonName =
    "common_name" in sighting &&
    typeof sighting.common_name === "string" &&
    sighting.common_name
      ? sighting.common_name
      : SIGHTING_TYPE_LABELS[sighting.sighting_type];

  const animalCount =
    "animal_count" in sighting ? sighting.animal_count : null;

  const behavior =
    "behavior" in sighting &&
    typeof sighting.behavior === "string" &&
    sighting.behavior
      ? sighting.behavior
      : null;

  const notes =
    "notes" in sighting &&
    typeof sighting.notes === "string" &&
    sighting.notes
      ? sighting.notes
      : sighting.description;

  const latitude =
    "locationLatitude" in sighting
      ? sighting.locationLatitude
      : null;

  const longitude =
    "locationLongitude" in sighting
      ? sighting.locationLongitude
      : null;

  function formatBehavior(value: string) {
    return value
      .toLowerCase()
      .replace("_", " ")
      .replace(/\b\w/g, (letter) => letter.toUpperCase());
  }

  return (
    <article className="card sighting-card">
      <div className="sighting-card-header">
        <div>
          <span className="tag">
            {SIGHTING_TYPE_LABELS[sighting.sighting_type]}
          </span>

          <h3 className="sighting-name">{commonName}</h3>
        </div>

        {animalCount != null && (
          <div className="sighting-count">
            <strong>{animalCount}</strong>
            <span>{animalCount === 1 ? "spotted" : "spotted"}</span>
          </div>
        )}
      </div>

      {notes && (
        <p className="sighting-description">
          {notes}
        </p>
      )}

      <div className="sighting-details">
        {behavior && (
          <div className="sighting-detail">
            <span className="detail-label">Behavior</span>
            <strong>{formatBehavior(behavior)}</strong>
          </div>
        )}

        <div className="sighting-detail">
          <span className="detail-label">Observed</span>
          <strong>{when}</strong>
        </div>

        {latitude != null && longitude != null && (
          <div className="sighting-detail">
            <span className="detail-label">Location</span>
            <strong>
              {Number(latitude).toFixed(4)}, {Number(longitude).toFixed(4)}
            </strong>
          </div>
        )}
      </div>
    </article>
  );
}