import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. 페이지 설정
st.set_page_config(page_title="Steam 게임 태그 분석", layout="wide")
st.title("🎮 Steam 게임 태그 연관 규칙 분석")

# 2. 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("datas.csv")
    # 태그를 콤마(,) 기준으로 분리하여 리스트로 변환
    df['tags'] = df['tags'].str.split(',')
    return df

df = load_data()

# 3. 데이터 전처리 (태그 폭발: explode)
df_tags = df.explode('tags')
df_tags['tags'] = df_tags['tags'].str.strip()

# 4. 분석 섹션
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 가장 인기 있는 태그 (레드오션)")
    tag_counts = df_tags['tags'].value_counts().head(10)
    st.bar_chart(tag_counts)

with col2:
    st.subheader("💡 태그 데이터 살펴보기")
    st.dataframe(df.head(10))

# 5. 전략적 제언
st.markdown("---")
st.subheader("🔍 전략적 분석 결과")

# 데이터 총 개수 계산 (행의 개수)
total_rows = df.shape[0]

# 화면에 표시
st.metric(label="전체 데이터 개수", value=f"{total_rows:,} 개")

st.write("""
- **레드오션:** 그래프에서 가장 높게 나타나는 태그들은 게임 시장에서 이미 경쟁이 매우 치열합니다.
- **틈새 전략:** 태그 빈도는 낮지만 평가가 좋은 태그 조합을 찾는 것이 전략적 핵심입니다.
""")

# 6. 추가 기능: 특정 태그 검색
search_tag = st.selectbox("분석하고 싶은 태그를 선택하세요:", df_tags['tags'].unique())
if search_tag:
    subset = df_tags[df_tags['tags'] == search_tag]
    st.write(f"'{search_tag}' 태그를 포함한 게임 수: {len(subset)}개")
