"""
Home.py — Enhanced entry point with animated hero, improved stats, and featured sections.
"""

import streamlit as st
from styles import inject_css, section_label, neon_divider, tag, sidebar_nav
from data import PROFILE, STATS, SKILLS, PROJECTS

st.set_page_config(
    page_title=f"{PROFILE['name']} — AI/ML Engineer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="auto",
)

inject_css()
sidebar_nav("Home")

# ── SIDEBAR ──────────────────
with st.sidebar:
    st.markdown("---")
    st.markdown(
        '<p style="font-family:var(--mono);font-size:9px;color:var(--muted);'
        'letter-spacing:2px;text-transform:uppercase;margin-bottom:12px;">Connect</p>',
        unsafe_allow_html=True,
    )
    if PROFILE.get("github"):
        st.markdown(f"[GitHub]({PROFILE['github']})")
    if PROFILE.get("linkedin"):
        st.markdown(f"[LinkedIn]({PROFILE['linkedin']})")
    if PROFILE.get("email"):
        st.markdown(f"[Email](mailto:{PROFILE['email']})")
    if PROFILE.get("instagram"):
        st.markdown(f"[Instagram]({PROFILE['instagram']})")
    st.markdown("---")
    st.caption("Built with 💙")

# ── HERO ────────────────
st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)

# Animated gradient name
name_parts = PROFILE["name"].split()
first = name_parts[0]
last  = " ".join(name_parts[1:]) if len(name_parts) > 1 else ""

st.markdown(
    f'<h1 class="hero-name" style="margin-bottom:12px;">{first}'
    + (f'<br><span class="outline">{last}</span>' if last else "")
    + "</h1>",
    unsafe_allow_html=True,
)

# Animated title with gradient
st.markdown(
    f'<p style="font-family:var(--mono);font-size:13px;letter-spacing:2px;'
    f'background:linear-gradient(135deg, #00ffe0 0%, #60a5fa 50%, #f472b6 100%);'
    f'-webkit-background-clip:text;-webkit-text-fill-color:transparent;'
    f'margin-bottom:20px;font-weight:600;">{PROFILE["title"]}</p>',
    unsafe_allow_html=True,
)

# Bio with better typography
st.markdown(
    f'<p class="hero-bio" style="max-width:680px;font-size:15px;line-height:2.0;">{PROFILE["tagline"]}</p>',
    unsafe_allow_html=True,
)

# CTA Buttons with improved styling
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3, _ = st.columns([1.6, 1.35, 1.6, 2.5])
with c1:
    st.page_link("pages/3_Projects.py", label="View Projects")
with c2:
    st.page_link("pages/5_Resume.py", label="📄Resume")
with c3:
    st.page_link("pages/6_Contact.py", label="Get In Touch")

st.markdown("</div>", unsafe_allow_html=True)
neon_divider()

# ── STATS WITH ENHANCED DESIGN ───────────────────
section_label("Key Metrics")
st.markdown(
    '<h3 style="font-size:20px;font-weight:500;margin-bottom:24px;color:var(--text);">Impact at a Glance</h3>',
    unsafe_allow_html=True,
)

cols = st.columns(len(STATS))
for col, s in zip(cols, STATS):
    with col:
        st.markdown(
            f'<div class="stat-box" style="position:relative;overflow:hidden;">'
            f'<div style="position:absolute;top:0;left:0;right:0;height:3px;'
            f'background:linear-gradient(90deg, var(--neon) 0%, transparent 100%);"></div>'
            f'<span class="stat-num" style="font-size:36px;">{s["num"]}</span>'
            f'<span class="stat-label" style="font-size:10px;">{s["label"]}</span>'
            f'</div>',
            unsafe_allow_html=True,
        )

neon_divider()

# ── ABOUT PREVIEW ────────────────
section_label("About Me")
st.markdown(
    '<h2 style="font-size:25px;font-weight:500;margin-bottom:24px;">Who I Am</h2>',
    unsafe_allow_html=True,
)

col_bio, col_skills = st.columns([1, 1], gap="large")

