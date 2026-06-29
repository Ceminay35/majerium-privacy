"""
ORBI DISCOVERY ENGINE (ODE)
Version: 2.0.0 - Mobile Ready
Akinator mantığıyla çalışan yer tahmin oyunu
TEK DOSYA - TÜM KOD BURADA
"""

import streamlit as st
import random
import math
import time
from typing import Dict, List, Optional

# ============================================
# SAYFA YAPILANDIRMASI (MOBİL UYUMLU)
# ============================================
st.set_page_config(
    page_title="Orbi Discovery",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================
# ÖZEL CSS (MOBİL UYUMLU DARK THEME)
# ============================================
st.markdown("""
<style>
    /* Ana tema - Mobil uyumlu */
    .stApp {
        background: linear-gradient(135deg, #0a0a1a 0%, #1a1a2e 50%, #0d1f3c 100%);
        min-height: 100vh;
    }
    
    /* Ana container - Mobil genişlik */
    .main-container {
        max-width: 480px;
        margin: 0 auto;
        padding: 10px 15px;
    }
    
    /* Orbi başlık - Mobil boyut */
    .orbi-title {
        color: #00d4ff;
        font-size: 2.2em;
        font-weight: 800;
        text-align: center;
        text-shadow: 0 0 30px rgba(0, 212, 255, 0.2);
        margin: 5px 0;
        letter-spacing: 1px;
    }
    
    .orbi-subtitle {
        color: #8899aa;
        text-align: center;
        font-size: 0.95em;
        margin-bottom: 15px;
        opacity: 0.8;
    }
    
    /* Kart tasarımı - Mobil uyumlu */
    .orbi-card {
        background: rgba(255, 255, 255, 0.04);
        border-radius: 16px;
        padding: 18px 20px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(10px);
        margin-bottom: 12px;
        transition: all 0.3s ease;
    }
    
    .orbi-card:hover {
        background: rgba(255, 255, 255, 0.06);
        border-color: rgba(0, 212, 255, 0.15);
    }
    
    /* Orbi konuşma balonu - Mobil */
    .orbi-speech {
        background: linear-gradient(135deg, #0d2847, #16213e);
        border-radius: 18px;
        padding: 16px 20px;
        border-left: 4px solid #00d4ff;
        color: #d0dce8;
        font-size: 1em;
        margin: 8px 0 15px 0;
        box-shadow: 0 4px 20px rgba(0, 212, 255, 0.05);
        position: relative;
    }
    
    .orbi-speech::before {
        content: "🧠";
        position: absolute;
        left: -12px;
        top: -10px;
        font-size: 1.5em;
        filter: drop-shadow(0 2px 8px rgba(0,212,255,0.3));
    }
    
    .orbi-speech .orbi-name {
        color: #00d4ff;
        font-weight: 700;
        font-size: 0.9em;
        display: block;
        margin-bottom: 4px;
        padding-left: 20px;
    }
    
    .orbi-speech .orbi-text {
        padding-left: 20px;
        line-height: 1.5;
    }
    
    /* Butonlar - Mobil dokunmatik */
    .stButton > button {
        background: linear-gradient(135deg, #00d4ff, #0077be);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 14px 20px;
        font-weight: 600;
        font-size: 1em;
        transition: all 0.2s ease;
        width: 100%;
        box-shadow: 0 4px 20px rgba(0, 212, 255, 0.15);
        cursor: pointer;
        touch-action: manipulation;
        min-height: 52px;
    }
    
    .stButton > button:active {
        transform: scale(0.96);
        box-shadow: 0 2px 10px rgba(0, 212, 255, 0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 25px rgba(0, 212, 255, 0.25);
        background: linear-gradient(135deg, #00e5ff, #0088cc);
    }
    
    /* Radio butonlar - Mobil uyumlu */
    .stRadio > div {
        gap: 6px;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
    }
    
    .stRadio label {
        background: rgba(255, 255, 255, 0.04);
        padding: 10px 18px;
        border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        color: #b0bcc8;
        transition: all 0.2s ease;
        cursor: pointer;
        font-size: 0.9em;
        min-width: 70px;
        text-align: center;
        touch-action: manipulation;
    }
    
    .stRadio label:hover {
        background: rgba(0, 212, 255, 0.08);
        border-color: rgba(0, 212, 255, 0.2);
    }
    
    .stRadio [data-baseweb="radio"] {
        display: none;
    }
    
    /* Metrik kartları - Mobil grid */
    .metric-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        gap: 6px;
        margin: 8px 0 12px 0;
    }
    
    .metric-card {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        padding: 10px 6px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.04);
    }
    
    .metric-value {
        color: #00d4ff;
        font-size: 1.6em;
        font-weight: 700;
        line-height: 1.2;
    }
    
    .metric-label {
        color: #667788;
        font-size: 0.65em;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: 2px;
    }
    
    /* Progress bar - Mobil */
    .stProgress > div > div {
        background: linear-gradient(90deg, #00d4ff, #0088cc);
        border-radius: 10px;
        height: 6px !important;
    }
    
    .stProgress > div {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        height: 6px !important;
    }
    
    /* Sonuç kartları - Mobil */
    .result-found {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.08), rgba(0, 136, 204, 0.05));
        border: 2px solid #00d4ff;
        border-radius: 20px;
        padding: 25px 20px;
        text-align: center;
        animation: pulse 2s infinite;
        margin: 10px 0;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 20px rgba(0, 212, 255, 0.05); }
        50% { box-shadow: 0 0 40px rgba(0, 212, 255, 0.15); }
        100% { box-shadow: 0 0 20px rgba(0, 212, 255, 0.05); }
    }
    
    .result-not-found {
        background: linear-gradient(135deg, rgba(255, 68, 68, 0.08), rgba(204, 0, 0, 0.05));
        border: 2px solid #ff4444;
        border-radius: 20px;
        padding: 25px 20px;
        text-align: center;
        margin: 10px 0;
    }
    
    .result-found h1 {
        color: #00d4ff;
        font-size: 1.8em;
        margin: 0;
    }
    
    .result-found h2 {
        color: white;
        font-size: 2em;
        margin: 5px 0;
    }
    
    .result-found .location-detail {
        color: #8899aa;
        font-size: 0.9em;
    }
    
    /* Footer - Mobil */
    .footer {
        color: #334455;
        text-align: center;
        padding: 15px 0 5px 0;
        font-size: 0.7em;
        border-top: 1px solid rgba(255, 255, 255, 0.03);
        margin-top: 20px;
        line-height: 1.6;
    }
    
    /* Özel durum mesajları */
    .warning-box {
        background: rgba(255, 193, 7, 0.08);
        border: 1px solid rgba(255, 193, 7, 0.2);
        border-radius: 12px;
        padding: 12px 16px;
        margin: 8px 0;
        color: #ffd54f;
        font-size: 0.9em;
        text-align: center;
    }
    
    .info-box {
        background: rgba(0, 212, 255, 0.05);
        border: 1px solid rgba(0, 212, 255, 0.1);
        border-radius: 12px;
        padding: 12px 16px;
        margin: 8px 0;
        color: #80d4ff;
        font-size: 0.9em;
        text-align: center;
    }
    
    /* Selectbox - Mobil */
    .stSelectbox > div {
        background: rgba(255, 255, 255, 0.04);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.06);
    }
    
    .stSelectbox label {
        color: #8899aa;
        font-size: 0.85em;
    }
    
    /* Input - Mobil */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 12px;
        color: #e0e8f0;
        padding: 12px 16px;
        font-size: 1em;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #00d4ff;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.05);
    }
    
    /* Checkbox - Mobil */
    .stCheckbox label {
        color: #b0bcc8;
        font-size: 0.9em;
    }
    
    /* Expander - Mobil */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        color: #8899aa;
        font-size: 0.9em;
    }
    
    .streamlit-expanderContent {
        background: rgba(255, 255, 255, 0.02);
        border-radius: 0 0 12px 12px;
    }
    
    /* Sidebar'ı gizle */
    .css-1d391kg {
        display: none;
    }
    
    /* Tüm içerik merkezde */
    .block-container {
        padding: 1rem 0.8rem !important;
        max-width: 480px !important;
        margin: 0 auto !important;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 3px;
    }
    ::-webkit-scrollbar-track {
        background: transparent;
    }
    ::-webkit-scrollbar-thumb {
        background: #00d4ff33;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# VERİTABANI - 35+ ÜNLÜ YER
# ============================================
LANDMARKS = [
    # Türkiye - 10 yer
    {
        "id": 1, "name": "Ayasofya", "continent": "Asia", "country": "Turkey", "city": "İstanbul",
        "category": "religious", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": True, "is_museum": True, "is_mosque": True, "is_church": True,
        "is_mountain": False, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": True, "height_meters": 55
    },
    {
        "id": 2, "name": "Pamukkale", "continent": "Asia", "country": "Turkey", "city": "Denizli",
        "category": "natural", "is_natural": True, "is_man_made": False, "is_unesco": True,
        "is_ancient": True, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": True, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": False, "height_meters": 0
    },
    {
        "id": 3, "name": "Kapadokya", "continent": "Asia", "country": "Turkey", "city": "Nevşehir",
        "category": "natural", "is_natural": True, "is_man_made": False, "is_unesco": True,
        "is_ancient": True, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": True, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": False, "height_meters": 0
    },
    {
        "id": 4, "name": "Göbeklitepe", "continent": "Asia", "country": "Turkey", "city": "Şanlıurfa",
        "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": True, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": False, "height_meters": 0
    },
    {
        "id": 5, "name": "Efes Antik Kenti", "continent": "Asia", "country": "Turkey", "city": "İzmir",
        "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": True, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": False, "height_meters": 0
    },
    {
        "id": 6, "name": "Ağrı Dağı", "continent": "Asia", "country": "Turkey", "city": "Ağrı",
        "category": "natural", "is_natural": True, "is_man_made": False, "is_unesco": False,
        "is_ancient": False, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": True, "is_water": False, "is_desert": False, "is_volcano": True,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": False,
        "is_underground": False, "night_light": False, "height_meters": 5137
    },
    {
        "id": 7, "name": "Yerebatan Sarnıcı", "continent": "Asia", "country": "Turkey", "city": "İstanbul",
        "category": "historical", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": True, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": True, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": True, "night_light": False, "height_meters": 0
    },
    {
        "id": 8, "name": "Sümela Manastırı", "continent": "Asia", "country": "Turkey", "city": "Trabzon",
        "category": "religious", "is_natural": False, "is_man_made": True, "is_unesco": False,
        "is_ancient": True, "is_museum": False, "is_mosque": False, "is_church": True,
        "is_mountain": True, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": False, "height_meters": 0
    },
    {
        "id": 9, "name": "Nemrut Dağı", "continent": "Asia", "country": "Turkey", "city": "Adıyaman",
        "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": True, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": True, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": False, "height_meters": 2150
    },
    {
        "id": 10, "name": "Safranbolu", "continent": "Asia", "country": "Turkey", "city": "Karabük",
        "category": "historical", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": False, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": False,
        "is_underground": False, "night_light": False, "height_meters": 0
    },
    # Dünya - 25 yer
    {
        "id": 11, "name": "Burj Khalifa", "continent": "Asia", "country": "United Arab Emirates", "city": "Dubai",
        "category": "modern", "is_natural": False, "is_man_made": True, "is_unesco": False,
        "is_ancient": False, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": False, "is_desert": True, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": True, "height_meters": 828
    },
    {
        "id": 12, "name": "Eyfel Kulesi", "continent": "Europe", "country": "France", "city": "Paris",
        "category": "modern", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": False, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": True, "height_meters": 330
    },
    {
        "id": 13, "name": "Piramitler", "continent": "Africa", "country": "Egypt", "city": "Giza",
        "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": True, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": False, "is_desert": True, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": False, "height_meters": 138
    },
    {
        "id": 14, "name": "Sfenks", "continent": "Africa", "country": "Egypt", "city": "Giza",
        "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": True, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": False, "is_desert": True, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": False, "height_meters": 20
    },
    {
        "id": 15, "name": "Taj Mahal", "continent": "Asia", "country": "India", "city": "Agra",
        "category": "religious", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": False, "is_museum": False, "is_mosque": True, "is_church": False,
        "is_mountain": False, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": True, "height_meters": 73
    },
    {
        "id": 16, "name": "Çin Seddi", "continent": "Asia", "country": "China", "city": "Beijing",
        "category": "historical", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": True, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": True, "is_water": False, "is_desert": True, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": False, "height_meters": 14
    },
    {
        "id": 17, "name": "Machu Picchu", "continent": "South America", "country": "Peru", "city": "Cusco",
        "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": True, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": True, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": False, "height_meters": 2430
    },
    {
        "id": 18, "name": "Petra", "continent": "Asia", "country": "Jordan", "city": "Wadi Musa",
        "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": True, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": False, "is_desert": True, "is_volcano": False,
        "is_cave": True, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": False, "height_meters": 0
    },
    {
        "id": 19, "name": "Stonehenge", "continent": "Europe", "country": "United Kingdom", "city": "Salisbury",
        "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": True, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": False, "height_meters": 0
    },
    {
        "id": 20, "name": "Kolezyum", "continent": "Europe", "country": "Italy", "city": "Rome",
        "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": True, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": True, "height_meters": 48
    },
    {
        "id": 21, "name": "Everest Dağı", "continent": "Asia", "country": "Nepal", "city": "Solukhumbu",
        "category": "natural", "is_natural": True, "is_man_made": False, "is_unesco": True,
        "is_ancient": False, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": True, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": False, "height_meters": 8848
    },
    {
        "id": 22, "name": "Niagara Şelalesi", "continent": "North America", "country": "USA", "city": "New York",
        "category": "natural", "is_natural": True, "is_man_made": False, "is_unesco": False,
        "is_ancient": False, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": True, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": False,
        "is_underground": False, "night_light": True, "height_meters": 51
    },
    {
        "id": 23, "name": "Büyük Kanyon", "continent": "North America", "country": "USA", "city": "Arizona",
        "category": "natural", "is_natural": True, "is_man_made": False, "is_unesco": True,
        "is_ancient": False, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": False, "is_desert": True, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": False, "height_meters": 1800
    },
    {
        "id": 24, "name": "Kuzey Işıkları", "continent": "Europe", "country": "Norway", "city": "Tromsø",
        "category": "natural", "is_natural": True, "is_man_made": False, "is_unesco": False,
        "is_ancient": False, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": False,
        "is_underground": False, "night_light": True, "height_meters": 0
    },
    {
        "id": 25, "name": "Sidney Opera Evi", "continent": "Australia", "country": "Australia", "city": "Sydney",
        "category": "modern", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": False, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": True, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": True, "height_meters": 67
    },
    {
        "id": 26, "name": "Angkor Wat", "continent": "Asia", "country": "Cambodia", "city": "Siem Reap",
        "category": "religious", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": True, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": False, "height_meters": 65
    },
    {
        "id": 27, "name": "Pisa Kulesi", "continent": "Europe", "country": "Italy", "city": "Pisa",
        "category": "modern", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": False, "is_museum": False, "is_mosque": False, "is_church": True,
        "is_mountain": False, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": False, "height_meters": 56
    },
    {
        "id": 28, "name": "Kurtarıcı İsa Heykeli", "continent": "South America", "country": "Brazil", "city": "Rio de Janeiro",
        "category": "modern", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": False, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": True, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": True, "height_meters": 38
    },
    {
        "id": 29, "name": "Moai Heykelleri", "continent": "South America", "country": "Chile", "city": "Easter Island",
        "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": True, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": True, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": False, "height_meters": 10
    },
    {
        "id": 30, "name": "Chichen Itza", "continent": "North America", "country": "Mexico", "city": "Yucatan",
        "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True,
        "is_ancient": True, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": False, "height_meters": 30
    },
    {
        "id": 31, "name": "Ölü Deniz", "continent": "Asia", "country": "Israel/Jordan", "city": "Dead Sea",
        "category": "natural", "is_natural": True, "is_man_made": False, "is_unesco": False,
        "is_ancient": False, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": True, "is_desert": True, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": False, "height_meters": -430
    },
    {
        "id": 32, "name": "Sahara Çölü", "continent": "Africa", "country": "Multiple", "city": "Sahara",
        "category": "natural", "is_natural": True, "is_man_made": False, "is_unesco": False,
        "is_ancient": False, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": False, "is_desert": True, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": False,
        "is_underground": False, "night_light": False, "height_meters": 0
    },
    {
        "id": 33, "name": "Tropik Adalar", "continent": "Oceania", "country": "Fiji", "city": "Fiji Islands",
        "category": "natural", "is_natural": True, "is_man_made": False, "is_unesco": False,
        "is_ancient": False, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": True, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": True, "has_tourists": True, "has_entry_fee": False,
        "is_underground": False, "night_light": False, "height_meters": 0
    },
    {
        "id": 34, "name": "Alpler", "continent": "Europe", "country": "Multiple", "city": "Alps",
        "category": "natural", "is_natural": True, "is_man_made": False, "is_unesco": True,
        "is_ancient": False, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": True, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": False,
        "is_underground": False, "night_light": False, "height_meters": 4808
    },
    {
        "id": 35, "name": "Tokyo Kulesi", "continent": "Asia", "country": "Japan", "city": "Tokyo",
        "category": "modern", "is_natural": False, "is_man_made": True, "is_unesco": False,
        "is_ancient": False, "is_museum": False, "is_mosque": False, "is_church": False,
        "is_mountain": False, "is_water": False, "is_desert": False, "is_volcano": False,
        "is_cave": False, "is_island": False, "has_tourists": True, "has_entry_fee": True,
        "is_underground": False, "night_light": True, "height_meters": 333
    }
]

# ============================================
# ORBİ KONUŞMALARI
# ============================================
ORBI_COMMENTS = {
    "start": [
        "Bir yer düşün, ben bulayım! 🌍",
        "Dünyanın neresini saklıyorsun? 🧭",
        "Keşfe başlayalım! Aklındaki yeri söyleme! 🔍"
    ],
    "high": [
        "Henüz çok fazla ihtimal var... 🤔",
        "Biraz sabır, başlangıçtayız! 🧠",
        "Adaylar arasında kayboldum! 😅"
    ],
    "medium": [
        "İşler netleşmeye başladı! 🎯",
        "Aday sayısı azalıyor! 📉",
        "Doğru yoldayım! 🔦"
    ],
    "low": [
        "Çok yaklaştım! Son birkaç aday! 🎪",
        "Artık biliyorum sanırım! 🕵️",
        "Neredeyse seni yakaladım! 🏹"
    ],
    "found": [
        "Orbi şaşmaz! Buldum işte! 🏆",
        "BULDUM! Seni yakaladım! 🎉",
        "İşte karşında! Tahmin ettim! ⭐"
    ],
    "not_found": [
        "Bilemedim... Veritabanımda yok. 😢",
        "Seni yendin! Orbi kaybetti. 💔",
        "Keşke bilseydim... Öğretir misin? 📚"
    ]
}

# ============================================
# ENGINE FONKSİYONLARI
# ============================================

def get_all_questions() -> List[Dict]:
    """Tüm soruları oluştur"""
    questions = []
    
    # Statik sorular
    questions.extend([
        {"id": "continent", "text": "Hangi kıtada?", "type": "categorical", 
         "options": ["Asia", "Europe", "Africa", "North America", "South America", "Australia", "Antarctica"]},
        {"id": "category", "text": "Kategorisi ne?", "type": "categorical",
         "options": ["natural", "archaeological", "religious", "modern", "historical"]}
    ])
    
    # Boolean özellikler
    boolean_props = {
        "is_natural": "Doğal oluşum mu?",
        "is_man_made": "İnsan yapımı mı?",
        "is_unesco": "UNESCO listesinde mi?",
        "is_ancient": "Antik dönemden mi?",
        "is_museum": "Müze mi?",
        "is_mosque": "Cami mi?",
        "is_church": "Kilise mi?",
        "is_mountain": "Dağ mı?",
        "is_island": "Ada mı?",
        "is_water": "Su ile ilgili mi?",
        "is_desert": "Çölde mi?",
        "is_volcano": "Volkan mı?",
        "is_cave": "Mağara mı?",
        "has_tourists": "Turistik bir yer mi?",
        "has_entry_fee": "Giriş ücretli mi?",
        "is_underground": "Yer altında mı?",
        "night_light": "Gece ışıklandırılıyor mu?"
    }
    
    for prop, text in boolean_props.items():
        questions.append({"id": prop, "text": text, "type": "boolean"})
    
    return questions

def calculate_information_gain(landmarks: List[Dict], question: Dict) -> float:
    """Bir sorunun bilgi kazancını hesapla"""
    if not landmarks:
        return 0
    
    total = len(landmarks)
    
    if question["type"] == "boolean":
        prop = question["id"]
        true_count = sum(1 for l in landmarks if l.get(prop, False))
        false_count = total - true_count
        
        if true_count == 0 or false_count == 0:
            return 0
        
        p_true = true_count / total
        p_false = false_count / total
        entropy = -(p_true * math.log2(p_true) + p_false * math.log2(p_false))
        gain = entropy * (1 - p_true**2 - p_false**2)
        return gain
    
    elif question["type"] == "categorical":
        prop = question["id"]
        values = {}
        for l in landmarks:
            val = l.get(prop, "unknown")
            values[val] = values.get(val, 0) + 1
        
        if len(values) <= 1:
            return 0
        
        entropy = 0
        for count in values.values():
            p = count / total
            entropy -= p * math.log2(p)
        
        gain = entropy * (1 - sum((count/total)**2 for count in values.values()))
        return gain
    
    return 0

def get_best_question(landmarks: List[Dict], asked_questions: List[str]) -> Optional[Dict]:
    """En iyi soruyu seç - Gelişmiş Akinator mantığı"""
    all_questions = get_all_questions()
    
    best_question = None
    best_score = -1
    
    for q in all_questions:
        if q["id"] in asked_questions:
            continue
        
        # 1. Information Gain
        ig = calculate_information_gain(landmarks, q)
        
        # 2. Popülerlik (soru ne kadar iyi böler?)
        total = len(landmarks)
        if q["type"] == "boolean":
            true_count = sum(1 for l in landmarks if l.get(q["id"], False))
            pop_score = 1 - abs((true_count / total) - 0.5) * 2
        else:
            values = {}
            for l in landmarks:
                val = l.get(q["id"], "unknown")
                values[val] = values.get(val, 0) + 1
            pop_score = 1 - sum((count/total)**2 for count in values.values())
        
        # 3. Zorluk (ne kadar eleyici?)
        diff_score = ig * 0.5
        
        # 4. Rastgelelik
        rand_score = random.random() * 0.1
        
        # TOPLAM SKOR
        total_score = ig * 0.4 + pop_score * 0.3 + diff_score * 0.2 + rand_score * 0.1
        
        if total_score > best_score:
            best_score = total_score
            best_question = q
    
    return best_question

def filter_landmarks(landmarks: List[Dict], question: Dict, answer: str) -> List[Dict]:
    """Soruyu cevaba göre filtrele"""
    if question["type"] == "boolean":
        prop = question["id"]
        if answer == "Evet":
            return [l for l in landmarks if l.get(prop, False)]
        elif answer == "Hayır":
            return [l for l in landmarks if not l.get(prop, False)]
        else:
            return landmarks
    
    elif question["type"] == "categorical":
        prop = question["id"]
        if answer in ["Bilmiyorum", "Belki"]:
            return landmarks
        return [l for l in landmarks if l.get(prop, "") == answer]
    
    return landmarks

def get_orbi_comment(candidates_count: int, is_found: bool = False) -> str:
    """Orbi'nin konuşmasını seç"""
    if is_found:
        return random.choice(ORBI_COMMENTS["found"])
    
    if candidates_count > 50:
        return random.choice(ORBI_COMMENTS["high"])
    elif candidates_count > 10:
        return random.choice(ORBI_COMMENTS["medium"])
    elif candidates_count > 1:
        return random.choice(ORBI_COMMENTS["low"])
    else:
        return "Sanırım seni yakaladım! 🎯"

def calculate_score(question_count: int, candidates_before: int, candidates_after: int) -> int:
    """Puan hesapla"""
    base_score = max(1000 - question_count * 15, 100)
    if candidates_after == 0:
        efficiency = 1
    else:
        efficiency = min(candidates_before / max(candidates_after, 1), 10)
    bonus = int(efficiency * 40)
    return base_score + bonus

# ============================================
# STREAMLIT ANA UYGULAMA
# ============================================

def init_session_state():
    """Session state'i başlat"""
    if "game_started" not in st.session_state:
        st.session_state.game_started = False
    if "landmarks" not in st.session_state:
        st.session_state.landmarks = LANDMARKS.copy()
    if "candidates" not in st.session_state:
        st.session_state.candidates = LANDMARKS.copy()
    if "asked_questions" not in st.session_state:
        st.session_state.asked_questions = []
    if "question_count" not in st.session_state:
        st.session_state.question_count = 0
    if "game_over" not in st.session_state:
        st.session_state.game_over = False
    if "found_landmark" not in st.session_state:
        st.session_state.found_landmark = None
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "total_games" not in st.session_state:
        st.session_state.total_games = 0
    if "total_wins" not in st.session_state:
        st.session_state.total_wins = 0
    if "current_question" not in st.session_state:
        st.session_state.current_question = None
    if "last_comment" not in st.session_state:
        st.session_state.last_comment = ""
    if "learning_mode" not in st.session_state:
        st.session_state.learning_mode = False

def reset_game():
    """Oyunu sıfırla"""
    st.session_state.game_started = True
    st.session_state.candidates = st.session_state.landmarks.copy()
    st.session_state.asked_questions = []
    st.session_state.question_count = 0
    st.session_state.game_over = False
    st.session_state.found_landmark = None
    st.session_state.learning_mode = False
    st.session_state.current_question = None
    st.session_state.last_comment = random.choice(ORBI_COMMENTS["start"])

def main():
    init_session_state()
    
    # ========== HEADER ==========
    st.markdown('<h1 class="orbi-title">🌍 ORBI DISCOVERY</h1>', unsafe_allow_html=True)
    st.markdown('<p class="orbi-subtitle">"Bir yer düşün, ben bulayım!"</p>', unsafe_allow_html=True)
    
    # ========== ORBİ KONUŞMASI ==========
    if st.session_state.last_comment:
        st.markdown(f"""
        <div class="orbi-speech">
            <span class="orbi-name">Orbi</span>
            <span class="orbi-text">{st.session_state.last_comment}</span>
        </div>
        """, unsafe_allow_html=True)
    
    # ========== OYUN BAŞLANGICI ==========
    if not st.session_state.game_started:
        st.markdown("""
        <div class="orbi-card" style="text-align: center;">
            <h2 style="color: #00d4ff; font-size: 1.4em;">🗺️ Dünyayı Keşfet!</h2>
            <p style="color: #8899aa; font-size: 0.95em; margin: 8px 0;">
                Aklından bir yer tut. Orbi sorularla bulmaya çalışsın!
            </p>
            <div style="display: flex; flex-wrap: wrap; gap: 6px; justify-content: center; margin: 10px 0; font-size: 0.8em; color: #667788;">
                <span>🌍 35+ yer</span>
                <span>🎯 Akinator mantığı</span>
                <span>🧠 AI motoru</span>
                <span>🏆 Puan sistemi</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Hadi Başlayalım!", use_container_width=True):
            reset_game()
            st.rerun()
        
        with st.expander("📌 Örnek Yerler"):
            sample = ["Ayasofya", "Pamukkale", "Kapadokya", "Göbeklitepe", 
                     "Burj Khalifa", "Eyfel Kulesi", "Büyük Kanyon", "Taj Mahal"]
            cols = st.columns(4)
            for i, place in enumerate(sample):
                cols[i % 4].markdown(f"- {place}")
    
    # ========== OYUN DÖNGÜSÜ ==========
    elif not st.session_state.game_over:
        
        # Metrikler
        st.markdown(f"""
        <div class="metric-grid">
            <div class="metric-card">
                <div class="metric-value">{len(st.session_state.candidates)}</div>
                <div class="metric-label">🏛️ Aday</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{st.session_state.question_count}</div>
                <div class="metric-label">❓ Soru</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{st.session_state.score}</div>
                <div class="metric-label">⭐ Puan</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">%{min(int(len(st.session_state.asked_questions) / 15 * 100), 100)}</div>
                <div class="metric-label">📊 İlerleme</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.progress(min(len(st.session_state.asked_questions) / 15, 1.0))
        
        # ========== SORU SOR ==========
        if st.session_state.current_question is None:
            best_q = get_best_question(st.session_state.candidates, st.session_state.asked_questions)
            
            if best_q:
                st.session_state.current_question = best_q
            else:
                st.session_state.game_over = True
                if st.session_state.candidates:
                    st.session_state.found_landmark = st.session_state.candidates[0]
                    st.session_state.total_games += 1
                    st.session_state.total_wins += 1
                    st.session_state.last_comment = get_orbi_comment(1, True)
                else:
                    st.session_state.last_comment = random.choice(ORBI_COMMENTS["not_found"])
                    st.session_state.total_games += 1
                st.rerun()
        
        # ========== SORUYU GÖSTER ==========
        if st.session_state.current_question:
            q = st.session_state.current_question
            
            st.markdown(f"""
            <div class="orbi-card">
                <h3 style="color: #00d4ff; font-size: 1.1em; margin: 0 0 8px 0;">❓ Soru {st.session_state.question_count + 1}</h3>
                <p style="color: #e0e8f0; font-size: 1.15em; margin: 0;">{q['text']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if q["type"] == "boolean":
                answer = st.radio(
                    "Cevabını seç:",
                    ["Evet", "Hayır", "Bilmiyorum"],
                    key=f"answer_{q['id']}",
                    horizontal=True,
                    label_visibility="collapsed"
                )
            else:
                options = ["Bilmiyorum"] + q["options"]
                answer = st.selectbox(
                    "Cevabını seç:",
                    options,
                    key=f"answer_{q['id']}"
                )
            
            if st.button("✅ Cevabı Gönder", key="submit_answer", use_container_width=True):
                before_count = len(st.session_state.candidates)
                
                if q["type"] == "boolean":
                    if answer != "Bilmiyorum":
                        st.session_state.candidates = filter_landmarks(
                            st.session_state.candidates, q, answer
                        )
                else:
                    if answer != "Bilmiyorum":
                        st.session_state.candidates = filter_landmarks(
                            st.session_state.candidates, q, answer
                        )
                
                after_count = len(st.session_state.candidates)
                
                if after_count < before_count:
                    st.session_state.score += calculate_score(
                        st.session_state.question_count, before_count, after_count
                    )
                
                st.session_state.asked_questions.append(q["id"])
                st.session_state.question_count += 1
                
                if after_count == 1:
                    st.session_state.found_landmark = st.session_state.candidates[0]
                    st.session_state.game_over = True
                    st.session_state.total_games += 1
                    st.session_state.total_wins += 1
                    st.session_state.last_comment = get_orbi_comment(1, True)
                elif after_count == 0:
                    st.session_state.game_over = True
                    st.session_state.total_games += 1
                    st.session_state.last_comment = random.choice(ORBI_COMMENTS["not_found"])
                else:
                    st.session_state.last_comment = get_orbi_comment(after_count)
                
                st.session_state.current_question = None
                st.rerun()
        
        # Uyarı
        if len(st.session_state.candidates) <= 3 and not st.session_state.game_over:
            st.markdown(f"""
            <div class="warning-box">
                ⚠️ Sadece {len(st.session_state.candidates)} aday kaldı! Orbi çok yaklaştı!
            </div>
            """, unsafe_allow_html=True)
    
    # ========== OYUN SONU ==========
    else:
        if st.session_state.found_landmark:
            l = st.session_state.found_landmark
            
            st.markdown(f"""
            <div class="result-found">
                <h1>🎉 {random.choice(['BULDUM!', 'SENİ YAKALADIM!', 'ORBI ŞAŞMAZ!'])}</h1>
                <h2>📍 {l['name']}</h2>
                <div class="location-detail">
                    🇺🇸 {l['country']} • {l['city']} • {l['continent']}
                </div>
                <div class="location-detail" style="font-size:0.8em; margin-top:4px;">
                    📂 Kategori: {l['category']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(f"""
                <div class="metric-card">
                    <div style="font-size:1.6em; color:#00d4ff;">{len(st.session_state.asked_questions)}</div>
                    <div class="metric-label">Soru</div>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown(f"""
                <div class="metric-card">
                    <div style="font-size:1.6em; color:#ffd700;">{st.session_state.score}</div>
                    <div class="metric-label">Puan</div>
                </div>
                """, unsafe_allow_html=True)
            with col3:
                st.markdown(f"""
                <div class="metric-card">
                    <div style="font-size:1.6em; color:#00ff88;">✅</div>
                    <div class="metric-label">Kazanıldı!</div>
                </div>
                """, unsafe_allow_html=True)
            
        else:
            st.markdown("""
            <div class="result-not-found">
                <h1 style="color:#ff4444; font-size:1.8em;">😢 Bilemedim...</h1>
                <p style="color:#8899aa;">Bu yer benim veritabanımda yok.</p>
            </div>
            """, unsafe_allow_html=True)
        
        # ========== ÖĞRENME MODU ==========
        if not st.session_state.found_landmark and not st.session_state.learning_mode:
            if st.button("📚 Bu Yeri Öğret!", use_container_width=True):
                st.session_state.learning_mode = True
                st.rerun()
        
        if st.session_state.learning_mode:
            st.markdown("""
            <div class="orbi-card">
                <h3 style="color:#00d4ff; font-size:1.1em;">📚 Yeni Yer Öğret</h3>
                <p style="color:#8899aa; font-size:0.9em;">Bu yeri veritabanına ekleyelim!</p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.form("learning_form"):
                col1, col2 = st.columns(2)
                with col1:
                    name = st.text_input("📍 Yer Adı", placeholder="Örn: Topkapı Sarayı")
                    country = st.text_input("🇺🇸 Ülke", placeholder="Örn: Türkiye")
                    city = st.text_input("🏙️ Şehir", placeholder="Örn: İstanbul")
                    continent = st.selectbox(
                        "🌍 Kıta",
                        ["Asia", "Europe", "Africa", "North America", "South America", "Australia", "Antarctica"]
                    )
                with col2:
                    category = st.selectbox(
                        "📂 Kategori",
                        ["natural", "archaeological", "religious", "modern", "historical"]
                    )
                    is_unesco = st.checkbox("UNESCO listesinde")
                    is_natural = st.checkbox("Doğal oluşum")
                    is_man_made = st.checkbox("İnsan yapımı")
                    has_tourists = st.checkbox("Turistik")
                
                submitted = st.form_submit_button("💾 Kaydet", use_container_width=True)
                if submitted and name and country:
                    new_landmark = {
                        "id": len(st.session_state.landmarks) + 1,
                        "name": name,
                        "continent": continent,
                        "country": country,
                        "city": city or "Bilinmiyor",
                        "category": category,
                        "is_natural": is_natural,
                        "is_man_made": is_man_made,
                        "is_unesco": is_unesco,
                        "has_tourists": has_tourists,
                        "is_ancient": False, "is_museum": False, "is_mosque": False,
                        "is_church": False, "is_mountain": False, "is_water": False,
                        "is_desert": False, "is_volcano": False, "is_cave": False,
                        "is_island": False, "has_entry_fee": False, "is_underground": False,
                        "night_light": False, "height_meters": 0
                    }
                    st.session_state.landmarks.append(new_landmark)
                    st.success(f"✅ {name} veritabanına eklendi!")
                    st.session_state.learning_mode = False
                    time.sleep(0.8)
                    reset_game()
                    st.rerun()
        
        # ========== TEKRAR OYNA ==========
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Yeni Oyun", use_container_width=True):
                reset_game()
                st.rerun()
        with col2:
            if st.button("📊 Sıralama", use_container_width=True):
                st.info("🏆 Dünya sıralaması yakında geliyor!")
    
    # ========== FOOTER ==========
    total_games = st.session_state.total_games
    win_rate = int((st.session_state.total_wins / max(total_games, 1)) * 100)
    
    st.markdown(f"""
    <div class="footer">
        <p>🌍 ORBI DISCOVERY ENGINE v2.0</p>
        <p>🧠 {len(st.session_state.landmarks)} yer • {total_games} oyun • %{win_rate} kazanma</p>
        <p>🔍 Akinator mantığı • Information Gain • Keşfet ve Öğren</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
