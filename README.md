# 🧠 InsightFlow — Personal AI Tutor

> **A full-stack personalized learning platform for data analysis topics — built to demonstrate adaptive content delivery, learning activity tracking, and feedback-driven tutor experiences.**

[![Backend](https://img.shields.io/badge/Backend-FastAPI-teal?style=for-the-badge&logo=fastapi)](#)
[![Frontend](https://img.shields.io/badge/Frontend-React%20%2B%20Vite-blue?style=for-the-badge&logo=react)](#)
[![Database](https://img.shields.io/badge/Database-SQLite%20%2B%20SQLAlchemy-orange?style=for-the-badge)](#)
[![Styling](https://img.shields.io/badge/Styling-Tailwind%20CSS-38bdf8?style=for-the-badge&logo=tailwindcss)](#)

---

## 👋 Hey, Welcome!

I'm **Nitin**, and I built InsightFlow to explore what a *truly personalized* learning experience looks like when you build the infrastructure for it from scratch.

Most learning platforms treat every user identically — same content, same order, same depth. InsightFlow was designed around the idea that learners have different proficiency levels, different preferred learning styles (visual, conceptual, example-driven), and different needs for detail. The platform tracks your learning activities, quiz scores, and explicit feedback to build a picture of how you're progressing — and could serve adaptive content based on that history.

The focus area is **data analysis**: topics like Python, Pandas, data visualization, statistics, and machine learning fundamentals. But the architecture is general enough to extend to any subject domain.

---

## 📸 What You Get

InsightFlow is a full-stack learning platform with:

- 👤 **User registration & login** with session-based auth
- 📚 **Course catalog** — structured data analysis topics with IDs and titles
- 🎯 **Learning activities** — tracked per user per topic (lessons, quizzes, exercises)
- 📊 **Quiz scores** — recorded with each activity for progress tracking
- 💬 **Feedback system** — learners rate topics and describe their proficiency, learning style, and detail preference
- 📈 **Activity history** — full log of what you've studied and how you've scored
- 🔐 **Secure sessions** — token-based auth with hashed passwords

---

## ✨ Features Breakdown

### 👤 **User Authentication**
Full registration and login flow:
- Register with full name, email, and password
- Passwords are hashed (never stored in plaintext)
- Login returns a session token stored server-side
- Protected routes require a valid active token
- Logout invalidates the session token immediately

### 📚 **Course Catalog**
A curated set of data analysis topics is seeded into the app:
- Each topic has a unique `topic_id` and human-readable title
- Topics span beginner to advanced: Python basics → Pandas → visualization → statistics → ML
- The course router serves the full topic list to the frontend

### 🎯 **Learning Activity Tracking**
Every time a learner interacts with a topic, an activity is recorded:

| Field | Description |
|:------|:------------|
| `topic_id` | Which topic was studied |
| `topic_title` | Human-readable topic name |
| `activity_type` | `lesson` / `quiz` / `exercise` / `review` |
| `score` | Numeric score (0–100), nullable for non-quiz activities |
| `detail` | Free-text notes or content summary |
| `created_at` | Timestamp of the activity |

Activity history lets the system (or a future AI layer) understand:
- Which topics a learner has covered
- How they're scoring over time
- Which areas need revisiting

### 💬 **Learner Feedback System**
After any topic, learners can submit structured feedback:

| Field | Description |
|:------|:------------|
| `proficiency_level` | `beginner` / `intermediate` / `advanced` |
| `learning_style` | `visual` / `conceptual` / `example-driven` / `mixed` |
| `detail_mode` | `brief` / `standard` / `deep-dive` |
| `rating` | 1–5 star rating for the topic experience |
| `quiz_score` | Score from associated quiz (0–100) |
| `comment` | Free-text feedback |

This feedback is stored per user per topic and can be used to adapt future content delivery.

### 📈 **Progress Dashboard**
The frontend surfaces:
- Recent learning activities
- Per-topic scores and history
- Feedback submitted by the learner
- Overall study statistics

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────┐
│           Browser (Client)               │
│                                          │
│  React 18 + Vite + Tailwind CSS          │
│  SPA — single-page application           │
│                                          │
│  API calls (fetch) ─────────────────┐   │
└─────────────────────────────────────┼───┘
                                      │
                        HTTP (REST)   │
                                      ▼
┌──────────────────────────────────────────┐
│            FastAPI Backend               │
│                                          │
│  /api/auth      ─ register, login, out   │
│  /api/courses   ─ topic catalog          │
│  /api/learning  ─ activities + feedback  │
│  /api/health    ─ health check           │
│                                          │
│  SQLAlchemy ORM + SQLite                 │
│  Pydantic v2 schemas                    │
│  Uvicorn ASGI server                    │
└──────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

### Frontend

| Technology | Role |
|:-----------|:-----|
| **React 18** | Component-based UI |
| **Vite 4** | Build tool + dev server |
| **Tailwind CSS 3** | Utility-first styling |
| **JavaScript (ES Module)** | No TypeScript — keeps it lean |

### Backend

| Technology | Role |
|:-----------|:-----|
| **FastAPI** | REST API with async support |
| **SQLAlchemy 2** | ORM with mapped column syntax |
| **SQLite** | Local database (zero-config) |
| **Pydantic v2** | Request/response validation |
| **python-dotenv** | Environment variable management |
| **Uvicorn** | ASGI server |

---

## 🗄️ Database Schema

```
users
├── id (PK)
├── full_name
├── email (unique)
├── password_hash
└── created_at

user_sessions
├── id (PK)
├── user_id (FK → users)
├── token_hash (unique)
└── created_at

learning_activities
├── id (PK)
├── user_id (FK → users)
├── topic_id
├── topic_title
├── activity_type     (lesson / quiz / exercise / review)
├── score             (nullable Float)
├── detail            (Text)
└── created_at

learner_feedback
├── id (PK)
├── user_id (FK → users, nullable)
├── learner_name
├── topic_id
├── proficiency_level
├── learning_style
├── detail_mode
├── rating            (1–5)
├── quiz_score
├── comment           (Text)
└── created_at
```

---

## 📁 Project Structure

```
InsightFlow---Personal-AI-Tutor/
│
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   │   ├── auth.py       # Register, login, logout endpoints
│   │   │   ├── course.py     # Topic catalog endpoint
│   │   │   ├── learning.py   # Activities + feedback CRUD
│   │   │   └── health.py     # /health check
│   │   ├── config.py         # Pydantic Settings config
│   │   ├── db.py             # SQLAlchemy engine + session
│   │   ├── models.py         # ORM models (User, Session, Activity, Feedback)
│   │   ├── schemas.py        # Pydantic request/response schemas
│   │   ├── seed_data.py      # Course topic definitions (~25 topics)
│   │   └── main.py           # FastAPI app setup + router mounting
│   ├── requirements.txt
│   └── .env.example
│
└── frontend/
    ├── src/
    │   ├── components/       # Reusable UI components
    │   ├── pages/            # Route-level page components
    │   └── main.jsx          # App entry point
    ├── index.html
    ├── package.json
    ├── tailwind.config.cjs
    └── vite.config.js
```

---

## 🚀 Getting Started

### Prerequisites
- **Node.js** 18+
- **Python** 3.10+
- **pip**

### 1. Backend Setup

```bash
cd backend

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

# Copy environment config
cp .env.example .env
# (Edit .env if needed — defaults work for local dev)

# Start the backend
uvicorn app.main:app --reload --port 8000
```

Backend runs at: **http://localhost:8000**

Useful endpoints to verify:
- `http://localhost:8000/health` → health check
- `http://localhost:8000/docs` → Swagger UI (interactive API explorer)

### 2. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at: **http://localhost:5173**

### 3. Seed the Database (Optional)

The database auto-creates tables on first startup. To seed course topic data:

```bash
cd backend
python -c "from app.seed_data import seed; seed()"
```

---

## ⚙️ Environment Variables

### Backend `.env`

```env
# Only required variable — defaults are fine for local dev
SECRET_KEY=your-secret-key-here
```

All other settings (database URL, CORS origins, etc.) have sensible defaults configured in `app/config.py` via Pydantic Settings.

---

## 🌐 API Overview

| Method | Endpoint | Auth | Description |
|:-------|:---------|:----:|:------------|
| `POST` | `/api/auth/register` | ❌ | Create new account |
| `POST` | `/api/auth/login` | ❌ | Login, returns session token |
| `POST` | `/api/auth/logout` | ✅ | Invalidate current session |
| `GET` | `/api/courses/topics` | ✅ | Get full course topic catalog |
| `POST` | `/api/learning/activity` | ✅ | Record a learning activity |
| `GET` | `/api/learning/activities` | ✅ | Get current user's activity history |
| `POST` | `/api/learning/feedback` | ✅ | Submit topic feedback |
| `GET` | `/api/learning/feedback` | ✅ | Get current user's feedback history |
| `GET` | `/health` | ❌ | Health check |

---

## 🌐 Browser Support

| Browser | Supported? |
|:--------|:----------:|
| **Chrome** | ✅ |
| **Firefox** | ✅ |
| **Edge** | ✅ |
| **Safari** | ✅ |
| **Mobile** | ✅ (responsive layout) |

---

## ⚠️ Known Limitations

| Limitation | Notes |
|:-----------|:------|
| 🗄️ SQLite only | Single-file DB, not suitable for concurrent multi-user production load |
| 🤖 No live AI integration | The "AI Tutor" label reflects the design intent — adaptive content delivery is not yet wired to an LLM |
| 📦 No deployment config | No Dockerfile or PaaS config included yet — see setup section for local dev |
| 🔑 Simple session tokens | Token stored as a hash in the DB — not using JWTs; no refresh token flow |

---

## 🗺️ Roadmap / Future Improvements

- 🤖 **Integrate an LLM** (Claude / GPT) to generate adaptive explanations based on learner feedback and activity history
- 📊 **Proficiency inference** — automatically estimate a learner's level from quiz score trends
- 🗄️ **Switch to PostgreSQL** for production readiness
- 🐳 **Add Docker + docker-compose** for easy local setup
- 🔐 **JWT with refresh tokens** for more robust auth
- 📱 **Mobile-responsive polish** across all dashboard views
- 📧 **Email verification** on registration
- 🎯 **Spaced repetition** — surface topics for review based on time since last activity + score

---

## 🤝 Contributing

Interested in extending InsightFlow? Great places to start:

- Connect an LLM API to the course router for dynamic content generation
- Build out the frontend dashboard with charts (topic score over time, activity frequency)
- Add a PostgreSQL deployment path with migration support (Alembic)
- Write integration tests for the learning activity endpoints

Open an issue to discuss before submitting a large PR — happy to collaborate! 😄

---

## 👤 Author

**Nitin Bhatti**

---

## 📜 License

Open source — for educational and portfolio use. Feel free to fork, extend, and build on top of this.

📂 **Repo:** [github.com/nitinbhatti1907/insightflow---personal-ai-tutor](https://github.com/nitinbhatti1907/insightflow---personal-ai-tutor)
