import { Link } from "react-router-dom";

export default function Links() {

  return (
    <div className="links text-page">
      <h1>Links</h1>
      <div className="link-list">
        <a href="https://docs.google.com/presentation/d/1HZclU-Pvp48y4NfisDufPINhNH3kYWII/edit?usp=drive_link&ouid=113964742563365653281&rtpof=true&sd=true" target="_blank" rel="noopener noreferrer">
          Google Slides
        </a>
        <a href="https://drive.google.com/file/d/1mFd9bCeoJsR1BV-cbqWOslptTu8up39b/view?usp=sharing" target="_blank" rel="noopener noreferrer">
          Phase 1 Report
        </a>
        <Link to="/source-code">Github and Source Code Summary</Link>
      </div>
    </div>
  );
}