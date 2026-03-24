"""
styles.py — Global CSS injection and shared UI helpers.
Called at the top of every page.
"""

GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap');

:root {
  --neon:    #00ffe0;
  --amber:   #f59e0b;
  --pink:    #f472b6;
  --blue:    #60a5fa;
  --green:   #34d399;
  --purple:  #a78bfa;
  --bg:      #080810;
  --bg2:     #0d0d1c;
  --bg3:     #111128;
  --text:    #e2e8f0;
  --muted:   #64748b;
  --border:  #1e1e3a;
  --mono:    'Space Mono', monospace;
  --sans:    'Syne', sans-serif;
  --glow:    0 0 18px rgba(0,255,224,0.35);
}

html, body, [data-testid="stApp"] {
  background-color: var(--bg) !important;
  font-family: var(--sans) !important;
}
[data-testid="stSidebar"] {
  background-color: var(--bg2) !important;
  border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { font-family: var(--mono) !important; }

#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }

/* Tighter overall layout */
.block-container {
  padding-top: 0.75rem !important;
  padding-bottom: 1rem !important;
  padding-left: 1.5rem !important;
  padding-right: 1.5rem !important;
  max-width: 980px !important;
}

/* Remove extra gap Streamlit adds above first element */
.block-container > div:first-child { margin-top: 0 !important; }

/* Tighter vertical gap between st elements */
[data-testid="stVerticalBlock"] > [data-testid="stVerticalBlockBorderWrapper"],
[data-testid="stVerticalBlock"] > div { gap: 0.4rem !important; }

/* Back-home nav bar */
.back-nav {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--border);
}
.back-nav a {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--muted);
  text-decoration: none;
  transition: color 0.2s;
}
.back-nav a:hover { color: var(--neon); }
.back-nav .sep {
  font-family: var(--mono); font-size: 10px;
  color: var(--border);
}
.back-nav .current {
  font-family: var(--mono); font-size: 10px;
  letter-spacing: 2px; text-transform: uppercase;
  color: var(--neon); opacity: 0.7;
}

/* Wider page_link / nav buttons */
[data-testid="stPageLink"] a,
[data-testid="stPageLink"] a:visited {
  font-family: var(--mono) !important;
  font-size: 10px !important;
  letter-spacing: 1.5px !important;
  text-transform: uppercase !important;
  color: var(--text) !important;
  border: 1px solid var(--border) !important;
  padding: 10px 22px !important;
  white-space: nowrap !important;
  min-width: 160px !important;
  display: inline-block !important;
  text-decoration: none !important;
  transition: border-color 0.2s, color 0.2s !important;
}
[data-testid="stPageLink"] a:hover {
  border-color: var(--neon) !important;
  color: var(--neon) !important;
}

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--neon); border-radius: 99px; }

h1, h2, h3, h4 { font-family: var(--sans) !important; font-weight: 800 !important; }

/* Grid background */
.grid-bg {
  position: fixed; inset: 0; z-index: -1; pointer-events: none;
  background-image:
    linear-gradient(rgba(0,255,224,0.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,255,224,0.025) 1px, transparent 1px);
  background-size: 50px 50px;
}

/* Section label */
.sec-label {
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: 4px;
  color: var(--neon);
  text-transform: uppercase;
  opacity: 0.8;
  margin-bottom: 4px;
}

/* Sidebar logo */
.sidebar-logo {
  font-family: var(--mono);
  font-size: 13px;
  color: var(--neon);
  letter-spacing: 2px;
  padding: 20px 16px 28px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 16px;
  text-shadow: 0 0 12px rgba(0,255,224,0.4);
}

/* Cards */
.card {
  background: var(--bg2);
  border: 1px solid var(--border);
  padding: 28px;
  margin-bottom: 20px;
  position: relative;
}
.card::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg, var(--neon), transparent);
  opacity: 0.4;
}

