import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Game Bida 3D",
    page_icon="🎱",
    layout="wide"
)

st.title("🎱 Game Bida 3D trên Streamlit")
st.write("Nhấn giữ chuột trái để tích lực, thả ra để đánh bi cái!")

# Đọc tệp html của game
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Chạy game trong ứng dụng Streamlit
components.html(html_code, height=650, scrolling=False)
