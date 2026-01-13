import json

import pandas as pd
from streamlit.testing.v1 import AppTest


def test_displayed_users():
    at = AppTest.from_file("manage_users.py").run()

    with open("users.json", "r") as file:
        users = json.load(file)

    users_df = pd.DataFrame(users).T.reset_index()
    users_df.columns = ["Username", "Password", "Role"]

    assert all(at.table[0].data == users_df[["Username", "Role"]])
