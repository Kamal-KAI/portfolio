"""
data.py — Your personal content lives here.
Edit this file to update your portfolio without touching any page code.
"""

# ── PERSONAL INFO ────────────────────────────────────────────────────────────
PROFILE = {
    "name":      "KAMAL KISHOR",
    "title":     "AIML ENGINEER · RESEARCHER · WRITER",
    "tagline":   (
        "A Data scientist with 3.5 years of experience delivering business "
        "impact through predictive modeling, machine learning, and automation. "
        "Skilled in Python, PySpark, and cloud platforms like Azure for building "
        "scalable solutions. Passionate about applying NLP, LLMs, and GenAI to "
        "real-world use cases in marketing and customer analytics. Recognized for "
        "automating critical workflows and bridging technical depth with stakeholder clarity."
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
    {"category": "ML/AI",         "color": "pink",   "items": ["Scikit-learn","Machine Learning", "LangChain", "Hugging Face"]},
]

# ── PROJECTS ─────────────────────────────────────────────────────────────────
PROJECTS = [
    {
        "num":    "01",
        "title":  "End-to-End Forecasting and MLOps Pipeline",
        "desc":   (
            "Built demand forecasting models deployed via Azure DevOps CI/CD, enabling automated "
            "retraining and monitoring on Azure ML for one of the largest FMCG client."
        ),
        "tags":   [("Python", "neon"), ("Snowflake", "amber"), ("AWS", "blue")],
        "github": "https://github.com/yourusername/project-one",
        "demo":   "",    # leave empty to hide
        "blog":   "",
    },
    {
        "num":    "02",
        "title":  "Predictive demand forecasting models (LightGBM, XGBoost, CatBoost)",
        "desc":   (
            "Built and deployed predictive demand forecasting models (LightGBM, XGBoost, CatBoost) "
            "using consolidated datasets (built using PySpark) across 10+ sources, resulting in a "
            "40% boost in revenue."
        ),
        "tags":   [("Machine Learning", "green"), ("Python", "pink"), ("Docker", "blue")],
        "github": "https://github.com/yourusername/project-two",
        "demo":   "",
        "blog":   "",
    },
    {
        "num":    "03",
        "title":  "Optimization of the delivery route to minimize the cost and improve the delivery time",
        "desc":   (
            "Developed and implemented machine learning algorithms for route optimization, enhancing "
            "efficiency and reducing operational costs by 13%"
        ),
        "tags":   [("ML", "amber"), ("Python", "neon"), ("Azure", "blue")],
        "github": "https://github.com/yourusername/project-three",
        "demo":   "https://yourdemo.link",
        "blog":   "",
    },
    {
        "num":    "04",
        "title":  "Developed a novel, cost-effective seismic Metamaterial for the shielding of seismic vibrations and low-frequency vibration",
        "desc":   (
            "Performed simulations in frequency and time domain study to obtain the effective design parameters using "
            "Finite Element software COMSOL Multiphysics and perfomed 1:40 scale-down lab experiments "
            "to validate the results obtained in Finite Element simulation studies"
        ),
        "tags":   [("COMSOL Multiphysics", "purple"), ("MATLAB", "blue"), ("Vibration Shaker", "green")],
        "github": "",
        "demo":   "",
        "blog":   "",
    },
    {
        "num":    "05",
        "title":  "Developed a suite of applications for manufacturing plants, streamlining operations and improving efficiency",
        "desc":   (
            "Developed a cloud-based application embedded within Power BI, facilitating "
            "users to execute CRUD operations for streamlined data management and analysis "
        ),
        "tags":   [("PySpark", "neon"), ("POWERAPPS", "purple"), ("POWER AUTOMATE", "blue"), ("POWERBI", "green")],
        "github": "",
        "demo":   "",
        "blog":   "",
    }
]

# ── EXPERIENCE ───────────────────────────────────────────────────────────────
EXPERIENCE = [
    {
        "period":   "Jan 2025 — Present",
        "role":     "AIML ENGINEER (DATA SCIENTIST)",
        "company":  "TIGER ANALYTICS",
        "location": "BANGALORE, INDIA",
        "points": [
            "Built demand forecasting models deployed via Azure DevOps CI/CD, enabling automated "
            "retraining and monitoring on Azure ML for one of the largest FMCG client.",
        ],
        "tags": [("Python", "neon"), ("MACHINE LEARNING", "amber"), ("PYSPARK", "green"), ("POWER BI", "neon")],
    },
    {
        "period":   "Jul 2023 — Dec 2024",
        "role":     "SENIOR DATA ANALYST",
        "company":  "TIGER ANALYTICS",
        "location": "BANGALORE, INDIA",
        "points": [
            "Built and deployed predictive demand forecasting models (LightGBM, XGBoost, CatBoost) "
            "using consolidated datasets (built using PySpark) across 10+ sources, resulting in a "
            "40% boost in revenue.",
        ],
        "tags": [("PYSPARK", "green"), ("PYTHON", "blue"), ("FASTAPI", "blue"), ("POWERAPPS", "neon")],
    },
    {
        "period":   "Jun 2022 — Jun 2023",
        "role":     "DATA ANALYST",
        "company":  "TIGER ANALYTICS",
        "location": "CHENNAI, INDIA",
        "points": [
            "Developed and implemented machine learning algorithms for route optimization, enhancing "
            "efficiency and reducing operational costs by 13%",
        ],
        "tags": [("SQL", "neon"), ("Python", "neon"), ("Azure", "blue"), ("POWERAPPS", "neon")],
    },
]

# ── EDUCATION ────────────────────────────────────────────────────────────────
EDUCATION = [
    {
        "degree": "MS(Research)",
        "school": "Indian Institute of Technology, Madras (IIT-M)",
        "year":   "2022",
        "detail":"CGPA: 8.6, "
                "Specialisation: Machine Design"
    },
]

# ── CERTIFICATIONS ────────────────────────────────────────────────────────────
CERTIFICATIONS = [
    {
        "title": "Kamal Kishor et al., “A clamped embedded seismic metamaterial with broadband "
        "ultra-low frequency bandgaps” presented at 12th International Conference on Metamaterials, "
        "Photonic Crystals and Plasmonics, Spain",
        "org":   "12th International Conference on Metamaterials, "
        "Photonic Crystals and Plasmonics, Spain",
        "date":  "2022",
    },
    {
        "title": "A research Article in the journal Engineering Structure: Proceedings under "
        "Elsevier Publisher entitled A Clamped Brick Seismic Metamaterial with Broadband "
        "Ultra-Low Frequency Bandgap",
        "org":   "Engineering Structure: Proceedings",
        "date":  "2023",
    },
    {
        "title": "Participated in the conference Non-Destructive Evaluation 2020 "
        "organized by Indian Society of Non-destructive Testing (ISNT)",
        "org":   "Indian Society of Non-destructive Testing (ISNT)",
        "date":  "2020",
    },
]
