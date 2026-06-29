import streamlit as st
import pandas as pd
from PIL import Image
import os

# --- 1. AYARLAR ---
st.set_page_config(page_title="ODE - Orbi Discovery Engine", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #f8fafc; }
    .stButton>button { width: 100%; border-radius: 10px; background: #1e293b; color: #deff9a; border: 1px solid #334155; }
    .stExpander { background-color: #1e293b; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- 2. VERİTABANI ---
@st.cache_data
def get_data():
    return pd.DataFrame([
        {"isim": "Piramitler", "kıta": "Afrika", "kategori": "Arkeoloji", "ikonik": "Evet", "modern": "Hayır"},
        {"isim": "Eyfel Kulesi", "kıta": "Avrupa", "kategori": "Modern", "ikonik": "Evet", "modern": "Evet"},
        {"isim": "Göbeklitepe", "kıta": "Asya", "kategori": "Arkeoloji", "ikonik": "Evet", "modern": "Hayır"},
        {"isim": "Machu Picchu", "kıta": "Güney Amerika", "kategori": "Arkeoloji", "ikonik": "Evet", "modern": "Hayır"},
        {"isim": "Burj Khalifa", "kıta": "Asya", "kategori": "Modern", "ikonik": "Evet", "modern": "Evet"}
    ])

# --- 3. SESSION STATE ---
if 'df' not in st.session_state:
    st.session_state.df = get_data()
    st.session_state.asked = []
    st.session_state.history = []

# --- 4. GÖRSEL VE BAŞLIK ---
if os.path.exists("orbi_ai.png"):
    st.image(Image.open("orbi_ai.png"), width=120)

st.title("ODE v1.5")
# Kalan aday sayısını buraya sabitliyoruz
st.metric("Kalan Aday Sayısı", len(st.session_state.df))
st.write("---")

# --- 5. OYUN MOTORU ---
df = st.session_state.df
features = ["kıta", "kategori", "ikonik", "modern"]
q = next((f for f in features if f not in st.session_state.asked), None)

if len(df) > 1 and q:
    st.subheader(f"🤔 Orbi: '{q}' özelliğine sahip mi?")
    c1, c2, c3 = st.columns(3)
    
    if c1.button("✅ Evet"):
        st.session_state.df = df[df[q] == "Evet"]
        st.session_state.asked.append(q)
        st.session_state.history.append((q, "Evet"))
        st.rerun()
    if c2.button("❌ Hayır"):
        st.session_state.df = df[df[q] != "Evet"]
        st.session_state.asked.append(q)
        st.session_state.history.append((q, "Hayır"))
        st.rerun()
    if c3.button("🤷 Bilmiyorum"):
        st.session_state.asked.append(q)
        st.rerun()

elif len(df) == 1:
    st.success(f"## 🎯 Buldum! Aklındaki yer: **{df.iloc[0]['isim']}**")
    if st.button("🔄 Yeni Keşif"):
        st.session_state.df = get_data()
        st.session_state.asked = []
        st.session_state.history = []
        st.rerun()
else:
    st.error("🚨 Hımm, bu yer radarımdaki seçeneklerle eşleşmiyor. Öğretmek ister misin?")
    if st.button("Baştan Başla"):
        st.session_state.df = get_data()
        st.session_state.asked = []
        st.session_state.history = []
        st.rerun()
