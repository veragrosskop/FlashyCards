# 📚 Flashcards Web App

A full-stack flashcard learning platform built with **Django**. 

Language learning has always been a hobby of mine, but there aren't many entertaining 
websites/apps out there that gamify the driest material of all: vocabulary. Well... 
Actually there is a couple, but usually you get blocked by a paywall pretty fast. 
I wanted to offer a gamified free approach, with a full set of study tools. 
Anything I'd want myself.

---
## ⚠️ This website is in active development

Please refer for an overview of the features that I'm currently implementing below.
I've worked on this app over the last years as a personal project and am currently in the process of refactoring code,
implementing new features and will merge these into this repository as soon as they are completed. 

---
## 🚀 Features

### 🧠 Smart Flashcards

* - [ ] Create and manage flashcards directly in the browser
* - [ ] Support for **bidirectional learning** (foreign → native and native → foreign)
* - [ ] Organize cards into **decks**, **topics**, and **resources**

### 📂 Flexible Input

* - [ ] Upload flashcards via file (e.g. CSV, txt, json)
* - [ ] Manual card creation through intuitive UI

### ⏱ Study System

* - [ ] Integrated **Pomodoro timer** for focused study sessions
* - [ ] Multiple **study modes** (e.g. drills, spaced repetition)
* - [ ] Multiple **quiz types**:

  * - [ ] Multiple choice
  * - [ ] Typed answers
  * - [ ] (Planned) listening-based quizzes

### 📊 Progress Tracking

* - [ ] Track study sessions and performance over time
* - [ ] Visual **calendar tracker** (bullet journal style)
* - [ ] Monitor learning streaks and consistency

### 🏆 Gamification

* - [ ] Unlock **achievements** based on study behavior
* - [ ] Encourage consistent learning habits

### 🔗 Social & Sharing

* - [ ] Share decks with other users
* - [ ] (Planned) public deck discovery

### 🎨 Customization

* - [ ] Multiple UI **color themes**
* - [ ] User-specific preferences

### 🔮 Future Features
* - [ ] NLP integration for auto-categorization 
* - [ ] Background tasks (Celery)

---

## 🏗️ Tech Stack

* **Backend**: Django (Python)
* **Frontend**: HTML, CSS (Django Templates)
* **Database**: SQLite (development)

**Django app structure**:

```
project_apps/
├── core/              # Base templates, global layout
├── cards/             # Flashcards & decks
├── games/             # Study sessions, quiz logic
├── achievements/      # Gamification system
├── users/             # Authentication & profiles
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/veragrosskop/FlashyCards.git
cd FlashyCards
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set environment variables

Create a `.env` file:

```
SECRET_KEY=your-secret-key
DEBUG=True
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Start server

```bash
python manage.py runserver
```

---

## 🧠 Future Improvements

* 🤖 NLP-based automatic card categorization
* 🧩 Semantic similarity & association-based learning
* 🔊 Text-to-speech for listening exercises
* 🌍 Public deck marketplace
* 📱 Mobile-friendly UI improvements

---

## 📬 Contact
Feel free to reach out or connect:

* GitHub: https://github.com/veragrosskop
* Linkedin: www.linkedin.com/in/vera-grosskop

---

## ⭐️ Show Your Support

If you like this project, consider giving it a star!
