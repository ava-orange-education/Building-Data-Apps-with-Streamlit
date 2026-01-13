import pandas as pd
import streamlit as st
import ydata_profiling
from scipy import stats
from streamlit_pandas_profiling import st_profile_report

data = st.session_state.get("data")

st.header(":material/preview: Preview")
st.dataframe(data)

st.header(":material/description: Description")
st.dataframe(data.describe())

st.header(":material/mop: Data Cleaning")


@st.cache_data
def drop_null_values(data: pd.DataFrame) -> tuple[int, float]:
    null_count = data.isna().any(axis=1).sum()
    null_percentage = null_count / len(data)

    return null_count, null_percentage


null_count, null_percentage = drop_null_values(data)
if null_count > 0:
    col1, col2 = st.columns(2)
    with col1:
        st.warning(
            f"Found **{null_count}** rows with NULL values (**{null_percentage:.2%}** of the dataset)"
        )
    with col2:
        if st.button(
            "Drop NULL values",
            icon=":material/warning:",
            use_container_width=True,
            help="This will remove all rows with **any** NULL values",
        ):
            data.dropna(inplace=True)
            st.session_state["data"] = data
            st.rerun()
else:
    st.success("No NULL values found", icon=":material/check_circle:")


@st.cache_data
def detect_outliers(data: pd.DataFrame, threshold: int) -> None:
    numeric_data = data.select_dtypes(include=["int64", "float64"])
    z_scores = abs(stats.zscore(numeric_data, nan_policy="omit"))
    outliers = numeric_data[(z_scores >= threshold).any(axis=1)]
    outlier_pct = len(outliers) / len(data)
    return outliers, outlier_pct


col1, col2, col3 = st.columns(3)
threshold = col1.slider("Z-score threshold", min_value=1, max_value=10, value=3)


outliers, outlier_pct = detect_outliers(data, threshold)


if outlier_pct > 0:
    col2.warning(
        f"Found **{len(outliers)}** rows with outliers (**{outlier_pct:.2%}** of the dataset)"
    )
    if col3.button(
        "Drop outliers",
        icon=":material/warning:",
        use_container_width=True,
        help="This will remove all rows with outliers",
    ):
        st.session_state["data"] = data[~data.index.isin(outliers.index)]
        st.rerun()
else:
    col2.success("No outliers found", icon=":material/check_circle:")

st.download_button(
    "Download cleaned Data",
    data.to_csv(),
    file_name=f"{st.session_state['dataset_name']}_cleaned.csv",
    mime="text/csv",
    icon=":material/download:",
)

st.header(":material/insights: Data Analysis")


@st.cache_data
def generate_profile_report(data: pd.DataFrame) -> ydata_profiling.ProfileReport:
    return data.profile_report()


if st.button(
    "Generate Dataset Report",
    icon=":material/insights:",
    type="primary",
):
    pr = generate_profile_report(data)
    st_profile_report(pr)

st.subheader(":material/bar_chart: Custom Plots")

col1, col2, col3, col4 = st.columns(4)

plot_type = col1.selectbox(
    "Select a plot",
    options=[
        st.area_chart,
        st.bar_chart,
        st.line_chart,
        st.map,
        st.scatter_chart,
    ],
    format_func=lambda x: x.__name__,
)

if plot_type.__name__ == st.map.__name__:
    latitude = col2.selectbox("Select Latitude Column", options=data.columns)
    longitude = col3.selectbox("Select Longitude Column", options=data.columns)
    plot_type(data, latitude=latitude, longitude=longitude)
else:
    x_axis = col2.selectbox("Select X-axis Column", options=data.columns)
    y_axis = col3.selectbox("Select Y-axis Column", options=data.columns)
    color = col4.selectbox("Select Color Column", options=data.columns)
    plot_type(data, x=x_axis, y=y_axis, color=color)
