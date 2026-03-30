"""
ai_assistant.py — Groq-powered AI assistant for portfolio
Provides intelligent summaries and answers questions about you
"""

import streamlit as st
import os
from typing import Optional, Dict, Any
from data import PROFILE, EXPERIENCE, PROJECTS, SKILLS, EDUCATION, CERTIFICATIONS, ACHIEVEMENTS

# Try to import groq, provide fallback if not available
try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False
    st.warning("Groq library not installed. Run: pip install groq")


class PortfolioAIAssistant:
    """
    AI Assistant that knows everything about the portfolio owner.
    Uses Groq's Llama models for fast, intelligent responses.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the AI assistant with Groq API."""
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        
        if GROQ_AVAILABLE and self.api_key:
            self.client = Groq(api_key=self.api_key)
            self.model = "llama-3.3-70b-versatile"
            self.enabled = True
        else:
            self.client = None
            self.enabled = False
        
        self.knowledge_base = self._build_knowledge_base()
        
    def _build_knowledge_base(self) -> str:
        """Build comprehensive knowledge base from portfolio data."""
        
        kb = f"""# PORTFOLIO KNOWLEDGE BASE

## PERSONAL INFORMATION
Name: {PROFILE['name']}
Title: {PROFILE['title']}
Location: {PROFILE['location']}
Email: {PROFILE['email']}

## PROFESSIONAL SUMMARY
{PROFILE['tagline']}

## BIO
{' '.join(PROFILE['bio_lines'])}

## CURRENT ROLE
AI/ML Engineer at Tiger Analytics, Bangalore, India
- Building production-grade ML systems for Fortune 500 clients
- Specializing in MLOps, forecasting, and intelligent automation

## SKILLS & EXPERTISE
"""
        
        # Add skills
        for skill in SKILLS:
            kb += f"\n### {skill['category']}\n"
            kb += ", ".join(skill['items']) + "\n"
        
        # Add experience
        kb += "\n## PROFESSIONAL EXPERIENCE\n"
        for exp in EXPERIENCE:
            kb += f"\n### {exp['role']} at {exp['company']} ({exp['period']})\n"
            kb += f"Location: {exp['location']}\n"
            kb += "Key achievements:\n"
            for point in exp['points']:
                kb += f"- {point}\n"
        
        # Add projects
        kb += "\n## KEY PROJECTS\n"
        for proj in PROJECTS:
            kb += f"\n### {proj['title']}\n"
            kb += f"{proj['desc']}\n"
            kb += f"Technologies: {', '.join([t[0] for t in proj.get('tags', [])])}\n"
        
        # Add education
        kb += "\n## EDUCATION\n"
        for edu in EDUCATION:
            kb += f"\n### {edu['degree']}\n"
            kb += f"{edu['school']} ({edu['year']})\n"
            if edu.get('detail'):
                kb += f"{edu['detail']}\n"
        
        # Add achievements
        kb += "\n## KEY ACHIEVEMENTS\n"
        for ach in ACHIEVEMENTS:
            kb += f"\n- {ach['title']} ({ach['year']}): {ach['desc']}\n"
        
        # Add certifications/publications
        kb += "\n## PUBLICATIONS & CERTIFICATIONS\n"
        for cert in CERTIFICATIONS:
            kb += f"\n- {cert['title']} ({cert['date']})\n"
            kb += f"  Organization: {cert['org']}\n"
        
        return kb
    
    def get_system_prompt(self, context: str = "general") -> str:
        """Generate context-aware system prompt."""
        
        base_prompt = f"""You are an AI assistant embedded in {PROFILE['name']}'s professional portfolio website. 
You have deep knowledge about their background, experience, projects, and skills.

KNOWLEDGE BASE:
{self.knowledge_base}

YOUR ROLE:
- Answer questions about {PROFILE['name']}'s experience, projects, and skills
- Provide intelligent summaries of their work
- Be concise, professional, and helpful
- Use specific examples and metrics when available
- If asked about something not in the knowledge base, politely say you don't have that information

TONE:
- Professional but friendly
- Confident but not boastful
- Technical when appropriate, accessible when needed
- First-person perspective when discussing {PROFILE['name']}'s work (use "I" not "they")

CONSTRAINTS:
- Keep responses under 200 words unless asked for details
- Always cite specific projects or achievements when relevant
- Don't make up information not in the knowledge base
"""
        
        # Context-specific additions
        context_prompts = {
            "about": "\nCONTEXT: User is on the About page. Focus on background, skills, and personal interests.",
            "experience": "\nCONTEXT: User is on the Experience page. Focus on work history and achievements.",
            "projects": "\nCONTEXT: User is on the Projects page. Focus on technical implementations and impact.",
            "contact": "\nCONTEXT: User is on the Contact page. Be helpful about collaboration opportunities.",
        }
        
        return base_prompt + context_prompts.get(context, "")
    
    def chat(self, 
             user_message: str, 
             context: str = "general",
             chat_history: Optional[list] = None) -> str:
        """
        Send message to AI assistant and get response.
        
        Args:
            user_message: User's question or prompt
            context: Current page context (about, experience, projects, etc.)
            chat_history: Previous messages for context
            
        Returns:
            AI assistant's response
        """
        
        if not self.enabled:
            return "⚠️ AI Assistant is not configured. Please add your GROQ_API_KEY."
        
        try:
            # Build messages
            messages = [
                {"role": "system", "content": self.get_system_prompt(context)}
            ]
            
            #chat history if provided
            if chat_history:
                messages.extend(chat_history)
            
            messages.append({"role": "user", "content": user_message})
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=500,
                top_p=0.9,
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"❌ Error: {str(e)}\n\nPlease check your Groq API key and connection."
    
    def get_page_summary(self, page_name: str) -> str:
        """Generate intelligent summary of a specific page."""
        
        prompts = {
            "about": f"Provide a 3-sentence summary of {PROFILE['name']}'s background, expertise, and what makes them unique as an AI/ML engineer.",
            "experience": f"Summarize {PROFILE['name']}'s career progression and key achievements in 3-4 bullet points.",
            "projects": f"List {PROFILE['name']}'s top 3 most impactful projects with one-line descriptions.",
            "home": f"Write a compelling 2-sentence elevator pitch for {PROFILE['name']} as an AI/ML engineer.",
        }
        
        prompt = prompts.get(page_name, f"Summarize {PROFILE['name']}'s profile.")
        return self.chat(prompt, context=page_name)
    
    def suggest_questions(self, context: str = "general") -> list:
        """Suggest relevant questions users might ask."""
        
        suggestions = {
            # "about": [
            #     "What's your educational background?",
            #     "What technologies do you specialize in?",
            #     "What are you currently learning?",
            #     "What are your hobbies outside of work?",
            # ],
            # "experience": [
            #     "What's your most significant achievement?",
            #     "How much revenue impact have you driven?",
            #     "What's your experience with MLOps?",
            #     "Tell me about your work with forecasting models",
            # ],
            # "projects": [
            #     "What's your most complex project?",
            #     "How do you approach ML model deployment?",
            #     "Tell me about your route optimization project",
            #     "What frameworks do you prefer for ML?",
            # ],
            "general": [
                "What's your background?",
                "What projects have you worked on?",
                "What are your core skills?",
                "Are you open to opportunities?",
            ],
        }
        
        return suggestions.get(context, suggestions["general"])


