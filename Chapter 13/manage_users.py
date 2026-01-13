import json

import pandas as pd
import streamlit as st

with open("users.json", "r") as file:
    users = json.load(file)

st.header("Manage Users :material/people:")

users_df = pd.DataFrame(users).T.reset_index()
users_df.columns = ["Username", "Password", "Role"]
st.table(users_df[["Username", "Role"]])
