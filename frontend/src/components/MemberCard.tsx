import defaultPfp from "../assets/icons8-user-default-96.png";

export type Member = {
  name: string;
  bio: string;
  blog?: string;
  pfp?: string;
};

type Props = {
  member: Member;
  show?: "blog" | "bio";
};

export default function MemberCard({ member, show = "bio" }: Props) {
  const textToShow = show === "blog" ? member.blog : member.bio;

  return (
    <div className="member-card">
      <img
        src={member.pfp || defaultPfp}
        alt={member.name}
        className="about-pfp"
      />

      <div className="member-card-content">
        <h4>{member.name}</h4>
        {textToShow && <p>{textToShow}</p>}
      </div>
    </div>
  );
}