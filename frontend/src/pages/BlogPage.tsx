import MemberCard from "../components/MemberCard";
import { members } from "../data/members";

export default function BlogPage() {
  const withPosts = members.filter((m) => m.blog);

  return (
    <div className="blog">
      <h1>Team Blog</h1>
      {withPosts.map((m) => (
        <MemberCard key={m.name} member={m} show="blog" />
      ))}
    </div>
  );
}