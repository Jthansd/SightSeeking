import badge from "../assets/sight-seeking-badge.png";
import MemberCard, {type Member} from "../components/MemberCard";
import { members } from "../data/members";




export default function AboutPage() {
  return (
    <div className="about">
      <img src={badge} alt="Sight Seeking badge" className="about-badge" />
      <h1>About Us</h1>

      <section>
        <h2>Our Mission</h2>
        <p>
          Sight Seeking is a company dedicated to encouraging outdoor exploration through
          providing a comprehensive platform for nature enthusiasts to discover and share
          their outdoor experiences.
        </p>
      </section>

      <section>
        <h2><br />Our Members</h2>
        <div className="member-grid">
          {members.map((m) => (
            <MemberCard key={m.name} member={m} />
          ))}
        </div>
      </section>
    </div>
  );
}