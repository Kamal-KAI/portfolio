"""
pages/2_Experience.py — Timeline of roles, education, certifications.
"""

import streamlit as st
from styles import inject_css, sidebar_nav, section_label, neon_divider, tag, back_home
from data import PROFILE, EXPERIENCE, EDUCATION, CERTIFICATIONS

st.set_page_config(
    page_title=f"Experience — {PROFILE['name']}",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)
inject_css()
sidebar_nav("Experience")

with st.sidebar:
    st.markdown("---")
    st.page_link("Home.py", label="← Home")
    st.markdown("---")
    st.caption("Built with Streamlit")

# ── HEADER ───────────────────────────────────────────────────────────────────
back_home("Experience")
section_label("02. Experience")
st.markdown(
    '<h1 style="font-size:48px;font-weight:800;margin-bottom:8px;">Where I\'ve Worked</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p style="color:var(--muted);font-size:14px;line-height:1.7;max-width:560px;margin-bottom:16px;">'
    'A timeline of roles, responsibilities, and what I shipped along the way.</p>',
    unsafe_allow_html=True,
)
neon_divider()

# ── EXPERIENCE TIMELINE ──────────────────────────────────────────────────────
section_label("Professional Experience")
st.markdown("<br>", unsafe_allow_html=True)

for exp in EXPERIENCE:
    tags_html   = "".join(tag(t[0], t[1]) for t in exp.get("tags", []))
    points_html = "".join(
        f'<li style="font-size:13px;color:var(--muted);line-height:1.7;'
        f'margin-bottom:8px;list-style:none;padding-left:4px;">'
        f'<span style="color:var(--neon);opacity:0.6;margin-right:6px;">▸</span>{pt}</li>'
        for pt in exp["points"]
    )
    st.markdown(
        f'<div class="timeline-item">'
        f'  <div class="timeline-dot"></div>'
        f'  <div class="timeline-period">{exp["period"]}</div>'
        f'  <div class="timeline-role">{exp["role"]}</div>'
        f'  <div class="timeline-company">{exp["company"]} · {exp["location"]}</div>'
        f'  <ul style="padding:0;margin:0 0 16px;">{points_html}</ul>'
        f'  <div>{tags_html}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

neon_divider()

# ── EDUCATION ────────────────────────────────────────────────────────────────
section_label("Education")
st.markdown("<br>", unsafe_allow_html=True)

for edu in EDUCATION:
    detail_html = (
        f'<p style="color:var(--muted);font-size:12px;margin-top:8px;margin-bottom:0;">'
        f'{edu["detail"]}</p>'
        if edu.get("detail") else ""
    )
    st.markdown(
        f'<div class="card">'
        f'<div style="font-family:var(--mono);font-size:10px;color:var(--neon);'
        f'letter-spacing:2px;text-transform:uppercase;margin-bottom:6px;">{edu["year"]}</div>'
        f'<h3 style="font-size:22px;font-weight:800;margin-bottom:4px;">{edu["degree"]}</h3>'
        f'<p style="color:var(--muted);font-size:14px;margin-bottom:0;">{edu["school"]}</p>'
        f'{detail_html}'
        f'</div>',
        unsafe_allow_html=True,
    )

neon_divider()

# ── CERTIFICATIONS ────────────────────────────────────────────────────────────
section_label("Certifications")
st.markdown("<br>", unsafe_allow_html=True)

cert_cols = st.columns(2, gap="medium")
for i, cert in enumerate(CERTIFICATIONS):
    cert_cols[i % 2].markdown(
        f'<div class="card" style="margin-bottom:14px;">'
        f'<div style="font-family:var(--mono);font-size:9px;color:var(--neon);'
        f'letter-spacing:2px;text-transform:uppercase;margin-bottom:6px;">{cert["date"]}</div>'
        f'<h4 style="font-size:16px;font-weight:700;margin-bottom:4px;">{cert["title"]}</h4>'
        f'<p style="color:var(--muted);font-size:12px;margin:0;">{cert["org"]}</p>'
        f'</div>',
        unsafe_allow_html=True,
    )

neon_divider()
st.page_link("pages/3_Projects.py", label="See My Projects →")
