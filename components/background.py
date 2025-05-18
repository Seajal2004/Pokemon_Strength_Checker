import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def set_background(image_path):
    bg_img = get_base64_image(image_path)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(255,255,255,0.7), rgba(255,255,255,0.7)), url("data:image/jpeg;base64,{bg_img}");
            background-size: cover;
            background-attachment: fixed;
        }}
        .glass {{
            background: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0px 4px 30px rgba(0,0,0,0.1);
        }}
        h1, h2, h3 {{
            color: #2E3A59;
        }}
        .stButton>button {{
            background-color: #2E3A59;
            color: white;
            border-radius: 8px;
        }}
        .stButton>button:hover {{
            background-color: #4A5A78;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )