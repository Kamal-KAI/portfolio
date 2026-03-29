"""
data.py — Your personal content lives here.
Edit this file to update your portfolio without touching any page code.
"""

# ── PERSONAL INFO ────────────────────────────────────────────────────────────
PROFILE = {
    "name":      "KAMAL KISHOR",
    "title":     "AI/ML ENGINEER · DATA SCIENTIST · RESEARCHER",
    "tagline":   (
        "AI/ML Engineer with 3.5+ years of experience driving business impact through "
        "advanced machine learning, predictive modeling, and intelligent automation. "
        "Specialized in leveraging Python, PySpark, and Azure to build scalable, production-ready "
        "solutions. Expert in NLP, Large Language Models, and Generative AI with a proven track "
        "record in marketing analytics and customer intelligence. Distinguished for automating "
        "critical workflows and translating complex technical concepts into actionable business insights."
    ),
    "location":  "BANGALORE, INDIA",
    "email":     "96kamal.k@gmail.com",
    "github":    "https://github.com/kamal-kai",
    "linkedin":  "https://www.linkedin.com/in/kamal-kishor-a17818146/",
    "instagram": "https://www.instagram.com/",
    "twitter":   "",   # leave empty to hide
    "bio_lines": [
        (
            "👋 Hi! I'm Kamal Kishor, an IIT Madras graduate and AI/ML Engineer passionate about "
            "transforming data into actionable intelligence. I thrive at the intersection of machine "
            "learning, automation, and scalable systems, building solutions that create measurable "
            "business impact."
        ),
        (
            "My expertise spans predictive modeling, Natural Language Processing, Large Language Models, "
            "and Generative AI. I leverage Python, PySpark, and cloud platforms (primarily Azure) to architect "
            "end-to-end ML pipelines—from data ingestion and feature engineering to model deployment and monitoring. "
            "I'm particularly passionate about solving complex problems in marketing analytics and customer intelligence."
        ),
        (
            "Beyond the technical stack, I'm known for automating critical workflows that save hundreds of hours, "
            "and for my ability to bridge the gap between data science complexity and stakeholder clarity. I believe "
            "the best solutions are both technically sound and practically adoptable."
        ),
        (
            "Outside of work, you'll find me sketching (results vary wildly😄), accepting chess challenges "
            "(and sometimes regretting them), and riding my Hunter 350 like I'm auditioning for a movie. "
            "Also on a long-term mission to visit Japan during cherry blossom season—mostly for the views, "
            "partly for the anime vibes.🌸"
        ),
    ],
}

# ── HOMEPAGE STATS ───────────────────────────────────────────────────────────
STATS = [
    {"num": "3.5+", "label": "Years Experience"},
    {"num": "15+",  "label": "Projects Delivered"},
    {"num": "40%",  "label": "Revenue Impact"},
    {"num": "13%",  "label": "Cost Reduction"},
]

# ── SKILLS ───────────────────────────────────────────────────────────────────
# color options: neon | amber | blue | green | pink | purple
SKILLS = [
    {
        "category": "Programming & Scripting",
        "color": "neon",
        "items": ["Python", "PySpark", "SQL", "Bash"]
    },
    {
        "category": "Machine Learning & AI",
        "color": "pink",
        "items": ["Scikit-learn", "XGBoost", "LightGBM", "TensorFlow", "LangChain", "Hugging Face"]
    },
    {
        "category": "Cloud & Infrastructure",
        "color": "blue",
        "items": ["Azure ML", "Azure DevOps", "Docker", "Kubernetes"]
    },
    {
        "category": "Data Engineering",
        "color": "amber",
        "items": ["PySpark", "Databricks", "Airflow", "DBT", "ETL/ELT"]
    },
    {
        "category": "Databases",
        "color": "purple",
        "items": ["PostgreSQL", "MySQL", "MongoDB"]
    },
    {
        "category": "Analytics & Visualization",
        "color": "green",
        "items": ["Power BI", "Tableau", "PowerApps", "Power Automate", "Excel"]
    },
]