# ── UI COMPONENT ─────────────────────────────────────────────────────────────

def render_ai_assistant(context: str = "general", position: str = "sidebar"):
    """
    Render AI assistant UI component.
    
    Args:
        context: Current page context (about, experience, projects, etc.)
        position: Where to render ("sidebar" or "main")
    """
    
    # Initialize assistant (singleton pattern)
    if 'ai_assistant' not in st.session_state:
        api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY", None)
        st.session_state.ai_assistant = PortfolioAIAssistant(api_key)
    
    assistant = st.session_state.ai_assistant
    
    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Initialize show state
    if 'show_ai_chat' not in st.session_state:
        st.session_state.show_ai_chat = False
    
    # Render based on position
    if position == "sidebar":
        _render_sidebar_assistant(assistant, context)
    else:
        _render_main_assistant(assistant, context)


def _render_sidebar_assistant(assistant, context):
    """Render compact AI assistant in sidebar."""
    
    st.markdown("---")
    st.markdown(
        '<p style="font-family:var(--mono);font-size:10px;color:var(--neon);'
        'letter-spacing:2px;text-transform:uppercase;margin-bottom:12px;">'
        '🤖 AI Assistant</p>',
        unsafe_allow_html=True,
    )
    
    if not assistant.enabled:
        st.caption("⚠️ Not configured")
        with st.expander("Setup Instructions"):
            st.markdown("""
            **To enable AI Assistant:**
            1. Get free API key from [console.groq.com](https://console.groq.com)
            2. Add to `.streamlit/secrets.toml`:
               ```toml
               GROQ_API_KEY = "your-key-here"
               ```
            3. Install: `pip install groq`
            4. Restart app
            """)
        return
    
    # Quick summary button
    if st.button("📝 Page Summary", key="quick_summary", use_container_width=True):
        with st.spinner("Generating..."):
            summary = assistant.get_page_summary(context)
            st.info(summary)
    
    # Toggle chat
    if st.button("💬 Ask AI", key="toggle_chat", use_container_width=True):
        st.session_state.show_ai_chat = not st.session_state.show_ai_chat
    
    # Chat interface (expandable)
    if st.session_state.show_ai_chat:
        st.markdown("<br>", unsafe_allow_html=True)
        
        # # Show suggested questions
        # st.caption("💡 Suggested questions:")
        # suggestions = assistant.suggest_questions(context)
        # for i, suggestion in enumerate(suggestions[:3]):
        #     if st.button(f"• {suggestion}", key=f"suggest_{i}", use_container_width=True):
        #         with st.spinner("Thinking..."):
        #             response = assistant.chat(suggestion, context, st.session_state.chat_history)
        #             st.session_state.chat_history.append({"role": "user", "content": suggestion})
        #             st.session_state.chat_history.append({"role": "assistant", "content": response})
        #             st.rerun()
        
        # User input
        user_input = st.text_input(
            "Your question:",
            key="ai_input_sidebar",
            placeholder="Ask me anything...",
            label_visibility="collapsed"
        )
        
        if user_input:
            with st.spinner("Thinking..."):
                response = assistant.chat(user_input, context, st.session_state.chat_history)
                st.session_state.chat_history.append({"role": "user", "content": user_input})
                st.session_state.chat_history.append({"role": "assistant", "content": response})
                st.rerun()
        
        # Show recent conversation
        if st.session_state.chat_history:
            st.markdown("---")
            st.caption("Recent chat:")
            for msg in st.session_state.chat_history[-4:]:  # Last 2 exchanges
                if msg["role"] == "user":
                    st.markdown(f"**You:** {msg['content']}")
                else:
                    st.markdown(f"**AI:** {msg['content']}")
            
            if st.button("🗑️ Clear Chat", use_container_width=True):
                st.session_state.chat_history = []
                st.rerun()


