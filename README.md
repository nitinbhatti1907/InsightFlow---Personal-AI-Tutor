# 🎓 InsightFlow — Personal AI Tutor

**An adaptive learning platform for data analysis — tracks your activities, scores, and feedback to build a picture of how you learn.**

🌐 **Live app:** [insightflow-personal-ai-tutor-1.onrender.com](https://insightflow-personal-ai-tutor-1.onrender.com)

---

## What can you learn here?

InsightFlow is built around a structured curriculum of **data analysis topics** — from Python fundamentals all the way to machine learning concepts. Every topic is tied to activities you complete and scores you earn, giving the platform the data it needs to understand where you are and what to prioritize next.

Current topic areas:

| Track | Topics Covered |
|-------|----------------|
| 🐍 Python Foundations | Variables, data types, control flow, functions, OOP basics |
| 📊 Data Wrangling | Pandas DataFrames, cleaning, merging, groupby, reshaping |
| 📈 Visualization | Matplotlib, Seaborn, Plotly, chart selection principles |
| 🔢 Statistics | Descriptive stats, probability, hypothesis testing, distributions |
| 🤖 ML Fundamentals | Scikit-learn, regression, classification, model evaluation |
| 🗃️ SQL & Databases | Queries, joins, aggregations, window functions |

---

## Your learning journey

```
  Sign up
     │
     ▼
  Browse course catalog
  (25+ topics across 6 tracks)
     │
     ▼
  Start a topic  ─────────────────────────────────────┐
     │                                                 │
     ▼                                                 │
  Complete an activity                                 │
  (lesson / quiz / exercise / review)                 │
     │                                                 │
     ▼                                                 │
  Score gets recorded ───────────────────────────────► Activity history
     │                                                 │
     ▼                                                 │
  Submit feedback ────────────────────────────────────►  Feedback store
  (proficiency · style · rating · comment)             │
     │                                                 │
     └───────────── next topic ────────────────────────┘
```

---

## The personalization layer

When you submit feedback on a topic, you tell the platform three things:

- **Your proficiency level** — `beginner` / `intermediate` / `advanced`
- **How you learn best** — `visual` / `conceptual` / `example-driven` / `mixed`
- **How much depth you want** — `brief` / `standard` / `deep-dive`

Combined with your quiz scores and activity history, this creates a learner profile that can drive adaptive content recommendations — serving the right depth, the right examples, and surfacing topics you haven't revisited in a while.

---

## Tech stack

### Backend

| | |
|---|---|
| **Framework** | FastAPI (async, auto-docs at `/docs`) |
| **ORM** | SQLAlchemy 2.x (mapped column syntax) |
| **Database** | SQLite (zero-config for dev and demo) |
| **Validation** | Pydantic v2 |
| **Auth** | Token-based sessions (hash stored in DB) |
| **Server** | Uvicorn (ASGI) |

### Frontend

| | |
|---|---|
| **Framework** | React 18 (SPA) |
| **Build tool** | Vite 4 |
| **Styling** | Tailwind CSS 3 |
| **Language** | JavaScript (ES Modules, no TypeScript) |

---

## Database schema at a glance

```
users                          user_sessions
─────────────────              ──────────────────────
id          INT  PK            id          INT  PK
full_name   STR                user_id     FK → users
email       STR  UNIQUE        token_hash  STR  UNIQUE
password_hash STR              created_at  DATETIME
created_at  DATETIME

learning_activities            learner_feedback
──────────────────────         ──────────────────────────
id            INT  PK          id                INT  PK
user_id       FK → users       user_id           FK → users
topic_id      STR              topic_id          STR
topic_title   STR              proficiency_level STR
activity_type STR              learning_style    STR
score         FLOAT (null ok)  detail_mode       STR
detail        TEXT             rating            INT (1-5)
created_at    DATETIME         quiz_score        FLOAT
                               comment           TEXT
                               created_at        DATETIME
```

---

## API endpoints

| Method | Path | Auth | Description |
|--------|------|:----:|-------------|
| `POST` | `/api/auth/register` | — | Create account |
| `POST` | `/api/auth/login` | — | Login, get session token |
| `POST` | `/api/auth/logout` | ✓ | Invalidate token |
| `GET` | `/api/courses/topics` | ✓ | Full topic catalog |
| `POST` | `/api/learning/activity` | ✓ | Record an activity |
| `GET` | `/api/learning/activities` | ✓ | Your activity history |
| `POST` | `/api/learning/feedback` | ✓ | Submit topic feedback |
| `GET` | `/api/learning/feedback` | ✓ | Your feedback history |
| `GET` | `/health` | — | Health check |

Interactive API docs available at `/docs` (Swagger UI) when running locally.

---

## Local setup

**Requirements:** Python 3.10+ · Node.js 18+

```bash
# ── Backend ──────────────────────────────────────────
cd backend
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
# API live at  http://localhost:8000
# Swagger UI   http://localhost:8000/docs

# ── Frontend ─────────────────────────────────────────
cd frontend
npm install
npm run dev
# App live at  http://localhost:5173
```

---

## Project structure

```
InsightFlow---Personal-AI-Tutor/
├── backend/
│   ├── .env.example
│   ├── requirements.txt
│   └── app/
│       ├── main.py          # FastAPI app + CORS + router mounting
│       ├── config.py        # Settings (Pydantic Settings)
│       ├── db.py            # Engine, session factory, Base
│       ├── models.py        # ORM: User, UserSession, LearningActivity, LearnerFeedback
│       ├── schemas.py       # Pydantic request/response models
│       ├── seed_data.py     # 25+ course topics with IDs and titles
│       └── routers/
│           ├── auth.py      # register · login · logout
│           ├── course.py    # topic catalog
│           ├── learning.py  # activities + feedback CRUD
│           └── health.py
└── frontend/
    ├── index.html
    ├── package.json
    ├── vite.config.js
    ├── tailwind.config.cjs
    └── src/
        ├── components/
        └── pages/
```

---

## What's next for InsightFlow

- [ ] **LLM integration** — use the learner's proficiency + style preferences to generate adaptive explanations via Claude or GPT
- [ ] **Spaced repetition engine** — surface topics for review based on time elapsed + last quiz score
- [ ] **Progress charts** — visualize score trends per topic over time
- [ ] **PostgreSQL support** — migration path for production deployments
- [ ] **JWT + refresh tokens** — replace simple session tokens
- [ ] **Email verification** — confirm accounts on registration
- [ ] **Docker compose** — one-command dev environment

---

*Built by **Nitin Bhatti** — [github.com/nitinbhatti1907](https://github.com/nitinbhatti1907)*
