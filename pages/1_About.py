"""
pages/1_About.py — Enhanced About page with AI Assistant
Deep-dive bio, skills, achievements, and AI-powered Q&A
"""

import streamlit as st
from styles import inject_css, sidebar_nav, section_label, neon_divider, tag, back_home
from data import PROFILE, SKILLS, EDUCATION, CERTIFICATIONS, ACHIEVEMENTS

# Import AI assistant
try:
    from ai_assistant import render_ai_assistant
    AI_ENABLED = True
except ImportError:
    AI_ENABLED = False

st.set_page_config(
    page_title=f"About — {PROFILE['name']}",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="auto",
)
inject_css()
sidebar_nav("About")

with st.sidebar:
    st.markdown("---")
    st.markdown("[Home](/) ", unsafe_allow_html=False)
    
    # AI Assistant in sidebar
    if AI_ENABLED:
        render_ai_assistant(context="about", position="sidebar")
    
    st.markdown("---")
    st.caption("Built with 💙")

# ── HEADER ───────────────────────────────────────────────────────────────────
back_home("About")
st.markdown(
    '<h1 style="font-size:25px;font-weight:200;margin-bottom:12px;background:linear-gradient(135deg, #00ffe0 0%, #60a5fa 100%);'
    '-webkit-background-clip:text;-webkit-text-fill-color:transparent;">About Me</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    f'<p style="font-family:var(--mono);font-size:11px;letter-spacing:2px;'
    f'color:var(--neon);margin-bottom:24px;opacity:0.8;">📍 {PROFILE["location"]}</p>',
    unsafe_allow_html=True,
)

neon_divider()

# ── AI ASSISTANT (MAIN) ──────────────────────────────────────────────────────
if AI_ENABLED:
    render_ai_assistant(context="about", position="main")
    neon_divider()

# ── BIO ──────────────────────────────────────────────────────────────────────
col_bio, col_quick = st.columns([3, 2], gap="large")

with col_bio:
    section_label("👨‍💻Biography")
    st.markdown("<br>", unsafe_allow_html=True)
    for line in PROFILE["bio_lines"]:
        st.markdown(
            f'<p style="color:var(--muted);line-height:2.0;font-size:15px;margin-bottom:18px;">'
            f'{line}</p>',
            unsafe_allow_html=True,
        )