def _render_main_assistant(assistant, context):
    """Render full-featured AI assistant in main area."""
    
    st.markdown(
        '<div style="background:rgba(0,255,224,0.03);border:1px solid var(--border);'
        'padding:28px;margin:32px 0;border-radius:8px;">',
        unsafe_allow_html=True,
    )
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("#### 🤖")
    
    with col2:
        st.markdown(
            '<p style="font-family:var(--mono);font-size:11px;color:var(--neon);'
            'letter-spacing:2px;text-transform:uppercase;margin-bottom:8px;">AI ASSISTANT (Beta🚧)</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p style="font-size:14px;color:var(--muted);margin-bottom:16px;">'
            'Ask me anything about my background, projects, or experience. '
            'Powered by Groq + Llama 3.3 70B.(This feature is in beta. Response times may vary, '
            'and usage is limited due to free API tier constraints. Also responses ' \
            'may not always be accurate)</p>',
            unsafe_allow_html=True,
        )
    
    if not assistant.enabled:
        st.warning("⚠️ AI Assistant not configured. See sidebar for setup instructions.")
        st.markdown('</div>', unsafe_allow_html=True)
        return
    
    # Suggested questions
    # st.markdown("**💡 Try asking:**")
    # suggestions = assistant.suggest_questions(context)
    
    # cols = st.columns(2)
    # for i, suggestion in enumerate(suggestions):
    #     with cols[i % 2]:
    #         if st.button(suggestion, key=f"main_suggest_{i}", use_container_width=True):
    #             with st.spinner("Thinking..."):
    #                 response = assistant.chat(suggestion, context)
    #                 st.session_state.last_response = response
    #                 st.rerun()
    
    # st.markdown("<br>", unsafe_allow_html=True)
    
    # User input
    user_question = st.text_input(
        "Ask your question:",
        placeholder="e.g., What's your experience with MLOps?",
        key="ai_input_main",
    )
    
    if user_question:
        with st.spinner("⚡Generating response..."):
            response = assistant.chat(user_question, context)
            st.session_state.last_response = response
            st.rerun()
    
    # Show last response
    if 'last_response' in st.session_state:
        st.markdown("---")
        st.markdown("**🤖 AI Response:**")
        st.markdown(
            f'<div style="background:var(--bg2);padding:20px;border-left:3px solid var(--neon);'
            f'margin-top:12px;">{st.session_state.last_response}</div>',
            unsafe_allow_html=True,
        )
    
    st.markdown('</div>', unsafe_allow_html=True)


# ── USAGE EXAMPLES ───────────────────────────────────────────────────────────

"""
HOW TO USE IN YOUR PAGES:

1. In sidebar (compact mode):
   ```python
   from ai_assistant import render_ai_assistant
   
   with st.sidebar:
       render_ai_assistant(context="about", position="sidebar")
   ```

2. In main content (full-featured):
   ```python
   from ai_assistant import render_ai_assistant
   
   render_ai_assistant(context="projects", position="main")
   ```

3. Custom usage:
   ```python
   from ai_assistant import PortfolioAIAssistant
   
   assistant = PortfolioAIAssistant()
   summary = assistant.get_page_summary("experience")
   st.write(summary)
   ```
"""
