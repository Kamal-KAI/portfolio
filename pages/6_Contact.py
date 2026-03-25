"""
pages/6_Contact.py — Contact page.
Mailto-based form (no backend needed), social links, availability status.
"""

import streamlit as st
import urllib.parse
from styles import inject_css, sidebar_nav, section_label, neon_divider, tag, back_home
from data import PROFILE

st.set_page_config(
    page_title=f"Contact — {PROFILE['name']}",
    page_icon="✉️",
    layout="wide",
    initial_sidebar_state="expanded",
)
inject_css()
sidebar_nav("Contact")

with st.sidebar:
    st.markdown("---")
    st.markdown("[Home](/) ", unsafe_allow_html=False)
    st.markdown("---")
    st.caption("Built with 💔")

# ── HEADER ───────────────────────────────────────────────────────────────────
back_home("Contact")
section_label("06. Contact")
st.markdown(
    '<h1 style="font-size:48px;font-weight:800;margin-bottom:8px;">Get In Touch</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p style="color:var(--muted);font-size:14px;line-height:1.7;max-width:520px;margin-bottom:16px;">'
    'Whether it\'s a project, a question, or just to say hello — '
    'my inbox is open. I try to reply within 48 hours.</p>',
    unsafe_allow_html=True,
)
neon_divider()

col_form, col_links = st.columns([3, 2], gap="large")

# ── CONTACT FORM ─────────────────────────────────────────────────────────────
with col_form:
    section_label("Send a Message")
    st.markdown("<br>", unsafe_allow_html=True)

    name    = st.text_input("Your Name",    placeholder="Jane Smith",          key="contact_name")
    email   = st.text_input("Your Email",   placeholder="jane@example.com",    key="contact_email")
    subject = st.text_input("Subject",      placeholder="Project collaboration / Question / Hello", key="contact_subject")
    message = st.text_area( "Message",      placeholder="What's on your mind?", height=160, key="contact_message")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Send Message →", key="send_btn"):
        # Validate
        if not name.strip():
            st.error("Please enter your name.")
        elif not email.strip() or "@" not in email:
            st.error("Please enter a valid email address.")
        elif not message.strip():
            st.error("Please write a message.")
        else:
            # Build a mailto link and open it via JS
            body_text = (
                f"Hi {PROFILE['name'].split()[0]},\n\n"
                f"{message.strip()}\n\n"
                f"---\n"
                f"From: {name.strip()} <{email.strip()}>"
            )
            mailto_params = urllib.parse.urlencode({
                "subject": subject.strip() or f"Message from {name.strip()}",
                "body":    body_text,
            })
            mailto_url = f"mailto:{PROFILE['email']}?{mailto_params}"

            # Open mailto in new tab via JS
            st.markdown(
                f'<script>window.open("{mailto_url}");</script>',
                unsafe_allow_html=True,
            )
            st.success(
                "✓ Your email client should open with the message pre-filled. "
                "Hit send from there!"
            )
            st.info(
                "💡 **Note:** This form uses `mailto:` — it opens your email client "
                "rather than sending directly. For a no-client alternative, "
                "reach out directly via LinkedIn or email below."
            )

# ── SOCIAL / DIRECT LINKS ────────────────────────────────────────────────────
with col_links:
    section_label("Find Me Online")

    # Availability status chip
    st.markdown(
        '<div style="display:inline-flex;align-items:center;gap:8px;'
        'background:rgba(52,211,153,0.08);border:1px solid rgba(52,211,153,0.3);'
        'padding:8px 16px;margin:12px 0 20px;">'
        '<span style="width:8px;height:8px;background:#34d399;border-radius:50%;'
        'display:inline-block;box-shadow:0 0 6px rgba(52,211,153,0.5);"></span>'
        '<span style="font-family:var(--mono);font-size:10px;letter-spacing:1.5px;'
        'color:#34d399;text-transform:uppercase;">Available for opportunities</span>'
        '</div>',
        unsafe_allow_html=True,
    )

    # Build channel list — only entries with non-empty values are shown
    contact_channels = [
        ("✉️",  "Email",     PROFILE.get("email", ""),     f"mailto:{PROFILE.get('email','')}"),
        ("💼",  "LinkedIn",  PROFILE.get("linkedin", ""),  PROFILE.get("linkedin", "")),
        ("📸",  "Instagram", PROFILE.get("instagram", ""), PROFILE.get("instagram", "")),
        ("🐙",  "GitHub",    PROFILE.get("github", ""),    PROFILE.get("github", "")),
        ("🐦",  "Twitter",   PROFILE.get("twitter", ""),   PROFILE.get("twitter", "")),
    ]

    # Render one card per channel — each as its own st.markdown call
    any_shown = False
    for icon, label, display, url in contact_channels:
        if not display:
            continue
        any_shown = True
        short = display.replace("https://", "").replace("http://", "").replace("mailto:", "")
        st.markdown(
            f'<div style="display:flex;gap:14px;align-items:center;padding:14px 16px;'
            f'background:#0d0d1c;border:1px solid #1e1e3a;margin-bottom:10px;">'
            f'<span style="font-size:20px;flex-shrink:0;">{icon}</span>'
            f'<div style="min-width:0;flex:1;">'
            f'<div style="font-family:monospace;font-size:9px;letter-spacing:2px;'
            f'color:#64748b;text-transform:uppercase;margin-bottom:3px;">{label}</div>'
            f'<div style="font-size:12px;color:#e2e8f0;overflow:hidden;'
            f'text-overflow:ellipsis;white-space:nowrap;">'
            f'<a href="{url}" target="_blank" style="color:#e2e8f0;text-decoration:none;">'
            f'{short}</a></div>'
            f'</div>'
            f'<span style="font-family:monospace;font-size:12px;color:#64748b;">↗</span>'
            f'</div>',
            unsafe_allow_html=True,
        )

    if not any_shown:
        st.markdown(
            '<p style="font-family:monospace;font-size:11px;color:#64748b;">'
            'Update your links in <code>data.py</code> → PROFILE</p>',
            unsafe_allow_html=True,
        )

    st.markdown(
        '<p style="font-family:var(--mono);font-size:10px;color:var(--muted);'
        'line-height:1.7;margin-top:12px;">'
        'Typically reply within 48 hours.<br>'
        'Best for work inquiries: LinkedIn or Email.</p>',
        unsafe_allow_html=True,
    )

neon_divider()

# # ── FAQ STYLE EXPANDERS ───────────────────────────────────────────────────────
# section_label("Common Questions")
# st.markdown("<br>", unsafe_allow_html=True)

# faqs = [
#     (
#         "Are you open to freelance / contract work?",
#         "Yes — depending on the project scope and timeline. Send me a message with details and I'll get back to you.",
#     ),
#     (
#         "Are you open to full-time roles?",
#         "Selectively. I'm most interested in data engineering, platform, or ML engineering roles. "
#         "Reach out with the role and company — I'm happy to chat.",
#     ),
#     (
#         "Can I collaborate on an open-source project?",
#         "Absolutely. Share a link to the repo and what you need — if it aligns with my interests I'd love to contribute.",
#     ),
#     (
#         "Can you speak at my event / write a guest post?",
#         "Possibly! Reach out with the topic, audience size, and format. "
#         "I'm most comfortable with data engineering, Python, and cloud topics.",
#     ),
# ]

# for q, a in faqs:
#     with st.expander(q):
#         st.markdown(
#             f'<p style="color:var(--muted);font-size:14px;line-height:1.7;margin:0;">{a}</p>',
#             unsafe_allow_html=True,
#         )
