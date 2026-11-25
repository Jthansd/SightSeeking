import { createContext, useContext } from "react";

export type User = {
  id: number;
  username: string;
  email: string;
};

export type AuthContextValue = {
  user: User | null;
  // Sent to the backend as "Authorization: Token <token>".
  token: string | null;
  // True while checking a saved token on page load.
  loading: boolean;
  login: (username: string, password: string) => Promise<void>;
  register: (username: string, email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  // Forget the session locally (e.g. when the backend says the token is invalid).
  clearSession: () => void;
};

export const AuthContext = createContext<AuthContextValue | null>(null);

// Use in any component: const { user, login, logout } = useAuth();
export function useAuth() {
  const value = useContext(AuthContext);

  if (!value) {
    throw new Error("useAuth must be used inside <AuthProvider>");
  }

  return value;
}
