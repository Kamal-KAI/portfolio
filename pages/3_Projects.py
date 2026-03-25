"""
pages/3_Projects.py — Full project grid with sidebar tag filter.
"""

import streamlit as st
from styles import inject_css, sidebar_nav, section_label, neon_divider, tag, back_home
from data import PROFILE, PROJECTS

st.set_page_config(
    page_title=f"Projects — {PROFILE['name']}",
    page_icon="🛠",
    layout="wide",
    initial_sidebar_state="expanded",
)
inject_css()
sidebar_nav("Projects")

with st.sidebar:
    st.markdown("---")
    st.markdown("[Home](/) ", unsafe_allow_html=False)
    st.markdown("---")
    st.markdown(
        '<p style="font-family:var(--mono);font-size:9px;color:var(--muted);'
        'letter-spacing:2px;text-transform:uppercase;margin-bottom:10px;">Filter by tag</p>',
        unsafe_allow_html=True,
    )
    all_tags     = sorted({t[0] for p in PROJECTS for t in p.get("tags", [])})
    selected_tag = st.selectbox("Tag", ["All"] + all_tags, label_visibility="collapsed")
    st.markdown("---")
    st.caption("Built with 💔")

# ── HEADER ───────────────────────────────────────────────────────────────────
back_home("Projects")
section_label("03. Projects")
st.markdown(
    '<h1 style="font-size:48px;font-weight:800;margin-bottom:8px;">Things I\'ve Built</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p style="color:var(--muted);font-size:14px;line-height:1.7;max-width:560px;margin-bottom:16px;">'
    'Data pipelines, tools, experiments, and side-quests. '
    'Filter by technology using the sidebar.</p>',
    unsafe_allow_html=True,
)
neon_divider()

# ── FILTER ───────────────────────────────────────────────────────────────────
filtered = (
    PROJECTS if selected_tag == "All"
    else [p for p in PROJECTS if any(t[0] == selected_tag for t in p.get("tags", []))]
)

if not filtered:
    st.info("No projects match that filter.")
    st.stop()

# ── 2-COLUMN GRID ────────────────────────────────────────────────────────────
for row_start in range(0, len(filtered), 2):
    pair = filtered[row_start:row_start + 2]
    cols = st.columns(2, gap="medium")
    for col, p in zip(cols, pair):
        tags_html  = "".join(tag(t[0], t[1]) for t in p.get("tags", []))
        links = []
        if p.get("github"):
            links.append(
                f'<a href="{p["github"]}" target="_blank" style="font-family:var(--mono);'
                f'font-size:10px;color:var(--muted);text-decoration:none;'
                f'letter-spacing:1px;margin-right:16px;">→ GitHub</a>'
            )
        if p.get("demo"):
            links.append(
                f'<a href="{p["demo"]}" target="_blank" style="font-family:var(--mono);'
                f'font-size:10px;color:var(--muted);text-decoration:none;'
                f'letter-spacing:1px;margin-right:16px;">→ Live Demo</a>'
            )
        if p.get("blog"):
            links.append(
                f'<a href="{p["blog"]}" target="_blank" style="font-family:var(--mono);'
                f'font-size:10px;color:var(--pink);text-decoration:none;letter-spacing:1px;">'
                f'→ Write-up</a>'
            )
        links_html = "".join(links)

        col.markdown(
            f'<div class="card">'
            f'<div style="font-family:var(--mono);font-size:11px;color:var(--neon);'
            f'opacity:0.4;margin-bottom:12px;">{p["num"]}</div>'
            f'<h3 style="font-size:20px;font-weight:800;margin-bottom:10px;">{p["title"]}</h3>'
            f'<p style="color:var(--muted);font-size:13px;line-height:1.7;margin-bottom:18px;">'
            f'{p["desc"]}</p>'
            f'<div style="margin-bottom:18px;">{tags_html}</div>'
            f'{links_html}'
            f'</div>',
            unsafe_allow_html=True,
        )

neon_divider()
st.page_link("/Blog", label="My blog")
