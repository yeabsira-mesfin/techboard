# TechBoard 🧑‍💻

A niche job board built for tech roles - remote, hybrid, and onsite. Employers can post listings, seekers can apply, and everyone gets a clean dashboard to manage their side of things.

Built as a portfolio project using Django, deployed on Render.

🔗 **Live site:** techboard (https://techboard-y5ej.onrender.com/jobs/)

---

## What it does

TechBoard connects tech employers with job seekers in a lightweight, no-fluff interface.

**If you're looking for a job**, you can browse and search listings by title, location, or tech stack, read full job details, and apply with a cover letter and resume PDF - all from one place. Your dashboard shows every application you've submitted and its current status.

**If you're hiring**, you get a simple employer dashboard where you can post new listings, edit or remove them, and review everyone who applied. You can mark applicants as Reviewed, Shortlisted, or Rejected directly from the applicants page.

---

## Tech stack

- **Backend:** Django 6 (Python)
- **Database:** SQLite (dev) / PostgreSQL (production)
- **Frontend:** Tailwind CSS via CDN
- **File storage:** Django FileField with local media serving
- **Deployment:** Render (free tier)
- **Auth:** Django's built-in auth system with a custom Profile model for roles

---

## Running it locally

**1. Clone the repo**
```bash
git clone https://github.com/yeabsira-mesfin/techboard.git
cd techboard
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create a `.env` file in the root**