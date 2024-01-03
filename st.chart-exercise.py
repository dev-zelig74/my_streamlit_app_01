import streamlit as st
import pandas as pd
import numpy as np
import altait as alt

st.header('Line chart')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['a','b','c'])

st.line_chart(chart_data)

st.subheader('Altair line chart')

c = (
   alt.Chart(chart_data)
   .mark_circle()
   .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.altair_chart(c, use_container_width=True)