# ── PROJECTS ─────────────────────────────────────────────────────────────────
PROJECTS = [
    {
        "num":    "01",
        "title":  "End-to-End MLOps Pipeline for Demand Forecasting",
        "desc":   (
            "Architected and deployed a production-grade demand forecasting system using Azure ML, featuring "
            "automated model retraining, A/B testing, and real-time monitoring. Implemented CI/CD via Azure DevOps "
            "for one of the world's largest FMCG companies, enabling dynamic inventory optimization across 1000+ SKUs."
        ),
        "tags":   [("Python", "neon"), ("Azure ML", "blue"), ("MLOps", "pink"), ("Snowflake", "amber")],
        "github": "",
        "demo":   "",
        "blog":   "",
    },
    {
        "num":    "02",
        "title":  "Multi-Model Ensemble for Revenue Forecasting",
        "desc":   (
            "Developed and productionized an ensemble forecasting system combining LightGBM, XGBoost, and CatBoost "
            "models. Built feature engineering pipeline using PySpark across 10+ data sources (sales, weather, promotions, "
            "competitor data). Achieved 40% revenue uplift through improved demand prediction accuracy and reduced stockouts."
        ),
        "tags":   [("PySpark", "amber"), ("LightGBM", "pink"), ("Feature Engineering", "green"), ("Python", "neon")],
        "github": "",
        "demo":   "",
        "blog":   "",
    },
    {
        "num":    "03",
        "title":  "Intelligent Route Optimization Engine",
        "desc":   (
            "Designed and implemented ML-based route optimization algorithms combining graph theory, vehicle routing "
            "problem (VRP) solvers, and predictive modeling. Optimized delivery routes for 500+ vehicles, reducing "
            "operational costs by 13% and improving on-time delivery by 22%. Integrated real-time traffic and weather data."
        ),
        "tags":   [("Optimization", "blue"), ("Python", "neon"), ("Graph Theory", "purple"), ("Real-time ML", "pink")],
        "github": "",
        "demo":   "",
        "blog":   "",
    },
    {
        "num":    "04",
        "title":  "Seismic Metamaterial for Vibration Shielding (Research)",
        "desc":   (
            "Pioneered novel seismic metamaterial design for low-frequency vibration attenuation using computational "
            "physics and finite element analysis. Conducted frequency/time domain simulations in COMSOL Multiphysics "
            "and validated with 1:40 scale laboratory experiments. Published in Engineering Structures (Elsevier) and "
            "presented at international conference in Spain."
        ),
        "tags":   [("COMSOL", "purple"), ("MATLAB", "amber"), ("FEA", "blue"), ("Research", "green")],
        "github": "",
        "demo":   "",
        "blog":   "",
    },
    {
        "num":    "05",
        "title":  "Cloud-Native Manufacturing Operations Suite",
        "desc":   (
            "Developed comprehensive suite of cloud-based applications for manufacturing plant operations, including "
            "inventory management, quality control tracking, and production scheduling. Built Power BI embedded app with "
            "full CRUD capabilities, integrated with PowerApps and Power Automate for end-to-end workflow automation."
        ),
        "tags":   [("PowerApps", "green"), ("Power BI", "purple"), ("Power Automate", "blue"), ("Azure", "neon")],
        "github": "",
        "demo":   "",
        "blog":   "",
    },
    {
        "num":    "06",
        "title":  "NLP-Powered Customer Sentiment Analysis System",
        "desc":   (
            "Built real-time sentiment analysis pipeline processing 100K+ customer reviews daily using transformer models "
            "(BERT, RoBERTa). Implemented multi-class classification for product feedback, automated alert system for negative "
            "sentiment spikes, and integrated insights into Power BI dashboards for stakeholder consumption."
        ),
        "tags":   [("NLP", "pink"), ("Transformers", "purple"), ("Python", "neon"), ("Real-time", "blue")],
        "github": "",
        "demo":   "",
        "blog":   "",
    },
]

