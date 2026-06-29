import streamlit as st
import pandas as pd
from PIL import Image
import os

# --- 1. TASARIM VE AYARLAR ---
st.set_page_config(page_title="ODE - Orbi Discovery Engine", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #f8fafc; }
    .stButton>button { width: 100%; border-radius: 10px; background: #1e293b; color: #deff9a; border: 1px solid #334155; }
    </style>
""", unsafe_allow_html=True)

# --- 2. VERİTABANI (Dinamik Genişletilebilir) ---
def get_data():
    return pd.DataFrame([
        {"isim": "Piramitler", "kıta": "Afrika", "kategori": "Arkeoloji", "ikonik": "Evet"},
        {"isim": "Eyfel Kulesi", "kıta": "Avrupa", "kategori": "Modern", "ikonik": "Evet"},
        {"isim": "Göbeklitepe", "kıta": "Asya", "kategori": "Arkeoloji", "ikonik": "Evet"},
        {"isim": "Machu Picchu", "kıta": "Güney Amerika", "kategori": "Arkeoloji", "ikonik": "Evet"},
        {"isim": "Ayasofya", "kıta": "Asya", "kategori": "Tarihi", "ikonik": "Evet"},
        {"isim": "Amazon Ormanı", "kıta": "Güney Amerika", "kategori": "Doğa", "ikonik": "Hayır"}
    ])

# --- 3. SESSION STATE ---
if 'df' not in st.session_state:
    st.session_state.df = get_data()
    st.session_state.asked = []

# --- 4. GÖRSEL ---
if os.path.exists("orbi_ai.png"):
    st.image(Image.open("orbi_ai.png"), width=120)

st.title("ODE v1.2: Analitik Mod")

# --- 5. OYUN MOTORU VE XAI (Açıklanabilir Zeka) ---
df = st.session_state.df
features = ["kıta", "kategori", "ikonik"]
q = next((f for f in features if f not in st.session_state.asked), None)

if len(df) > 1 and q:
    st.info(f"🧠 **Orbi'nin Analizi:** '{q}' kriterini kullanarak aday listemi {len(df)}'den daraltıyorum...")
    
    st.subheader(f"Soru: Bu yerin '{q}' özelliği var mı?")
    
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
    st.balloons()
    st.success(f"## 🎯 Buldum! Aklındaki yer: {df.iloc[0]['isim']}")
    st.write("---")
    st.write("### 📝 Orbi'nin Notu:")
    st.write(f"Seni bu sonuca ulaştırmak için '{st.session_state.asked}' özelliklerini kullandım.")
    if st.button("🔄 Yeni Keşif"):
        st.session_state.df = get_data()
        st.session_state.asked = []
        st.rerun()
else:
    st.error("Bu yeri henüz keşfetmedim!")
    if st.button("Baştan Başla"):
        st.session_state.df = get_data()
        st.session_state.asked = []
        st.rerun()
