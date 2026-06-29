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
    </style>
""", unsafe_allow_html=True)

# --- 2. VERİTABANI (Dinamik) ---
@st.cache_data
def get_data():
    # Burayı ileride 'pd.read_json("data/landmarks.json")' ile değiştireceğiz.
    return pd.DataFrame([
        {"isim": "Piramitler", "kıta": "Afrika", "kategori": "Arkeoloji", "ikonik": "Evet"},
        {"isim": "Eyfel Kulesi", "kıta": "Avrupa", "kategori": "Modern", "ikonik": "Evet"},
        {"isim": "Göbeklitepe", "kıta": "Asya", "kategori": "Arkeoloji", "ikonik": "Evet"}
    ])

# --- 3. SESSION STATE ---
if 'df' not in st.session_state:
    st.session_state.df = get_data()
    st.session_state.asked = []

# --- 4. GÖRSEL ---
if os.path.exists("orbi_ai.png"):
    st.image(Image.open("orbi_ai.png"), width=120)

st.title("ODE v1.3: Öğrenen Motor")

# --- 5. OYUN & ÖĞRENME MODU ---
df = st.session_state.df
features = ["kıta", "kategori", "ikonik"]
q = next((f for f in features if f not in st.session_state.asked), None)

if len(df) > 1 and q:
    st.subheader(f"Soru: Burası '{q}' kategorisine uygun mu?")
    c1, c2, c3 = st.columns(3)
    if c1.button("✅ Evet"):
        st.session_state.df = df[df[q] == "Evet"]
        st.session_state.asked.append(q)
        st.rerun()
    if c2.button("❌ Hayır"):
        st.session_state.df = df[df[q] != "Evet"]
        st.session_state.asked.append(q)
        st.rerun()
    if c3.button("🤷 Bilmiyorum"):
        st.session_state.asked.append(q)
        st.rerun()

elif len(df) == 1:
    st.success(f"🎯 Orbi'nin Tahmini: {df.iloc[0]['isim']}")
    if st.button("🔄 Yeni Keşif"):
        st.session_state.df = get_data()
        st.session_state.asked = []
        st.rerun()

else:
    st.warning("Orbi bu yeri henüz bilmiyor!")
    with st.form("ogrenme_formu"):
        yeni_yer = st.text_input("Tuttuğun yer neresi?")
        kategori = st.selectbox("Kategori", ["Arkeoloji", "Modern", "Doğa"])
        submit = st.form_submit_button("Orbi'ye Öğret")
        if submit:
            st.success(f"Teşekkürler! '{yeni_yer}' keşif listeme eklendi (Pending).")
