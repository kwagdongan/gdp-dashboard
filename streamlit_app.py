import streamlit as st
import pandas as pd

st.set_page_config(page_title="Steam 분석 앱", layout="wide")

st.title("🎮 Steam 게임 태그 분석 대시보드")
st.write("왼쪽 사이드바에서 분석 페이지를 선택하세요.")
# 사이드바에 글자 하나만 띄워보기
st.sidebar.title("테스트 사이드바")

st.title("메인 페이지")

# 버튼을 누르면 'pages/01_레드오션_분석.py'로 이동
if st.button("레드오션 분석 페이지로 이동"):
    st.switch_page("pages/01_page.py")

# 버튼을 누르면 'pages/02_평점_분석.py'로 이동
if st.button("평점 분석 페이지로 이동"):
    st.switch_page("pages/02_평점_분석.py")



@st.cache_data
def load_data():
    return pd.read_csv("datas.csv")

df = load_data()
st.metric("전체 데이터 개수", f"{df.shape[0]:,} 개")
