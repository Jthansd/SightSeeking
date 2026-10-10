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
    <div>
        <br /><img src={member.pfp || defaultPfp} alt={member.name} className="about-pfp" />
        <h4>{member.name}</h4>
        {textToShow && <p>{textToShow}</p>}
    </div>
    );
};