/* Tags */
.tag {
  display: inline-block;
  font-family: var(--mono);
  font-size: 9px;
  padding: 3px 9px;
  border-radius: 2px;
  margin: 2px;
  letter-spacing: 1px;
  text-transform: uppercase;
}
.tag-neon   { background:rgba(0,255,224,0.08);  border:1px solid rgba(0,255,224,0.3);  color:#00ffe0; }
.tag-amber  { background:rgba(245,158,11,0.1);  border:1px solid rgba(245,158,11,0.3); color:#f59e0b; }
.tag-blue   { background:rgba(96,165,250,0.1);  border:1px solid rgba(96,165,250,0.3); color:#60a5fa; }
.tag-green  { background:rgba(52,211,153,0.1);  border:1px solid rgba(52,211,153,0.3); color:#34d399; }
.tag-pink   { background:rgba(244,114,182,0.1); border:1px solid rgba(244,114,182,0.3);color:#f472b6; }
.tag-purple { background:rgba(167,139,250,0.1); border:1px solid rgba(167,139,250,0.3);color:#a78bfa; }

/* Neon divider */
.neon-divider {
  height: 1px;
  background: linear-gradient(90deg, var(--neon) 0%, transparent 70%);
  opacity: 0.2;
  margin: 20px 0;
}

/* Timeline */
.timeline-item {
  border-left: 1px solid rgba(0,255,224,0.2);
  padding: 0 0 40px 32px;
  position: relative;
  margin-left: 10px;
}
.timeline-item:last-child { padding-bottom: 0; }
.timeline-dot {
  position: absolute; left: -5px; top: 5px;
  width: 10px; height: 10px;
  background: var(--neon); border-radius: 50%;
  box-shadow: 0 0 10px rgba(0,255,224,0.5);
}
.timeline-period {
  font-family: var(--mono); font-size: 10px;
  letter-spacing: 2px; color: var(--neon);
  text-transform: uppercase; margin-bottom: 6px;
}
.timeline-role {
  font-family: var(--sans); font-size: 22px;
  font-weight: 800; color: var(--text); margin-bottom: 2px;
}
.timeline-company { font-size: 13px; color: var(--muted); margin-bottom: 14px; }

/* Hero */
.hero-wrap { padding: 8px 0 32px; }
.hero-tag {
  font-family: var(--mono); font-size: 11px;
  letter-spacing: 3px; color: var(--neon);
  text-transform: uppercase; margin-bottom: 12px; opacity: 0.8;
}
.hero-name {
  font-family: var(--sans);
  font-size: clamp(42px, 6vw, 78px);
  font-weight: 800; line-height: 0.95;
  color: var(--text); margin-bottom: 18px;
}
.hero-name .outline {
  color: transparent;
  -webkit-text-stroke: 1.5px var(--neon);
}
.hero-bio {
  font-size: 14px; color: var(--muted);
  max-width: 520px; line-height: 1.8; margin-bottom: 28px;
}

/* Stat boxes */
.stat-box {
  background: var(--bg2); border: 1px solid var(--border);
  padding: 24px 20px; text-align: center;
}
.stat-num {
  font-family: var(--mono); font-size: 32px; font-weight: 700;
  color: var(--neon); text-shadow: var(--glow); display: block;
}
.stat-label {
  font-family: var(--mono); font-size: 9px;
  letter-spacing: 2px; color: var(--muted);
  text-transform: uppercase; margin-top: 6px; display: block;
}

/* Blog cards */
.blog-card {
  background: var(--bg2); border: 1px solid var(--border);
  padding: 28px; margin-bottom: 18px;
}
.blog-meta {
  font-family: var(--mono); font-size: 10px;
  letter-spacing: 1px; color: var(--muted); margin-bottom: 10px;
}
.blog-title {
  font-family: var(--sans); font-size: 20px; font-weight: 700;
  color: var(--text); margin-bottom: 10px; line-height: 1.3;
}
.blog-excerpt { font-size: 13px; color: var(--muted); line-height: 1.7; margin-bottom: 16px; }

/* Skill boxes */
.skill-box {
  background: var(--bg2); border: 1px solid var(--border);
  padding: 20px; position: relative; margin-bottom: 14px;
}
.skill-box::before {
  content:''; position:absolute; top:0; left:0; right:0; height:2px;
  background: linear-gradient(90deg, var(--neon), transparent); opacity: 0.5;
}
.skill-cat {
  font-family: var(--mono); font-size: 10px;
  letter-spacing: 2px; color: var(--neon);
  text-transform: uppercase; margin-bottom: 12px;
}

/* Resume zone */
.resume-zone {
  border: 2px dashed var(--border); padding: 52px;
  text-align: center; margin-bottom: 24px;
}

/* Streamlit widget polish */
[data-testid="stFileUploader"] {
  background: var(--bg2) !important;
  border: 1px solid var(--border) !important;
  border-radius: 0 !important;
}
[data-testid="stDownloadButton"] button,
.stButton button {
  background: transparent !important;
  border: 1px solid var(--neon) !important;
  color: var(--neon) !important;
  font-family: var(--mono) !important;
  font-size: 11px !important;
  letter-spacing: 2px !important;
  text-transform: uppercase !important;
  border-radius: 0 !important;
  padding: 10px 24px !important;
}
[data-testid="stDownloadButton"] button:hover,
.stButton button:hover {
  background: var(--neon) !important;
  color: var(--bg) !important;
}
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea {
  background: var(--bg3) !important;
  border: 1px solid var(--border) !important;
  border-radius: 0 !important;
  color: var(--text) !important;
}
[data-testid="stTextInput"] input:focus,
[data-testid="stTextArea"] textarea:focus {
  border-color: var(--neon) !important;
  box-shadow: 0 0 8px rgba(0,255,224,0.1) !important;
}
[data-testid="stTabs"] [data-baseweb="tab"] {
  font-family: var(--mono) !important;
  font-size: 11px !important;
  letter-spacing: 2px !important;
  text-transform: uppercase !important;
}
[data-testid="stTabs"] [aria-selected="true"] {
  color: var(--neon) !important;
  border-bottom-color: var(--neon) !important;
}
[data-testid="stSelectbox"] > div > div {
  background: var(--bg3) !important;
  border: 1px solid var(--border) !important;
  border-radius: 0 !important;
  color: var(--text) !important;
}
</style>
"""


def inject_css():
    import streamlit as st
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
    st.markdown('<div class="grid-bg"></div>', unsafe_allow_html=True)


def sidebar_nav(current: str = ""):
    import streamlit as st
    from data import PROFILE
    st.sidebar.markdown(
        f'<div class="sidebar-logo">{PROFILE["name"].upper()}</div>',
        unsafe_allow_html=True,
    )


def back_home(current_page: str = ""):
    """Breadcrumb-style back-to-home nav at the top of every page."""
    import streamlit as st
    crumb = (
        f'<span class="sep"> / </span><span class="current">{current_page}</span>'
        if current_page else ""
    )
    st.markdown(
        f'<div class="back-nav">'
        f'<a href="/" target="_self">⌂ Home</a>'
        f'{crumb}'
        f'</div>',
        unsafe_allow_html=True,
    )


def section_label(text: str):
    import streamlit as st
    st.markdown(f'<p class="sec-label">{text}</p>', unsafe_allow_html=True)


def neon_divider():
    import streamlit as st
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)


def tag(text: str, color: str = "neon") -> str:
    return f'<span class="tag tag-{color}">{text}</span>'
