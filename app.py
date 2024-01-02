import streamlit as st
from streamlit_chat import message

from chatty import Chatty

st.header(
    # "Sir Shakespeare's bot invites you to chat :sunglasses:"
    "Sir Shakespeare's bot invites you to chat",
    divider="rainbow",
)
st.markdown(
    """
*Hark! Pray, dost thou* \n
*indulge in a moment of discourse?* \n
*Let our words dance* \n
*like fair maidens and gallant knights* \n
*upon the stage of conversation.* \n
*What say thee?* \n
"""
)


def display_messages():
    for i, (msg, is_user) in enumerate(st.session_state["messages"]):
        message(msg, is_user=is_user, key=str(i))
    st.session_state["thinking_spinner"] = st.empty()


def process_input():
    if (
        st.session_state["user_input"]
        and len(st.session_state["user_input"].strip()) > 0
    ):
        user_text = st.session_state["user_input"].strip()
        with st.session_state["thinking_spinner"], st.spinner(
            f"I muse upon this"
        ):
            agent_text = st.session_state["assistant"].ask(user_text)

        st.session_state["messages"].append((user_text, True))
        st.session_state["messages"].append((agent_text, False))


def page():
    if len(st.session_state) == 0:
        st.session_state["messages"] = []
        st.session_state["assistant"] = Chatty()

    st.session_state["ingestion_spinner"] = st.empty()
    display_messages()
    st.text_input(" ", key="user_input", on_change=process_input)


if __name__ == "__main__":
    page()
