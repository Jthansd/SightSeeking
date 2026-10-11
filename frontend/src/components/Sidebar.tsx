import { Link } from "react-router-dom";
import "./Sidebar.css";

type Props = {
  isOpen: boolean;
  onToggle: () => void;
  onClose: () => void;
};

export default function Sidebar({ isOpen, onToggle, onClose }: Props) {
  return (
    <nav className={`sidebar ${isOpen ? "open" : ""}`}>
      <button
        className="sidebar-toggle"
        onClick={onToggle}
        aria-label={isOpen ? "Close menu" : "Open menu"}
      >
        {isOpen ? "✕" : "☰"}
      </button>

      {isOpen && (
        <div className="sidebar-links">
          <Link to="/" onClick={onClose}>Home</Link>
          <Link to="/about" onClick={onClose}>About</Link>
          <Link to="/blog" onClick={onClose}>Blog</Link>
        </div>
      )}
    </nav>
  );
}