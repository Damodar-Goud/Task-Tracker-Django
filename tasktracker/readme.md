# 📝 Damodar's Task Manager

A sleek, full-stack Django web app for managing personal tasks with search, pagination, dashboard analytics, and JWT-secured REST API. Built with clean UI, modular views, and recruiter-ready polish.

## 🚀 Live Demo

🔗 [https://damodar-task-app.herokuapp.com](https://damodar-task-app.herokuapp.com)

## 📸 Screenshots

![Dashboard](static/images/dashboard_preview.png)
![Task List](static/images/task_list_preview.png)

## ✨ Features

- 🔐 User authentication (login/register/logout)
- 🧠 Smart task search with pagination
- 📊 Dashboard with task stats and Chart.js visualization
- 🧱 Modular views with class-based and function-based logic
- 🔄 REST API secured with JWT (DRF + SimpleJWT)
- 🎨 Branded UI with custom logo, Bootstrap styling, and favicon
- 🌐 Deployed on Heroku with PostgreSQL

## 🛠️ Tech Stack

- Django 4.x
- Django REST Framework
- Bootstrap 5
- Chart.js
- Heroku (Gunicorn + Whitenoise)
- PostgreSQL

## 📦 Installation

```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
