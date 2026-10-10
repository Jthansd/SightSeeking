import { Link } from "react-router-dom";

export default function Sidebar() {

    return(
        <nav className="sidebar">
            <Link to="/">Home</Link>
            <Link to="/about">About</Link>
            <Link to="/blog">Blog</Link>
        </nav>
    );

}