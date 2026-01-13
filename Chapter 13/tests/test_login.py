import pytest
from streamlit.testing.v1 import AppTest


@pytest.mark.parametrize(
    "username, password, role",
    [
        ["hacker123", "password123", None],
        ["viewer01", "password", None],
        ["hacker123", "password", None],
        ["johndoe", "password123", "admin"],
        ["janedoe", "securepass456", "editor"],
        ["viewer01", "viewonly789", "viewer"],
    ],
)
def test_login(username: str, password: str, role: str | None):
    """Test that login fails for an incorrect username-password combination
    and succeeds with the correct role assigned for a correct username-password combination.

    Args:
        username (str): The username to test
        password (str): The password to test
        role (str | None): The expected role
    """
    at = AppTest.from_file("login.py").run()

    at.text_input[0].set_value(username).run()
    at.text_input[1].set_value(password).run()
    at.button[0].click().run()

    if role is None:
        # Login failed
        assert at.get("form")[0].children[3].value.startswith("Login failed")
        assert at.sidebar.get("button") == []
    else:
        # Login successful
        assert at.sidebar.get("success")[0].value == f"Welcome **{username}** ({role}) :wave:"
        assert at.sidebar.button[0].label == "Logout"


def test_logout():
    """Test that clicking the Logout button shows the login form and hides the Logout button."""
    at = AppTest.from_file("login.py")

    # Simulate a successful login
    at.session_state.role = "viewer"
    at.run()

    # Click the Logout button
    at.sidebar.button[0].click().run()

    # Check that the login form is displayed
    login_form_elements = at.get("form")[0].children

    # Check that the Username text input is empty
    assert login_form_elements[0].label == "Username"
    assert login_form_elements[0].value == ""

    # Check that the Password text input is empty
    assert login_form_elements[1].label == "Password"
    assert login_form_elements[1].value == ""

    # Check that the Login button is displayed
    assert login_form_elements[2].label == "Login"
