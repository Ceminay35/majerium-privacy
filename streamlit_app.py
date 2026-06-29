import streamlit as st
import pandas as pd
from PIL import Image
import os

# --- 1. AYARLAR & CSS ---
st.set_page_config(page_title="ODE - Orbi Discovery Engine", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #f8fafc; }
    .stButton>button { width: 100%; border-radius: 12px; background: #1e293b; color: #deff9a; border: 1px solid #334155; }
    </style>
""", unsafe_allow_html=True)

# --- 2. GÖRSEL YÖNETİMİ ---
# Görselin varlığını kontrol et
if os.path.exists("orbi_ai.png"):
    image = Image.open("orbi_ai.png")
    st.image(image, width=150)
else:
    st.write("🤖 Orbi keşfe hazır!")

st.title("ODE - Orbi Discovery Engine")

# --- 3. VERİ YÖNETİMİ ---
# Veritabanı iskeleti
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame([
        {"isim": "Piramitler", "kıta": "Afrika", "kategori": "Arkeoloji", "yapı": "Evet"},
        {"isim": "Eyfel Kulesi", "kıta": "Avrupa", "kategori": "Modern", "yapı": "Evet"},
        {"isim": "Göbeklitepe", "kıta": "Asya", "kategori": "Arkeoloji", "yapı": "Evet"}
    ])
    st.session_state.asked = []

# --- 4. OYUN MOTORU (HIZLI AKIŞ) ---
df = st.session_state.df
features = ["kıta", "kategori", "yapı"]

# Henüz sorulmamış soru bul
q = next((f for f in features if f not in st.session_state.asked), None)

if len(df) > 1 and q:
    st.subheader(f"Soru: Bu yerin özelliği '{q}' mu?")
    col1, col2 = st.columns(2)
    if col1.button("Evet"):
        st.session_state.df = df[df[q] == "Evet"]
        st.session_state.asked.append(q)
        st.rerun()
    if col2.button("Hayır"):
        st.session_state.df = df[df[q] != "Evet"]
        st.session_state.asked.append(q)
        st.rerun()
elif len(df) == 1:
    st.success(f"🎉 Buldum: {df.iloc[0]['isim']}")
    if st.button("Tekrar Oyna"):
        st.session_state.df = None
        st.rerun()
