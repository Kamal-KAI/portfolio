"""
styles.py — Enhanced global CSS with animations, improved components, and refined UI.
Called at the top of every page.
"""

GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap');
@import url('https://fonts.googleapis.com/icon?family=Material+Icons');

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
  scroll-behavior: smooth;
}

[data-testid="stSidebar"] {
  background-color: var(--bg2) !important;
  border-right: 1px solid var(--border) !important;
  display: block !important;
}

[data-testid="stSidebar"] *:not([data-testid="collapsedControl"]):not([data-testid="collapsedControl"] *):not(button):not(button *) { 
  font-family: var(--mono) !important; 
}

#MainMenu, footer { visibility: hidden; }
header { visibility: hidden; }
header [data-testid="stSidebarCollapsedControl"] { visibility: visible !important; }
[data-testid="stDecoration"] { display: none; }

/* Improved container spacing */
.block-container {
  padding-top: 1rem !important;
  padding-bottom: 1.5rem !important;
  padding-left: 2rem !important;
  padding-right: 2rem !important;
  max-width: 1100px !important;
}

.block-container > div:first-child { margin-top: 0 !important; }

[data-testid="stVerticalBlock"] > [data-testid="stVerticalBlockBorderWrapper"],
[data-testid="stVerticalBlock"] > div { gap: 0.5rem !important; }

/* Enhanced back-home nav */
.back-nav {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 24px;
  padding-bottom: 18px;
  border-bottom: 1px solid var(--border);
}

.back-nav a {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--muted);
  text-decoration: none;
  transition: all 0.2s ease;
}

.back-nav a:hover {
  color: var(--neon);
  transform: translateX(-2px);
}

.back-nav .sep {
  font-family: var(--mono);
  font-size: 10px;
  color: var(--border);
}

.back-nav .current {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--neon);
  opacity: 0.8;
}

/* Enhanced page links */
[data-testid="stPageLink"] a,
[data-testid="stPageLink"] a:visited {
  font-family: var(--mono) !important;
  font-size: 10px !important;
  letter-spacing: 1.5px !important;
  text-transform: uppercase !important;
  color: var(--text) !important;
  border: 1px solid var(--border) !important;
  padding: 12px 24px !important;
  white-space: nowrap !important;
  min-width: 160px !important;
  display: inline-block !important;
  text-align: center !important;
  text-decoration: none !important;
  transition: all 0.3s ease !important;
  position: relative !important;
  overflow: hidden !important;
}

[data-testid="stPageLink"] a::before {
  content: '' !important;
  position: absolute !important;
  top: 0 !important;
  left: -100% !important;
  width: 100% !important;
  height: 100% !important;
  background: linear-gradient(90deg, transparent, rgba(0,255,224,0.1), transparent) !important;
  transition: left 0.5s ease !important;
}

[data-testid="stPageLink"] a:hover {
  border-color: var(--neon) !important;
  color: var(--neon) !important;
  box-shadow: 0 0 12px rgba(0,255,224,0.2) !important;
  transform: translateY(-2px) !important;
}

[data-testid="stPageLink"] a:hover::before {
  left: 100% !important;
}

/* Improved scrollbar */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { 
  background: linear-gradient(180deg, var(--neon) 0%, var(--blue) 100%);
  border-radius: 99px;
}
::-webkit-scrollbar-thumb:hover { background: var(--neon); }

h1, h2, h3, h4 {
  font-family: var(--sans) !important;
  font-weight: 800 !important;
  line-height: 1.2 !important;
}

/* Animated grid background */
.grid-bg {
  position: fixed;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  background-image:
    linear-gradient(rgba(0,255,224,0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,255,224,0.02) 1px, transparent 1px);
  background-size: 50px 50px;
  animation: grid-move 20s linear infinite;
}

@keyframes grid-move {
  0% { background-position: 0 0; }
  100% { background-position: 50px 50px; }
}

/* Enhanced section label */
.sec-label {
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: 4px;
  color: var(--neon);
  text-transform: uppercase;
  opacity: 0.9;
  margin-bottom: 8px;
  position: relative;
  display: inline-block;
}

.sec-label::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 40px;
  height: 2px;
  background: var(--neon);
  opacity: 0.3;
}

/* Enhanced sidebar logo */
.sidebar-logo {
  font-family: var(--mono);
  font-size: 14px;
  color: var(--neon);
  letter-spacing: 3px;
  padding: 24px 16px 32px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 20px;
  text-shadow: 0 0 15px rgba(0,255,224,0.5);
  animation: glow-pulse 3s ease-in-out infinite;
}

@keyframes glow-pulse {
  0%, 100% { text-shadow: 0 0 15px rgba(0,255,224,0.5); }
  50% { text-shadow: 0 0 25px rgba(0,255,224,0.7); }
}

