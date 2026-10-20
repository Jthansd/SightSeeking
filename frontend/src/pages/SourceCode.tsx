import "./SourceCode.css";

// Paste the GitHub repository URL here (e.g. "https://github.com/...").
// While it's empty, the page shows a "Link coming soon" placeholder.
const GITHUB_URL = "https://github.com/Jthansd/SightSeeking";

const MODEL_SNIPPET = `class Sighting(models.Model):

    class SightingType(models.TextChoices):
        ANIMAL = "ANIMAL", "Animal"
        VEGETATION = "VEGETATION", "Vegetation"
        VIEWING = "VIEWING", "Viewing"
        OTHER = "OTHER", "Other"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sightings"
    )

    sighting_type = models.CharField(
        max_length=20,
        choices=SightingType.choices
    )

    locationLongitude = models.FloatField()
    locationLatitude = models.FloatField()

    region = models.ForeignKey(
        Region,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="sightings"
    )
    ...`;

const SQL_SNIPPET = `cursor.execute('''
    SELECT s.id, s.sighting_type, s.description,
           s."locationLatitude", s."locationLongitude",
           s.observed_at, s.animal_count, s.behavior,
           a.common_name
    FROM api_sighting s
    LEFT JOIN api_animal_sighting a
        ON a.sighting_id = s.id
    ORDER BY s.id DESC
''')`;

const TRANSACTION_SNIPPET = `with transaction.atomic():
    sighting = Sighting.objects.create(
        user=user,
        sighting_type=Sighting.SightingType.ANIMAL,
        locationLatitude=float(latitude),
        locationLongitude=float(longitude),
        observed_at=observed_at,
        animal_count=animal_count,
        behavior=behavior,
        notes=notes,
        ...
    )
    Animal_Sighting.objects.create(
        sighting=sighting,
        common_name=species_name,
        species_record=species_record,
        ... 
        species (scientific name)
    )`;

const FETCH_SNIPPET = `export const API_URL = import.meta.env.VITE_API_URL ?? "";

useEffect(() => {
  const controller = new AbortController();

  async function loadSightings() {
    const response = await fetch(\`\${API_URL}/api/sightings/\`, {
      signal: controller.signal,
    });
    if (!response.ok) throw new Error("Failed to load sightings");
    setSightings(await response.json());
  }

  loadSightings();
  return () => controller.abort();
}, []);`;

function CodeBlock({ file, code }: { file: string; code: string }) {
  return (
    <figure className="code-block">
      <figcaption>{file}</figcaption>
      <pre>
        <code>{code}</code>
      </pre>
    </figure>
  );
}

export default function SourceCode() {
  return (
    <div className="source-code">
      <h1>Source Code</h1>

      <div className="repo-box card">
        <h3>GitHub Repository</h3>
          <a href={GITHUB_URL} target="_blank" rel="noopener noreferrer">
            {GITHUB_URL}
          </a>
      </div>

      <section>
        <h2>How Sight Seeking Is Built</h2>
        <p>
          Sight Seeking has three layers. The frontend is a
          React + TypeScript app built with Vite, hosted on Cloudflare. It talks
          to the backend written in Python with Django, hosted on
          Render, which exposes a JSON API under <code>/api/</code>. The backend
          stores everything in a PostgreSQL database hosted on
          Supabase. When you open the home page, your browser downloads the
          React app, the app asks the API for sightings, and the API queries the
          database and sends the results back as JSON.
        </p>
      </section>

      <section>
        <h2>1. Database Design: Modeling a Sighting</h2>
        <p>
          Every sighting is a row in the Sighting table. Each row
          links to the user who reported it and, optionally, to lookup tables
          for region, habitat and weather. Fixed lists like sighting type are
          stored as choices so the database only accepts valid values. Django
          turns these Python classes into real PostgreSQL tables through
          migrations. Animal details live in a separate{" "}
          <code>Animal_Sighting</code> table that has a one-to-one link back to
          its sighting.
        </p>
        <CodeBlock file="backend/api/models.py" code={MODEL_SNIPPET} />
      </section>

      <section>
        <h2>2. The API: Putting Things Together</h2>
        <p>
          The <code>/api/sightings/</code> endpoint handles both reading and
          creating sightings. For reading, it runs a SQL query that joins each sighting with its animal details.
          The join query keeps sightings that aren't animals too, such as
          views or plants.
        </p>
        <CodeBlock file="backend/api/views.py" code={SQL_SNIPPET} />
        <p>
          For creating a sighting, it first checks the input (required fields,
          valid behavior, count of at least 1). Then it saves the sighting and
          its animal record, so either
          both rows are saved or neither is, and the database never holds an incomplete sighting.
        </p>
        <CodeBlock file="backend/api/views.py" code={TRANSACTION_SNIPPET} />
      </section>

      <section>
        <h2>3. The Frontend: Loading Live Data</h2>
        <p>
          The home page asks the API for sightings when it first loads. It then
          stores them in React state, and each one is drawn as a{" "}
          <code>SightingCard</code>. The backend's address comes from one
          environment variable, <code>VITE_API_URL</code>. Locally that's the
          dev server, and on the live site it's Render, with no code changes
          between the two. An <code>AbortController</code> cancels the request
          if the user leaves the page before it finishes.
        </p>
        <CodeBlock
          file="frontend/src/api.ts + frontend/src/pages/HomePage.tsx"
          code={FETCH_SNIPPET}
        />
      </section>
    </div>
  );
}