with col_quick:
    section_label("Quick Facts")
    st.markdown("<br>", unsafe_allow_html=True)

    facts = [
        ("📍", "Location",    PROFILE.get("location", "—")),
        ("🎓", "Education",   "IIT Madras (MS)"),
        ("💼", "Currently",   "AI/ML Engineer at Tiger Analytics"),
        ("🔬", "Research",    "Published in Elsevier · Presented in Spain"),
        ("✍️", "Writing",     "Technical & Personal Blog"),
        ("🌐", "Languages",   "English · Hindi · Learning Spanish"),
    ]
    for icon, label, value in facts:
        st.markdown(
            f'<div style="display:flex;gap:12px;align-items:flex-start;'
            f'margin-bottom:20px;padding-bottom:16px;border-bottom:1px solid var(--border);">'
            f'<span style="font-size:18px;margin-top:2px;">{icon}</span>'
            f'<div style="flex:1;">'
            f'<div style="font-family:var(--mono);font-size:9px;letter-spacing:2px;'
            f'color:var(--muted);text-transform:uppercase;margin-bottom:4px;">{label}</div>'
            f'<div style="font-size:14px;color:var(--text);line-height:1.5;">{value}</div>'
            f'</div></div>',
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Social links with icons
    social_links = []
    if PROFILE.get("github"):
        social_links.append(f'<a href="{PROFILE["github"]}" target="_blank" style="color:var(--text);text-decoration:none;'
                          f'border:1px solid var(--border);padding:8px 16px;display:inline-block;margin:4px;'
                          f'font-family:var(--mono);font-size:10px;letter-spacing:1px;transition:all 0.2s;"'
                          f'onmouseover="this.style.borderColor=\'var(--neon)\';this.style.color=\'var(--neon)\';"'
                          f'onmouseout="this.style.borderColor=\'var(--border)\';this.style.color=\'var(--text)\';">'
                          f'GitHub ↗</a>')
    if PROFILE.get("linkedin"):
        social_links.append(f'<a href="{PROFILE["linkedin"]}" target="_blank" style="color:var(--text);text-decoration:none;'
                          f'border:1px solid var(--border);padding:8px 16px;display:inline-block;margin:4px;'
                          f'font-family:var(--mono);font-size:10px;letter-spacing:1px;transition:all 0.2s;"'
                          f'onmouseover="this.style.borderColor=\'var(--blue)\';this.style.color=\'var(--blue)\';"'
                          f'onmouseout="this.style.borderColor=\'var(--border)\';this.style.color=\'var(--text)\';">'
                          f'LinkedIn ↗</a>')
    if PROFILE.get("email"):
        social_links.append(f'<a href="mailto:{PROFILE["email"]}" style="color:var(--text);text-decoration:none;'
                          f'border:1px solid var(--border);padding:8px 16px;display:inline-block;margin:4px;'
                          f'font-family:var(--mono);font-size:10px;letter-spacing:1px;transition:all 0.2s;"'
                          f'onmouseover="this.style.borderColor=\'var(--pink)\';this.style.color=\'var(--pink)\';"'
                          f'onmouseout="this.style.borderColor=\'var(--border)\';this.style.color=\'var(--text)\';">'
                          f'Email ↗</a>')
    
    st.markdown('<div style="display:flex;flex-wrap:wrap;gap:4px;">' + ''.join(social_links) + '</div>', 
                unsafe_allow_html=True)

neon_divider()

# ── ACHIEVEMENTS ─────────────────────────────────────────────────────────────
section_label("🏆Key Achievements")
st.markdown(
    '<h2 style="font-size:24px;font-weight:600;margin-bottom:24px;">Highlights & Recognition</h2>',
    unsafe_allow_html=True,
)

achievement_cols = st.columns(2, gap="medium")
for i, ach in enumerate(ACHIEVEMENTS):
    achievement_cols[i % 2].markdown(
        f'<div class="card" style="position:relative;padding:24px;">'
        f'<div style="position:absolute;top:-12px;right:20px;background:var(--bg);'
        f'padding:4px 12px;font-family:var(--mono);font-size:9px;color:var(--neon);'
        f'border:1px solid var(--neon);letter-spacing:2px;">{ach["year"]}</div>'
        f'<div style="font-size:32px;margin-bottom:12px;">{ach["icon"]}</div>'
        f'<p style="font-size:16px;font-weight:600;margin-bottom:8px;line-height:1.3;">'
        f'{ach["title"]}</p>'
        f'<p style="color:var(--muted);font-size:13px;line-height:1.7;margin:0;">'
        f'{ach["desc"]}</p>'
        f'</div>',
        unsafe_allow_html=True,
    )

neon_divider()

# ── SKILLS ───────────────────────────────────────────────────────────────────
section_label("Skills & Technologies")
st.markdown(
    '<h2 style="font-size:24px;font-weight:600;margin-bottom:24px;">What I Work With</h2>',
    unsafe_allow_html=True,
)

skill_cols = st.columns(3, gap="medium")
for i, sk in enumerate(SKILLS):
    tags_html = "".join(tag(item, sk["color"]) for item in sk["items"])
    skill_cols[i % 3].markdown(
        f'<div class="skill-box">'
        f'<div class="skill-cat">{sk["category"]}</div>'
        f'{tags_html}'
        f'</div>',
        unsafe_allow_html=True,
    )

neon_divider()

# ── CURRENTLY LEARNING ──────────
section_label("🎯Current Focus")
st.markdown(
    '<h2 style="font-size:24px;font-weight:600;margin-bottom:20px;">What\'s on My Radar</h2>',
    unsafe_allow_html=True,
)

learning_items = [
    {
        "icon":  "🤖",
        "title": "Advanced LLM Applications",
        "desc":  "Building production-grade RAG systems with LangChain, vector databases (Pinecone, Weaviate), "
                 "and exploring fine-tuning techniques for domain-specific applications.",
        "color": "pink",
    },
    {
        "icon":  "☁️",
        "title": "Cloud-Native ML Architecture",
        "desc":  "Deepening expertise in Kubernetes, serverless ML deployment, and building cost-efficient "
                 "ML infrastructure on Azure and AWS.",
        "color": "blue",
    },
    {
        "icon":  "📊",
        "title": "MLOps & Experiment Tracking",
        "desc":  "Mastering MLflow, Weights & Biases, and DVC for reproducible ML experiments. Building "
                 "automated model versioning and A/B testing frameworks.",
        "color": "amber",
    },
    {
        "icon":  "🌐",
        "title": "Building in Public",
        "desc":  "Documenting learnings through technical blogs, open-source contributions, and sharing "
                 "the messy middle—not just the polished outcome.",
        "color": "green",
    },
]

learn_cols = st.columns(2, gap="medium")
for i, item in enumerate(learning_items):
    learn_cols[i % 2].markdown(
        f'<div class="card" style="text-align:left;padding:24px;">'
        f'<div style="font-size:32px;margin-bottom:14px;">{item["icon"]}</div>'
        f'<p style="font-size:17px;font-weight:600;margin-bottom:10px;line-height:1.3;">'
        f'{item["title"]}</p>'
        f'<p style="color:var(--muted);font-size:13px;line-height:1.8;margin:0;">'
        f'{item["desc"]}</p>'
        f'</div>',
        unsafe_allow_html=True,
    )

neon_divider()

# ── INTERESTS / OUTSIDE WORK ──────────────────────────────────────────────────
section_label("Beyond the Terminal")
st.markdown(
    '<h2 style="font-size:24px;font-weight:600;margin-bottom:28px;">Life Outside Work</h2>',
    unsafe_allow_html=True,
)

interests = [
    ("📚", "Reading", "Non-fiction, systems thinking, behavioral economics, and the occasional sci-fi thriller"),
    ("✍️", "Writing", "Maintaining this blog as a commitment to learn in public and document my journey"),
    ("🏃", "Running", "5K three times a week—slow but consistent. Working toward a sub-25 minute mark"),
    ("♟️", "Chess", "Rated 1600+ on chess.com. Always up for a friendly game (or a competitive one)"),
    ("🏍️", "Riding", "Weekend warrior on my Hunter 350. Dream trip: Leh-Ladakh someday"),
    ("🎮", "Gaming", "Strategy games (Civilization, Age of Empires) when I need to shut the analytical brain off"),
    ("🎨", "Sketching", "Casual sketching—portraits and landscapes. Results vary from 'decent' to 'abstract art'"),
]

interest_cols = st.columns(2, gap="medium")
for i, (icon, title, text) in enumerate(interests):
    interest_cols[i % 2].markdown(
        f'<div style="display:flex;gap:14px;align-items:flex-start;'
        f'padding:20px;border-left:2px solid var(--border);margin-bottom:16px;">'
        f'<span style="font-size:24px;flex-shrink:0;">{icon}</span>'
        f'<div>'
        f'<p style="font-weight:600;font-size:14px;margin-bottom:6px;color:var(--text);">{title}</p>'
        f'<p style="color:var(--muted);font-size:13px;line-height:1.7;margin:0;">{text}</p>'
        f'</div></div>',
        unsafe_allow_html=True,
    )

neon_divider()

# ── CTA SECTION ───────────────────────────────────────────────────────────────
st.markdown(
    '<div style="text-align:center;padding:40px 20px;background:linear-gradient(135deg, rgba(0,255,224,0.05) 0%, rgba(96,165,250,0.05) 100%);'
    'border:1px solid var(--border);margin:32px 0;">'
    '<p style="font-size:18px;font-weight:600;margin-bottom:12px;">Let\'s Connect</p>'
    '<p style="color:var(--muted);font-size:14px;max-width:500px;margin:0 auto 24px;line-height:1.7;">'
    'Interested in collaboration, have a question, or just want to chat about ML, data, or motorcycles?</p>',
    unsafe_allow_html=True,
)

c1, c2, c3, _ = st.columns([1.5, 1.5, 1.5, 3.75])
with c1:
    st.page_link("pages/2_Experience.py", label="My Experience")
with c2:
    st.page_link("pages/3_Projects.py", label="View Projects")
with c3:
    st.page_link("pages/6_Contact.py", label="Get In Touch")

st.markdown('</div>', unsafe_allow_html=True)
