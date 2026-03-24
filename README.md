# Personal Portfolio — Streamlit

Dark, techy personal portfolio built with Streamlit.  
Multi-page: **Home · Experience · Projects · Blog · Resume**

---

## Quick Start (Local)

```bash
git clone https://github.com/yourusername/portfolio.git
cd portfolio
pip install -r requirements.txt
streamlit run Home.py
```

Open **http://localhost:8501**

---

## Project Structure

```
portfolio/
├── Home.py                      ← Entry point (homepage)
├── pages/
│   ├── 2_Experience.py          ← Timeline of roles + education + certs
│   ├── 3_Projects.py            ← Project cards with tag filter
│   ├── 4_Blog.py                ← Blog reader (Technical / Personal tabs)
│   └── 5_Resume.py              ← Resume upload & download
├── posts/
│   ├── technical/               ← Technical blog posts (.md files)
│   └── personal/                ← Personal blog posts (.md files)
├── assets/
│   └── resume.pdf               ← Drop your resume here (optional)
├── data.py                      ← ✏️  ALL personal content lives here
├── styles.py                    ← Global CSS + UI helpers
├── requirements.txt
├── app.py                       ← Hugging Face Spaces shim
└── .streamlit/
    └── config.toml              ← Theme + server config
```

---

## Customising Your Content

**Open `data.py`** and update:

| Variable        | What it controls                            |
|-----------------|---------------------------------------------|
| `PROFILE`       | Name, title, tagline, bio, social links     |
| `STATS`         | The four stat boxes on the homepage         |
| `SKILLS`        | Skill categories and tags                   |
| `PROJECTS`      | Project cards, tags, GitHub/demo links      |
| `EXPERIENCE`    | Timeline entries                            |
| `EDUCATION`     | Degree(s)                                   |
| `CERTIFICATIONS`| Certification cards                         |

No other files need to be touched for content updates.

---

## Adding Blog Posts

Create a `.md` file in `posts/technical/` or `posts/personal/`:

```markdown
---
title: My Post Title
date: March 23, 2025
excerpt: One or two sentence preview shown on the card.
tags: Python, Snowflake, DBT
---

# Post content in Markdown

Normal paragraphs, **bold**, _italic_, `code`, fenced blocks — all supported.
```

**Naming:** Prefix with `YYYY-MM-DD-` for automatic newest-first ordering.  
Example: `2025-03-23-building-a-dbt-framework.md`

---

## Adding a Permanent Resume

1. Copy your PDF to `assets/resume.pdf`
2. Commit and push:
   ```bash
   git add assets/resume.pdf
   git commit -m "add resume"
   git push
   ```
The Resume page auto-detects `assets/resume.pdf` and switches to permanent download mode.

---

## Hosting

### Option A — Streamlit Community Cloud *(recommended)*

1. Push repo to GitHub (public or private)
2. Go to **https://share.streamlit.io** → New app
3. Set: Main file path = `Home.py`
4. Click **Deploy** — live in ~2 minutes, free forever

URL format: `https://yourusername-portfolio-home-xxxx.streamlit.app`

### Option B — Hugging Face Spaces

1. Create a Space at **https://huggingface.co/spaces** (SDK: Streamlit)
2. Add remote and push:
   ```bash
   git remote add hf https://huggingface.co/spaces/yourusername/portfolio
   git push hf main
   ```
HF auto-detects `requirements.txt` and builds. Uses `app.py` as entry point (already included).

---

## Tech Stack

- [Streamlit](https://streamlit.io) — UI framework  
- Pure CSS — no extra frontend dependencies  
- Markdown files — blog storage  
- No database — everything is flat files  

---

Built with ⚡ and Streamlit.
