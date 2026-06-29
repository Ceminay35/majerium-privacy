import streamlit as st
import pandas as pd
from PIL import Image

# 1. ORBI ENGINE: VERİTABANI
def get_landmarks():
    # Bu kısmı ileride data/landmarks.json'dan okuyacağız
    return pd.DataFrame([
        {"isim": "Piramitler", "kıta": "Afrika", "kategori": "Arkeoloji", "yapı": "Evet", "ikonik": "Evet"},
        {"isim": "Eyfel Kulesi", "kıta": "Avrupa", "kategori": "Modern", "yapı": "Evet", "ikonik": "Evet"},
        {"isim": "Göbeklitepe", "kıta": "Asya", "kategori": "Arkeoloji", "yapı": "Evet", "ikonik": "Evet"},
        {"isim": "Machu Picchu", "kıta": "Güney Amerika", "kategori": "Arkeoloji", "yapı": "Evet", "ikonik": "Evet"}
    ])

# 2. ENGINE: BİLGİ KAZANCI (FILTERING)
def get_best_question(df, asked_questions):
    features = ["kıta", "kategori", "yapı", "ikonik"]
    for f in features:
        if f not in asked_questions:
            return f
    return None

# 3. UI: ARAYÜZ
st.set_page_config(page_title="Orbi Discovery Engine", layout="centered")

# Görsel Yükleme
try:
    st.image(Image.open("orbi_ai.png"), width=200)
except:
    st.write("Orbi yükleniyor...")

st.title("Orbi Discovery Engine v1.0")

# Session State Yönetimi
if 'df' not in st.session_state:
    st.session_state.df = get_landmarks()
    st.session_state.asked = []

# Oyun Döngüsü
current_df = st.session_state.df
if len(current_df) > 1:
    q = get_best_question(current_df, st.session_state.asked)
    if q:
        st.write(f"### Orbi'nin Keşif Sorusu: Bu yerin özelliği '{q}' mu?")
        col1, col2, col3 = st.columns(3)
        if col1.button("Evet"):
            st.session_state.df = current_df[current_df[q] == "Evet"]
            st.session_state.asked.append(q)
            st.rerun()
        if col2.button("Hayır"):
            st.session_state.df = current_df[current_df[q] != "Evet"]
            st.session_state.asked.append(q)
            st.rerun()
else:
    winner = current_df.iloc[0]['isim'] if not current_df.empty else "Bilinmeyen"
    st.success(f"🎉 Orbi buldu: {winner}")
    if st.button("Yeni Keşif"):
        del st.session_state.df
        del st.session_state.asked
        st.rerun()
