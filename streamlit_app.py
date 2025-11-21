# -------- 标题 --------
st.set_page_config(page_title="首尔天气仪表板", layout="wide")
st.title("🌦️ 首尔天气数据仪表板")
st.markdown("显示气温、湿度和降雨量的变化趋势，可按年份和月份筛选数据。")

# -------- 读取 CSV --------
df = pd.read_csv("weather.csv")
df["time"] = pd.to_datetime(df["time"])
df["year"] = df["time"].dt.year
df["month"] = df["time"].dt.month

# -------- 侧边栏筛选 --------
st.sidebar.header("筛选条件")
years = df["year"].unique()
selected_year = st.sidebar.selectbox("选择年份", years)
months = list(range(1,13))
selected_month = st.sidebar.selectbox("选择月份 (1-12)", months)

# -------- 筛选数据 --------
filtered = df[(df["year"] == selected_year) & (df["month"] == selected_month)]

# -------- 数据预览 --------
st.subheader(f"{selected_year}年{selected_month}月 数据预览")
st.dataframe(filtered[["time","temperature_2m_mean","relativehumidity_2m_mean","precipitation_sum"]])

# -------- 气温折线图 --------
st.subheader("🌡️ 气温变化")
fig1, ax1 = plt.subplots(figsize=(10,4))
ax1.plot(filtered["time"], filtered["temperature_2m_mean"], color='red', marker='o')
ax1.set_xlabel("日期")
ax1.set_ylabel("气温 (°C)")
ax1.grid(True)
st.pyplot(fig1)

# -------- 湿度折线图 --------
st.subheader("💧 湿度变化")
fig2, ax2 = plt.subplots(figsize=(10,4))
ax2.plot(filtered["time"], filtered["relativehumidity_2m_mean"], color='blue', marker='o')
ax2.set_xlabel("日期")
ax2.set_ylabel("湿度 (%)")
ax2.grid(True)
st.pyplot(fig2)

# -------- 降雨量柱状图 --------
st.subheader("🌧️ 降雨量")
fig3, ax3 = plt.subplots(figsize=(10,4))
ax3.bar(filtered["time"], filtered["precipitation_sum"], color='green')
ax3.set_xlabel("日期")
ax3.set_ylabel("降水量 (mm)")
ax3.grid(True)
st.pyplot(fig3)

# -------- 数据下载 --------
st.subheader("📥 下载筛选后的数据")
st.download_button(
    label="下载 CSV",
    data=filtered.to_csv(index=False).encode('utf-8-sig'),
    file_name=f"Seoul_weather_{selected_year}_{selected_month}.csv",
    mime="text/csv"
)
streamlit run dashboard.py
