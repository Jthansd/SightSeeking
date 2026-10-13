import { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import AboutPage from "./pages/AboutPage";
import BlogPage from "./pages/BlogPage";
import Sidebar from "./components/Sidebar";
import LinksPage from "./pages/Links";
import "./App.css";
import "./AboutPage.css";

export default function App() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <BrowserRouter>
      <Sidebar
        isOpen={isOpen}
        onToggle={() => setIsOpen(!isOpen)}
        onClose={() => setIsOpen(false)}
      />

      <main className="page-content">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/blog" element={<BlogPage />} />
          <Route path="/links" element={<LinksPage />} />
        </Routes>
      </main>
    </BrowserRouter>
  );
}