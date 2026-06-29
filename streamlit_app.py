import streamlit as st

# 1. Orbi'nin Keşif Veri Tabanı
LANDMARKS = [
    {"isim": "Piramitler", "kategori": "Arkeoloji", "konum": "Afrika", "tip": "Dış Mekan", "ikonik": "Evet"},
    {"isim": "Eyfel Kulesi", "kategori": "Fotojenik", "konum": "Avrupa", "tip": "Yapı", "ikonik": "Evet"},
    {"isim": "Amazon Ormanı", "kategori": "Doğal", "konum": "Güney Amerika", "tip": "Dış Mekan", "ikonik": "Hayır"},
    {"isim": "Çin Seddi", "kategori": "Arkeoloji", "konum": "Asya", "tip": "Dış Mekan", "ikonik": "Evet"},
    {"isim": "Machu Picchu", "kategori": "Arkeoloji", "konum": "Güney Amerika", "tip": "Dış Mekan", "ikonik": "Evet"},
    {"isim": "Kolezyum", "kategori": "Arkeoloji", "konum": "Avrupa", "tip": "Yapı", "ikonik": "Evet"},
    {"isim": "Göbeklitepe", "kategori": "Arkeoloji", "konum": "Türkiye", "tip": "Dış Mekan", "ikonik": "Evet"}
]

# 2. Oyun Yönetimi
if 'data' not in st.session_state:
    st.session_state.data = LANDMARKS.copy()
    st.session_state.sorular = ["konum", "kategori", "tip", "ikonik"]
    st.session_state.current_q = 0

st.image("orbi_ai.png", width=200)
st.title("Orbi Discovery 🌍")

if len(st.session_state.data) > 1:
    attr = st.session_state.sorular[st.session_state.current_q]
    
    # Orbi'nin karakteristik yorumu
    st.write(f"### Orbi Keşifte: '{attr}' hakkında ipucu arıyorum...")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Evet"):
            st.session_state.data = [i for i in st.session_state.data if i[attr] == "Evet"]
            st.session_state.current_q += 1
            st.rerun()
    with col2:
        if st.button("Hayır"):
            st.session_state.data = [i for i in st.session_state.data if i[attr] != "Evet"]
            st.session_state.current_q += 1
            st.rerun()
else:
    result = st.session_state.data[0]['isim']
    st.success(f"## Buldum! Aklındaki yer: {result} 🎯")
    if st.button("Yeni Keşif 🔄"):
        st.session_state.data = LANDMARKS.copy()
        st.session_state.current_q = 0
        st.rerun()
