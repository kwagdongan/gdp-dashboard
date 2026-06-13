import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. 페이지 설정
st.set_page_config(page_title="Steam 분석 앱")
st.title("🎮 Steam 게임 분석 메인")

@st.cache_data
def load_data():
    return pd.read_csv("dataset.csv")

df = load_data()
st.metric("전체 데이터 개수", f"{df.shape[0]:,} 개")
st.write("왼쪽 사이드바에서 페이지를 이동하여 분석을 시작하세요.")
