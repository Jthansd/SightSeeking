// Base URL of the Django backend.
// - Local dev: leave VITE_API_URL empty so requests stay relative ("/api/...")
//   and the Vite proxy in vite.config.ts forwards them to localhost:8000.
// - Production (Cloudflare Pages): set VITE_API_URL to the Render URL in the
//   Pages build settings; Vite bakes it into the build at `npm run build` time.
export const API_URL = import.meta.env.VITE_API_URL ?? "";
