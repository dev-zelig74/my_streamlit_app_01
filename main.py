import streamlit as st
import pandas as pd

st.title('My first streamlit app')
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

st.write(df)
st.write(df["Age"])

ages = pd.Series("Age": [22,35,58])
st.write(ages)

