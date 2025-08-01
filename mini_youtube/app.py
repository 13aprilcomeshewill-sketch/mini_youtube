
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mini YouTube", layout="wide")
st.title("🎬 Mini YouTube (หมวดหมู่)")

# โหลดข้อมูลวิดีโอ
df = pd.read_csv("data/videos.csv")
categories = df["category"].unique()

selected_category = st.sidebar.selectbox("เลือกหมวดหมู่", categories)

# กรองวิดีโอตามหมวดหมู่
filtered_videos = df[df["category"] == selected_category]

for idx, row in filtered_videos.iterrows():
    st.subheader(row["title"])
    st.video(row["url"])
    st.markdown("---")
