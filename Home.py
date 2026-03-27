"""
Home.py — Entry point. Hero · Stats · About · Featured Projects.
"""

import streamlit as st
from styles import inject_css, section_label, neon_divider, tag, sidebar_nav
from data import PROFILE, STATS, SKILLS, PROJECTS

st.set_page_config(
    page_title=f"{PROFILE['name']}",
    page_icon="",
    layout="wide",
    initial_sidebar_state="auto",
)

inject_css()
sidebar_nav("Home")

# ── SIDEBAR ──────────────────
with st.sidebar:
    st.markdown("---")
    if PROFILE.get("github"):
        st.markdown(f"[GitHub]({PROFILE['github']})")
    if PROFILE.get("linkedin"):
        st.markdown(f"[LinkedIn]({PROFILE['linkedin']})")
    if PROFILE.get("email"):
        st.markdown(f"[Email](mailto:{PROFILE['email']})")
    if PROFILE.get("Instagram"):
        st.markdown(f"[Instagram]({PROFILE['Instagram']})")
    st.markdown("---")
    st.caption("Built with 💔")

# ── HERO ────────────────
st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)

name_parts = PROFILE["name"].split()
first = name_parts[0]
last  = " ".join(name_parts[1:]) if len(name_parts) > 1 else ""
st.markdown(
    f'<h1 class="hero-name">{first}'
    + (f'<br><span class="outline">{last}</span>' if last else "")
    + "</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    f'<p style="font-family:var(--mono);font-size:13px;letter-spacing:1.5px;'
    f'color:var(--neon);margin-bottom:18px;opacity:0.9;">{PROFILE["title"]}</p>',
    unsafe_allow_html=True,
)
st.markdown(f'<p class="hero-bio">{PROFILE["tagline"]}</p>', unsafe_allow_html=True)

c1, c2, c3, _ = st.columns([1.4, 1.2, 1.4, 2.25])
with c1:
    st.page_link("pages/3_Projects.py", label="View Projects")
with c2:
    st.page_link("pages/5_Resume.py",   label="My Resume")
with c3:
    st.page_link("pages/6_Contact.py",  label="Get In Touch")

st.markdown("</div>", unsafe_allow_html=True)
neon_divider()

# ── STATS ───────────────────
section_label("At a glance")
cols = st.columns(len(STATS))
for col, s in zip(cols, STATS):
    with col:
        st.markdown(
            f'<div class="stat-box">'
            f'<span class="stat-num">{s["num"]}</span>'
            f'<span class="stat-label">{s["label"]}</span>'
            f'</div>',
            unsafe_allow_html=True,
        )

neon_divider()

# ── ABOUT ────────────────
section_label("About Me")
st.markdown(
    '<h2 style="font-size:25px;font-weight:200;margin-bottom:20px;">Who I Am</h2>',
    unsafe_allow_html=True,
)

col_bio, col_skills = st.columns([1, 1], gap="large")

with col_bio:
    for line in PROFILE["bio_lines"]:
        st.markdown(
            f'<p style="color:var(--muted);line-height:1.9;font-size:14px;margin-bottom:16px;">'
            f'{line}</p>',
            unsafe_allow_html=True,
        )
    st.markdown("<br>", unsafe_allow_html=True)
    st.page_link("pages/2_Experience.py", label="Full Experience")

with col_skills:
    skill_cols = st.columns(2)
    for i, sk in enumerate(SKILLS):
        tags_html = "".join(tag(item, sk["color"]) for item in sk["items"])
        skill_cols[i % 2].markdown(
            f'<div class="skill-box">'
            f'<div class="skill-cat">{sk["category"]}</div>'
            f'{tags_html}'
            f'</div>',
            unsafe_allow_html=True,
        )

neon_divider()

# ── FEATURED PROJECTS ─────────────────────────────────────────────────────────
section_label("Featured Work")
st.markdown(
    '<h3 style="font-size:25px;font-weight:200;margin-bottom:28px;">Recent Projects</h3>',
    unsafe_allow_html=True,
)

proj_cols = st.columns(2, gap="medium")
for i, p in enumerate(PROJECTS[:2]):
    tags_html  = "".join(tag(t[0], t[1]) for t in p["tags"])
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
            f'→ Live Demo</a>'
        )
    proj_cols[i].markdown(
        f'<div class="card">'
        f'<div style="font-family:var(--mono);font-size:11px;color:var(--neon);'
        f'opacity:0.4;margin-bottom:12px;">{p["num"]}</div>'
        f'<h3 style="font-size:16px;margin-bottom:10px;">{p["title"]}</h3>'
        f'<p style="color:var(--muted);font-size:13px;line-height:1.7;margin-bottom:16px;">'
        f'{p["desc"]}</p>'
        f'<div style="margin-bottom:16px;">{tags_html}</div>'
        f'{links_html}'
        f'</div>',
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)
st.page_link("pages/3_Projects.py", label="View Projects")
neon_divider()

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown(
    f'<div style="text-align:center;padding:20px 0;">'
    f'<p style="font-family:var(--mono);font-size:10px;color:var(--muted);letter-spacing:1.5px;">'
    f'© 2026 {PROFILE["name"]}'
    f'</p></div>',
    unsafe_allow_html=True,
)
