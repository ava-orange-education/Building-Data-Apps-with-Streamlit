import streamlit as st

lcol, rcol = st.columns(2)

checkbox = lcol.checkbox("This is a checkbox")
lcol.write(f"Value of checkbox: {checkbox}")

toggle = rcol.toggle("This is a toggle")
rcol.write(f"Value of toggle: {toggle}")

color = lcol.color_picker("This is a color picker")
lcol.write(f"Value of color picker: {color}")

multiselect = rcol.multiselect(
    "This is a multiselect", ["Option 1", "Option 2", "Option 3"]
)
rcol.write(f"Value of multiselect: {multiselect}")

radio = lcol.radio(
    "This is a radio",
    ["Option 1", "Option 2", "Option 3"],
    horizontal=True,
)
lcol.write(f"Value of radio: {radio}")

select_slider = rcol.slider(
    "This is a slider",
    value=(0, 10),
)
rcol.write(f"Value of slider: {select_slider}")

select_slider = lcol.select_slider(
    "This is a select slider",
    ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"],
    value=["Option 1", "Option 3"],
)
lcol.write(f"Value of select slider: {select_slider}")

date = rcol.date_input("This is a date input")
rcol.write(f"Value of date input: {date}")

time = lcol.time_input("This is a time input")
lcol.write(f"Value of time input: {time}")

text_area = rcol.text_area("This is a text area")
rcol.write(f"Value of text area: {text_area}")

chat_input = lcol.chat_input()
lcol.write(f"Value of chat input: {chat_input}")
