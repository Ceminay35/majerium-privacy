import streamlit as st

st.set_page_config(page_title="Orbi: Dünya Kaşifi", page_icon="🤖", layout="centered")

# Canva Robotunu Göster (GitHub'a orbi.png olarak yüklediğini varsayıyorum)
try:
    st.image("orbi.png", width=200)
except:
    st.info("Robot resmi (orbi.png) henüz yüklenmedi, ama Orbi burada! 🤖")

st.title("Orbi: Dünya Kaşifi 🌍")
st.subheader("Dünya üzerindeki gizemli yerleri keşfetmeye hazır mısın?")

# Soru ve Seçenekler (Dün konuştuğumuz yapı)
questions = [
    "Piramitlerin içinde gizli odalar olduğuna inanıyor musun?",
    "Çin Seddi uzaydan çıplak gözle görülebilir mi?",
    "Amazon ormanlarında henüz keşfedilmemiş şehirler var mıdır?"
]

if 'current_q' not in st.session_state:
    st.session_state.current_q = 0

if st.session_state.current_q < len(questions):
    st.write(f"### Soru {st.session_state.current_q + 1}: {questions[st.session_state.current_q]}")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Evet"): st.session_state.current_q += 1; st.rerun()
    with col2:
        if st.button("Hayır"): st.session_state.current_q += 1; st.rerun()
    with col3:
        if st.button("Bilmiyorum"): st.session_state.current_q += 1; st.rerun()
    with col4:
        if st.button("Belki"): st.session_state.current_q += 1; st.rerun()
else:
    st.success("Tebrikler! Tüm soruları yanıtladın. Orbi seninle gurur duyuyor! 🎉")
    if st.button("Baştan Başla"):
        st.session_state.current_q = 0
        st.rerun()
