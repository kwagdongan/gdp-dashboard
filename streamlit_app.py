import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="Steam 분석 대시보드", layout="wide")

# 2. 데이터 로드 (캐싱 사용)
@st.cache_data
def load_data():
    # 파일 경로 문제 해결을 위해 단순화
    return pd.read_csv("datas.csv")

df = load_data()

# 3. 사이드바 메뉴 구성
st.sidebar.title("🎮 메뉴")
menu = st.sidebar.radio("분석 페이지 선택", ["메인", "레드오션 분석", "평점 분석"])

# 4. 페이지별 내용 분기
if menu == "메인":
    st.title("Steam 게임 데이터 분석 메인")
    st.write("사이드바에서 분석 메뉴를 선택하세요.")
    st.metric("전체 데이터 개수", f"{df.shape[0]:,} 개")

elif menu == "레드오션 분석":
    st.title("📊 레드오션 분석 (가장 많은 태그)")
    
    # 태그 분리 및 빈도 계산
    tags = df['tags'].str.split('|').explode().str.strip()
    tag_counts = tags.value_counts().head(20).sort_values()
    
    st.bar_chart(tag_counts)
    st.write("이 태그들은 시장에서 가장 많이 사용되는 태그입니다.")

elif menu == "평점 분석":
    st.title("⭐ 평점 분석")
    st.write("평점 관련 데이터 분석을 수행하는 페이지입니다.")
    # 예: st.line_chart(...)
