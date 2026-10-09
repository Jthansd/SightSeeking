import SightingCard from "../components/SightingCard";
import { mockSightings } from "../mockData";

export default function HomePage() {
  return (
    <div className="home">
      <section className="intro">
        <h1>Sight Seeking</h1>
        <p>Spotted something worth exploring? Share it so others can find it too.</p>
      </section>

      <div className="add-sighting">
        <h2>Add a New Sighting</h2>
        <p>Share your wildlife encounters with the community!</p>
        <button onClick={() => console.log("Add Sighting clicked")}>
          Add Sighting!
        </button>
      </div>

      <div className="home-layout">
        <section>
          <h2>Recent Sightings</h2>
          {mockSightings.map((s) => (
            <SightingCard key={s.id} sighting={s} />
          ))}
        </section>

        <aside className="map-placeholder">Map coming soon</aside>
      </div>
    </div>
  );
}