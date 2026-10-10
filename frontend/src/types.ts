export type SightingType = "ANIMAL" | "VEGETATION" | "VIEWING" | "OTHER";

export type Behavior =
  | "FEEDING" | "RESTING" | "MOVING" | "DRINKING" | "HUNTING"
  | "CALLING" | "NESTING" | "MATING" | "FLEEING" | "OTHER"
  | "";                                   

export type Sighting = {
  id: number;
  user: number;                         
  sighting_type: SightingType;
  timestamp: string;
  description: string;
  locationLongitude: number;
  locationLatitude: number;
  observed_at: string | null;
  region: number | null;                
  habitat: number | null;
  weather: number | null;
  temperature_f: number | null;
  animal_count: number;
  behavior: Behavior;
  notes: string;
  is_public: boolean;
  updated_at: string;
};

export const SIGHTING_TYPE_LABELS: Record<SightingType, string> = {
  ANIMAL: "Animal",
  VEGETATION: "Vegetation",
  VIEWING: "Viewing",
  OTHER: "Other",
};