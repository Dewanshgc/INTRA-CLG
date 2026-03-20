# 🚀 IntraClg – All-in-One Platform for College Students

## 📌 Overview
IntraClg is a comprehensive web-based platform designed to unify academic, social, and extracurricular activities for college students into a single ecosystem.

Instead of using multiple disconnected platforms, students can:
- Access study materials  
- Participate in events  
- Connect with peers  
- Explore internships  
- Buy/sell items within campus  

---

## 🎯 Problem Statement
Students often rely on multiple systems for:
- Academics (LMS)
- Communication
- Events & clubs
- Career opportunities  

This creates a fragmented and inefficient experience.

👉 IntraClg solves this by providing a centralized platform.

---

## ✨ Key Features

### 🔐 Authentication System
- Secure Login & Signup  
- Role-based access  

### 🏠 Student Dashboard
- Personalized interface  
- Quick access to all modules  

### 📰 Social Feed
- Create posts  
- Like & comment  

### 📚 Study Hub
- Upload/download materials  
- Department & subject-based filtering  

### 🎉 Events & Clubs
- View upcoming events  
- Register easily  

### 🛒 Marketplace
- Buy & sell items within campus  

### 🎓 Tutoring System
- Peer-to-peer learning  

### 💼 Internship Portal
- Discover and share opportunities  

### 💬 Messaging
- Basic one-to-one chat  

---

## 🛠️ Tech Stack

- Backend: Django (Python)  
- Frontend: HTML, CSS, Bootstrap, JavaScript  
- Database: SQLite / MySQL  
- Version Control: Git & GitHub  
- IDE: VS Code  

---

## 🏗️ Architecture
- 3-Tier Architecture:
  - Frontend (Presentation Layer)
  - Backend (Application Layer)
  - Database (Data Layer)

- Modular Django Apps:
  - Authentication  
  - Feed  
  - Study Hub  
  - Events  
  - Marketplace  
  - Internship  

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/your-username/intraclg.git
cd intraclg

python -m venv venv

# Activate environment
venv\Scripts\activate
# or
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
