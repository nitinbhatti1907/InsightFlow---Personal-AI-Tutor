# Data Analysis with Python Learning Assistant

A full-stack course-bounded project for **Advanced Software Engineering**.

This product is intentionally limited to **one course only: Data Analysis with Python**. Instead of re-reading the same PDF and repeating existing material, it generates a fresh explanation for a requested topic, shows curated blog or documentation summaries, builds a mini-quiz, and then offers a **Learn More** flow for deeper study.

## Why this project fits the revised idea

Your educator's concern was valid: if the answer already exists in the uploaded PDF, a tool that only extracts the same information adds limited value.

This project solves that by shifting the core experience to:

- **Topic-based content generation** within a single course boundary
- **Personalized response shaping** by learning style, proficiency, and depth
- **Curated resource suggestions** with short summaries
- **Quiz generation and evaluation** after the explanation
- **Optional deeper content** after the first response
- **Educator-side feedback visibility** to detect learning bottlenecks

## Final project scope

- Course scope: **Data Analysis with Python only**
- User types: **Learners and educators**
- Current data source strategy: **curated internal course topics + curated external resource links/summaries**
- AI behavior in this version: **rule-based content generation with adaptive templates**
- Future-ready extension: can later plug in a real LLM or retrieval pipeline

## Features

### Learner side
- Pick a topic or search with your own words
- Choose:
  - proficiency level: beginner / intermediate / advanced
  - learning style: visual / hands-on / reading / exam-prep
  - detail mode: quick / standard / deep
- Generate a fresh explanation
- See recommended blogs or docs with summaries
- Attempt a quiz
- Get automated quiz evaluation and feedback
- Open **Learn More** for deeper sections, reflection questions, and a mini-project

### Educator side
- Save learner feedback to SQLite
- Review average ratings and quiz scores
- See most-requested topics
- See recent comments and detect bottlenecks

## Tech stack

### Frontend
- React 18
- Vite 4
- Tailwind CSS 3.4

### Backend
- Python 3.14.0
- FastAPI
- Pydantic v2
- SQLAlchemy 2
- SQLite

## Folder structure

```text
data-analysis-learning-assistant/
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   ├── services/
│   │   ├── config.py
│   │   ├── db.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── seed_data.py
│   ├── .env.example
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   ├── postcss.config.cjs
│   ├── tailwind.config.cjs
│   └── vite.config.js
└── README.md
```

## System design

### Backend modules
- `seed_data.py`
  - bounded course topics
  - curated learning objectives
  - examples, quiz banks, resource summaries
- `content_service.py`
  - matches topic from ID or free-text query
  - generates adaptive sections
  - provides Learn More content
- `quiz_service.py`
  - evaluates learner answers
  - returns score and reviewed explanations
- `feedback_service.py`
  - stores learner feedback
  - produces dashboard metrics
- `routers/`
  - course routes
  - learning routes
  - health route

### Frontend modules
- `Hero.jsx`
  - product summary and project positioning
- `TopicExplorer.jsx`
  - topic selection and personalization controls
- `LearningOutput.jsx`
  - generated lesson sections
- `QuizPanel.jsx`
  - interactive MCQ experience
- `LearnMorePanel.jsx`
  - deeper explanation flow
- `FeedbackForm.jsx`
  - feedback collection
- `DashboardPanel.jsx`
  - educator metrics and bottleneck visibility

## API endpoints

### Course endpoints
- `GET /api/health`
- `GET /api/course/overview`
- `GET /api/course/topics`
- `GET /api/course/topics/{topic_id}`

### Learning endpoints
- `POST /api/learning/generate`
- `POST /api/learning/learn-more`
- `POST /api/learning/evaluate-quiz`
- `POST /api/learning/feedback`
- `GET /api/learning/dashboard`

## How to run locally

## 1. Backend setup

```bash
cd backend
python -m venv .venv
```

### Windows PowerShell
```bash
.venv\Scripts\Activate.ps1
```

### macOS/Linux
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn app.main:app --reload --port 8000
```

Open:
- API root: `http://127.0.0.1:8000`
- Swagger docs: `http://127.0.0.1:8000/docs`

## 2. Frontend setup

```bash
cd frontend
npm install
npm run dev
```

Open:
- `http://localhost:5173`

## Environment configuration

### Backend
Copy `.env.example` to `.env` if needed.

### Frontend
If your backend is not on the default port, create a `.env` file in `frontend/`:

```bash
VITE_API_BASE_URL=http://127.0.0.1:8000/api
```

## Example user flow

1. Select **Pandas for Tabular Data**
2. Choose **Beginner**, **Visual**, **Standard**
3. Click **Generate content**
4. Read sections and suggested resources
5. Attempt the quiz
6. Click **Open Learn More**
7. Save learner feedback
8. Review the educator dashboard

## Suggested future improvements

- Integrate a real LLM provider for richer generation
- Add authentication for learner and educator roles
- Store learner history per user
- Add uploaded dataset analysis and notebook export
- Use topic mastery history to recommend the next topic
- Add course admin panel for topic editing
- Add stronger analytics and charts
- Connect to external blog APIs or a vetted resource database

## Important academic note

This version is intentionally designed as a **bounded educational product** for a single course because that makes the project clearer, more realistic, and easier to validate during demonstration.

That means your presentation can clearly argue:
- the problem is not “extract the same answer from PDFs”
- the solution is “generate tailored learning support around one course topic space”
- the educator benefits through feedback, quizzes, and bottleneck detection

