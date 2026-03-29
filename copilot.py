import streamlit as st
from agent import get_portfolio_response

def render_copilot(current_page: str, page_data: str = ""):
    st.markdown("### Portfolio Copilot")

    if "portfolio_chat" not in st.session_state:
        st.session_state.portfolio_chat = []

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Summarize this page"):
            question = "Summarize this page in 3 concise bullet points."
            reply = get_portfolio_response(question, current_page, page_data)
            st.session_state.portfolio_chat.append(("You", question))
            st.session_state.portfolio_chat.append(("Copilot", reply))

    with col2:
        if st.button("Tell me more about Kamal"):
            question = "Tell me more about Kamal beyond the visible page content."
            reply = get_portfolio_response(question, current_page, page_data)
            st.session_state.portfolio_chat.append(("You", question))
            st.session_state.portfolio_chat.append(("Copilot", reply))

    user_input = st.text_input("Ask about experience, projects, skills, or interests")

    if st.button("Send") and user_input:
        reply = get_portfolio_response(user_input, current_page, page_data)
        st.session_state.portfolio_chat.append(("You", user_input))
        st.session_state.portfolio_chat.append(("Copilot", reply))

    for speaker, message in st.session_state.portfolio_chat[::-1]:
        if speaker == "You":
            st.markdown(f"**You:** {message}")
        else:
            st.markdown(f"**Copilot:** {message}")