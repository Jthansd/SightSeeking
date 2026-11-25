import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../auth/authContext";
import "./Sidebar.css";

type Props = {
  isOpen: boolean;
  onToggle: () => void;
  onClose: () => void;
};

export default function Sidebar({ isOpen, onToggle, onClose }: Props) {
  const navigate = useNavigate();
  const { user, loading, logout } = useAuth();

  return (
    <nav className="top-nav">
      <div className="nav-inner">
        <Link to="/" className="nav-brand" onClick={onClose}>
          Sight Seeking
        </Link>

        <button
          className="mobile-menu-toggle"
          onClick={onToggle}
          aria-label={isOpen ? "Close menu" : "Open menu"}
        >
          {isOpen ? "✕" : "☰"}
        </button>

        <div className={`nav-links ${isOpen ? "open" : ""}`}>
          <Link to="/" onClick={onClose}>Explore</Link>
          {/* <Link to="/" onClick={onClose}>Species</Link> */}
          {/* <Link to="/" onClick={onClose}>Stats</Link> */}
          <Link to="/blog" onClick={onClose}>Blog</Link>
          <Link to="/about" onClick={onClose}>About Us</Link>
          <Link to="/instructions" onClick={onClose}>Instructions</Link>
          <Link to="/links" onClick={onClose}>Links</Link>
          {/* <Link to="/" onClick={onClose}>Finder</Link> */}
          {/* <Link to="/" onClick={onClose}>Hunting Seasons</Link> */}

          {/* Hidden while a saved login is being checked, to avoid a flicker */}
          {!loading &&
            (user ? (
              <>
                <span className="nav-user">Hi, {user.username}</span>
                <button
                  className="nav-logout-button"
                  onClick={async () => {
                    onClose();
                    await logout();
                    navigate("/");
                  }}
                >
                  Log Out
                </button>
              </>
            ) : (
              <>
                <Link to="/login" onClick={onClose}>Log In</Link>
                <Link to="/signup" onClick={onClose}>Sign Up</Link>
              </>
            ))}

          <button
            className="nav-report-button"
            onClick={() => {
              onClose();
              navigate("/report");
            }}
          >
            Report a Sighting
          </button>
        </div>
      </div>
    </nav>
  );
}