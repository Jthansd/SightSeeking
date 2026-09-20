import { useEffect, useState } from "react";

type Member = {
  id: number;
  first_name: string;
  last_name: string;
  grade_in_years: number;
};

const API_URL = "http://127.0.0.1:8000";

export default function App() {
  const [members, setMembers] = useState<Member[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch(`${API_URL}/api/members/`)
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then((data: Member[]) => setMembers(data))
      .catch((e: Error) => setError(e.message));
  }, []);

  return (
    <main>
      <h1>Members</h1>
      {error && <p>Error: {error}</p>}
      <ul>
        {members.map((m) => (
          <li key={m.id}>
            {m.first_name} {m.last_name} (grade {m.grade_in_years})
          </li>
        ))}
      </ul>
    </main>
  );
}