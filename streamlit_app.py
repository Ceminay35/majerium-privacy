import streamlit as st
import pandas as pd
from PIL import Image
import os
import random

# --- 1. AYARLAR & CSS ---
st.set_page_config(page_title="ODE - Orbi Discovery Engine", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #f8fafc; }
    .stButton>button { width: 100%; border-radius: 12px; background: #1e293b; color: #deff9a; border: 1px solid #334155; }
    </style>
""", unsafe_allow_html=True)

# --- 2. ORBI MESAJLARI (KARAKTER) ---
comments = {
    "başlangıç": ["Keşif başlıyor! İlk ipucunu arıyorum...", "Dünya haritasını tarıyorum..."],
    "devam": ["Hmm, bu veri adaylarımı yarıya düşürdü!", "Güzel... Artık daha dar bir alandayız."],
    "final": ["Buldum! İşte aradığımız yer tam burada!"]
}

# --- 3. VERİ YÖNETİMİ ---
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame([
        {"isim": "Piramitler", "kıta": "Afrika", "kategori": "Arkeoloji", "yapı": "Evet", "ikonik": "Evet"},
        {"isim": "Eyfel Kulesi", "kıta": "Avrupa", "kategori": "Modern", "yapı": "Evet", "ikonik": "Evet"},
        {"isim": "Göbeklitepe", "kıta": "Asya", "kategori": "Arkeoloji", "yapı": "Evet", "ikonik": "Evet"},
        {"isim": "Machu Picchu", "kıta": "Güney Amerika", "kategori": "Arkeoloji", "yapı": "Evet", "ikonik": "Evet"}
    ])
    st.session_state.asked = []

# --- 4. GÖRSEL & BAŞLIK ---
if os.path.exists("orbi_ai.png"):
    st.image(Image.open("orbi_ai.png"), width=150)
st.title("ODE - Orbi Discovery Engine")

# --- 5. OYUN MOTORU ---
df = st.session_state.df
features = ["kıta", "kategori", "yapı", "ikonik"]
q = next((f for f in features if f not in st.session_state.asked), None)

if len(df) > 1 and q:
    st.subheader(f"🤔 Soru: Bu yerin özelliği '{q}' mı?")
    st.write(f"Kalan aday sayısı: {len(df)}")
    
    col1, col2, col3 = st.columns(3)
    if col1.button("✅ Evet"):
        st.session_state.df = df[df[q] == "Evet"]
        st.session_state.asked.append(q)
        st.success(random.choice(comments["devam"]))
        st.rerun()
    if col2.button("❌ Hayır"):
        st.session_state.df = df[df[q] != "Evet"]
        st.session_state.asked.append(q)
        st.rerun()
    if col3.button("🤷 Bilmiyorum"):
        st.session_state.asked.append(q)
        st.rerun()

elif len(df) == 1:
    st.success(f"## 🎉 {random.choice(comments['final'])}")
    st.subheader(f"Tahmin: **{df.iloc[0]['isim']}**")
    if st.button("🔄 Yeni Keşif"):
        st.session_state.df = None
        st.session_state.asked = []
        st.rerun()
