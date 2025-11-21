# 파일명: korea_weather_dashboard_kr.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import StringIO

st.title("한국 날씨 데이터 대시보드 🌦️")

# 데이터 가져오기 (예시: 공개 CSV 링크 사용)
DATA_URL = "https://raw.githubusercontent.com/your-repo/korea-weather/main/weather_data.csv"

@st.cache_data
def load_data():
    response = requests.get(DATA_URL)
    response.raise_for_status()
    csv_data = StringIO(response.text)
    df = pd.read_csv(csv_data, parse_dates=["날짜"])  # 날짜 컬럼
    return df

data = load_data()

# 원본 데이터 보여주기
st.subheader("원본 데이터")
st.dataframe(data)

# 시각화 선택
st.subheader("데이터 시각화")
option = st.selectbox("표시할 지표 선택", ["기온", "습도", "강수량"])

# 그래프 그리기
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(data["날짜"], data[option], marker='o', linestyle='-', color='skyblue')
ax.set_xlabel("날짜")
ax.set_ylabel(option)
ax.s
pip install streamlit pandas matplotlib requests
streamlit run korea_weather_dashboard_kr.py
