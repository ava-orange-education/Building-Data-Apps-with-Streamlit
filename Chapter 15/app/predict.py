import pandas as pd
import streamlit as st
from autogluon.tabular import TabularPredictor

data = st.session_state["data"]
target = st.selectbox("Select the target column", options=data.columns)

with st.expander("Model Parameters", icon=":material/settings:"):
    col1, col2, col3 = st.columns([2, 2, 1])

    with col1:
        init_params = {}
        init_params["learner_kwargs"] = {}
        init_params["learner_kwargs"]["ignored_columns"] = st.multiselect(
            "Columns to ignore",
            options=[col for col in data.columns if col != target],
            placeholder="Select columns to ignore",
            key=f"ignored_columns_{st.session_state.get('key_suffix', 0)}",
        )

    with col2:
        fit_params = {}
        fit_params["presets"] = st.multiselect(
            "Select preset configurations",
            options=[
                "best_quality",
                "high_quality",
                "good_quality",
                "medium_quality",
                "experimental_quality",
                "optimize_for_deployment",
                "interpretable",
                "ignore_text",
            ],
            default=["best_quality", "optimize_for_deployment"],
            help="List of preset configurations. ",
            placeholder="Select preset configurations",
            key=f"presets_{st.session_state.get('key_suffix', 0)}",
        )

    with col3:
        fit_params["time_limit"] = st.number_input(
            "Training time limit (in seconds)",
            min_value=0,
            value=0,
            step=10,
            help="`0` will remove any time limit",
            key=f"time_limit_{st.session_state.get('key_suffix', 0)}",
        )
        fit_params["time_limit"] = (
            None if fit_params["time_limit"] == 0 else fit_params["time_limit"]
        )

    if st.button("Reset", icon=":material/refresh:"):
        st.session_state["key_suffix"] = st.session_state.get("key_suffix", 0) + 1
        st.rerun()


@st.cache_resource(show_spinner="Training model...")
def train_model(
    target: str, data: pd.DataFrame, init_params: dict, fit_params: dict
) -> TabularPredictor:
    predictor = TabularPredictor(label=target, verbosity=0, **init_params).fit(data, **fit_params)

    return predictor


if st.button("Train Model", icon=":material/model_training:", type="primary"):
    st.session_state["predictor"] = train_model(
        target=target,
        data=data,
        init_params=init_params,
        fit_params=fit_params,
    )

if st.session_state.get("predictor"):
    st.success("Model trained successfully!", icon=":material/check_circle:")
    predictor = st.session_state["predictor"]

    with st.expander("Model Details", icon=":material/info:"):
        if st.button("Fetch Model Details", icon=":material/info:"):
            st.subheader(":material/leaderboard: Model Leaderboard")
            st.dataframe(predictor.leaderboard(data))
            st.subheader(":material/bar_chart: Feature Importance")
            st.dataframe(predictor.feature_importance(data))
            st.subheader(":material/info: Model Info")
            st.write(predictor.info())

    st.subheader(":material/input: Enter data to get prediction")
    input_columns = [
        col
        for col in data.columns
        if col not in init_params["learner_kwargs"]["ignored_columns"] and col != target
    ]
    user_input = {}
    layout_columns = st.columns(3)
    for idx, column in enumerate(sorted(input_columns)):
        if data[column].dtype == "object":
            user_input[column] = layout_columns[idx % 3].selectbox(
                column,
                options=sorted(data[column].fillna("").unique()),
                accept_new_options=True,
            )
        else:
            user_input[column] = layout_columns[idx % 3].number_input(
                column,
                min_value=data[column].min(),
                max_value=data[column].max(),
            )

    st.subheader("Entered data")
    st.table(user_input)

    if st.button("Predict", icon=":material/rocket:", type="primary"):
        prediction = predictor.predict(
            pd.DataFrame([user_input]),
            as_pandas=False,
        )
        st.subheader(f"{target}: {prediction[0]}")
