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
    {
    id: 2, user: 1, sighting_type: "ANIMAL",
    timestamp: "2026-10-12T12:34:00Z", updated_at: "2026-10-12T12:34:00Z",
    description: "Litter of cottontail rabbits by the creek",
    locationLatitude: 23.123, locationLongitude: -111.456,
    observed_at: "2026-10-01T17:30:00Z",
    region: null, habitat: null, weather: null, temperature_f: 72,
    animal_count: 1, behavior: "NESTING", notes: "", is_public: true,
  },
    {
    id: 3, user: 1, sighting_type: "VEGETATION",
    timestamp: "2026-10-09T18:00:00Z", updated_at: "2026-10-09T18:00:00Z",
    description: "Pointed-leaf manzanita in bloom",
    locationLatitude: 32.7341, locationLongitude: -117.1446,
    observed_at: "2026-10-09T18:00:00Z",
    region: null, habitat: null, weather: null, temperature_f: 72,
    animal_count: 1, behavior: "", notes: "", is_public: true,
  },
    {
    id: 4, user: 1, sighting_type: "VIEWING",
    timestamp: "2026-10-01T18:00:00Z", updated_at: "2026-10-01T18:00:00Z",
    description: "Creek with a waterfall after light rain",
    locationLatitude: 32.7341, locationLongitude: -117.1446,
    observed_at: "2026-10-01T17:30:00Z",
    region: null, habitat: null, weather: null, temperature_f: 72,
    animal_count: 1, behavior: "", notes: "", is_public: true,
  },
    {
    id: 5, user: 1, sighting_type: "OTHER",
    timestamp: "2026-10-01T18:00:00Z", updated_at: "2026-10-01T18:00:00Z",
    description: "Grafiti on the canyon wall",
    locationLatitude: 32.7341, locationLongitude: -117.1446,
    observed_at: "2026-10-01T17:30:00Z",
    region: null, habitat: null, weather: null, temperature_f: 72,
    animal_count: 1, behavior: "HUNTING", notes: "", is_public: true,
  },

];