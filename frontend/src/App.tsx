import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import "./App.css";
import "./AboutPage.css";
import AboutPage from "./pages/AboutPage";
import BlogPage from "./pages/BlogPage";
import Sidebar from "./components/Sidebar";

export default function App() {
  return (
    <BrowserRouter>
    <Sidebar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/blog" element={<BlogPage />} />
      </Routes>
    </BrowserRouter>
  );
}