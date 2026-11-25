import { useCallback, useEffect, useMemo, useState, type ReactNode } from "react";
import { API_URL } from "../api";
import { AuthContext, type User } from "./authContext";

const TOKEN_KEY = "sightseeking-token";

// localStorage can throw (private browsing, blocked storage), so wrap it.
function readStoredToken() {
  try {
    return localStorage.getItem(TOKEN_KEY);
  } catch {
    return null;
  }
}

function storeToken(token: string | null) {
  try {
    if (token) {
      localStorage.setItem(TOKEN_KEY, token);
    } else {
      localStorage.removeItem(TOKEN_KEY);
    }
  } catch {
    // Not fatal: the user just won't stay logged in after a refresh.
  }
}

async function postJson(path: string, body: unknown) {
  const response = await fetch(`${API_URL}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });

  // A crashed backend sends an HTML error page instead of JSON.
  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    throw new Error(
      data.error ||
        `Something went wrong (server error ${response.status}). Please try again.`
    );
  }

  return data as { token: string; user: User };
}

export default function AuthProvider({ children }: { children: ReactNode }) {
  const [token, setToken] = useState<string | null>(readStoredToken);
  const [user, setUser] = useState<User | null>(null);
  // Only need to check with the backend if a token was saved earlier.
  const [loading, setLoading] = useState(() => token !== null);

  const startSession = useCallback((newToken: string, newUser: User) => {
    storeToken(newToken);
    setToken(newToken);
    setUser(newUser);
  }, []);

  const clearSession = useCallback(() => {
    storeToken(null);
    setToken(null);
    setUser(null);
  }, []);

  // On page load, ask the backend who the saved token belongs to.
  useEffect(() => {
    if (!token || user) return;

    const controller = new AbortController();

    fetch(`${API_URL}/api/auth/me/`, {
      headers: { Authorization: `Token ${token}` },
      signal: controller.signal,
    })
      .then(async (response) => {
        if (response.ok) {
          const data = await response.json();
          setUser(data.user);
        } else if (response.status === 401) {
          // Token was deleted (logged out elsewhere) or is invalid.
          clearSession();
        }
      })
      .catch(() => {
        // Backend unreachable: keep the token and try again next load.
      })
      .finally(() => {
        if (!controller.signal.aborted) setLoading(false);
      });

    return () => controller.abort();
  }, [token, user, clearSession]);

  const login = useCallback(
    async (username: string, password: string) => {
      const data = await postJson("/api/auth/login/", { username, password });
      startSession(data.token, data.user);
    },
    [startSession]
  );

  const register = useCallback(
    async (username: string, email: string, password: string) => {
      const data = await postJson("/api/auth/register/", {
        username,
        email,
        password,
      });
      startSession(data.token, data.user);
    },
    [startSession]
  );

  const logout = useCallback(async () => {
    if (token) {
      // Delete the token on the backend so it can't be reused.
      await fetch(`${API_URL}/api/auth/logout/`, {
        method: "POST",
        headers: { Authorization: `Token ${token}` },
      }).catch(() => {});
    }
    clearSession();
  }, [token, clearSession]);

  const value = useMemo(
    () => ({ user, token, loading, login, register, logout, clearSession }),
    [user, token, loading, login, register, logout, clearSession]
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}
