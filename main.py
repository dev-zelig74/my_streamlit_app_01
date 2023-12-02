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

ages = pd.Series([22,35,58], name="Age")
st.write(ages)
st.write(ages.max())
st.write(ages.describe())


