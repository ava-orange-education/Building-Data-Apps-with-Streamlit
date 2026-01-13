import streamlit as st
from google import genai
from google.genai import types

SYSTEM_PROMPT = f"""
You are a helpful data analyst. Answer the user's questions in markdown format based on the following data.

Data:
{st.session_state["data"].to_string()}
"""

WELCOME_MESSAGE = {
    "role": "assistant",
    "content": f"""
Hello! I am the DataConverse Assistant.\n
Ask me anything about the __{st.session_state["dataset_name"]}__ data.
    """,
}


with st.sidebar:
    st.divider()
    st.session_state["gemini_api_key"] = st.text_input(
        "Enter your Gemini API Key",
        type="password",
        help="API key will not be stored in the app.",
        value=st.session_state.get("gemini_api_key", ""),
    )

if st.session_state.get("gemini_api_key") == "":
    st.warning(
        "Enter your Gemini API Key to start chatting."
        " You can create a free Gemini API Key [here](https://aistudio.google.com/app/api-keys).",
        icon=":material/warning:",
    )
    st.stop()


@st.cache_resource
def get_client(api_key: str):
    return genai.Client(api_key=api_key)


client = get_client(st.session_state["gemini_api_key"])


@st.dialog("New Chat")
def select_model():
    st.session_state["model"] = st.selectbox(
        ":material/robot: Select a model to use for this chat",
        options=sorted(
            [
                model.name.replace("models/", "")
                for model in client.models.list()
                if model.name.endswith("latest")
                and "generateContent" in getattr(model, "supported_actions", [])
            ]
        ),
        index=None,
        help="Details of all models can be found [here](https://ai.google.dev/gemini-api/docs/models).",
    )

    st.info(
        next(
            (
                model.description
                for model in client.models.list()
                if model.name.replace("models/", "") == st.session_state["model"]
            ),
            "Select model to see description",
        ),
        icon=":material/info:",
    )

    if st.button(
        "Start Chat",
        icon=":material/chat:",
        use_container_width=True,
        type="primary",
        disabled=st.session_state.get("model") is None,
    ):
        st.session_state["chat"] = client.chats.create(model=st.session_state["model"])
        st.session_state["messages"] = [WELCOME_MESSAGE]

        st.rerun()


st.sidebar.button(
    "New Chat",
    icon=":material/chat:",
    use_container_width=True,
    on_click=select_model,
)


if st.session_state.get("model"):
    with st.sidebar:
        st.markdown(
            f"**:material/robot: Chat Model:** {st.session_state['model']}",
            help="""
The model to use for this chat. Start a new chat to change the model.

Details of all models can be found [here](https://ai.google.dev/gemini-api/docs/models).
""",
        )
        temperature = st.slider(
            "**:material/thermometer: Temperature**",
            min_value=0.0,
            max_value=2.0,
            value=1.0,
            step=0.1,
            help="""Temperature controls the randomness of the model's output.
Lower values make the output more focused and deterministic, while higher values make it more creative and varied.
Learn more about temperature [here](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/content-generation-parameters#temperature).

You can change the temperature for each message in the chat.""",
        )


if st.session_state.get("chat"):
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_prompt := st.chat_input("Ask me anything about the data..."):
        st.session_state["messages"].append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.markdown(user_prompt)
        with st.chat_message("assistant"):
            placeholder = st.empty()
            response_chunks = []
            for chunk in st.session_state["chat"].send_message_stream(
                user_prompt,
                config=types.GenerateContentConfig(
                    temperature=temperature,
                    system_instruction=SYSTEM_PROMPT,
                ),
            ):
                response_chunks.append(chunk.text)
                placeholder.markdown("".join(response_chunks))

            st.session_state["messages"].append(
                {
                    "role": "assistant",
                    "content": "".join(response_chunks),
                }
            )

    with st.sidebar:
        st.download_button(
            "Download Conversation",
            "\n".join(
                [
                    f"### {message['role'].capitalize()}\n{message['content']}\n"
                    for message in st.session_state["messages"]
                ]
            ),
            file_name="conversation.md",
            mime="text/markdown",
            use_container_width=True,
            icon=":material/download:",
        )
