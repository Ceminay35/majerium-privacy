import streamlit as st
import pandas as pd
from PIL import Image

# 1. AYARLAR & TASARIM
st.set_page_config(page_title="Orbi Discovery v1.0", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #f8fafc; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5em; background: #1e293b; color: #deff9a; border: 1px solid #334155; font-weight: bold; }
    .stButton>button:hover { background: #334155; border: 1px solid #deff9a; }
    </style>
""", unsafe_allow_html=True)

# 2. VERİTABANI (ODE Engine v1.0)
def get_landmarks():
    return pd.DataFrame([
        {"isim": "Piramitler", "kıta": "Afrika", "kategori": "Arkeoloji", "yapı": "Evet", "ikonik": "Evet"},
        {"isim": "Eyfel Kulesi", "kıta": "Avrupa", "kategori": "Modern", "yapı": "Evet", "ikonik": "Evet"},
        {"isim": "Göbeklitepe", "kıta": "Asya", "kategori": "Arkeoloji", "yapı": "Evet", "ikonik": "Evet"},
        {"isim": "Machu Picchu", "kıta": "Güney Amerika", "kategori": "Arkeoloji", "yapı": "Evet", "ikonik": "Evet"},
        {"isim": "Amazon Ormanı", "kıta": "Güney Amerika", "kategori": "Doğa", "yapı": "Hayır", "ikonik": "Evet"},
        {"isim": "Kolezyum", "kıta": "Avrupa", "kategori": "Arkeoloji", "yapı": "Evet", "ikonik": "Evet"}
    ])

# 3. BAŞLATMA
try:
    st.image(Image.open("orbi_ai.png"), width=200)
except:
    st.write("🤖 Orbi yükleniyor...")

st.title("Orbi Discovery Engine")
st.write("---")

if 'df' not in st.session_state:
    st.session_state.df = get_landmarks()
    st.session_state.asked = []

# 4. OYUN MOTORU (ELEME)
df = st.session_state.df
features = ["kıta", "kategori", "yapı", "ikonik"]

# Henüz sorulmamış bir soru bul
q = next((f for f in features if f not in st.session_state.asked), None)

if len(df) > 1 and q:
    st.subheader(f"🤔 Orbi'nin Keşif Sorusu:")
    st.write(f"Sence burası **'{q}'** kategorisine uygun bir yer mi?")
    
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
    
    st.write(f"---")
    st.caption(f"Kalan aday sayısı: {len(df)}")
    
elif len(df) == 1:
    winner = df.iloc[0]['isim']
    st.success(f"## 🎉 Buldum! Aklındaki yer: **{winner}**")
    if st.button("🔄 Yeni Keşif"):
        st.session_state.df = get_landmarks()
        st.session_state.asked = []
        st.rerun()
else:
    st.error("Hımm, kafam karıştı! Bu yeri henüz öğrenmedim.")
    if st.button("Baştan Başla"):
        st.session_state.df = get_landmarks()
        st.session_state.asked = []
        st.rerun()
