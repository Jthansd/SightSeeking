import defaultPfp from "../assets/icons8-user-default-96.png";

export type Member = {
  name: string;
  bio: string;
  pfp?: string;
};

type Props = {
  member: Member;
};

export default function MemberCard({ member }: Props) {
    return (
    <div>
        <br /><img src={member.pfp || defaultPfp} alt={member.name} className="about-pfp" />
        <h4>{member.name}</h4>
        <p>{member.bio}</p>
    </div>
    );
};