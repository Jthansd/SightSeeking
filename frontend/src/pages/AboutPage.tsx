import badge from "../assets/sight-seeking-badge.png";
import MemberCard, {type Member} from "../components/MemberCard";


const members: Member[] = [
    {
      name: "Jonathan Wilson",
      bio: "Jonathan has a bachelor's degree in Software Engineering, and is now studying for a master's degree in Computer Science at San Diego State University. He looks forward to contributing to our team's success and engineering the means to allow our users to experience the great outdoors on a new level."
    },
    {
      name: "Seth Vanegas",
      bio: "Seth needs to add a introduction here :)"
    },
    {
      name: "Fadhil Al Salihi",
      bio: "Fadhil needs to add a introduction here :)"
    },
    {
      name: "Hosna Hyat",
      bio: "Hosna needs to add a introduction here :)"
    },
    {
      name: "Vlad Jerohhin",
      bio: "Vlad needs to add a introduction here :)"
    },
    {
      name: "Christena Bell",
      bio: "Christena needs to add a introduction here :)"
    }
  ];

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