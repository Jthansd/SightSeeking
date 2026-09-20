# SightSeeking

Wildlife and nature sighting map. React (Vite + TypeScript) frontend, Django backend, Supabase Postgres database.

## Prerequisites (please install)

- Git
- Python 3.11 or newer
- Node.js (current LTS)

## Backend setup

```powershell
cd backend
python -m venv .venv
.venv\Scripts\activate          # Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Create `backend/.env` by copying `backend/.env.example`, then fill in `DATABASE_URL`.
Use the Supabase **session pooler** connection string (host contains `pooler.supabase.com`,
port 5432), not the direct connection. Ask the project owner for the password.
Never commit `.env`.

```powershell
python manage.py migrate
python manage.py runserver
```

Check http://127.0.0.1:8000/api/health/ returns `{"status": "ok"}`.

## Frontend setup

```powershell
cd frontend
npm install
npm run dev
```

Open http://localhost:5173 (use `localhost`, not `127.0.0.1`, because of CORS).
Both servers must be running at the same time, each in its own terminal.

## Workflow

- Do not commit directly to `main`. Create a branch, push it, and open a pull request.
- Run `git status` before every commit and make sure `.env` and `node_modules` are not listed.