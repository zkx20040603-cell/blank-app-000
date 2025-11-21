# 文件名：korea_weather_dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import StringIO

st.title("韩国天气数据仪表板 🌦️")

# 数据获取（示例使用一个公开 CSV 链接，可根据需要更换）
DATA_URL = "https://raw.githubusercontent.com/your-repo/korea-weather/main/weather_data.csv"

@st.cache_data
def load_data():
    response = requests.get(DATA_URL)
    response.raise_for_status()
    csv_data = StringIO(response.text)
    df = pd.read_csv(csv_data, parse_dates=["날짜"])  # 韩国天气数据一般列名为 날짜(日期)
    return df

data = load_data()

# 显示原始数据
st.subheader("原始数据")
st.dataframe(data)

# 可视化选项
st.subheader("数据可视化")
option = st.selectbox("选择要显示的指标", ["기온", "습도", "강수량"])  # 气温, 湿度, 降雨量

# 绘图
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(data["날짜"], data[option], marker='o', linestyle='-', color='skyblue')
ax.set_xlabel("日期")
ax.set_ylabel(option)
ax.set_title(f"{option} 趋势")
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# 统计信息
st.subheader("统计信息")
st.write(data.describe())
pip install streamlit pandas matplotlib requests
streamlit run korea_weather_dashboard.py
