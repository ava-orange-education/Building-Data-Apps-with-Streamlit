import numpy as np
import pandas as pd
import streamlit as st

chart_data = pd.DataFrame(np.random.randn(50, 2), columns=["LAT", "LON"])

lcol, rcol = st.columns(2)

lcol.write("Scatter plot")
lcol.scatter_chart(chart_data)

rcol.write("Area chart")
rcol.area_chart(chart_data)

lcol.write("Bar chart")
lcol.bar_chart(chart_data)

rcol.write("Map")
rcol.map(chart_data + [22, 79])
