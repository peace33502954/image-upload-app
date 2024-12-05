
# pip install streamlit
# streamlit run app.py
# pip install pyngrok

import os
import streamlit as st
from PIL import Image

# 設置圖片保存的文件夾
UPLOAD_FOLDER = "uploaded_images"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # 如果文件夾不存在，則創建

# 標題
st.title("用戶圖片上傳與管理系統")

# 上傳圖片
uploaded_file = st.file_uploader("請上傳圖片", type=["jpg", "jpeg", "png"])
if uploaded_file:
    # 保存圖片到 UPLOAD_FOLDER
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"圖片已成功上傳！文件名：{uploaded_file.name}")
    # 顯示上傳的圖片
    st.image(file_path, caption="您上傳的圖片", use_column_width=True)

# 瀏覽所有上傳的圖片
st.header("所有用戶上傳的圖片")
image_files = os.listdir(UPLOAD_FOLDER)  # 列出文件夾中的所有文件
if image_files:
    selected_image = st.selectbox("選擇要刪除的圖片", image_files)  # 下拉菜單選擇圖片
    col1, col2 = st.columns([3, 1])  # 設置兩列布局

    with col1:
        # 顯示所選圖片
        if selected_image:
            image_path = os.path.join(UPLOAD_FOLDER, selected_image)
            st.image(image_path, caption=f"當前選擇: {selected_image}", use_column_width=True)
    
    with col2:
        # 添加刪除按鈕
        if st.button("刪除圖片"):
            os.remove(image_path)  # 刪除所選圖片
            st.success(f"圖片 {selected_image} 已被刪除！")
            st.experimental_rerun()  # 刷新頁面
else:
    st.write("目前沒有上傳的圖片。")


# 請將圖片檔改成 姓名_學號-圖片類型