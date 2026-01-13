import streamlit as st

st.header("Bells and Whistles :material/engineering:")

disabled = st.session_state.get("role", "viewer") not in ["admin", "editor"]

lcol, mcol, rcol = st.columns(3)

lcol.checkbox("Checkbox1", disabled=disabled)

mcol.color_picker("Color Picker", disabled=disabled)

rcol.multiselect(
    "Multiselect",
    ["Option 1", "Option 2", "Option 3"],
    disabled=disabled,
)

lcol.radio("Radio", ["Option 1", "Option 2", "Option 3"], disabled=disabled)

mcol.selectbox(
    "Select Box",
    ["Option 1", "Option 2", "Option 3"],
    disabled=disabled,
)

rcol.select_slider(
    "Select Slider",
    ["Option 1", "Option 2", "Option 3"],
    disabled=disabled,
)

lcol.toggle("Toggle", disabled=disabled)

mcol.number_input("Number Input", disabled=disabled)

rcol.slider("Slider", disabled=disabled)

lcol.date_input("Date Input", disabled=disabled)

mcol.time_input("Time Input", disabled=disabled)

rcol.text_input("Text Input", disabled=disabled)
