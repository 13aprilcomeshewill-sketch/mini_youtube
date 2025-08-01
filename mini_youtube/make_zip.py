import zipfile
import os

# สร้างโฟลเดอร์โปรเจกต์
project_name = "mini_youtube"
os.makedirs(f"{project_name}/data", exist_ok=True)

# สร้างไฟล์ app.py
app_code = '''
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
'''
with open(f"{project_name}/app.py", "w", encoding="utf-8") as f:
    f.write(app_code)

# สร้าง requirements.txt
with open(f"{project_name}/requirements.txt", "w") as f:
    f.write("streamlit\npandas")

# สร้าง data/videos.csv
video_data = '''title,category,url
เรียน Python เบื้องต้น,ความรู้,https://www.youtube.com/watch?v=rfscVS0vtbw
10 หนังน่าดูบน Netflix,บันเทิง,https://www.youtube.com/watch?v=tzkWB85ULJY
รีวิวมือถือรุ่นใหม่,เทคโนโลยี,https://www.youtube.com/watch?v=tRWFDprpJXE
'''
with open(f"{project_name}/data/videos.csv", "w", encoding="utf-8") as f:
    f.write(video_data)

# สร้าง ZIP
with zipfile.ZipFile(f"{project_name}.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
    for folder, _, files in os.walk(project_name):
        for file in files:
            full_path = os.path.join(folder, file)
            arcname = os.path.relpath(full_path, project_name)
            zipf.write(full_path, arcname)
