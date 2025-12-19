# Full Stack Web Application – 
##  Project Overview
This project is a full-stack web application developed as part of a placement assignment.  
It consists of a landing page and an admin panel for managing projects, clients, contact form submissions, and newsletter subscriptions.

The application follows the given requirements and uses a blue-themed professional UI inspired by a consultation/marketing website.
---
##  Tech Stack

### Frontend
- HTML
- CSS (Blue Theme)
- JavaScript (Fetch API)

### Backend
- Python
- Flask
- Flask-CORS

### Database
- SQLite (auto-created, no external database required)

---
##  Project Structure
```
Fullstackproject/
│
├── backend/
│   ├── app.py
│   ├── database.db
│   ├── models.sql
│   └── requirements.txt
│
├── frontend/
│   ├── css/
│   │   └── style.css
│   ├── admin.html
│   └── index.html
│
└── README.md
````
---
##  Features
### Landing Page
- **Our Projects**
  - Displays projects fetched dynamically from backend
  - Shows project image, name, description
  - Dummy “Read More” button
- **Happy Clients**
  - Displays client testimonials dynamically
  - Includes client image, description, name, and designation
- **Contact Form**
  - Full Name
  - Email Address
  - Mobile Number
  - City
  - Submits data to backend
- **Newsletter Subscription**
  - Stores subscribed email addresses
---
### Admin Panel
- Add new projects
- Add new clients
- View contact form submissions
- View newsletter subscribers
---
##  API Endpoints

| Method | Endpoint | Description |
|------|--------|------------|
| GET | `/projects` | Fetch all projects |
| POST | `/projects` | Add a project |
| GET | `/clients` | Fetch all clients |
| POST | `/clients` | Add a client |
| GET | `/contact` | View contact form submissions |
| POST | `/contact` | Submit contact form |
| GET | `/subscribe` | View subscribers |
| POST | `/subscribe` | Subscribe email |
---
## How to Run the Project (Windows)
### Step 1: Backend Setup
```powershell
cd backend
pip install -r requirements.txt
python app.py
````
You should see:
```
Running on http://127.0.0.1:5000
```
### Step 2: Frontend
Open the following files directly in your browser:
* `frontend/admin.html`
* `frontend/index.html`
---
##  Application Flow
```
Admin Panel
   ↓
SQLite Database (Auto-created)
   ↓
Landing Page fetches & displays data
```

