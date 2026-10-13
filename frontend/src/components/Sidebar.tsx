import { Link, useNavigate } from "react-router-dom";
import "./Sidebar.css";

type Props = {
  isOpen: boolean;
  onToggle: () => void;
  onClose: () => void;
};

export default function Sidebar({ isOpen, onToggle, onClose }: Props) {
  const navigate = useNavigate();

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
          <Link to="/" onClick={onClose}>Species</Link>
          <Link to="/" onClick={onClose}>Finder</Link>
          <Link to="/" onClick={onClose}>Hunting Seasons</Link>
          <Link to="/" onClick={onClose}>Stats</Link>
          <Link to="/blog" onClick={onClose}>Blog</Link>
          <Link to="/about" onClick={onClose}>About</Link>

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