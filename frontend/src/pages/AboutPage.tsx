import badge from "../assets/sight-seeking-badge.png";
import MemberCard from "../components/MemberCard";
import { members } from "../data/members";




export default function AboutPage() {
  return (
    <div className="about text-page">
      <img src={badge} alt="Sight Seeking badge" className="about-badge" />
      <h1>About Us</h1>
        <p> Sight Seeking is a company dedicated to encouraging outdoor exploration through
          providing a comprehensive platform for nature enthusiasts to discover and share
          their outdoor experiences.
        </p>

      <section>
        <h2>Our Mission</h2>
        <p>
          At sight seeking, our mission is to inspire and empower individuals to connect with nature by providing a user-friendly platform that facilitates the discovery and sharing of wildlife sightings. We aim to foster a community of outdoor enthusiasts who can learn from each other's experiences, contribute to the collective knowledge of local ecosystems, and promote outdoor activities.
        </p>
      </section>

      <section> 
        <h2>The Problem</h2>
        <p>
          In today's fast-paced world, many people struggle to find time to explore the outdoors and connect with nature. Additionally, social media platforms are often targeted at keeping users on the platform through algorithms aimed at keeping users addicted. Because of this, there is a lack of accessible platforms that allow individuals to share their wildlife sightings and experiences with others. This can lead to missed opportunities for learning about local ecosystems, discovering new species, and exploring the world around them.
        </p>
        <h2>The Solution</h2>
        <p>
          Sight Seeking addresses these challenges by providing a dedicated platform for wildlife enthusiasts to share their sightings and experiences. Users will view sightings posted on our platform and used it for as a resource for disocvering wildlife that they may not know exists around them. Saw a post with an awesome view of the beach? Travel to those locations to experience t for yourself? Caught a rare species of fish? Let others know so they can try? Are you out of town and looking for new adventures? Check out the listings in your area. We believe sight seeking could turn into a small startup one day largely due to the lack of competition in the market. Additionally, by offering a free platform for users to share their wildlife sightings, we make it easy for everyone to participate and contribute to the community.
        </p>

      </section>

      <section>
        <h2>Our Members</h2>
        <div className="member-grid">
          {members.map((m) => (
            <MemberCard key={m.name} member={m} />
          ))}
        </div>
      </section>
    </div>
  );
}