import streamlit as st
import pandas as pd

st.set_page_config(page_title="Steam 분석 앱", layout="wide")

st.title("🎮 Steam 게임 태그 분석 대시보드")
st.write("왼쪽 사이드바에서 분석 페이지를 선택하세요.")

@st.cache_data
def load_data():
    return pd.read_csv("datas.csv")

df = load_data()
st.metric("전체 데이터 개수", f"{df.shape[0]:,} 개")
