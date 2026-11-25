import { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import AboutPage from "./pages/AboutPage";
import BlogPage from "./pages/BlogPage";
import Sidebar from "./components/Sidebar";
import LinksPage from "./pages/Links";
import "./App.css";
import "./AboutPage.css";
import ReportSightingPage from "./pages/ReportSightingPage";
import InstructionsPage from "./pages/InstructionsPage";
import SourceCode from "./pages/SourceCode";
import LoginPage from "./pages/LoginPage";
import SignupPage from "./pages/SignupPage";
import AuthProvider from "./auth/AuthProvider";

export default function App() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    // AuthProvider makes the logged-in user available to every page.
    <AuthProvider>
      <BrowserRouter>
        <Sidebar
          isOpen={isOpen}
          onToggle={() => setIsOpen(!isOpen)}
          onClose={() => setIsOpen(false)}
        />

        <main className="page-content">
          <Routes>
            <Route path="/report" element={<ReportSightingPage />} />
            <Route path="/" element={<HomePage />} />
            <Route path="/about" element={<AboutPage />} />
            <Route path="/blog" element={<BlogPage />} />
            <Route path="/links" element={<LinksPage />} />
            <Route path="/instructions" element={<InstructionsPage />} />
            <Route path="/source-code" element={<SourceCode />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/signup" element={<SignupPage />} />
          </Routes>
        </main>
      </BrowserRouter>
    </AuthProvider>
  );
}
