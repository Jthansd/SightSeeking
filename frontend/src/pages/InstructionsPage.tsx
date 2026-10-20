import badge from "../assets/sight-seeking-badge.png";

export default function InstructionsPage() {
    return (
        <div className="about text-page">
            <img src={badge} alt="Sight Seeking badge" className="about-badge" />
            <h1>Instructions</h1>
            <h2>Existing Features</h2>
            <h3>Navigation</h3>    
            <p>Use the menu bar at the top of the page to navigate between different sections of the application.</p>
            <h4>Explore</h4>
            <p>Use the Explore section to view current sightings.</p>
            <h4>Blog</h4>
            <p>Read blog posts from our team and community members about their experiences with Sight Seeking.</p>
            <h4>Blog</h4>
            <p>Read how our members envision Sight Seeking will evolve.</p>
            <h4>About Us</h4>
            <p>Learn about the team behind Sight Seeking and our mission.</p>
            <h4>Links</h4>
            <p>Access links to external documents on our project.</p>
            <h4>Report a Sighting</h4>
            <p>Use the Report a Sighting feature to submit new observations.</p>

            <h3>Reporting a Sighting</h3>
            <p>To report a sighting, first navigate to the "Report a Sighting" section from the menu bar. Once there, you'll be prompted to enter the details of the sighting. Simply describe what you saw, where you saw it, and any additional information that might be helpful and press the "Submit Sighting" button.</p>
            <h3>Viewing Sightings</h3>
            <p>To view existing sightings, navigate to the "Explore" section from the menu bar. Here, you'll find a list of all reported sightings.</p>
        
            <h2>Future Features</h2>
            <p>As Sight Seeking continues to evolve, we plan to introduce several exciting features, including advanced search capabilities, user profiles, and enhanced data visualization tools through an interactive gps interface. As of now, users are prompted to reporting sightings manually, entering information that may not be fully accurate. In the coming updates, we plan on automating lots of the sighting process including handling location, as well as allowing users to sort the sightings that they wish to view based on region, sighting type, etc.</p>
        </div>
    )
};