/* Enhanced cards with hover effect */
.card {
  background: var(--bg2);
  border: 1px solid var(--border);
  padding: 28px;
  margin-bottom: 20px;
  position: relative;
  transition: all 0.3s ease;
}

.card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--neon), transparent);
  opacity: 0.4;
  transition: opacity 0.3s ease;
}

.card:hover {
  border-color: rgba(0,255,224,0.3);
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0,255,224,0.1);
}

.card:hover::before {
  opacity: 0.7;
}

/* Enhanced tags */
.tag {
  display: inline-block;
  font-family: var(--mono);
  font-size: 9px;
  padding: 4px 10px;
  border-radius: 3px;
  margin: 3px;
  letter-spacing: 1px;
  text-transform: uppercase;
  transition: all 0.2s ease;
}

.tag:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

.tag-neon   { background:rgba(0,255,224,0.08);  border:1px solid rgba(0,255,224,0.3);  color:#00ffe0; }
.tag-amber  { background:rgba(245,158,11,0.1);  border:1px solid rgba(245,158,11,0.3); color:#f59e0b; }
.tag-blue   { background:rgba(96,165,250,0.1);  border:1px solid rgba(96,165,250,0.3); color:#60a5fa; }
.tag-green  { background:rgba(52,211,153,0.1);  border:1px solid rgba(52,211,153,0.3); color:#34d399; }
.tag-pink   { background:rgba(244,114,182,0.1); border:1px solid rgba(244,114,182,0.3);color:#f472b6; }
.tag-purple { background:rgba(167,139,250,0.1); border:1px solid rgba(167,139,250,0.3);color:#a78bfa; }

/* Animated neon divider */
.neon-divider {
  height: 1px;
  background: linear-gradient(90deg, var(--neon) 0%, var(--blue) 50%, transparent 100%);
  opacity: 0.25;
  margin: 32px 0;
  position: relative;
}

.neon-divider::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  height: 1px;
  width: 100px;
  background: var(--neon);
  box-shadow: 0 0 10px var(--neon);
  animation: slide 3s ease-in-out infinite;
}

@keyframes slide {
  0%, 100% { left: 0; opacity: 0; }
  50% { left: calc(100% - 100px); opacity: 1; }
}

/* Enhanced timeline */
.timeline-item {
  border-left: 2px solid rgba(0,255,224,0.15);
  padding: 0 0 48px 36px;
  position: relative;
  margin-left: 12px;
  transition: border-color 0.3s ease;
}

.timeline-item:hover {
  border-left-color: rgba(0,255,224,0.4);
}

.timeline-item:last-child { padding-bottom: 0; }

.timeline-dot {
  position: absolute;
  left: -6px;
  top: 6px;
  width: 12px;
  height: 12px;
  background: var(--neon);
  border-radius: 50%;
  box-shadow: 0 0 12px rgba(0,255,224,0.6);
  animation: pulse-dot 2s ease-in-out infinite;
}

@keyframes pulse-dot {
  0%, 100% { transform: scale(1); box-shadow: 0 0 12px rgba(0,255,224,0.6); }
  50% { transform: scale(1.2); box-shadow: 0 0 20px rgba(0,255,224,0.8); }
}

.timeline-period {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 2px;
  color: var(--neon);
  text-transform: uppercase;
  margin-bottom: 8px;
}

.timeline-role {
  font-family: var(--sans);
  font-size: 20px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 4px;
}

.timeline-company {
  font-size: 13px;
  color: var(--muted);
  margin-bottom: 16px;
}

/* Enhanced hero section */
.hero-wrap {
  padding: 16px 0 48px;
  position: relative;
}

.hero-name {
  font-family: var(--sans);
  font-size: clamp(44px, 7vw, 84px);
  font-weight: 800;
  line-height: 0.95;
  color: var(--text);
  margin-bottom: 20px;
  animation: fade-in-up 0.8s ease-out;
}

@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.hero-name .outline {
  color: transparent;
  -webkit-text-stroke: 2px var(--neon);
  animation: stroke-glow 3s ease-in-out infinite;
}

@keyframes stroke-glow {
  0%, 100% { -webkit-text-stroke: 2px var(--neon); filter: drop-shadow(0 0 8px rgba(0,255,224,0.5)); }
  50% { -webkit-text-stroke: 2px var(--blue); filter: drop-shadow(0 0 15px rgba(96,165,250,0.6)); }
}

.hero-bio {
  font-size: 15px;
  color: var(--muted);
  max-width: 600px;
  line-height: 1.9;
  margin-bottom: 32px;
  animation: fade-in-up 0.8s ease-out 0.2s both;
}

/* Enhanced stat boxes */
.stat-box {
  background: var(--bg2);
  border: 1px solid var(--border);
  padding: 28px 24px;
  text-align: center;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.stat-box::after {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(0,255,224,0.05) 0%, transparent 70%);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.stat-box:hover {
  border-color: var(--neon);
  transform: translateY(-6px);
  box-shadow: 0 10px 30px rgba(0,255,224,0.15);
}

.stat-box:hover::after {
  opacity: 1;
}

.stat-num {
  font-family: var(--mono);
  font-size: 38px;
  font-weight: 700;
  color: var(--neon);
  text-shadow: var(--glow);
  display: block;
  position: relative;
  z-index: 1;
}

.stat-label {
  font-family: var(--mono);
  font-size: 9px;
  letter-spacing: 2px;
  color: var(--muted);
  text-transform: uppercase;
  margin-top: 8px;
  display: block;
  position: relative;
  z-index: 1;
}

/* Enhanced blog cards */
.blog-card {
  background: var(--bg2);
  border: 1px solid var(--border);
  padding: 28px;
  margin-bottom: 20px;
  transition: all 0.3s ease;
  cursor: pointer;
}

.blog-card:hover {
  border-color: rgba(0,255,224,0.3);
  transform: translateX(8px);
  box-shadow: -4px 0 20px rgba(0,255,224,0.1);
}

.blog-meta {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 1px;
  color: var(--muted);
  margin-bottom: 12px;
}

.blog-title {
  font-family: var(--sans);
  font-size: 20px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 12px;
  line-height: 1.3;
  transition: color 0.2s ease;
}

.blog-card:hover .blog-title {
  color: var(--neon);
}

.blog-excerpt {
  font-size: 14px;
  color: var(--muted);
  line-height: 1.8;
  margin-bottom: 16px;
}

/* Enhanced skill boxes */
.skill-box {
  background: var(--bg2);
  border: 1px solid var(--border);
  padding: 22px;
  position: relative;
  margin-bottom: 16px;
  transition: all 0.3s ease;
}

.skill-box::before {
  content:'';
  position:absolute;
  top:0;
  left:0;
  right:0;
  height:2px;
  background: linear-gradient(90deg, var(--neon), transparent);
  opacity: 0.5;
}

.skill-box:hover {
  border-color: rgba(0,255,224,0.3);
  transform: translateY(-4px);
}

.skill-cat {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 2px;
  color: var(--neon);
  text-transform: uppercase;
  margin-bottom: 14px;
}

/* Resume zone */
.resume-zone {
  border: 2px dashed var(--border);
  padding: 60px;
  text-align: center;
  margin-bottom: 28px;
  transition: all 0.3s ease;
}

.resume-zone:hover {
  border-color: var(--neon);
  background: rgba(0,255,224,0.02);
}

/* Enhanced buttons */
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
  padding: 12px 28px !important;
  transition: all 0.3s ease !important;
}

[data-testid="stDownloadButton"] button:hover,
.stButton button:hover {
  background: var(--neon) !important;
  color: var(--bg) !important;
  box-shadow: 0 0 20px rgba(0,255,224,0.3) !important;
  transform: translateY(-2px) !important;
}

/* Enhanced form inputs */
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea {
  background: var(--bg3) !important;
  border: 1px solid var(--border) !important;
  border-radius: 0 !important;
  color: var(--text) !important;
  font-family: var(--mono) !important;
  font-size: 13px !important;
  transition: all 0.3s ease !important;
}

[data-testid="stTextInput"] input:focus,
[data-testid="stTextArea"] textarea:focus {
  border-color: var(--neon) !important;
  box-shadow: 0 0 12px rgba(0,255,224,0.15) !important;
}

/* Enhanced tabs */
[data-testid="stTabs"] [data-baseweb="tab"] {
  font-family: var(--mono) !important;
  font-size: 11px !important;
  letter-spacing: 2px !important;
  text-transform: uppercase !important;
  color: var(--muted) !important;
  transition: all 0.2s ease !important;
}

[data-testid="stTabs"] [aria-selected="true"] {
  color: var(--neon) !important;
  border-bottom-color: var(--neon) !important;
}

[data-testid="stTabs"] [data-baseweb="tab"]:hover {
  color: var(--text) !important;
}

/* Enhanced selectbox */
[data-testid="stSelectbox"] > div > div {
  background: var(--bg3) !important;
  border: 1px solid var(--border) !important;
  border-radius: 0 !important;
  color: var(--text) !important;
  font-family: var(--mono) !important;
  font-size: 12px !important;
}

/* Loading animation */
@keyframes loading {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .block-container {
    padding-left: 1rem !important;
    padding-right: 1rem !important;
  }
  
  .hero-name {
    font-size: clamp(32px, 10vw, 60px);
  }
  
  .stat-box {
    padding: 20px 16px;
  }
  
  .card {
    padding: 20px;
  }
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
