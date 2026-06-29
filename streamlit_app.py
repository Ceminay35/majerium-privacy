"""
ORBI DISCOVERY ENGINE v3.0
TIKLANABİLİR BUTONLAR + MOBİL UYUMLU
"""

import streamlit as st
import random
import time
import math
from typing import List, Dict, Optional

# ============================================
# MOBİL UYUMLU SAYFA YAPILANDIRMASI
# ============================================
st.set_page_config(
    page_title="Orbi Discovery",
    page_icon="🌍",
    layout="centered",  # Mobil dostu
    initial_sidebar_state="collapsed"
)

# ============================================
# CSS - MOBİL + TABLET + PC UYUMLU
# ============================================
st.markdown("""
<style>
    /* ANA TEMA */
    .stApp {
        background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #16213e 100%);
    }
    
    /* BAŞLIK */
    .orbi-title {
        color: #00d4ff;
        font-size: 2.5em;
        font-weight: 800;
        text-align: center;
        text-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
        margin-bottom: 5px;
    }
    
    .orbi-subtitle {
        color: #8899aa;
        text-align: center;
        font-size: 1em;
        margin-bottom: 20px;
    }
    
    /* KART */
    .orbi-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        margin-bottom: 15px;
    }
    
    /* ORBI KONUŞMASI */
    .orbi-speech {
        background: linear-gradient(135deg, #1a3a5c, #0d1f3c);
        border-radius: 20px;
        padding: 15px 20px;
        border-left: 5px solid #00d4ff;
        color: #e0e8f0;
        font-size: 1em;
        margin: 15px 0;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.1);
    }
    
    .orbi-speech .orbi-name {
        color: #00d4ff;
        font-weight: bold;
        font-size: 1.1em;
    }
    
    /* METRİK KARTLARI */
    .metric-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 12px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    .metric-value {
        color: #00d4ff;
        font-size: 1.8em;
        font-weight: bold;
    }
    
    .metric-label {
        color: #8899aa;
        font-size: 0.8em;
    }
    
    /* SONUÇ */
    .result-found {
        background: linear-gradient(135deg, #00d4ff22, #0088cc22);
        border: 2px solid #00d4ff;
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 20px rgba(0, 212, 255, 0.2); }
        50% { box-shadow: 0 0 40px rgba(0, 212, 255, 0.5); }
        100% { box-shadow: 0 0 20px rgba(0, 212, 255, 0.2); }
    }
    
    .result-not-found {
        background: linear-gradient(135deg, #ff444422, #cc000022);
        border: 2px solid #ff4444;
        border-radius: 20px;
        padding: 25px;
        text-align: center;
    }
    
    .footer {
        color: #445566;
        text-align: center;
        padding: 15px;
        font-size: 0.7em;
        border-top: 1px solid rgba(255, 255, 255, 0.05);
        margin-top: 30px;
    }
    
    /* ============================================
       BUTONLAR - TIKLANABİLİR + MOBİL UYUMLU
       ============================================ */
    .stButton > button {
        background: linear-gradient(135deg, #00d4ff, #0088cc);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 15px 10px;
        font-weight: 700;
        font-size: 1.1em;
        transition: all 0.3s ease;
        width: 100%;
        min-height: 55px;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.2);
        cursor: pointer !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 212, 255, 0.4);
        background: linear-gradient(135deg, #00e5ff, #0099dd);
    }
    
    .stButton > button:active {
        transform: scale(0.95);
    }
    
    /* Telefon için butonlar */
    @media (max-width: 480px) {
        .stButton > button {
            min-height: 50px;
            padding: 12px 5px;
            font-size: 0.95em;
            border-radius: 12px;
        }
        
        .orbi-title {
            font-size: 1.8em !important;
        }
        
        .metric-value {
            font-size: 1.4em !important;
        }
        
        .orbi-card {
            padding: 15px;
        }
        
        .orbi-speech {
            padding: 12px 15px;
            font-size: 0.9em;
        }
    }
    
    /* Tablet için */
    @media (min-width: 481px) and (max-width: 768px) {
        .stButton > button {
            min-height: 60px;
            padding: 15px 10px;
            font-size: 1.05em;
        }
        
        .orbi-title {
            font-size: 2.2em !important;
        }
    }
    
    /* Bilgisayar için */
    @media (min-width: 769px) {
        .stButton > button {
            min-height: 60px;
            padding: 18px 15px;
            font-size: 1.15em;
        }
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# VERİTABANI (30+ yer)
# ============================================
LANDMARKS = [
    {"id": 1, "name": "Ayasofya", "continent": "Asia", "country": "Turkey", "city": "İstanbul", "category": "religious", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": True, "is_temple": False, "is_museum": True, "is_mosque": True, "is_church": True, "is_mountain": False, "is_island": False, "is_water": False, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": True, "height_meters": 55},
    {"id": 2, "name": "Pamukkale", "continent": "Asia", "country": "Turkey", "city": "Denizli", "category": "natural", "is_natural": True, "is_man_made": False, "is_unesco": True, "is_ancient": True, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": False, "is_water": True, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": False, "height_meters": 0},
    {"id": 3, "name": "Kapadokya", "continent": "Asia", "country": "Turkey", "city": "Nevşehir", "category": "natural", "is_natural": True, "is_man_made": False, "is_unesco": True, "is_ancient": True, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": False, "is_water": False, "is_desert": False, "is_volcano": False, "is_cave": True, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": False, "height_meters": 0},
    {"id": 4, "name": "Göbeklitepe", "continent": "Asia", "country": "Turkey", "city": "Şanlıurfa", "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": True, "is_temple": True, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": False, "is_water": False, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": False, "height_meters": 0},
    {"id": 5, "name": "Efes Antik Kenti", "continent": "Asia", "country": "Turkey", "city": "İzmir", "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": True, "is_temple": True, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": False, "is_water": False, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": False, "height_meters": 0},
    {"id": 6, "name": "Ağrı Dağı", "continent": "Asia", "country": "Turkey", "city": "Ağrı", "category": "natural", "is_natural": True, "is_man_made": False, "is_unesco": False, "is_ancient": False, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": True, "is_island": False, "is_water": False, "is_desert": False, "is_volcano": True, "is_cave": False, "has_tourists": True, "has_entry_fee": False, "is_underground": False, "night_light": False, "height_meters": 5137},
    {"id": 7, "name": "Yerebatan Sarnıcı", "continent": "Asia", "country": "Turkey", "city": "İstanbul", "category": "historical", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": True, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": False, "is_water": True, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": True, "night_light": False, "height_meters": 0},
    {"id": 8, "name": "Sümela Manastırı", "continent": "Asia", "country": "Turkey", "city": "Trabzon", "category": "religious", "is_natural": False, "is_man_made": True, "is_unesco": False, "is_ancient": True, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": True, "is_mountain": True, "is_island": False, "is_water": False, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": False, "height_meters": 0},
    {"id": 9, "name": "Nemrut Dağı", "continent": "Asia", "country": "Turkey", "city": "Adıyaman", "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": True, "is_temple": True, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": True, "is_island": False, "is_water": False, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": False, "height_meters": 2150},
    {"id": 10, "name": "Safranbolu", "continent": "Asia", "country": "Turkey", "city": "Karabük", "category": "historical", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": False, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": False, "is_water": False, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": False, "is_underground": False, "night_light": False, "height_meters": 0},
    {"id": 11, "name": "Burj Khalifa", "continent": "Asia", "country": "United Arab Emirates", "city": "Dubai", "category": "modern", "is_natural": False, "is_man_made": True, "is_unesco": False, "is_ancient": False, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": False, "is_water": False, "is_desert": True, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": True, "height_meters": 828},
    {"id": 12, "name": "Eyfel Kulesi", "continent": "Europe", "country": "France", "city": "Paris", "category": "modern", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": False, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": False, "is_water": False, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": True, "height_meters": 330},
    {"id": 13, "name": "Piramitler", "continent": "Africa", "country": "Egypt", "city": "Giza", "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": True, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": False, "is_water": False, "is_desert": True, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": False, "height_meters": 138},
    {"id": 14, "name": "Sfenks", "continent": "Africa", "country": "Egypt", "city": "Giza", "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": True, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": False, "is_water": False, "is_desert": True, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": False, "height_meters": 20},
    {"id": 15, "name": "Taj Mahal", "continent": "Asia", "country": "India", "city": "Agra", "category": "religious", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": False, "is_temple": False, "is_museum": False, "is_mosque": True, "is_church": False, "is_mountain": False, "is_island": False, "is_water": False, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": True, "height_meters": 73},
    {"id": 16, "name": "Çin Seddi", "continent": "Asia", "country": "China", "city": "Beijing", "category": "historical", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": True, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": True, "is_island": False, "is_water": False, "is_desert": True, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": False, "height_meters": 14},
    {"id": 17, "name": "Machu Picchu", "continent": "South America", "country": "Peru", "city": "Cusco", "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": True, "is_temple": True, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": True, "is_island": False, "is_water": False, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": False, "height_meters": 2430},
    {"id": 18, "name": "Petra", "continent": "Asia", "country": "Jordan", "city": "Wadi Musa", "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": True, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": False, "is_water": False, "is_desert": True, "is_volcano": False, "is_cave": True, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": False, "height_meters": 0},
    {"id": 19, "name": "Stonehenge", "continent": "Europe", "country": "United Kingdom", "city": "Salisbury", "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": True, "is_temple": True, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": False, "is_water": False, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": False, "height_meters": 0},
    {"id": 20, "name": "Kolezyum", "continent": "Europe", "country": "Italy", "city": "Rome", "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": True, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": False, "is_water": False, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": True, "height_meters": 48},
    {"id": 21, "name": "Everest Dağı", "continent": "Asia", "country": "Nepal", "city": "Solukhumbu", "category": "natural", "is_natural": True, "is_man_made": False, "is_unesco": True, "is_ancient": False, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": True, "is_island": False, "is_water": False, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": False, "height_meters": 8848},
    {"id": 22, "name": "Niagara Şelalesi", "continent": "North America", "country": "USA", "city": "New York", "category": "natural", "is_natural": True, "is_man_made": False, "is_unesco": False, "is_ancient": False, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": False, "is_water": True, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": False, "is_underground": False, "night_light": True, "height_meters": 51},
    {"id": 23, "name": "Büyük Kanyon", "continent": "North America", "country": "USA", "city": "Arizona", "category": "natural", "is_natural": True, "is_man_made": False, "is_unesco": True, "is_ancient": False, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": False, "is_water": False, "is_desert": True, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": False, "height_meters": 1800},
    {"id": 24, "name": "Kuzey Işıkları", "continent": "Europe", "country": "Norway", "city": "Tromsø", "category": "natural", "is_natural": True, "is_man_made": False, "is_unesco": False, "is_ancient": False, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": False, "is_water": False, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": False, "is_underground": False, "night_light": True, "height_meters": 0},
    {"id": 25, "name": "Sidney Opera Evi", "continent": "Australia", "country": "Australia", "city": "Sydney", "category": "modern", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": False, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": False, "is_water": True, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": True, "height_meters": 67},
    {"id": 26, "name": "Angkor Wat", "continent": "Asia", "country": "Cambodia", "city": "Siem Reap", "category": "religious", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": True, "is_temple": True, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": False, "is_water": False, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": False, "height_meters": 65},
    {"id": 27, "name": "Pisa Kulesi", "continent": "Europe", "country": "Italy", "city": "Pisa", "category": "modern", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": False, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": True, "is_mountain": False, "is_island": False, "is_water": False, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": False, "height_meters": 56},
    {"id": 28, "name": "Kurtarıcı İsa Heykeli", "continent": "South America", "country": "Brazil", "city": "Rio de Janeiro", "category": "modern", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": False, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": True, "is_island": False, "is_water": False, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": True, "height_meters": 38},
    {"id": 29, "name": "Moai Heykelleri", "continent": "South America", "country": "Chile", "city": "Easter Island", "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": True, "is_temple": False, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": True, "is_water": False, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": False, "height_meters": 10},
    {"id": 30, "name": "Chichen Itza", "continent": "North America", "country": "Mexico", "city": "Yucatan", "category": "archaeological", "is_natural": False, "is_man_made": True, "is_unesco": True, "is_ancient": True, "is_temple": True, "is_museum": False, "is_mosque": False, "is_church": False, "is_mountain": False, "is_island": False, "is_water": False, "is_desert": False, "is_volcano": False, "is_cave": False, "has_tourists": True, "has_entry_fee": True, "is_underground": False, "night_light": False, "height_meters": 30}
]

# ============================================
# ORBİ KONUŞMALARI
# ============================================
ORBI_COMMENTS = {
    "start": ["Bir yer düşün, ben bulayım! 🌍", "Hazır mısın? Dünyanın neresini saklıyorsun? 🧭", "Keşfe başlayalım! Aklındaki yeri söylemeden ben bulayım. 🔍"],
    "high_candidates": ["Hmm... Henüz çok fazla ihtimal var. 🤔", "Daha başlangıçtayız, biraz sabır... 🧠", "Adaylar arasında kayboldum, biraz ipucu ver! 😅"],
    "medium_candidates": ["İşler netleşmeye başladı! 🎯", "Gidiyoruz! Aday sayısı azalıyor. 📉", "İpucu peşindeyim, doğru yoldayım! 🔦"],
    "low_candidates": ["Çok yaklaştım! Son birkaç aday kaldı. 🎪", "Bence artık biliyorum! 🕵️", "Neredeyse seni yakaladım! 🏹"],
    "found": ["BULDUM! 🎉 Seni yakaladım!", "İşte karşında! Tahmin ettim! ⭐", "Orbi şaşmaz! Buldum işte! 🏆"],
    "not_found": ["Bilemedim... Bu yer benim veritabanımda yok. 😢", "Seni yendin! Orbi bugün kaybetti. 💔", "Keşke bu yeri bilseydim... Öğretir misin? 📚"]
}

# ============================================
# ENGINE FONKSİYONLARI
# ============================================

def get_all_questions() -> List[Dict]:
    questions = []
    static_questions = [
        {"id": "continent", "text": "Hangi kıtada?", "type": "categorical", "options": ["Asia", "Europe", "Africa", "North America", "South America", "Australia", "Antarctica"]},
        {"id": "category", "text": "Kategorisi ne?", "type": "categorical", "options": ["natural", "archaeological", "religious", "modern", "historical"]},
    ]
    boolean_props = {
        "is_natural": "Doğal oluşum mu?",
        "is_man_made": "İnsan yapımı mı?",
        "is_unesco": "UNESCO listesinde mi?",
        "is_ancient": "Antik dönemden mi?",
        "is_temple": "Tapınak mı?",
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
        gain = entropy * (1 - (true_count/total)**2 - (false_count/total)**2)
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
    all_questions = get_all_questions()
    best_question = None
    best_gain = -1
    for q in all_questions:
        if q["id"] in asked_questions:
            continue
        gain = calculate_information_gain(landmarks, q)
        if gain > best_gain + 0.01:
            best_gain = gain
            best_question = q
        elif gain > best_gain - 0.01 and random.random() < 0.3:
            best_question = q
    return best_question

def filter_landmarks(landmarks: List[Dict], question: Dict, answer: str) -> List[Dict]:
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
    if is_found:
        return random.choice(ORBI_COMMENTS["found"])
    if candidates_count > 100:
        return random.choice(ORBI_COMMENTS["high_candidates"])
    elif candidates_count > 20:
        return random.choice(ORBI_COMMENTS["medium_candidates"])
    elif candidates_count > 2:
        return random.choice(ORBI_COMMENTS["low_candidates"])
    else:
        return "Sanırım seni yakaladım! 🎯"

def calculate_score(question_count: int, candidates_before: int, candidates_after: int) -> int:
    base_score = max(1000 - question_count * 20, 100)
    efficiency = min(candidates_before / max(candidates_after, 1), 10)
    bonus = int(efficiency * 50)
    return base_score + bonus

# ============================================
# SESSION STATE
# ============================================

def init_session_state():
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
    if "answer_submitted" not in st.session_state:
        st.session_state.answer_submitted = False
    if "temp_answer" not in st.session_state:
        st.session_state.temp_answer = None

def reset_game():
    st.session_state.game_started = True
    st.session_state.candidates = st.session_state.landmarks.copy()
    st.session_state.asked_questions = []
    st.session_state.question_count = 0
    st.session_state.game_over = False
    st.session_state.found_landmark = None
    st.session_state.learning_mode = False
    st.session_state.current_question = None
    st.session_state.last_comment = random.choice(ORBI_COMMENTS["start"])
    st.session_state.answer_submitted = False
    st.session_state.temp_answer = None

# ============================================
# ANA UYGULAMA
# ============================================

def main():
    init_session_state()
    
    # HEADER
    st.markdown('<h1 class="orbi-title">🌍 ORBI DISCOVERY</h1>', unsafe_allow_html=True)
    st.markdown('<p class="orbi-subtitle">"Bir yer düşün, ben bulayım!"</p>', unsafe_allow_html=True)
    
    # SIDEBAR (Mobilde gizlenebilir)
    with st.sidebar:
        st.markdown("### 📊 İstatistikler")
        if st.session_state.total_games > 0:
            c1, c2 = st.columns(2)
            with c1:
                st.metric("Toplam Oyun", st.session_state.total_games)
            with c2:
                win_rate = int((st.session_state.total_wins / st.session_state.total_games) * 100)
                st.metric("Kazanma Oranı", f"%{win_rate}")
        st.markdown("---")
        st.markdown("### 🎯 Zorluk")
        st.selectbox("Seviye", ["Bronz 🥉", "Gümüş 🥈", "Altın 🥇", "Elmas 💎"], key="difficulty")
        st.markdown("---")
        if st.button("🔄 Yeni Oyun", use_container_width=True):
            reset_game()
            st.rerun()
        st.markdown("---")
        st.markdown(f"### 📚 Veritabanı")
        st.info(f"{len(st.session_state.landmarks)} yer")
        if st.session_state.question_count > 0:
            st.success(f"{st.session_state.question_count} soru")
            st.info(f"{len(st.session_state.candidates)} aday")
    
    # ORBI KONUŞMASI
    if st.session_state.last_comment:
        st.markdown(f"""
        <div class="orbi-speech">
            <span class="orbi-name">🧠 Orbi:</span> {st.session_state.last_comment}
        </div>
        """, unsafe_allow_html=True)
    
    # ========== BAŞLANGIÇ ==========
    if not st.session_state.game_started:
        st.markdown("""
        <div class="orbi-card" style="text-align: center;">
            <h2 style="color: #00d4ff;">🗺️ Dünyayı Keşfet!</h2>
            <p style="color: #8899aa;">Aklından bir yer tut, Orbi bulsun!</p>
            <p style="color: #667788; font-size: 0.9em;">
                🌍 30+ yer • 🎯 Akinator • 🧠 Information Gain
            </p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Başla!", use_container_width=True):
            reset_game()
            st.rerun()
    
    # ========== OYUN ==========
    elif not st.session_state.game_over:
        # METRİKLER
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{len(st.session_state.candidates)}</div>
                <div class="metric-label">🏛️ Aday</div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{st.session_state.question_count}</div>
                <div class="metric-label">❓ Soru</div>
            </div>
            """, unsafe_allow_html=True)
        with c3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{st.session_state.score}</div>
                <div class="metric-label">⭐ Puan</div>
            </div>
            """, unsafe_allow_html=True)
        with c4:
            progress = min(len(st.session_state.asked_questions) / 15, 1.0)
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">%{int(progress*100)}</div>
                <div class="metric-label">📊 İlerleme</div>
            </div>
            """, unsafe_allow_html=True)
        st.progress(progress)
        
        # SORU SEÇ
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
        
        # ========== SORU GÖSTER + CEVAP BUTONLARI ==========
        if st.session_state.current_question:
            q = st.session_state.current_question
            
            st.markdown(f"""
            <div class="orbi-card">
                <h3 style="color: #00d4ff;">❓ Soru {st.session_state.question_count + 1}</h3>
                <p style="color: #e0e8f0; font-size: 1.2em;">{q['text']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # ===== CEVAP BUTONLARI =====
            if q["type"] == "boolean":
                c1, c2, c3 = st.columns(3)
                with c1:
                    if st.button("✅ Evet", key=f"yes_{q['id']}_{st.session_state.question_count}", use_container_width=True):
                        st.session_state.temp_answer = "Evet"
                        st.session_state.answer_submitted = True
                        st.rerun()
                with c2:
                    if st.button("❌ Hayır", key=f"no_{q['id']}_{st.session_state.question_count}", use_container_width=True):
                        st.session_state.temp_answer = "Hayır"
                        st.session_state.answer_submitted = True
                        st.rerun()
                with c3:
                    if st.button("🤷 Bilmiyorum", key=f"idk_{q['id']}_{st.session_state.question_count}", use_container_width=True):
                        st.session_state.temp_answer = "Bilmiyorum"
                        st.session_state.answer_submitted = True
                        st.rerun()
            else:
                options = ["Bilmiyorum"] + q["options"]
                answer = st.selectbox("Cevabını seç:", options, key=f"select_{q['id']}")
                if st.button("✅ Cevabı Gönder", key="submit_ans", use_container_width=True):
                    st.session_state.temp_answer = answer
                    st.session_state.answer_submitted = True
                    st.rerun()
            
            # ===== CEVAP İŞLE =====
            if st.session_state.answer_submitted:
                answer = st.session_state.temp_answer
                before = len(st.session_state.candidates)
                
                if q["type"] == "boolean":
                    if answer != "Bilmiyorum":
                        st.session_state.candidates = filter_landmarks(st.session_state.candidates, q, answer)
                else:
                    if answer != "Bilmiyorum":
                        st.session_state.candidates = filter_landmarks(st.session_state.candidates, q, answer)
                
                after = len(st.session_state.candidates)
                if after < before:
                    st.session_state.score += calculate_score(st.session_state.question_count, before, after)
                
                st.session_state.asked_questions.append(q["id"])
                st.session_state.question_count += 1
                
                if after == 1:
                    st.session_state.found_landmark = st.session_state.candidates[0]
                    st.session_state.game_over = True
                    st.session_state.total_games += 1
                    st.session_state.total_wins += 1
                    st.session_state.last_comment = get_orbi_comment(1, True)
                elif after == 0:
                    st.session_state.game_over = True
                    st.session_state.total_games += 1
                    st.session_state.last_comment = random.choice(ORBI_COMMENTS["not_found"])
                else:
                    st.session_state.last_comment = get_orbi_comment(after)
                
                st.session_state.current_question = None
                st.session_state.answer_submitted = False
                st.session_state.temp_answer = None
                st.rerun()
        
        # UYARI
        if len(st.session_state.candidates) <= 3 and not st.session_state.game_over:
            st.warning(f"⚠️ Sadece {len(st.session_state.candidates)} aday kaldı!")
    
    # ========== OYUN SONU ==========
    else:
        if st.session_state.found_landmark:
            lm = st.session_state.found_landmark
            st.markdown(f"""
            <div class="result-found">
                <h1 style="color: #00d4ff;">🎉 {random.choice(['BULDUM!', 'SENİ YAKALADIM!', 'İŞTE BURADA!'])}</h1>
                <h2 style="color: white; font-size: 2.2em;">📍 {lm['name']}</h2>
                <p style="color: #8899aa;">{lm['country']} • {lm['city']} • {lm['continent']}</p>
                <p style="color: #e0e8f0;">📂 {lm['category']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric("Soru", len(st.session_state.asked_questions))
            with c2:
                st.metric("Puan", st.session_state.score)
            with c3:
                st.metric("Durum", "✅ Kazanıldı!")
        else:
            st.markdown("""
            <div class="result-not-found">
                <h1 style="color: #ff4444;">😢 Bilemedim...</h1>
                <p style="color: #e0e8f0;">Bu yer veritabanımda yok.</p>
            </div>
            """, unsafe_allow_html=True)
        
        # ÖĞRENME
        if not st.session_state.found_landmark and not st.session_state.learning_mode:
            if st.button("📚 Bu Yeri Öğret!", use_container_width=True):
                st.session_state.learning_mode = True
                st.rerun()
        
        if st.session_state.learning_mode:
            with st.form("learn"):
                col1, col2 = st.columns(2)
                with col1:
                    name = st.text_input("📍 Yer Adı")
                    country = st.text_input("🇺🇸 Ülke")
                    city = st.text_input("🏙️ Şehir")
                with col2:
                    category = st.selectbox("📂 Kategori", ["natural", "archaeological", "religious", "modern", "historical"])
                    is_unesco = st.checkbox("UNESCO")
                    is_natural = st.checkbox("Doğal")
                if st.form_submit_button("💾 Kaydet"):
                    if name and country:
                        new = {
                            "id": len(st.session_state.landmarks) + 1,
                            "name": name,
                            "continent": "Asia",
                            "country": country,
                            "city": city or "Bilinmiyor",
                            "category": category,
                            "is_natural": is_natural,
                            "is_man_made": not is_natural,
                            "is_unesco": is_unesco,
                            "has_tourists": True,
                            "has_entry_fee": False,
                            "is_ancient": False,
                            "is_temple": False,
                            "is_museum": False,
                            "is_mosque": False,
                            "is_church": False,
                            "is_mountain": False,
                            "is_island": False,
                            "is_water": False,
                            "is_desert": False,
                            "is_volcano": False,
                            "is_cave": False,
                            "is_underground": False,
                            "night_light": False,
                            "height_meters": 0
                        }
                        st.session_state.landmarks.append(new)
                        st.success(f"✅ {name} eklendi!")
                        st.session_state.learning_mode = False
                        time.sleep(0.5)
                        reset_game()
                        st.rerun()
        
        # TEKRAR
        c1, c2 = st.columns(2)
        with c1:
            if st.button("🔄 Yeni Oyun", use_container_width=True):
                reset_game()
                st.rerun()
        with c2:
            if st.button("📊 Sıralama", use_container_width=True):
                st.info("🏆 Sıralama yakında!")
    
    # FOOTER
    st.markdown(f"""
    <div class="footer">
        🌍 ORBI v3.0 • {len(st.session_state.landmarks)} yer • {st.session_state.total_games} oyun • %{int((st.session_state.total_wins/max(st.session_state.total_games,1))*100)} kazanma
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
