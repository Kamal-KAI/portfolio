"""
data.py — Your personal content lives here.
Edit this file to update your portfolio without touching any page code.
"""

# ── PERSONAL INFO ────────────────────────────────────────────────────────────
PROFILE = {
    "name":      "KAMAL KISHOR",
    "title":     "AIML Engineer · RESEARCHER · Writer",
    "tagline":   (
        "I am an Indian Institute of Technology, Madras (IIT-M) graduate and an AI/ML Engineer "
        "with 3+ years of experience building impactful, "
        "data-driven solutions. I specialize in predictive modeling, "
        "machine learning, and automating critical workflows. "
        "Proficient in Python, PySpark, and Azure, I develop scalable, "
        "production-ready systems. I’m passionate about applying NLP, " 
        "LLMs, and Generative AI to real-world problems in marketing " 
        "and customer analytics. I focus on bridging deep technical " 
        "expertise with clear, business-oriented insights."
    ),
    "location":  "BANGALORE, INDIA",
    "email":     "96kamal.k@email.com",
    "github":    "https://github.com/yourusername",
    "linkedin":  "https://www.linkedin.com/in/kamal-kishor-a17818146/",
    "Instagram":  "https://Instagram.com/",
    "twitter":   "",   # leave empty to hide
    "bio_lines": [
        (
            "Hi! I'm Kamal Kishor, an IIT Madras graduate and AI/ML "
            "Engineer passionate about building data-driven solutions "
            "that create real world impact. I enjoy working at the intersection "
            "of machine learning, automation, and scalable systems."
        ),
        (
            "I specialise in predictive modeling, NLP, LLMs, and Generative AI, "
            "using Python, PySpark, and Azure to solve problems in marketing and customer analytics."
        ),
        (
            "Outside of work, I sketch (results may vary), confidently accept" 
            "chess challenges (and occasionally regret them), and ride my Hunter "
            "like I’m in a movie. Also on a long-term mission to visit Japan" 
            "during cherry blossom season mostly for the views, partly for the anime vibes🌸"
        ),
    ],
}

# ── HOMEPAGE STATS ───────────────────────────────────────────────────────────
STATS = [
    {"num": "3+",  "label": "Years Experience"},
    {"num": "10+", "label": "Projects Shipped"},
    {"num": "5+",  "label": "Blog Posts"},
    {"num": "2",   "label": "Certifications"},
]

# ── SKILLS ───────────────────────────────────────────────────────────────────
# color options: neon | amber | blue | green | pink | purple
SKILLS = [
    {"category": "Languages",       "color": "neon",   "items": ["Python", "SQL", "Bash"]},
    {"category": "Cloud",           "color": "blue",   "items": ["AWS", "Azure", "GCP"]},
    {"category": "Data & ETL",      "color": "amber",  "items": ["Snowflake", "DBT", "Airflow", "Spark"]},
    {"category": "DevOps & Tools",  "color": "green",  "items": ["Docker", "Git", "Terraform"]},
    {"category": "Databases",       "color": "purple", "items": ["PostgreSQL", "MySQL", "MongoDB"]},
    {"category": "ML / AI",         "color": "pink",   "items": ["Scikit-learn", "LangChain", "Hugging Face"]},
]

# ── PROJECTS ─────────────────────────────────────────────────────────────────
PROJECTS = [
    {
        "num":    "01",
        "title":  "Project Title One",
        "desc":   (
            "A short description of what this project does, the problem it solves, "
            "and the impact it had. Use numbers — e.g. reduced latency by 40%."
        ),
        "tags":   [("Python", "neon"), ("Snowflake", "amber"), ("AWS", "blue")],
        "github": "https://github.com/yourusername/project-one",
        "demo":   "",    # leave empty to hide
        "blog":   "",
    },
    {
        "num":    "02",
        "title":  "Project Title Two",
        "desc":   (
            "What did you build? What was the challenge? "
            "What technologies did you use and what was the outcome?"
        ),
        "tags":   [("DBT", "green"), ("Airflow", "pink"), ("Docker", "blue")],
        "github": "https://github.com/yourusername/project-two",
        "demo":   "",
        "blog":   "",
    },
    {
        "num":    "03",
        "title":  "Project Title Three",
        "desc":   (
            "Two to three sentences max. "
            "Link to a write-up or demo if you have one."
        ),
        "tags":   [("ML", "amber"), ("Python", "neon"), ("Azure", "blue")],
        "github": "https://github.com/yourusername/project-three",
        "demo":   "https://yourdemo.link",
        "blog":   "",
    },
    {
        "num":    "04",
        "title":  "Project Title Four",
        "desc":   (
            "Placeholder for a fourth project. "
            "Add as many entries as you like — the grid adapts automatically."
        ),
        "tags":   [("FastAPI", "purple"), ("PostgreSQL", "blue"), ("Docker", "green")],
        "github": "",
        "demo":   "",
        "blog":   "",
    },
]

# ── EXPERIENCE ───────────────────────────────────────────────────────────────
EXPERIENCE = [
    {
        "period":   "Jan 2025 — Present",
        "role":     "Your Current Role",
        "company":  "Company Name",
        "location": "City, Country",
        "points": [
            "Key achievement or responsibility — use numbers and impact wherever possible.",
            "Another bullet point describing what you built or delivered.",
            "Third highlight — tools used, scale of work, outcomes achieved.",
        ],
        "tags": [("Python", "neon"), ("Snowflake", "amber")],
    },
    {
        "period":   "Jul 2023 — Dec 2024",
        "role":     "Previous Role Title",
        "company":  "Company Name",
        "location": "City, Country",
        "points": [
            "Key project or achievement at this role.",
            "Another highlight — use percentages and metrics.",
            "Technologies used and what you shipped.",
        ],
        "tags": [("DBT", "green"), ("AWS", "blue"), ("Docker", "blue")],
    },
    {
        "period":   "Jun 2022 — Jun 2023",
        "role":     "Earlier Role Title",
        "company":  "Company Name",
        "location": "City, Country",
        "points": [
            "Describe what you did in this position.",
            "Technologies, scale, and scope of your work.",
        ],
        "tags": [("SQL", "neon"), ("Python", "neon"), ("Azure", "blue")],
    },
]

# ── EDUCATION ────────────────────────────────────────────────────────────────
EDUCATION = [
    {
        "degree": "MS (Research)",
        "school": "Indian Institute of Technology, Madras (IIT-M)",
        "year":   "2022",
        "detail": "Optional: GPA, specialisation, thesis, honours, etc.",
    },
]

# ── CERTIFICATIONS ────────────────────────────────────────────────────────────
CERTIFICATIONS = [
    {
        "title": "Certification Name",
        "org":   "Issuing Organisation",
        "date":  "Month Year",
    },
    {
        "title": "Another Certification",
        "org":   "Issuing Organisation",
        "date":  "Month Year",
    },
]
