import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Steam 태그 분석",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("datas.csv")

df = load_data()

st.title("🎮 Steam 게임 태그 분석")

st.markdown("""
### 분석 내용

- 가장 많이 사용되는 태그 (레드오션)
- 가장 평가가 좋은 태그
- 가장 평가가 나쁜 태그

왼쪽 메뉴에서 원하는 분석을 선택하세요.
""")

col1, col2 = st.columns(2)

with col1:
    st.metric("게임 수", len(df))

with col2:
    st.metric("컬럼 수", len(df.columns))

st.subheader("데이터 미리보기")
st.dataframe(df.head())
