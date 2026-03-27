"""
pages/5_Resume.py — Upload a PDF; visitors can download it.
For a permanent resume, drop resume.pdf in assets/ and see the expander below.
"""

import streamlit as st
from pathlib import Path
from styles import inject_css, sidebar_nav, section_label, neon_divider, back_home
from data import PROFILE

st.set_page_config(
    page_title=f"Resume — {PROFILE['name']}",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="auto",
)
inject_css()
sidebar_nav("Resume")

with st.sidebar:
    st.markdown("---")
    st.markdown("[Home](/) ", unsafe_allow_html=False)
    st.markdown("---")
    st.caption("Built with 💔")

# ── HEADER ───────────────────────────────────────────────────────────────────
back_home("Resume")
section_label("05. Resume")
st.markdown(
    '<h1 style="font-size:25px;font-weight:200;margin-bottom:8px;">My Resume</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p style="color:var(--muted);font-size:14px;line-height:1.7;max-width:560px;margin-bottom:16px;">'
    'You can download it directly from "Download Button"</p>',
    unsafe_allow_html=True,
)
neon_divider()

# ── CHECK FOR COMMITTED RESUME ───────────────────────────────────────────────
ASSETS_DIR     = Path(__file__).parent.parent / "assets"
PERMANENT_PDF  = ASSETS_DIR / "Kamal_AIML.pdf"
permanent_mode = PERMANENT_PDF.exists()

col_main, col_side = st.columns([2, 1], gap="large")

# with col_main:
#     if permanent_mode:
#         # Serve the committed PDF directly
#         st.markdown(
#             '<div class="resume-zone">'
#             '<div style="font-size:40px;margin-bottom:16px;">📄</div>'
#             '<p style="font-family:var(--mono);font-size:14px;font-weight:700;'
#             'color:var(--text);margin-bottom:8px;">Resume ready</p>'
#             '<p style="font-family:var(--mono);font-size:11px;color:var(--muted);">'
#             'Click below to download</p>'
#             '</div>',
#             unsafe_allow_html=True,
#         )
#         st.markdown("<br>", unsafe_allow_html=True)
#         with open(PERMANENT_PDF, "rb") as f:
#             st.download_button(
#                 label="⬇  Download Resume",
#                 data=f.read(),
#                 file_name=f"{PROFILE['name'].replace(' ', '_')}_Resume.pdf",
#                 mime="application/pdf",
#             )
#     else:
#         # Session-based upload mode
#         st.markdown(
#             '<div class="resume-zone">'
#             '<div style="font-size:40px;margin-bottom:16px;">⬆</div>'
#             '<p style="font-family:var(--mono);font-size:14px;font-weight:700;'
#             'color:var(--text);margin-bottom:8px;">Upload Your Resume</p>'
#             '<p style="font-family:var(--mono);font-size:11px;color:var(--muted);">'
#             'PDF only · Max 5 MB</p>'
#             '</div>',
#             unsafe_allow_html=True,
#         )
#         st.markdown("<br>", unsafe_allow_html=True)

#         uploaded = st.file_uploader(
#             "Choose PDF",
#             type=["pdf"],
#             label_visibility="collapsed",
#             key="resume_upload",
#         )

#         if uploaded:
#             if len(uploaded.getvalue()) > 5 * 1024 * 1024:
#                 st.error("File exceeds 5 MB. Please upload a smaller file.")
#             else:
#                 st.session_state["resume_bytes"] = uploaded.getvalue()
#                 st.session_state["resume_name"]  = uploaded.name
#                 st.success(f"✓ {uploaded.name} — ready to download")

#         if st.session_state.get("resume_bytes"):
#             st.markdown("<br>", unsafe_allow_html=True)
#             st.download_button(
#                 label="⬇  Download Resume",
#                 data=st.session_state["resume_bytes"],
#                 file_name=st.session_state.get("resume_name", "resume.pdf"),
#                 mime="application/pdf",
#             )
#             st.markdown(
#                 '<p style="font-family:var(--mono);font-size:10px;color:var(--muted);'
#                 'letter-spacing:1px;margin-top:12px;">'
#                 '⚠ Session only — resets on page refresh. '
#                 'See the tip below to make it permanent.</p>',
#                 unsafe_allow_html=True,
#             )
with col_main:
    st.markdown(
        '<div class="resume-zone">'
        '<div style="font-size:25px;margin-bottom:16px;">📄</div>'
        '<p style="font-family:var(--mono);font-size:14px;font-weight:700;'
        'color:var(--text);margin-bottom:12px;">My Resume</p>'
        '<p style="font-family:var(--mono);font-size:12px;color:var(--muted);'
        'line-height:1.8;max-width:420px;margin:0 auto 24px;">'
        'A summary of my experience, skills, projects, and education. '
        'Click below to download a copy.</p>'
        '</div>',
        unsafe_allow_html=True,
    )
    if permanent_mode:
        with open(PERMANENT_PDF, "rb") as f:
            st.download_button(
                label="⬇  Download Resume",
                data=f.read(),
                file_name=f"{PROFILE['name'].replace(' ', '_')}_Resume.pdf",
                mime="application/pdf",
            )
    else:
        st.markdown(
            '<p style="font-family:var(--mono);font-size:11px;color:var(--muted);'
            'text-align:center;margin-top:12px;">'
            '⚠ No resume found. Add <code>resume.pdf</code> to the <code>assets/</code> folder.</p>',
            unsafe_allow_html=True,
        )

with col_side:
    links_html = ""
    if PROFILE.get("linkedin"):
        links_html += (
            f'<a href="{PROFILE["linkedin"]}" target="_blank" style="display:block;'
            f'font-family:var(--mono);font-size:11px;color:var(--text);text-decoration:none;'
            f'letter-spacing:1px;border:1px solid var(--border);padding:10px 14px;margin-bottom:10px;">'
            f'LinkedIn</a>'
        )
    if PROFILE.get("github"):
        links_html += (
            f'<a href="{PROFILE["github"]}" target="_blank" style="display:block;'
            f'font-family:var(--mono);font-size:11px;color:var(--text);text-decoration:none;'
            f'letter-spacing:1px;border:1px solid var(--border);padding:10px 14px;margin-bottom:10px;">'
            f'GitHub</a>'
        )
    if PROFILE.get("email"):
        links_html += (
            f'<a href="mailto:{PROFILE["email"]}" style="display:block;'
            f'font-family:var(--mono);font-size:11px;color:var(--text);text-decoration:none;'
            f'letter-spacing:1px;border:1px solid var(--border);padding:10px 14px;">'
            f'Email Me</a>'
        )

    st.markdown(
        f'<div class="card">'
        f'<div style="font-family:var(--mono);font-size:10px;color:var(--neon);'
        f'letter-spacing:2px;text-transform:uppercase;margin-bottom:16px;">Quick Links</div>'
        f'{links_html}'
        f'</div>',
        unsafe_allow_html=True,
    )

neon_divider()

# with st.expander("💡  How to make the resume download permanent"):
#     st.markdown(f"""
# The file uploader is session-only — it resets on refresh.

# **To make it permanent:**

# 1. Place your PDF file at `assets/resume.pdf` in the project folder
# 2. Commit and push to GitHub:

# ```bash
# cp /path/to/your-resume.pdf assets/resume.pdf
# git add assets/resume.pdf
# git commit -m "add resume"
# git push
# ```

# 3. The page will automatically detect `assets/resume.pdf` and switch to permanent mode.

# The download file will be named `{PROFILE["name"].replace(" ", "_")}_Resume.pdf`.
# """)
