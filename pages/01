import streamlit as st
import pandas as pd

st.title("📊 레드오션 태그 분석")

@st.cache_data
def load_data():
    return pd.read_csv("dataset.csv")

df = load_data()

# 태그 분리 및 카운트
df_tags = df['tags'].str.split(',').explode().str.strip()
tag_counts = df_tags.value_counts().head(10)

st.subheader("가장 게임이 많은 상위 10개 태그")
st.bar_chart(tag_counts)

st.write("위 태그들은 게임 시장에서 경쟁이 가장 치열한 '레드오션' 분야입니다.")
