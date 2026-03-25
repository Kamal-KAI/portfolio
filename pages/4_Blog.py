"""
pages/4_Blog.py — Technical & Personal tabs.
Features: search, tag filter sidebar, estimated read time, full post reader.
Posts live in posts/technical/*.md and posts/personal/*.md
"""

import re
import math
import streamlit as st
from pathlib import Path
from styles import inject_css, sidebar_nav, section_label, neon_divider, tag, back_home
from data import PROFILE

st.set_page_config(
    page_title=f"Blog — {PROFILE['name']}",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
)
inject_css()
sidebar_nav("Blog")

POSTS_DIR  = Path(__file__).parent.parent / "posts"
TAG_COLORS = ["neon", "amber", "blue", "green", "pink", "purple"]


def parse_frontmatter(content: str) -> tuple[dict, str]:
    meta, body = {}, content
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, _, v = line.partition(":")
                meta[k.strip()] = v.strip()
        body = content[m.end():]
    return meta, body


def read_time(body: str) -> int:
    return max(1, math.ceil(len(body.split()) / 200))


def load_posts(category: str) -> list[dict]:
    folder = POSTS_DIR / category
    posts  = []
    if not folder.exists():
        return posts
    for md_file in sorted(folder.glob("*.md"), reverse=True):
        meta, body = parse_frontmatter(md_file.read_text(encoding="utf-8"))
        if not meta.get("title"):
            meta["title"] = md_file.stem.replace("-", " ").title()
        if isinstance(meta.get("tags"), str):
            meta["tags"] = [t.strip() for t in meta["tags"].split(",") if t.strip()]
        else:
            meta["tags"] = []
        meta["body"]      = body
        meta["filename"]  = md_file.stem
        meta["category"]  = category
        meta["read_time"] = read_time(body)
        posts.append(meta)
    return posts


def matches_search(post: dict, query: str) -> bool:
    if not query:
        return True
    q = query.lower()
    return (
        q in post["title"].lower()
        or q in post.get("excerpt", "").lower()
        or q in post["body"].lower()
        or any(q in t.lower() for t in post.get("tags", []))
    )


