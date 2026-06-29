import streamlit as st

# Orbi görselini çağırıyoruz
st.image("orbi_ai.png", width=200)

# Başlığı ayarlıyoruz
st.title("Orbi: Dünya Kaşifi 🌍")

# Akinatör mantığı (Orbi Discovery)
st.write("Dünya üzerindeki gizemli yerleri keşfetmeye hazır mısın?")

# Örnek bir soru (Bunu geliştireceğiz)
if 'adim' not in st.session_state:
    st.session_state.adim = 1

if st.session_state.adim == 1:
    st.write("Soru 1: Piramitlerin içinde gizli odalar olduğuna inanıyor musun?")
    col1, col2 = st.columns(2)
    if col1.button("Evet"):
        st.session_state.adim = 2
        st.rerun()
    if col2.button("Hayır"):
        st.session_state.adim = 2
        st.rerun()