with col_bio:
    # First bio paragraph only
    st.markdown(
        f'<p style="color:var(--muted);line-height:2.0;font-size:15px;margin-bottom:20px;">'
        f'{PROFILE["bio_lines"][0]}</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<p style="color:var(--muted);line-height:2.0;font-size:15px;margin-bottom:24px;">'
        f'{PROFILE["bio_lines"][1]}</p>',
        unsafe_allow_html=True,
    )
    
    st.markdown(
        '<div style="padding:20px;background:rgba(0,255,224,0.03);border-left:3px solid var(--neon);">'
        '<p style="font-family:var(--mono);font-size:11px;color:var(--neon);'
        'letter-spacing:2px;text-transform:uppercase;margin-bottom:8px;">Currently</p>'
        '<p style="font-size:14px;color:var(--text);margin:0;">AI/ML Engineer at Tiger Analytics, '
        'building production ML systems for Fortune 500 clients</p>'
        '</div>',
        unsafe_allow_html=True,
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.page_link("pages/1_About.py", label="Full Story")

with col_skills:
    st.markdown(
        '<p style="font-family:var(--mono);font-size:10px;color:var(--muted);'
        'letter-spacing:2px;text-transform:uppercase;margin-bottom:16px;">Core Competencies</p>',
        unsafe_allow_html=True,
    )
    
    skill_cols = st.columns(2)
    for i, sk in enumerate(SKILLS[:4]):  # Show first 4 skill categories
        tags_html = "".join(tag(item, sk["color"]) for item in sk["items"][:3])  # First 3 items
        skill_cols[i % 2].markdown(
            f'<div class="skill-box" style="margin-bottom:14px;">'
            f'<div class="skill-cat">{sk["category"]}</div>'
            f'{tags_html}'
            f'</div>',
            unsafe_allow_html=True,
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.page_link("pages/1_About.py", label="All Skills & Technologies")

neon_divider()

# ── FEATURED PROJECTS ─────────────────────────────────────────────────────────
section_label("Featured Work")
st.markdown(
    '<h3 style="font-size:25px;font-weight:500;margin-bottom:12px;">Recent Projects</h3>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p style="color:var(--muted);font-size:14px;max-width:600px;margin-bottom:32px;line-height:1.8;">'
    'Selected projects showcasing ML engineering, data science, and research work. '
    'From production MLOps pipelines to published research.</p>',
    unsafe_allow_html=True,
)

# Show first 3 projects
proj_cols = st.columns(3, gap="medium")
for i, p in enumerate(PROJECTS[:3]):
    tags_html = "".join(tag(t[0], t[1]) for t in p["tags"][:3])  # First 3 tags only
    
    links_html = ""
    if p.get("github"):
        links_html += (
            f'<a href="{p["github"]}" target="_blank" style="font-family:var(--mono);'
            f'font-size:10px;color:var(--muted);text-decoration:none;'
            f'letter-spacing:1px;margin-right:16px;">→ GitHub</a>'
        )
    if p.get("demo"):
        links_html += (
            f'<a href="{p["demo"]}" target="_blank" style="font-family:var(--mono);'
            f'font-size:10px;color:var(--muted);text-decoration:none;letter-spacing:1px;">'
            f'→ Demo</a>'
        )
    
    proj_cols[i].markdown(
        f'<div class="card" style="height:100%;display:flex;flex-direction:column;">'
        f'<div style="font-family:var(--mono);font-size:10px;color:var(--neon);'
        f'opacity:0.5;margin-bottom:14px;">{p["num"]}</div>'
        f'<p style="font-size:17px;font-weight:600;margin-bottom:12px;line-height:1.3;">{p["title"]}</p>'
        f'<p style="color:var(--muted);font-size:13px;line-height:1.8;margin-bottom:18px;flex:1;">'
        f'{p["desc"][:180]}...</p>'
        f'<div style="margin-bottom:16px;">{tags_html}</div>'
        f'{links_html}'
        f'</div>',
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)
col1, col2, _ = st.columns([1.6, 1.5, 5.25])
with col1:
    st.page_link("pages/3_Projects.py", label="All Projects")
with col2:
    st.page_link("pages/4_Blog.py", label="Read Blog")

neon_divider()

# ── LATEST BLOG POSTS ─────────────────────────────────────────────────────────
section_label("Latest Writing")
st.markdown(
    '<h3 style="font-size:25px;font-weight:500;margin-bottom:12px;">From the Blog</h3>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p style="color:var(--muted);font-size:14px;max-width:600px;margin-bottom:28px;line-height:1.8;">'
    'Technical deep-dives, lessons learned, and occasional musings on data, ML, and building things.</p>',
    unsafe_allow_html=True,
)

# Placeholder for latest blog posts
blog_previews = [
    {
        "title": "Building Production-Ready RAG Systems",
        "excerpt": "A practical guide to building retrieval-augmented generation systems that actually work in production...",
        "date": "Coming Soon",
        "tag": "LLMs",
    },
    {
        "title": "MLOps on Azure: End-to-End Pipeline",
        "excerpt": "How we built an automated ML pipeline with monitoring, retraining, and deployment for a Fortune 500 client...",
        "date": "Coming Soon",
        "tag": "MLOps",
    },
]

blog_cols = st.columns(2, gap="medium")
for col, post in zip(blog_cols, blog_previews):
    col.markdown(
        f'<div class="blog-card">'
        f'<div class="blog-meta">{post["date"]}</div>'
        f'<div class="blog-title" style="font-size:18px;">{post["title"]}</div>'
        f'<div class="blog-excerpt">{post["excerpt"]}</div>'
        f'<div style="margin-top:12px;">{tag(post["tag"], "neon")}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)
st.page_link("pages/4_Blog.py", label="All Posts")

neon_divider()

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown(
    '<div style="text-align:center;padding:40px 20px;margin-top:40px;">'
    '<p style="font-family:var(--mono);font-size:11px;color:var(--muted);'
    'letter-spacing:2px;margin-bottom:12px;">OPEN TO OPPORTUNITIES</p>'
    '<p style="font-size:16px;font-weight:600;margin-bottom:12px;">Interested in collaboration?</p>'
    '<p style="color:var(--muted);font-size:14px;max-width:500px;margin:0 auto 24px;line-height:1.7;">'
    'Currently open to ML engineering roles, consulting opportunities, and interesting side projects.</p>',
    unsafe_allow_html=True,
)

fc1, fc2, _ = st.columns([1.9, 2, 4.5])
with fc1:
    st.page_link("pages/5_Resume.py", label="📄View Resume")
with fc2:
    st.page_link("pages/6_Contact.py", label="✉️ Get In Touch")

st.markdown(
    f'<p style="font-family:var(--mono);font-size:9px;color:var(--muted);'
    f'letter-spacing:1.5px;margin-top:32px;">© 2026 · {PROFILE["name"]}</p>'
    '</div>',
    unsafe_allow_html=True,
)
