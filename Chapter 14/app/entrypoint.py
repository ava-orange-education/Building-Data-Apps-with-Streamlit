import pandas as pd
import streamlit as st

# Section 1: Page favicon and title
st.set_page_config(
    page_icon=":crystal_ball:",
    page_title="DataConverse",
    layout="wide",
)

# Section 2: App logo, title, and description
st.title(":crystal_ball: DataConverse")
st.write("Welcome to DataConverse, your personal data assistant.")

if "data" not in st.session_state:
    # Section 3: Data upload section
    @st.cache_data(ttl="1h")
    def cached_upload_data(file):
        return pd.read_csv(file)

    col1, col2 = st.columns([2, 3])
    with col1:
        file = st.file_uploader("Upload a CSV file", type=["csv"])
        if file:
            st.session_state["data"] = cached_upload_data(file)
            st.session_state["dataset_name"] = file.name
            st.rerun()

    # Section 4: Sample data selection
    @st.cache_data
    def cached_sample_datasets(path):
        return pd.read_csv(path)

    SAMPLE_DATASETS = {
        "Iris": {"path": "data/iris.csv", "icon": ":material/local_florist:"},
        "Wine": {"path": "data/wine.csv", "icon": ":material/local_bar:"},
        "Housing": {"path": "data/housing.csv", "icon": ":material/home:"},
    }

    with col2:
        st.text("Or select a sample dataset")
        columns = st.columns(len(SAMPLE_DATASETS))
        for i, (dataset_name, dataset_info) in enumerate(SAMPLE_DATASETS.items()):
            if columns[i].button(
                dataset_name,
                icon=dataset_info["icon"],
                use_container_width=True,
            ):
                st.session_state["data"] = cached_sample_datasets(dataset_info["path"])
                st.session_state["dataset_name"] = dataset_name
                st.rerun()

else:
    with st.sidebar:
        # Section 5: Display data info
        st.info(
            f"Using **{st.session_state['dataset_name']}** (Size: **{len(st.session_state['data'])}**)",
            icon=":material/description:",
        )

        # Section 6: Reset Button
        @st.dialog("⚠️ Are you sure?")
        def reset():
            st.write("This will reset the app to its initial state.")
            col1, col2 = st.columns(2)
            if col1.button("Yes, reset the app", use_container_width=True):
                st.session_state.clear()
                st.cache_data.clear()
                st.cache_resource.clear()
                st.rerun()
            elif col2.button(
                "No, I changed my mind",
                use_container_width=True,
                type="primary",
            ):
                st.rerun()

        st.button(
            "Reset",
            use_container_width=True,
            icon=":material/refresh:",
            on_click=reset,
        )

        # Section 7: Page Navigation
        st.divider()

        analyze_page = st.Page("analyze.py", title="Analyze")
        predict_page = st.Page("predict.py", title="Predict")
        chat_page = st.Page("chat.py", title="Chat")

        page = st.navigation(
            [analyze_page, predict_page, chat_page],
            position="hidden",
        )

        st.page_link(analyze_page, icon=":material/insights:")
        st.page_link(predict_page, icon=":material/batch_prediction:")
        st.page_link(chat_page, icon=":material/chat:")

    page.run()
