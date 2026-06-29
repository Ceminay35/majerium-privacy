"""
Orbi Discovery - Dünya Harikaları Tahmin Oyunu
Akinator mantığıyla çalışan, Information Gain prensibiyle soru seçen
interaktif bir keşif oyunu.
"""

import streamlit as st
import math
from copy import deepcopy

# ─────────────────────────────────────────────
# 1. SAYFA AYARLARI
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Orbi Discovery",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# 2. VİZUEL TASARIM (CSS)
# ─────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Lato:wght@300;400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Lato', sans-serif;
        background-color: #0d1117;
        color: #e8dcc8;
    }

    .stApp { background: linear-gradient(160deg, #0d1117 0%, #1a2035 100%); }

    /* Başlık */
    .orbi-header {
        text-align: center;
        padding: 10px 0 20px 0;
    }
    .orbi-title {
        font-family: 'Cinzel', serif;
        font-size: 2.4rem;
        font-weight: 700;
        background: linear-gradient(90deg, #f0c060, #e07b39, #c0392b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 3px;
        margin: 0;
    }
    .orbi-subtitle {
        font-size: 0.85rem;
        color: #8a9ab5;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-top: 4px;
    }

    /* Orbi konuşma balonu */
    .orbi-bubble {
        background: linear-gradient(135deg, #1e2d45 0%, #16213e 100%);
        border: 1px solid #2a4a6b;
        border-left: 4px solid #f0c060;
        border-radius: 12px;
        padding: 18px 22px;
        margin: 16px 0;
        font-size: 1.05rem;
        line-height: 1.6;
        color: #d4c9b0;
    }

    /* Soru kutusu */
    .question-box {
        background: linear-gradient(135deg, #1a2a1a 0%, #0f1f0f 100%);
        border: 1px solid #2d5a2d;
        border-left: 4px solid #4caf50;
        border-radius: 12px;
        padding: 20px 24px;
        margin: 20px 0;
        font-size: 1.15rem;
        font-weight: 700;
        color: #a8d8a8;
        text-align: center;
    }

    /* İstatistik rozetleri */
    .stat-row {
        display: flex;
        gap: 10px;
        justify-content: center;
        flex-wrap: wrap;
        margin: 12px 0;
    }
    .stat-badge {
        background: #1e2d3d;
        border: 1px solid #2a4a6b;
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 0.8rem;
        color: #8ab4d4;
    }

    /* Tahmin kutusu */
    .guess-box {
        background: linear-gradient(135deg, #2a1a0a 0%, #1a0f05 100%);
        border: 2px solid #f0a030;
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        margin: 20px 0;
    }
    .guess-name {
        font-family: 'Cinzel', serif;
        font-size: 1.8rem;
        color: #f0c060;
        margin-bottom: 6px;
    }

    /* Aday listesi */
    .candidate-item {
        background: #141e2b;
        border: 1px solid #1e3a4a;
        border-radius: 8px;
        padding: 8px 14px;
        margin: 4px 0;
        font-size: 0.9rem;
        display: flex;
        justify-content: space-between;
    }
    .score-bar {
        color: #f0c060;
        font-weight: bold;
    }

    /* Butonlar */
    .stButton > button {
        border-radius: 30px !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        padding: 10px 28px !important;
        transition: all 0.2s ease !important;
    }

    /* Kazanma ekranı */
    .win-box {
        background: linear-gradient(135deg, #0a2a0a, #0f1f05);
        border: 2px solid #4caf50;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        margin: 20px 0;
    }
    .win-title {
        font-family: 'Cinzel', serif;
        font-size: 2rem;
        color: #7ed56f;
    }

    /* Kaybetme ekranı */
    .lose-box {
        background: linear-gradient(135deg, #2a0a0a, #1f0505);
        border: 2px solid #c0392b;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# 3. VERİ SETİ — 15+ Dünya Harikası
# ─────────────────────────────────────────────
WONDERS = {
    "Büyük Piramitler (Giza)": {
        "kıta": "Afrika",
        "ülke": "Mısır",
        "kategori": "Antik",
        "yapı_türü": "Anıt Mezar",
        "ikonik": True,
        "su_kenarı": False,
        "dağlık": False,
        "tapınak_mı": False,
        "uygarlık": "Mısır",
        "yüzyıl_inşa": "MÖ 26",
        "doğal_mı": False,
        "duvar_var_mı": False,
        "ada_mı": False,
        "iklim": "Çöl",
        "ziyaretçi_yoğunluğu": "Çok Yüksek",
        "açıklama": "Dünyanın 7 harikasından biri olan, Mısır firavunlarına ait devasa mezar kompleksi."
    },
    "Machu Picchu": {
        "kıta": "Güney Amerika",
        "ülke": "Peru",
        "kategori": "Antik",
        "yapı_türü": "Şehir Kalıntısı",
        "ikonik": True,
        "su_kenarı": False,
        "dağlık": True,
        "tapınak_mı": False,
        "uygarlık": "İnka",
        "yüzyıl_inşa": "MS 15",
        "doğal_mı": False,
        "duvar_var_mı": True,
        "ada_mı": False,
        "iklim": "Tropikal Dağ",
        "ziyaretçi_yoğunluğu": "Yüksek",
        "açıklama": "Bulutların arasındaki gizemli İnka şehri, And Dağları'nın zirvesinde."
    },
    "Göbeklitepe": {
        "kıta": "Asya",
        "ülke": "Türkiye",
        "kategori": "Antik",
        "yapı_türü": "Tapınak Kompleksi",
        "ikonik": True,
        "su_kenarı": False,
        "dağlık": True,
        "tapınak_mı": True,
        "uygarlık": "Prehistorik",
        "yüzyıl_inşa": "MÖ 10",
        "doğal_mı": False,
        "duvar_var_mı": False,
        "ada_mı": False,
        "iklim": "Karasal",
        "ziyaretçi_yoğunluğu": "Orta",
        "açıklama": "Dünyanın bilinen en eski tapınak kompleksi, Şanlıurfa'da."
    },
    "Büyük Çin Seddi": {
        "kıta": "Asya",
        "ülke": "Çin",
        "kategori": "Tarihi",
        "yapı_türü": "Savunma Duvarı",
        "ikonik": True,
        "su_kenarı": False,
        "dağlık": True,
        "tapınak_mı": False,
        "uygarlık": "Çin",
        "yüzyıl_inşa": "MÖ 7",
        "doğal_mı": False,
        "duvar_var_mı": True,
        "ada_mı": False,
        "iklim": "Çeşitli",
        "ziyaretçi_yoğunluğu": "Çok Yüksek",
        "açıklama": "Binlerce kilometre uzanan tarihin en büyük duvarı."
    },
    "Petra": {
        "kıta": "Asya",
        "ülke": "Ürdün",
        "kategori": "Antik",
        "yapı_türü": "Kaya Kenti",
        "ikonik": True,
        "su_kenarı": False,
        "dağlık": True,
        "tapınak_mı": False,
        "uygarlık": "Nebati",
        "yüzyıl_inşa": "MÖ 4",
        "doğal_mı": False,
        "duvar_var_mı": False,
        "ada_mı": False,
        "iklim": "Çöl",
        "ziyaretçi_yoğunluğu": "Yüksek",
        "açıklama": "Kayalara oyulmuş Pembe Şehir, Nebati uygarlığının başkenti."
    },
    "Koloseum": {
        "kıta": "Avrupa",
        "ülke": "İtalya",
        "kategori": "Antik",
        "yapı_türü": "Amfitiyatro",
        "ikonik": True,
        "su_kenarı": False,
        "dağlık": False,
        "tapınak_mı": False,
        "uygarlık": "Roma",
        "yüzyıl_inşa": "MS 1",
        "doğal_mı": False,
        "duvar_var_mı": True,
        "ada_mı": False,
        "iklim": "Akdeniz",
        "ziyaretçi_yoğunluğu": "Çok Yüksek",
        "açıklama": "Roma'nın kalbi, gladyatörlerin arenası."
    },
    "Angkor Wat": {
        "kıta": "Asya",
        "ülke": "Kamboçya",
        "kategori": "Antik",
        "yapı_türü": "Tapınak Kompleksi",
        "ikonik": True,
        "su_kenarı": True,
        "dağlık": False,
        "tapınak_mı": True,
        "uygarlık": "Khmer",
        "yüzyıl_inşa": "MS 12",
        "doğal_mı": False,
        "duvar_var_mı": True,
        "ada_mı": False,
        "iklim": "Tropikal",
        "ziyaretçi_yoğunluğu": "Yüksek",
        "açıklama": "Dünyanın en büyük dini anıtı, Khmer İmparatorluğu'nun tacı."
    },
    "Çiçen İtza": {
        "kıta": "Kuzey Amerika",
        "ülke": "Meksika",
        "kategori": "Antik",
        "yapı_türü": "Maya Piramidi",
        "ikonik": True,
        "su_kenarı": False,
        "dağlık": False,
        "tapınak_mı": True,
        "uygarlık": "Maya",
        "yüzyıl_inşa": "MS 6",
        "doğal_mı": False,
        "duvar_var_mı": False,
        "ada_mı": False,
        "iklim": "Tropikal",
        "ziyaretçi_yoğunluğu": "Yüksek",
        "açıklama": "Maya uygarlığının astronomik mühendislik harikası."
    },
    "Tac Mahal": {
        "kıta": "Asya",
        "ülke": "Hindistan",
        "kategori": "Tarihi",
        "yapı_türü": "Türbe",
        "ikonik": True,
        "su_kenarı": True,
        "dağlık": False,
        "tapınak_mı": False,
        "uygarlık": "Babür",
        "yüzyıl_inşa": "MS 17",
        "doğal_mı": False,
        "duvar_var_mı": True,
        "ada_mı": False,
        "iklim": "Muson",
        "ziyaretçi_yoğunluğu": "Çok Yüksek",
        "açıklama": "Bir imparatorun sevgi anıtı, beyaz mermerin şiiri."
    },
    "Stonehenge": {
        "kıta": "Avrupa",
        "ülke": "İngiltere",
        "kategori": "Antik",
        "yapı_türü": "Megalit",
        "ikonik": True,
        "su_kenarı": False,
        "dağlık": False,
        "tapınak_mı": True,
        "uygarlık": "Prehistorik",
        "yüzyıl_inşa": "MÖ 30",
        "doğal_mı": False,
        "duvar_var_mı": False,
        "ada_mı": True,
        "iklim": "Okyanus",
        "ziyaretçi_yoğunluğu": "Yüksek",
        "açıklama": "Gizemli taş halkası, Druidlerin sırlarını saklar."
    },
    "Aya Sofya": {
        "kıta": "Avrupa",
        "ülke": "Türkiye",
        "kategori": "Tarihi",
        "yapı_türü": "Dini Yapı",
        "ikonik": True,
        "su_kenarı": True,
        "dağlık": False,
        "tapınak_mı": True,
        "uygarlık": "Bizans",
        "yüzyıl_inşa": "MS 6",
        "doğal_mı": False,
        "duvar_var_mı": True,
        "ada_mı": False,
        "iklim": "Akdeniz",
        "ziyaretçi_yoğunluğu": "Çok Yüksek",
        "açıklama": "İstanbul'un kalbi, Bizans mühendisliğinin zirvesi."
    },
    "Efes Antik Kenti": {
        "kıta": "Asya",
        "ülke": "Türkiye",
        "kategori": "Antik",
        "yapı_türü": "Şehir Kalıntısı",
        "ikonik": True,
        "su_kenarı": False,
        "dağlık": False,
        "tapınak_mı": False,
        "uygarlık": "Roma",
        "yüzyıl_inşa": "MÖ 10",
        "doğal_mı": False,
        "duvar_var_mı": True,
        "ada_mı": False,
        "iklim": "Akdeniz",
        "ziyaretçi_yoğunluğu": "Yüksek",
        "açıklama": "Antik dünyanın en büyük şehirlerinden biri, Artemis Tapınağı'na ev sahipliği yaptı."
    },
    "Borobudur": {
        "kıta": "Asya",
        "ülke": "Endonezya",
        "kategori": "Antik",
        "yapı_türü": "Tapınak Kompleksi",
        "ikonik": False,
        "su_kenarı": False,
        "dağlık": False,
        "tapınak_mı": True,
        "uygarlık": "Budist",
        "yüzyıl_inşa": "MS 8",
        "doğal_mı": False,
        "duvar_var_mı": False,
        "ada_mı": True,
        "iklim": "Tropikal",
        "ziyaretçi_yoğunluğu": "Orta",
        "açıklama": "Dünyanın en büyük Budist tapınak kompleksi, Java Adası'nda."
    },
    "Mesa Verde": {
        "kıta": "Kuzey Amerika",
        "ülke": "ABD",
        "kategori": "Antik",
        "yapı_türü": "Kaya Yerleşimi",
        "ikonik": False,
        "su_kenarı": False,
        "dağlık": True,
        "tapınak_mı": False,
        "uygarlık": "Anasazi",
        "yüzyıl_inşa": "MS 6",
        "doğal_mı": False,
        "duvar_var_mı": True,
        "ada_mı": False,
        "iklim": "Karasal",
        "ziyaretçi_yoğunluğu": "Orta",
        "açıklama": "Kayalıklara gömülü gizemli Pueblo yerleşimi, Colorado'da."
    },
    "İnka Yolu (Qhapaq Ñan)": {
        "kıta": "Güney Amerika",
        "ülke": "Peru",
        "kategori": "Antik",
        "yapı_türü": "Yol Sistemi",
        "ikonik": False,
        "su_kenarı": False,
        "dağlık": True,
        "tapınak_mı": False,
        "uygarlık": "İnka",
        "yüzyıl_inşa": "MS 15",
        "doğal_mı": False,
        "duvar_var_mı": False,
        "ada_mı": False,
        "iklim": "Çeşitli",
        "ziyaretçi_yoğunluğu": "Düşük",
        "açıklama": "30.000 km'lik İnka yol ağı, And Dağları'nı baştan başa keser."
    },
    "Karnak Tapınağı": {
        "kıta": "Afrika",
        "ülke": "Mısır",
        "kategori": "Antik",
        "yapı_türü": "Tapınak Kompleksi",
        "ikonik": False,
        "su_kenarı": True,
        "dağlık": False,
        "tapınak_mı": True,
        "uygarlık": "Mısır",
        "yüzyıl_inşa": "MÖ 20",
        "doğal_mı": False,
        "duvar_var_mı": True,
        "ada_mı": False,
        "iklim": "Çöl",
        "ziyaretçi_yoğunluğu": "Orta",
        "açıklama": "Nil kıyısındaki dünyanın en büyük dini kompleksi."
    },
}

# ─────────────────────────────────────────────
# 4. SORU HAVUZU (özellik adı → soru metni, değer)
# ─────────────────────────────────────────────
QUESTIONS = [
    {
        "id": "kıta_asya",
        "metin": "Bu yer Asya kıtasında mı?",
        "özellik": "kıta",
        "değer": "Asya",
        "orbi_evet": "Hmm, Asya'ya odaklanıyorum... Çok sayıda gizemli yapı var orada!",
        "orbi_hayır": "Tamam, Asya'yı listeden çıkardım. Haritayı daraltıyorum...",
    },
    {
        "id": "kıta_avrupa",
        "metin": "Bu yer Avrupa'da mı?",
        "özellik": "kıta",
        "değer": "Avrupa",
        "orbi_evet": "Avrupa! Roma'dan Stonehenge'e... İzimi daraltıyorum.",
        "orbi_hayır": "Avrupa değil, güzel! Rotamı değiştiriyorum.",
    },
    {
        "id": "kıta_g_amerika",
        "metin": "Bu yer Güney Amerika'da mı?",
        "özellik": "kıta",
        "değer": "Güney Amerika",
        "orbi_evet": "And Dağları ve Amazon... Keşfediyorum!",
        "orbi_hayır": "Güney Amerika değil. Devam...",
    },
    {
        "id": "kıta_k_amerika",
        "metin": "Bu yer Kuzey Amerika'da mı?",
        "özellik": "kıta",
        "değer": "Kuzey Amerika",
        "orbi_evet": "Maya, Aztec, Pueblo... Kuzey Amerika'ya iniş!",
        "orbi_hayır": "Kuzey Amerika değil. Haritayı güncelliyorum.",
    },
    {
        "id": "kıta_afrika",
        "metin": "Bu yer Afrika kıtasında mı?",
        "özellik": "kıta",
        "değer": "Afrika",
        "orbi_evet": "Afrika! Piramitler ve antik medeniyetler geliyor aklıma...",
        "orbi_hayır": "Afrika dışında bir yer. Devam ediyorum.",
    },
    {
        "id": "dağlık",
        "metin": "Bu yer dağlık veya yüksek rakımlı bir konumda mı?",
        "özellik": "dağlık",
        "değer": True,
        "orbi_evet": "Yüksek rakım... Dağların arasında gizlenmiş olmalı!",
        "orbi_hayır": "Düzlükte veya ova üzerinde. Veri tabanımı güncelliyorum.",
    },
    {
        "id": "tapınak",
        "metin": "Bu yapı dini bir tapınak veya ibadet yeri mi?",
        "özellik": "tapınak_mı",
        "değer": True,
        "orbi_evet": "Kutsal bir mekân... Tanrılara adanmış!",
        "orbi_hayır": "Dini amaçlı değil. İlginç, başka bir işlevi var demek.",
    },
    {
        "id": "su_kenarı",
        "metin": "Bu yer nehir, göl veya deniz kenarında mı?",
        "özellik": "su_kenarı",
        "değer": True,
        "orbi_evet": "Su kenarı! Nehir uygarlıkları aklıma geliyor...",
        "orbi_hayır": "Suya yakın değil. İç bölgelerde olabilir.",
    },
    {
        "id": "doğal",
        "metin": "Bu yer tamamen doğal bir oluşum mu (insan yapımı değil)?",
        "özellik": "doğal_mı",
        "değer": True,
        "orbi_evet": "Saf doğa... Hiçbir insan eli değmemiş!",
        "orbi_hayır": "İnsan yapımı. İşçiliği hayal edebiliyorum!",
    },
    {
        "id": "duvar",
        "metin": "Bu yapıda büyük ya da anıtsal duvarlar/surlar var mı?",
        "özellik": "duvar_var_mı",
        "değer": True,
        "orbi_evet": "Surlar! Savunma mı, sınır mı, yoksa ihtişam mı?",
        "orbi_hayır": "Duvarsız bir yapı. Belki açık alan ya da anıt.",
    },
    {
        "id": "ada",
        "metin": "Bu yer bir adada mı ya da adayla bağlantılı mı?",
        "özellik": "ada_mı",
        "değer": True,
        "orbi_evet": "Ada! Denizle çevrili gizemli bir yer...",
        "orbi_hayır": "Ada değil. Ana karada bir yerde.",
    },
    {
        "id": "ikonik",
        "metin": "Bu yer dünyanın en tanınmış simgelerinden biri mi (herkes tanır)?",
        "özellik": "ikonik",
        "değer": True,
        "orbi_evet": "Süper ikonik! Fotoğrafı akıllarda kalıcı...",
        "orbi_hayır": "Pek bilinmeyen ya da gizli bir hazine olabilir.",
    },
    {
        "id": "antik",
        "metin": "Bu yer MS 1000'den önce inşa edildi mi (antik çağa mı ait)?",
        "özellik": "kategori",
        "değer": "Antik",
        "orbi_evet": "Antik dönem... Binlerce yıllık bir sır!",
        "orbi_hayır": "Daha yakın tarihli bir yapı. Orta Çağ veya sonrası.",
    },
    {
        "id": "tropikal",
        "metin": "Bu yerin iklimi tropikal ya da sıcak ve nemli mi?",
        "özellik": "iklim",
        "değer": "Tropikal",
        "orbi_evet": "Tropikal cennet! Yeşillikler arasında bir gizem...",
        "orbi_hayır": "Tropikal değil. Belki çöl, dağ veya ılıman.",
    },
    {
        "id": "çöl",
        "metin": "Bu yer çöl ya da kurak bir bölgede mi?",
        "özellik": "iklim",
        "değer": "Çöl",
        "orbi_evet": "Kum ve güneş... Antik Mısır veya Orta Doğu olabilir!",
        "orbi_hayır": "Çöl değil. Farklı bir iklim.",
    },
    {
        "id": "türkiye",
        "metin": "Bu yer Türkiye'de mi?",
        "özellik": "ülke",
        "değer": "Türkiye",
        "orbi_evet": "Türkiye! Göbeklitepe, Efes, Aya Sofya... Çok zengin bir miras!",
        "orbi_hayır": "Türkiye değil. Devam...",
    },
    {
        "id": "mısır",
        "metin": "Bu yer Mısır'da mı?",
        "özellik": "ülke",
        "değer": "Mısır",
        "orbi_evet": "Mısır! Firavunlar ve tanrılar diyarı...",
        "orbi_hayır": "Mısır değil. Devam ediyorum.",
    },
]

# ─────────────────────────────────────────────
# 5. INFORMATION GAIN HESAPLAMA
# ─────────────────────────────────────────────

def entropy(candidates: dict) -> float:
    """Verilen adayların Shannon entropisini hesaplar."""
    n = len(candidates)
    if n == 0:
        return 0.0
    scores = [v.get("_skor", 1.0) for v in candidates.values()]
    total = sum(scores)
    if total == 0:
        return 0.0
    ent = 0.0
    for s in scores:
        p = s / total
        if p > 0:
            ent -= p * math.log2(p)
    return ent


def information_gain(candidates: dict, question: dict) -> float:
    """Bir sorunun bilgi kazancını hesaplar (0-1 arası)."""
    ozellik = question["özellik"]
    deger = question["değer"]

    evet_grup = {}
    hayir_grup = {}

    for name, props in candidates.items():
        if props.get(ozellik) == deger:
            evet_grup[name] = props
        else:
            hayir_grup[name] = props

    n_total = len(candidates)
    if n_total == 0:
        return 0.0

    n_evet = len(evet_grup)
    n_hayir = len(hayir_grup)

    h_before = entropy(candidates)
    h_after = (n_evet / n_total) * entropy(evet_grup) + \
              (n_hayir / n_total) * entropy(hayir_grup)

    return h_before - h_after


def best_question(candidates: dict, asked: list) -> dict | None:
    """Sorulmamış sorular arasından en yüksek information gain'e sahip olanı seçer."""
    best_q = None
    best_gain = -1.0
    for q in QUESTIONS:
        if q["id"] in asked:
            continue
        gain = information_gain(candidates, q)
        if gain > best_gain:
            best_gain = gain
            best_q = q
    return best_q

# ─────────────────────────────────────────────
# 6. OTURUM DURUMU BAŞLATMA
# ─────────────────────────────────────────────

def init_state():
    """Oyun durumunu sıfırdan başlatır."""
    if "initialized" not in st.session_state:
        st.session_state.initialized = True
        st.session_state.game_phase = "playing"   # playing | guessing | win | lose
        st.session_state.candidates = deepcopy(WONDERS)
        # Her adaya başlangıç skoru ver
        for name in st.session_state.candidates:
            st.session_state.candidates[name]["_skor"] = 1.0
        st.session_state.asked_ids = []           # Sorulmuş soru id'leri
        st.session_state.current_question = None  # O anki soru
        st.session_state.soru_no = 0              # Soru sayacı
        st.session_state.orbi_mesaj = (
            "Merhaba! Ben **Orbi** 🌍 — Dünya Harikalarını keşfeden bir yapay zeka! "
            "Aklındaki yeri düşün... Sorularımla bulmaya çalışacağım. Hazır mısın?"
        )
        st.session_state.tahmin = None            # Son tahmin adı
        st.session_state.cevap_log = []           # Soru-cevap geçmişi


def reset_game():
    """Oyunu sıfırlar."""
    for key in list(st.session_state.keys()):
        del st.session_state[key]


# ─────────────────────────────────────────────
# 7. CEVAP İŞLEME
# ─────────────────────────────────────────────

def process_answer(cevap: str):
    """
    Kullanıcının cevabını işler:
    - Evet  → özelliği eşleşmeyenlerin skoru düşer
    - Hayır → özelliği eşleşenlerin skoru düşer
    - Belki → hafif skor değişimi
    - Bilmiyorum → skor değişmez
    """
    q = st.session_state.current_question
    if q is None:
        return

    ozellik = q["özellik"]
    deger = q["değer"]

    # Log'a ekle
    st.session_state.cevap_log.append({
        "soru": q["metin"],
        "cevap": cevap
    })

    for name, props in st.session_state.candidates.items():
        esleşti = (props.get(ozellik) == deger)

        if cevap == "Evet":
            if not esleşti:
                props["_skor"] *= 0.05   # Eşleşmeyenleri neredeyse sıfırla
            else:
                props["_skor"] *= 1.5    # Eşleşenleri güçlendir
        elif cevap == "Hayır":
            if esleşti:
                props["_skor"] *= 0.05   # Eşleşenleri neredeyse sıfırla
            else:
                props["_skor"] *= 1.3    # Eşleşmeyenleri güçlendir
        elif cevap == "Belki":
            if esleşti:
                props["_skor"] *= 1.1    # Hafif artış
            else:
                props["_skor"] *= 0.8    # Hafif düşüş
        # "Bilmiyorum" → değişiklik yok

    # Çok düşük skorluları (≤ 0.001) listeden çıkar
    st.session_state.candidates = {
        name: props
        for name, props in st.session_state.candidates.items()
        if props["_skor"] > 0.001
    }

    # Orbi mesajı güncelle
    if cevap == "Evet":
        st.session_state.orbi_mesaj = q["orbi_evet"]
    elif cevap == "Hayır":
        st.session_state.orbi_mesaj = q["orbi_hayır"]
    elif cevap == "Belki":
        st.session_state.orbi_mesaj = "Belki... Olasılığı tamamen silmiyorum ama zayıf tutuyorum."
    else:
        st.session_state.orbi_mesaj = "Anladım, bu konuda emin değilsin. Devam ediyorum."

    st.session_state.asked_ids.append(q["id"])
    st.session_state.current_question = None
    st.session_state.soru_no += 1

    # Oyun durumunu güncelle
    update_game_phase()


def update_game_phase():
    """Aday listesine göre oyun fazını günceller."""
    n = len(st.session_state.candidates)

    if n == 0:
        st.session_state.game_phase = "lose"
        st.session_state.orbi_mesaj = (
            "Bütün adayları eledim ama hâlâ bulamadım! 🤔 "
            "Bu çok nadir bir yer olmalı — haritamda yok sanırım!"
        )
    elif n == 1:
        st.session_state.tahmin = list(st.session_state.candidates.keys())[0]
        st.session_state.game_phase = "guessing"
        st.session_state.orbi_mesaj = (
            f"🎯 Çok yaklaştım! Sadece **{n}** aday kaldı. "
            "Tahmini hazırlıyorum..."
        )
    elif st.session_state.soru_no >= 10:
        # 10 soruda bitiremezsek en yüksek skorlu adayı tahmin et
        en_iyi = max(
            st.session_state.candidates.items(),
            key=lambda x: x[1]["_skor"]
        )
        st.session_state.tahmin = en_iyi[0]
        st.session_state.game_phase = "guessing"
        st.session_state.orbi_mesaj = (
            f"10 soruyu doldurdum! En güçlü izim **{n}** aday içinde. "
            "Son tahmini yapıyorum..."
        )

# ─────────────────────────────────────────────
# 8. ANA SAYFA ÇİZİMİ
# ─────────────────────────────────────────────

def render_header():
    """Logo ve başlık."""
    # GitHub'dan orbi_ai.png yüklemeyi dene; hata olursa emoji göster
    try:
        st.image(
            "https://raw.githubusercontent.com/yourusername/yourrepo/main/orbi_ai.png",
            width=200,
        )
    except Exception:
        pass  # Resim yoksa sessizce geç

    st.markdown("""
    <div class="orbi-header">
        <div class="orbi-title">ORBI DISCOVERY</div>
        <div class="orbi-subtitle">🌍 &nbsp; Dünya Harikaları Tahmin Oyunu &nbsp; 🌍</div>
    </div>
    """, unsafe_allow_html=True)


def render_stats():
    """Kalan aday sayısı ve soru sayacı."""
    n_aday = len(st.session_state.candidates)
    n_soru = st.session_state.soru_no
    st.markdown(f"""
    <div class="stat-row">
        <div class="stat-badge">🔍 Kalan Aday: <b>{n_aday}</b></div>
        <div class="stat-badge">❓ Soru: <b>{n_soru}/10</b></div>
    </div>
    """, unsafe_allow_html=True)


def render_orbi_bubble():
    """Orbi'nin keşif mesajı."""
    st.markdown(f"""
    <div class="orbi-bubble">
        🤖 <b>Orbi:</b> {st.session_state.orbi_mesaj}
    </div>
    """, unsafe_allow_html=True)


def render_playing():
    """Soru-cevap aşaması."""
    # Mevcut soru yoksa yeni soru seç
    if st.session_state.current_question is None:
        q = best_question(
            st.session_state.candidates,
            st.session_state.asked_ids
        )
        if q is None:
            # Soracak soru kalmadı → tahmin yap
            update_game_phase()
            return
        st.session_state.current_question = q

    q = st.session_state.current_question

    # Soru kutusunu göster
    st.markdown(f"""
    <div class="question-box">
        {st.session_state.soru_no + 1}. {q['metin']}
    </div>
    """, unsafe_allow_html=True)

    # Cevap butonları
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("✅ Evet", use_container_width=True, key="btn_evet"):
            process_answer("Evet")
            st.rerun()
    with col2:
        if st.button("❌ Hayır", use_container_width=True, key="btn_hayir"):
            process_answer("Hayır")
            st.rerun()
    with col3:
        if st.button("🤔 Belki", use_container_width=True, key="btn_belki"):
            process_answer("Belki")
            st.rerun()
    with col4:
        if st.button("❓ Bilmiyorum", use_container_width=True, key="btn_bilmiyorum"):
            process_answer("Bilmiyorum")
            st.rerun()

    # Gizli aday listesi (expander ile)
    with st.expander("🗺️ Orbi'nin radarında neler var?", expanded=False):
        sorted_candidates = sorted(
            st.session_state.candidates.items(),
            key=lambda x: x[1]["_skor"],
            reverse=True
        )
        for name, props in sorted_candidates[:8]:  # İlk 8'i göster
            skor = props["_skor"]
            bar = "█" * min(int(skor * 5), 10)
            st.markdown(f"""
            <div class="candidate-item">
                <span>🏛️ {name}</span>
                <span class="score-bar">{bar} ({skor:.2f})</span>
            </div>
            """, unsafe_allow_html=True)


def render_guessing():
    """Tahmin aşaması."""
    tahmin = st.session_state.tahmin
    props = WONDERS.get(tahmin, {})

    st.markdown(f"""
    <div class="guess-box">
        <div style="font-size:2rem; margin-bottom:8px;">🎯</div>
        <div style="color:#8ab4d4; font-size:0.9rem; letter-spacing:2px;">ORBİ'NİN TAHMİNİ</div>
        <div class="guess-name">{tahmin}</div>
        <div style="color:#8a9ab5; font-size:0.9rem; margin-top:8px;">
            📍 {props.get('ülke','?')} &nbsp;|&nbsp; 🌐 {props.get('kıta','?')} 
            &nbsp;|&nbsp; 🏛️ {props.get('yapı_türü','?')}
        </div>
        <div style="color:#d4c9b0; font-size:0.95rem; margin-top:12px; font-style:italic;">
            "{props.get('açıklama','')}"
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎉 Evet, bu doğru!", use_container_width=True, type="primary"):
            st.session_state.game_phase = "win"
            st.rerun()
    with col2:
        if st.button("😔 Hayır, yanlış tahmin", use_container_width=True):
            st.session_state.game_phase = "lose"
            st.session_state.orbi_mesaj = (
                f"Tahminim yanlışmış! Haritamı genişletmem gerekiyor. "
                "Bu gizemli yeri veritabanıma eklemem lazım!"
            )
            st.rerun()


def render_win():
    """Kazanma ekranı."""
    tahmin = st.session_state.tahmin
    props = WONDERS.get(tahmin, {})
    n_soru = st.session_state.soru_no

    st.markdown(f"""
    <div class="win-box">
        <div class="win-title">🏆 Buldum!</div>
        <div style="font-size:2.5rem; margin:10px 0;">🌟</div>
        <div style="font-size:1.4rem; color:#a8d8a8; margin-bottom:8px;">{tahmin}</div>
        <div style="color:#5a8a5a; font-size:0.9rem;">
            {n_soru} soruda keşfettim &nbsp;|&nbsp; {props.get('ülke','?')} &nbsp;|&nbsp; {props.get('kıta','?')}
        </div>
        <div style="color:#7a9a7a; font-size:0.85rem; margin-top:12px; font-style:italic;">
            "{props.get('açıklama','')}"
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 Yeni Keşif Başlat", use_container_width=True, type="primary"):
        reset_game()
        st.rerun()


def render_lose():
    """Kaybetme ekranı."""
    n_soru = st.session_state.soru_no

    st.markdown(f"""
    <div class="lose-box">
        <div style="font-size:2.5rem; margin-bottom:8px;">🗺️</div>
        <div style="font-family:'Cinzel',serif; font-size:1.8rem; color:#e07070;">
            Haritamda bu yer yok!
        </div>
        <div style="color:#a07070; font-size:0.95rem; margin-top:12px;">
            {n_soru} soruda bulamadım. Bu sefer sen kazandın! 
            Hangi yeri düşündüğünü merak ediyorum...
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 Tekrar Oyna", use_container_width=True, type="primary"):
        reset_game()
        st.rerun()


def render_question_log():
    """Soru-cevap geçmişini göster."""
    if st.session_state.cevap_log:
        with st.expander("📜 Soru-Cevap Geçmişi", expanded=False):
            for i, item in enumerate(st.session_state.cevap_log, 1):
                emoji = {"Evet": "✅", "Hayır": "❌", "Belki": "🤔", "Bilmiyorum": "❓"}
                e = emoji.get(item["cevap"], "•")
                st.write(f"**{i}.** {item['soru']} → {e} *{item['cevap']}*")


# ─────────────────────────────────────────────
# 9. ANA AKIŞ
# ─────────────────────────────────────────────

def main():
    init_state()

    render_header()

    # İstatistikler (son ekranlar hariç)
    if st.session_state.game_phase in ("playing", "guessing"):
        render_stats()

    render_orbi_bubble()

    phase = st.session_state.game_phase

    if phase == "playing":
        render_playing()
    elif phase == "guessing":
        render_guessing()
    elif phase == "win":
        render_win()
    elif phase == "lose":
        render_lose()

    # Soru geçmişi her zaman altta
    if st.session_state.game_phase not in ("win",):
        render_question_log()

    # Sıfırla butonu (her aşamada)
    st.divider()
    col_r, _ = st.columns([1, 3])
    with col_r:
        if st.button("↩️ Sıfırla", help="Oyunu baştan başlat"):
            reset_game()
            st.rerun()


if __name__ == "__main__":
    main()
