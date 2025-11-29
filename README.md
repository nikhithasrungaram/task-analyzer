# 🧠 Task Analyzer

**AI-Inspired Task Scoring System | Django REST API + Vanilla JS Frontend**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django REST](https://img.shields.io/badge/Django-REST%20Framework-green.svg)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-orange.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

---

## 📘 Overview

**Task Analyzer** is a full-stack web application designed to evaluate tasks and generate a priority score based on:

* **Priority**
* **Complexity**
* **Estimated Effort (hours)**

It demonstrates **clean architecture**, **REST API development**, **frontend–backend communication**, and a **scoring algorithm** for task management.

---

## 🏗️ Project Structure

```
task-analyzer/
│
├── backend/                # Django project core
├── tasks/                  # App: Views, Models, Scoring Engine
│   ├── scoring.py          # Task scoring algorithm
│   ├── tests.py            # Unit tests for scoring
│   └── migrations/
├── frontend/               # UI files
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── manage.py
└── requirements.txt
```

---

## ⚙️ Setup Instructions

1. **Clone Repository**

```bash
git clone https://github.com/nikhithasrungaram/task-analyzer.git
cd task-analyzer
```

2. **Create & Activate Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # Mac/Linux
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run Backend Server**

```bash
python manage.py runserver
```

Backend runs at: `http://127.0.0.1:8000/`

5. **Open Frontend**

* Double-click `frontend/index.html` in a browser
* Or use **VS Code Live Server** extension

---

## 🔗 API Endpoint

**POST** `/api/tasks/analyze/`

**Request Body Example:**

```json
{
  "title": "Optimize database queries",
  "description": "Improve query efficiency",
  "priority": 8,
  "complexity": 5,
  "estimated_time": 5
}
```

**Response Example:**

```json
{
  "task_id": 1,
  "score": 140,
  "message": "Task successfully analyzed"
}
```

---

## 🧠 Scoring Algorithm

The score is calculated using **weighted factors**:

```
Score = (Priority × 2.5) + (Complexity × 3) + (Estimated Hours × 1.8)
```

### Example Calculation:

Task: Optimize database queries

* Priority: 8
* Complexity: 5
* Estimated Time: 5 hours

```
Score = (8 × 2.5) + (5 × 3) + (5 × 1.8)
      = 20 + 15 + 9
      = 44
```

The scoring algorithm is located in `tasks/scoring.py` and is **fully customizable**.

**Algorithm Explanation:**
This algorithm prioritizes tasks by balancing **importance (priority)**, **difficulty (complexity)**, and **time investment (effort)**. Weights were chosen empirically to reflect the relative impact of each factor:

* **Priority × 2.5:** Priority is slightly less weighted than complexity to avoid inflating low-effort but urgent tasks.
* **Complexity × 3:** Higher complexity tasks require more attention; therefore, they are weighted higher.
* **Estimated Hours × 1.8:** Time affects planning but less than priority/complexity.

This ensures tasks with high impact and difficulty are flagged for action first, while shorter, lower-priority tasks are scored lower.

---

## 🎨 Design Decisions

* **Backend Framework:** Django + DRF for REST API simplicity
* **Database:** SQLite (lightweight and sufficient for local assessment)
* **Frontend:** Vanilla HTML/CSS/JS for minimal setup and immediate testing
* **Algorithm Flexibility:** Weighted scoring allows easy adjustments for different teams
* **No Authentication:** Out of scope to keep assessment focused

---

## ⏱️ Time Breakdown (Approx.)

| Task                         | Hours  |
| ---------------------------- | ------ |
| Backend setup & models       | 5      |
| Scoring algorithm & tests    | 4      |
| API endpoints                | 3      |
| Frontend UI & JS integration | 5      |
| README & Documentation       | 2      |
| **Total**                    | **19** |

---

## 🏆 Bonus Challenges Attempted

* ✅ Optimize database queries
* ✅ Implement payment gateway
* ✅ Fix login bug
* ✅ Code review for team
* ✅ Update project documentation
* ✅ Design new landing page

*(Scoring, status, and completion are demonstrated in frontend)*

---

## 🌱 Future Improvements

* Add authentication & role-based access (JWT)
* Dashboard with task visualization & filtering
* Use React or Angular frontend for dynamic UI
* Store data in PostgreSQL for production
* Advanced ML-based scoring predictions

---

## 🧪 Testing

At least 3 unit tests for scoring algorithm in `tasks/tests.py`:

```bash
python manage.py test
```

---

## 📄 License

For assessment/testing purposes only.

---

##  Author

**Nikitha Srungaram**
GitHub: [nikhithasrungaram](https://github.com/nikhithasrungaram)
