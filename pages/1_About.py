"""
pages/1_About.py — Full About page.
Deep-dive bio, skills, what I'm currently learning, and interests.
"""

import streamlit as st
from styles import inject_css, sidebar_nav, section_label, neon_divider, tag, back_home
from data import PROFILE, SKILLS, EDUCATION, CERTIFICATIONS

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
    st.markdown("---")
    st.caption("Built with 💔")

# ── HEADER ───────────────────────────────────────────────────────────────────
back_home("About")
st.markdown(
    '<h1 style="font-size:25px;font-weight:200;margin-bottom:8px;">About Me</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    f'<p style="font-family:var(--mono);font-size:12px;letter-spacing:2px;'
    f'color:var(--neon);margin-bottom:16px;opacity:0.8;">'
    f'{PROFILE["location"]}</p>',
    unsafe_allow_html=True,
)

neon_divider()

# ── BIO ──────────────────────────────────────────────────────────────────────
col_bio, col_quick = st.columns([3, 2], gap="large")

with col_bio:
    section_label("Bio")
    st.markdown("<br>", unsafe_allow_html=True)
    for line in PROFILE["bio_lines"]:
        st.markdown(
            f'<p style="color:var(--muted);line-height:1.9;font-size:14px;margin-bottom:10px;">'
            f'{line}</p>',
            unsafe_allow_html=True,
        )

with col_quick:
    section_label("Quick facts")
    st.markdown("<br>", unsafe_allow_html=True)

    facts = [
        ("📍", "Location",    PROFILE.get("location", "—")),
        ("🎓", "Education",   EDUCATION[0]["school"] if EDUCATION else "—"),
        ("💼", "Currently",   "AIML ENGINEER at TIGER ANALYTICS" ),
        ("✍️", "Writing",     "Technical & personal blog"),
        ("🌐", "Languages",   "English · Hindi · Learning Spanish"),
    ]
    for icon, label, value in facts:
        st.markdown(
            f'<div style="display:flex;gap:10px;align-items:flex-start;'
            f'margin-bottom:16px;padding-bottom:14px;border-bottom:1px solid var(--border);">'
            f'<span style="font-size:16px;margin-top:2px;">{icon}</span>'
            f'<div>'
            f'<div style="font-family:var(--mono);font-size:9px;letter-spacing:2px;'
            f'color:var(--muted);text-transform:uppercase;margin-bottom:2px;">{label}</div>'
            f'<div style="font-size:14px;color:var(--text);">{value}</div>'
            f'</div></div>',
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    if PROFILE.get("github"):
        st.markdown(f"[GitHub]({PROFILE['github']})")
    if PROFILE.get("linkedin"):
        st.markdown(f"[LinkedIn]({PROFILE['linkedin']})")
    if PROFILE.get("email"):
        st.markdown(f"[Email](mailto:{PROFILE['email']})")

neon_divider()

# ── SKILLS ───────────────────────────────────────────────────────────────────
section_label("Skills & Technologies")
st.markdown(
    '<h2 style="font-size:25px;font-weight:200;margin-bottom:20px;">What I Work With</h2>',
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
section_label("Currently Learning")
st.markdown(
    '<h4 style="font-size:20px;font-weight:50;margin-bottom:10px;">What\'s on My Radar</h4>',
    unsafe_allow_html=True,
)

# Edit these to reflect what you're actually learning right now
learning_items = [
    {
        "icon":  "🤖",
        "title": "LLMs & Retrieval-Augmented Generation",
        "desc":  "Exploring LangChain, vector databases, and how to build production-grade RAG pipelines.",
        "color": "pink",
    },
    {
        "icon":  "⚙️",
        "title": "Apache Iceberg & the Modern Data Lakehouse",
        "desc":  "Table formats, time-travel queries, and how Iceberg compares to Delta Lake and Hudi.",
        "color": "amber",
    },
    {
        "icon":  "🌐",
        "title": "Building in Public",
        "desc":  "Writing more, shipping more, sharing the process — not just the polished outcome.",
        "color": "blue",
    },
]

learn_cols = st.columns(len(learning_items), gap="medium")
for col, item in zip(learn_cols, learning_items):
    col.markdown(
        f'<div class="card" style="text-align:left;">'
        f'<div style="font-size:28px;margin-bottom:14px;">{item["icon"]}</div>'
        f'<p style="font-size:18px;font-weight:600;margin-bottom:10px;line-height:1.3;">'
        f'{item["title"]}</p>'
        f'<p style="color:var(--muted);font-size:13px;line-height:1.7;margin:0;">'
        f'{item["desc"]}</p>'
        f'</div>',
        unsafe_allow_html=True,
    )

neon_divider()

# ── INTERESTS / OUTSIDE WORK ──────────────────────────────────────────────────
section_label("Outside Work")
st.markdown(
    '<h2 style="font-size:25px;font-weight:200;margin-bottom:28px;">Beyond the Terminal</h2>',
    unsafe_allow_html=True,
)

# Replace with your actual interests
interests = [
    ("📚", "Reading — mostly non-fiction, systems thinking, and the occasional novel"),
    ("✍️", "Writing — this blog is part of a commitment to write more in public"),
    ("🏃", "Running — 5K three times a week, slow but consistent"),
    ("🎮", "Gaming — strategy games when I need to shut the brain off"),
]

for icon, text in interests:
    st.markdown(
        f'<div style="display:flex;gap:14px;align-items:flex-start;'
        f'padding:16px 0;border-bottom:1px solid var(--border);">'
        f'<span style="font-size:20px;">{icon}</span>'
        f'<p style="color:var(--muted);font-size:14px;line-height:1.7;margin:0;">{text}</p>'
        f'</div>',
        unsafe_allow_html=True,
    )

neon_divider()

c1, c2, _ = st.columns([1.5, 1.5, 4.25])
with c1:
    st.page_link("pages/2_Experience.py", label="My Experience")
with c2:
    st.page_link("pages/6_Contact.py",    label="Get In Touch")
