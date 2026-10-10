import type { Sighting } from "./types";

export const mockSightings: Sighting[] = [
  {
    id: 1, user: 1, sighting_type: "ANIMAL",
    timestamp: "2026-10-01T18:00:00Z", updated_at: "2026-10-01T18:00:00Z",
    description: "Red-tailed hawk circling the canyon",
    locationLatitude: 32.7341, locationLongitude: -117.1446,
    observed_at: "2026-10-01T17:30:00Z",
    region: null, habitat: null, weather: null, temperature_f: 72,
    animal_count: 1, behavior: "HUNTING", notes: "", is_public: true,
  },
  // copy and edit for more entries
];