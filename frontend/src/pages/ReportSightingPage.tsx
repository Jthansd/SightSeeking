import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

type SpeciesOption = {
  id: number;
  common_name: string;
  scientific_name: string;
  category: string;
};

export default function ReportSightingPage() {
  const navigate = useNavigate();

  const [speciesOptions, setSpeciesOptions] = useState<SpeciesOption[]>([]);
  const [speciesLoading, setSpeciesLoading] = useState(true);

  const [formData, setFormData] = useState({
    species: "",
    latitude: "",
    longitude: "",
    observedAt: "",
    animalCount: 1,
    behavior: "",
    notes: "",
  });

  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);

  useEffect(() => {
    async function loadSpecies() {
      try {
        const response = await fetch("/api/species/");

        if (!response.ok) {
          throw new Error("Failed to load species.");
        }

        const data: SpeciesOption[] = await response.json();
        setSpeciesOptions(data);
      } catch (err) {
        console.error(err);
      } finally {
        setSpeciesLoading(false);
      }
    }

    loadSpecies();
  }, []);

  function handleChange(
    e: React.ChangeEvent<
      HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement
    >
  ) {
    const { name, value } = e.target;

    setFormData((prev) => ({
      ...prev,
      [name]: name === "animalCount" ? Number(value) : value,
    }));
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    setSubmitting(true);
    setError(null);
    setSuccess(null);

    try {
      const response = await fetch("/api/sightings/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Failed to create sighting.");
      }

      setSuccess("Sighting submitted successfully!");

      setFormData({
        species: "",
        latitude: "",
        longitude: "",
        observedAt: "",
        animalCount: 1,
        behavior: "",
        notes: "",
      });

      setTimeout(() => {
        navigate("/");
      }, 1200);
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "Something went wrong while submitting the sighting."
      );
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <main className="report-page">
      <div className="report-container">
        <div className="report-heading">
          <p className="eyebrow">Community Field Guide</p>
          <h1>Report a Sighting</h1>
          <p>
            Share what you saw so other wildlife enthusiasts can discover it too.
          </p>
        </div>

        <form className="report-form card" onSubmit={handleSubmit}>
          <div className="form-grid">
            <div className="form-group">
              <label htmlFor="species">Species</label>

              <select
                id="species"
                name="species"
                value={formData.species}
                onChange={handleChange}
                required
              >
                <option value="">
                  {speciesLoading
                    ? "Loading species..."
                    : "Select a species"}
                </option>

                {speciesOptions.map((species) => (
                  <option
                    key={species.id}
                    value={species.common_name}
                  >
                    {species.common_name}
                    {species.scientific_name
                      ? ` — ${species.scientific_name}`
                      : ""}
                  </option>
                ))}
              </select>
            </div>

            <div className="form-group">
              <label htmlFor="observedAt">Date & Time</label>

              <input
                id="observedAt"
                name="observedAt"
                type="datetime-local"
                value={formData.observedAt}
                onChange={handleChange}
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="latitude">Latitude</label>

              <input
                id="latitude"
                name="latitude"
                type="number"
                step="any"
                placeholder="Example: 32.9595"
                value={formData.latitude}
                onChange={handleChange}
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="longitude">Longitude</label>

              <input
                id="longitude"
                name="longitude"
                type="number"
                step="any"
                placeholder="Example: -116.5797"
                value={formData.longitude}
                onChange={handleChange}
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="animalCount">Number Spotted</label>

              <input
                id="animalCount"
                name="animalCount"
                type="number"
                min="1"
                value={formData.animalCount}
                onChange={handleChange}
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="behavior">Behavior</label>

              <select
                id="behavior"
                name="behavior"
                value={formData.behavior}
                onChange={handleChange}
              >
                <option value="">Select behavior</option>
                <option value="FEEDING">Feeding</option>
                <option value="RESTING">Resting</option>
                <option value="MOVING">Moving</option>
                <option value="DRINKING">Drinking</option>
                <option value="HUNTING">Hunting</option>
                <option value="CALLING">Calling</option>
                <option value="NESTING">Nesting</option>
                <option value="MATING">Rutting/Mating</option>
                <option value="FLEEING">Fleeing</option>
                <option value="OTHER">Other</option>
              </select>
            </div>

            <div className="form-group full-width">
              <label htmlFor="notes">Notes</label>

              <textarea
                id="notes"
                name="notes"
                rows={5}
                placeholder="Describe what you saw..."
                value={formData.notes}
                onChange={handleChange}
              />
            </div>
          </div>

          {error && (
            <p
              style={{
                color: "#a12626",
                marginBottom: "16px",
                fontWeight: 600,
              }}
            >
              {error}
            </p>
          )}

          {success && (
            <p
              style={{
                color: "#245a3b",
                marginBottom: "16px",
                fontWeight: 700,
              }}
            >
              {success}
            </p>
          )}

          <button
            type="submit"
            className="primary-button"
            disabled={submitting}
          >
            {submitting ? "Submitting..." : "Submit Sighting"}
          </button>
        </form>
      </div>
    </main>
  );
}