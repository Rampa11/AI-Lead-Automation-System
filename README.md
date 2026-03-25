# 🚀 AI Lead Automation Platform

AI-powered lead automation system that classifies inbound leads, triggers automated responses, and provides real-time analytics through a full-stack architecture.

---

## 🌍 Live Demo

- 🔗 **API (FastAPI):** https://ai-lead-automation-system.onrender.com
- 📊 **Dashboard (Streamlit):** https://ai-lead-automation-system.streamlit.app/

---

## 🧠 Overview

This project solves a common business problem:

> Companies lose leads due to slow response times, scattered communication channels, and manual workflows.

This system automates the entire pipeline:
- Capturing leads
- Classifying intent (HOT / WARM / COLD)
- Triggering responses
- Storing data
- Visualizing insights

---

## ⚙️ Features

- ✅ AI-powered lead classification (with fallback logic)
- ✅ Automated email responses via SendGrid
- ✅ FastAPI backend (production deployed)
- ✅ Real-time lead dashboard (Streamlit)
- ✅ REST API for lead ingestion
- ✅ Persistent storage using SQLAlchemy
- ✅ Production deployment (Render + Streamlit Cloud)
- ✅ Debugged and production-tested workflow

---

## 🏗️ Architecture
User (Streamlit UI)
↓
FastAPI Backend (Render)
↓
AI Processing (OpenAI / Fallback Logic)
↓
Database (SQLAlchemy)
↓
Automation Layer (SendGrid Email)
↓
Dashboard Analytics (Streamlit)

---

## 🔧 Tech Stack

- **Backend:** FastAPI, Python
- **Frontend:** Streamlit
- **Database:** SQLAlchemy (SQLite/Postgres-ready)
- **AI:** OpenAI API (with fallback logic)
- **Email Automation:** SendGrid API
- **Deployment:** Render (backend), Streamlit Cloud (frontend)
- **Version Control:** Git & GitHub

---

## 📡 API Endpoints

### Create Lead

GET /leads/
#### Example Request:
```json
{
  "name": "Akpor",
  "email": "example@email.com",
  "message": "I want 5000 units urgently"
}

Get All Leads
GET /leads/

---

## 📊 Dashboard Features
Submit new leads
View all stored leads
Analyze lead distribution (HOT / WARM / COLD)
Real-time updates from backend API

---

## 🔐 Environment Variables

Create a .env file:
  SENDGRID_API_KEY=your_sendgrid_key
  EMAIL_USER=your_verified_email
  OPENAI_API_KEY=your_openai_key (optional)

---

## ▶️ Run Locally
Backend
  uvicorn app.main:app --reload

Frontend
  streamlit run dashboard.py

---

## 🚀 Deployment
Backend deployed on Render
Frontend deployed on Streamlit Cloud
Environment variables securely managed in production

---

## 🧠 Key Learnings
Production debugging (API, async tasks, env variables)
External API integration (SendGrid, OpenAI)
Full-stack system design
Deployment and DevOps fundamentals
Real-time data pipelines

---

## 🎯 Use Case

This system can be used by:

SaaS companies
E-commerce businesses
Agencies handling inbound leads
Sales teams needing automation

---

## 🎯 Use Case

This system can be used by:

SaaS companies
E-commerce businesses
Agencies handling inbound leads
Sales teams needing automation

---

## 👤 Author

Akpor Unukogbon

GitHub: https://github.com/Rampa11
LinkedIn: www.linkedin.com/in/akpor-unukogbon-104532b8
