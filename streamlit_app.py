import streamlit as st

st.title("🎈import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv("weather.csv")

# 将日期转换为日期格式
df["date"] = pd.to_datetime(df["date"])

# ======= 预览数据 =======
print(df.head())
print(df.describe())

# -------------------------
# 1. 温度折线图
# -------------------------
plt.figure(figsize=(12,5))
plt.plot(df["date"], df["temperature_2m_mean"])
plt.title("Daily Temperature")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.show()

# -------------------------
# 2. 湿度折线图
# -------------------------
plt.figure(figsize=(12,5))
plt.plot(df["date"], df["relativehumidity_2m_mean"])
plt.title("Daily Humidity")
plt.xlabel("Date")
plt.ylabel("Humidity (%)")
plt.grid()
plt.show()

# -------------------------
# 3. 降雨量柱状图
# -------------------------
plt.figure(figsize=(12,5))
plt.bar(df["date"], df["precipitation_sum"])
plt.title("Daily Precipitation")
plt.xlabel("Date")
plt.ylabel("Rainfall (mm)")
plt.grid()
plt.show()
")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
