import streamlit as st

# Uygulama başlığı
st.set_page_config(page_title="Orbi Uygulaması", page_icon="🚀")
st.title("🚀 Orbi Yayında!")

st.write("Hoş geldin! Burası senin yeni uygulama alanın.")

# Basit bir kullanıcı etkileşimi ekleyelim
isim = st.text_input("İsmini öğrenebilir miyim?")
if isim:
    st.write(f"Merhaba {isim}, Duru Beril'e selamlar!")

# Bir buton ekleyelim
if st.button("Bana tıkla"):
    st.balloons()
    st.success("Harika gidiyorsun!")
