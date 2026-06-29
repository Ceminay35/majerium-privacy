import streamlit as st
import pandas as pd
from PIL import Image
import os
import random

# --- 1. ARAYÜZ AYARLARI ---
st.set_page_config(page_title="ODE - Orbi Discovery Engine", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #f8fafc; }
    .stButton>button { width: 100%; border-radius: 12px; background: #1e293b; color: #deff9a; border: 1px solid #334155; }
    </style>
""", unsafe_allow_html=True)

# --- 2. VERİTABANI (ODE Engine Veri Seti) ---
def get_data():
    return pd.DataFrame([
        {"isim": "Piramitler", "kıta": "Afrika", "kategori": "Arkeoloji", "yapı": "Evet", "ikonik": "Evet"},
        {"isim": "Eyfel Kulesi", "kıta": "Avrupa", "kategori": "Modern", "yapı": "Evet", "ikonik": "Evet"},
        {"isim": "Göbeklitepe", "kıta": "Asya", "kategori": "Arkeoloji", "yapı": "Evet", "ikonik": "Evet"},
        {"isim": "Machu Picchu", "kıta": "Güney Amerika", "kategori": "Arkeoloji", "yapı": "Evet", "ikonik": "Evet"},
        {"isim": "Ayasofya", "kıta": "Asya", "kategori": "Tarihi", "yapı": "Evet", "ikonik": "Evet"},
        {"isim": "Kapadokya", "kıta": "Asya", "kategori": "Doğa", "yapı": "Hayır", "ikonik": "Evet"}
    ])

# --- 3. SESSION STATE ---
if 'df' not in st.session_state:
    st.session_state.df = get_data()
    st.session_state.asked = []

# --- 4. GÖRSEL VE BAŞLIK ---
if os.path.exists("orbi_ai.png"):
    st.image(Image.open("orbi_ai.png"), width=150)
st.title("ODE - Orbi Discovery Engine")

# --- 5. OYUN MOTORU (Akıllı Filtreleme) ---
df = st.session_state.df
features = ["kıta", "kategori", "yapı", "ikonik"]
q = next((f for f in features if f not in st.session_state.asked), None)

if len(df) > 1 and q:
    st.write(f"### 🧠 Orbi Keşifte: '{q}' hakkında ipucu arıyorum...")
    st.write(f"Kalan Aday: {len(df)}")
    
    col1, col2, col3 = st.columns(3)
    if col1.button("✅ Evet"):
        st.session_state.df = df[df[q] == "Evet"]
        st.session_state.asked.append(q)
        st.rerun()
    if col2.button("❌ Hayır"):
        st.session_state.df = df[df[q] != "Evet"]
        st.session_state.asked.append(q)
        st.rerun()
    if col3.button("🤷 Bilmiyorum"):
        st.session_state.asked.append(q)
        st.rerun()

elif len(df) == 1:
    st.success(f"## 🎉 Buldum! Aklındaki yer: **{df.iloc[0]['isim']}**")
    if st.button("🔄 Yeni Keşif"):
        st.session_state.df = get_data()
        st.session_state.asked = []
        st.rerun()
else:
    st.error("Orbi bu yerin izini kaybetti. Öğrenmemi ister misin?")
    if st.button("Baştan Başla"):
        st.session_state.df = get_data()
        st.session_state.asked = []
        st.rerun()
