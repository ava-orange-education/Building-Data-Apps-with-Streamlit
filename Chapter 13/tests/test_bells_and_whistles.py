import pytest
from streamlit.testing.v1 import AppTest


@pytest.mark.parametrize("role", ["admin", "editor", "viewer"])
def test_bells_and_whistles(role: str):
    at = AppTest.from_file("bells_and_whistles.py")
    at.session_state.role = role
    at.run()

    disabled = role == "viewer"

    widgets = [
        at.checkbox,
        at.color_picker,
        at.multiselect,
        at.radio,
        at.selectbox,
        at.select_slider,
        at.toggle,
        at.number_input,
        at.slider,
        at.date_input,
        at.time_input,
        at.text_input,
    ]

    for widget in widgets:
        assert widget[0].disabled == disabled
