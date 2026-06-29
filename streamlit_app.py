import streamlit as st
import pandas as pd
import json

class ODEEngine:
    def __init__(self, data_path="landmarks.json"):
        # Veri Yükleme (Phase 2'de burası dinamik olacak)
        self.df = pd.DataFrame([
            {"isim": "Piramitler", "kıta": "Afrika", "kategori": "Arkeoloji", "yapı": "Evet", "ikonik": "Evet"},
            {"isim": "Eyfel Kulesi", "kıta": "Avrupa", "kategori": "Modern", "yapı": "Evet", "ikonik": "Evet"}
        ])
        
    def filter_data(self, df, feature, answer):
        # Aday eleme motoru
        if answer == "Evet": return df[df[feature] == "Evet"]
        if answer == "Hayır": return df[df[feature] != "Evet"]
        return df # Bilmiyorum durumu

class ODEUI:
    @staticmethod
    def render_header():
        st.title("🌍 ODE - Orbi Discovery Engine")
        st.markdown("---")

# Uygulama Çalıştırma
engine = ODEEngine()
ODEUI.render_header()

# Durum Yönetimi
if 'current_df' not in st.session_state:
    st.session_state.current_df = engine.df

# Aday sayısı kontrolü ve soru akışı...
# (Buradan itibaren senin belirttiğin o 18 maddelik mimariyi parça parça ekleyeceğiz)