def render_post_card(post: dict, idx: int, category: str):
    tags_html = "".join(
        tag(t, TAG_COLORS[i % len(TAG_COLORS)])
        for i, t in enumerate(post.get("tags", []))
    )
    excerpt = post.get("excerpt") or (post["body"][:220].replace("\n", " ").strip() + "…")
    rt      = post.get("read_time", 1)
    st.markdown(
        f'<div class="blog-card">'
        f'<div class="blog-meta">{post.get("date","")}&nbsp;·&nbsp;{rt} min read</div>'
        f'<div class="blog-title">{post["title"]}</div>'
        f'<div class="blog-excerpt">{excerpt}</div>'
        f'<div style="margin-bottom:14px;">{tags_html}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )
    if st.button("Read Post →", key=f"btn_{category}_{idx}"):
        st.session_state["open_post"] = post
        st.rerun()


# ── FULL POST VIEW ────────────────────────────────────────────────────────────
if "open_post" in st.session_state:
    post = st.session_state["open_post"]
    if st.button("← Back to Blog"):
        del st.session_state["open_post"]
        st.rerun()
    neon_divider()
    cat_color = "#00ffe0" if post["category"] == "technical" else "#f472b6"
    st.markdown(
        f'<span style="font-family:var(--mono);font-size:9px;letter-spacing:2px;'
        f'text-transform:uppercase;padding:4px 10px;border:1px solid {cat_color};'
        f'color:{cat_color};display:inline-block;margin-bottom:16px;">'
        f'{post["category"]}</span>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<h1 style="font-size:40px;font-weight:800;margin:12px 0 8px;line-height:1.1;">'
        f'{post["title"]}</h1>',
        unsafe_allow_html=True,
    )
    tags_html = "".join(
        tag(t, TAG_COLORS[i % len(TAG_COLORS)])
        for i, t in enumerate(post.get("tags", []))
    )
    st.markdown(
        f'<p style="font-family:var(--mono);font-size:10px;color:var(--muted);'
        f'letter-spacing:1.5px;margin-bottom:12px;">'
        f'{post.get("date","")}&nbsp;·&nbsp;{post.get("read_time",1)} min read</p>'
        f'<div style="margin-bottom:32px;">{tags_html}</div>',
        unsafe_allow_html=True,
    )
    neon_divider()
    st.markdown(post["body"])
    neon_divider()
    if st.button("← Back to Blog", key="back_bottom"):
        del st.session_state["open_post"]
        st.rerun()
    st.stop()

# ── BLOG LIST ─────────────────────────────────────────────────────────────────
all_posts = load_posts("technical") + load_posts("personal")

# Sidebar
with st.sidebar:
    st.markdown("---")
    st.markdown("[Home](/) ", unsafe_allow_html=False)
    st.markdown("---")
    st.markdown(
        '<p style="font-family:var(--mono);font-size:9px;color:var(--muted);'
        'letter-spacing:2px;text-transform:uppercase;margin-bottom:8px;">Search</p>',
        unsafe_allow_html=True,
    )
    search_query = st.text_input("Search", placeholder="keyword, tag…", label_visibility="collapsed")
    st.markdown(
        '<p style="font-family:var(--mono);font-size:9px;color:var(--muted);'
        'letter-spacing:2px;text-transform:uppercase;margin:16px 0 8px;">Filter by Tag</p>',
        unsafe_allow_html=True,
    )
    all_tags     = sorted({t for p in all_posts for t in p.get("tags", [])})
    selected_tag = st.selectbox("Tag", ["All tags"] + all_tags, label_visibility="collapsed")
    st.markdown("---")
    tc = sum(1 for p in all_posts if p["category"] == "technical")
    pc = len(all_posts) - tc
    st.markdown(
        f'<p style="font-family:var(--mono);font-size:10px;color:var(--muted);">'
        f'⚙ {tc} technical<br>✦ {pc} personal</p>',
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.caption("Built with 💔")

back_home("Blog")
section_label("04. Blog")
st.markdown(
    '<h1 style="font-size:48px;font-weight:800;margin-bottom:8px;">Thoughts & Writing</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p style="color:var(--muted);font-size:14px;line-height:1.7;max-width:560px;margin-bottom:32px;">'
    'Data engineering, tools, and occasional life posts. '
    'All stored as Markdown files — search or filter by tag on the left.</p>',
    unsafe_allow_html=True,
)
neon_divider()

# Filter
def filter_posts(posts):
    result = [p for p in posts if matches_search(p, search_query)]
    if selected_tag != "All tags":
        result = [p for p in result if selected_tag in p.get("tags", [])]
    return result

if search_query or selected_tag != "All tags":
    filtered = filter_posts(all_posts)
    label = f"// {len(filtered)} result{'s' if len(filtered) != 1 else ''} found"
    if search_query:
        label += f' for "{search_query}"'
    if selected_tag != "All tags":
        label += f' · tag: {selected_tag}'
    section_label(label)
    st.markdown("<br>", unsafe_allow_html=True)
    if filtered:
        for i, p in enumerate(filtered):
            render_post_card(p, i, p["category"])
    else:
        st.markdown(
            '<div class="blog-card"><div class="blog-title" style="opacity:0.4;">No posts match</div>'
            '<div class="blog-excerpt">Try a different keyword or tag.</div></div>',
            unsafe_allow_html=True,
        )
else:
    tab_tech, tab_personal = st.tabs(["⚙  Technical", "✦  Personal"])
    with tab_tech:
        tech_posts = load_posts("technical")
        if tech_posts:
            for i, p in enumerate(tech_posts):
                render_post_card(p, i, "technical")
        else:
            st.markdown(
                '<div class="blog-card"><div class="blog-title" style="opacity:0.4;">No posts yet</div>'
                '<div class="blog-excerpt">Add <code>.md</code> files to <code>posts/technical/</code>.</div></div>',
                unsafe_allow_html=True,
            )
    with tab_personal:
        personal_posts = load_posts("personal")
        if personal_posts:
            for i, p in enumerate(personal_posts):
                render_post_card(p, i, "personal")
        else:
            st.markdown(
                '<div class="blog-card"><div class="blog-title" style="opacity:0.4;">No posts yet</div>'
                '<div class="blog-excerpt">Add <code>.md</code> files to <code>posts/personal/</code>.</div></div>',
                unsafe_allow_html=True,
            )

neon_divider()

with st.expander("📌  How to add a new blog post"):
    st.markdown("""
Create a `.md` file in `posts/technical/` or `posts/personal/`:

```markdown
---
title: My Post Title
date: March 23, 2025
excerpt: One or two sentences shown as the card preview.
tags: Python, Snowflake, DBT
---

# Post content here in Markdown
```

**Naming tip:** Prefix with `YYYY-MM-DD-` for newest-first ordering.
""")