# ── EXPERIENCE ───────────────────────────────────────────────────────────────
EXPERIENCE = [
    {
        "period":   "Jan 2025 — Present",
        "role":     "AI/ML ENGINEER (DATA SCIENTIST)",
        "company":  "TIGER ANALYTICS",
        "location": "BANGALORE, INDIA",
        "points": [
            "Architecting end-to-end MLOps pipelines using Azure ML and Azure DevOps, enabling automated model retraining, "
            "monitoring, and deployment for Fortune 500 FMCG client",
            "Implementing advanced forecasting models (Prophet, ARIMA, deep learning) with 95%+ accuracy for demand prediction across 1000+ SKUs",
            "Leading technical design sessions with stakeholders, translating business requirements into scalable ML solutions",
            "Mentoring junior data scientists on ML best practices, code reviews, and cloud architecture patterns",
        ],
        "tags": [("Azure ML", "blue"), ("MLOps", "pink"), ("Python", "neon"), ("Leadership", "green")],
    },
    {
        "period":   "Jul 2023 — Dec 2024",
        "role":     "SENIOR DATA ANALYST",
        "company":  "TIGER ANALYTICS",
        "location": "BANGALORE, INDIA",
        "points": [
            "Built and productionized ensemble ML models (LightGBM, XGBoost, CatBoost) achieving 40% revenue uplift through improved demand forecasting",
            "Engineered scalable feature pipelines using PySpark, consolidating 10+ disparate data sources (sales, inventory, promotions, weather, competitor data)",
            "Developed FastAPI-based model serving infrastructure with sub-100ms latency, handling 10K+ daily predictions",
            "Created automated data quality monitoring system, reducing data issues by 60% and improving model reliability",
            "Designed interactive Power BI dashboards with advanced DAX calculations, serving 50+ business users across multiple teams",
        ],
        "tags": [("PySpark", "amber"), ("ML Models", "pink"), ("FastAPI", "blue"), ("Power BI", "green")],
    },
    {
        "period":   "Jun 2022 — Jun 2023",
        "role":     "DATA ANALYST",
        "company":  "TIGER ANALYTICS",
        "location": "CHENNAI, INDIA",
        "points": [
            "Developed ML-based route optimization algorithms reducing delivery costs by 13% and improving on-time delivery by 22%",
            "Built PowerApps-based fleet management system with real-time vehicle tracking and automated dispatching",
            "Created ETL pipelines in Azure Data Factory, processing 5M+ records daily with 99.9% reliability",
            "Automated weekly reporting workflows using Power Automate, saving 20+ hours of manual work per week",
            "Collaborated with operations team to identify optimization opportunities, translating business pain points into analytical solutions",
        ],
        "tags": [("Route Optimization", "purple"), ("PowerApps", "green"), ("Azure", "blue"), ("SQL", "neon")],
    },
]

# ── EDUCATION ────────────────────────────────────────────────────────────────
EDUCATION = [
    {
        "degree": "MS(Research)",
        "school": "Indian Institute of Technology Madras (IIT-M)",
        "year":   "2020 — 2022",
        "detail": "CGPA: 8.6/10 · Specialization: Machine Design & Computational Mechanics · "
                 "Thesis: Novel Seismic Metamaterials for Low-Frequency Vibration Attenuation"
    },
    # {
    #     "degree": "Bachelor of Technology in Mechanical Engineering",
    #     "school": "BIET JHANSI",
    #     "year":   "2014 — 2018",
    #     "detail": "CGPA: 8.06/10 · Focus: Design, Manufacturing, and Thermal Engineering"
    # },
]

# ── CERTIFICATIONS & PUBLICATIONS ────────────────────────────────────────────
CERTIFICATIONS = [
    {
        "title": "International Conference Presentation: Metamaterials, Photonic Crystals and Plasmonics",
        "org":   "12th META Conference, Torremolinos, Spain",
        "date":  "Jul 2022",
    },
    {
        "title": "Research Publication: 'A Clamped Brick Seismic Metamaterial with Broadband Ultra-Low Frequency Bandgap'",
        "org":   "Engineering Structures: Proceedings (Elsevier) - IF: 5.6",
        "date":  "Apr 2023",
    },
    {
        "title": "Conference Participation: Non-Destructive Evaluation (NDE 2020)",
        "org":   "Indian Society of Non-Destructive Testing (ISNT)",
        "date":  "Dec 2020",
    },
    {
        "title": "Azure Data Scientist Associate Certification (In Progress)",
        "org":   "Microsoft",
        "date":  "Expected 2026",
    },
    {
        "title": "AWS Certified Machine Learning – Specialty (Preparing)",
        "org":   "Amazon Web Services",
        "date":  "Expected 2026",
    },
]

# ── ACHIEVEMENTS ─────────────────────────────────────────────────────────────
ACHIEVEMENTS = [
    # {
    #     "icon": "🏆",
    #     "title": "Tiger Star Award",
    #     "desc": "Recognized for exceptional performance and business impact in Q3 2024",
    #     "year": "2024"
    # },
    {
        "icon": "📊",
        "title": "40% Revenue Uplift",
        "desc": "Led forecasting initiative resulting in $2M+ incremental revenue for FMCG client",
        "year": "2024"
    },
    {
        "icon": "🎓",
        "title": "International Conference Presentation: Metamaterials, Photonic Crystals and Plasmonics",
        "desc": "12th META Conference, Torremolinos, Spain",
        "year": "2022"
    },
    # {
    #     "icon": "🎓",
    #     "title": "IIT Madras Excellence Award",
    #     "desc": "Outstanding research contribution in computational mechanics",
    #     "year": "2022"
    # },
]
