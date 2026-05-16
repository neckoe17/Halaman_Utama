import streamlit as st
import base64
import pandas as pd
import requests
from pathlib import Path
from streamlit.components.v1 import html

# ==================== KONFIGURASI HALAMAN ====================
st.set_page_config(
    page_title="Loka Dalam Genggaman",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== BACKGROUND GAMBAR (BASE64) ====================
background_image_path = Path("MRAP122.jpg")  # Ganti dengan file background anda
background_base64 = ""

if background_image_path.exists():
    with open(background_image_path, "rb") as img_file:
        background_base64 = base64.b64encode(img_file.read()).decode()
else:
    st.warning("File MRAP122.jpg tidak ditemukan. Gunakan background default.")

# ==================== CSS KUSTOM (ELEGAN, LUX, MODERN) ====================
if background_base64:
    bg_style = f"url('data:image/jpeg;base64,{background_base64}')"
else:
    bg_style = "linear-gradient(135deg, #0a1a2b, #1b4a6f)"

custom_css = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,600;14..32,700&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
    }}
    
    /* Background utama dengan overlay gelap */
    .stApp {{
        background: {bg_style} no-repeat center center fixed;
        background-size: cover;
    }}
    
    .main {{
        background: rgba(0, 0, 0, 0.55);
        backdrop-filter: blur(14px);
        border-radius: 0;
        padding: 1rem 2rem;
    }}
    
    /* Header mewah */
    .dashboard-title {{
        text-align: center;
        padding: 0.5rem 0 1rem 0;
        margin-bottom: 0.5rem;
    }}
    .dashboard-title h1 {{
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #F9D976, #F39F86, #E6C87A);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        text-shadow: 0 2px 12px rgba(0,0,0,0.3);
        letter-spacing: -0.5px;
    }}
    .dashboard-sub {{
        color: #FAF3E0;
        font-size: 1rem;
        font-weight: 500;
        max-width: 700px;
        margin: 0 auto;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
        background: rgba(0,0,0,0.3);
        padding: 8px 20px;
        border-radius: 40px;
        display: inline-block;
        backdrop-filter: blur(4px);
    }}
    
    /* Card Carousel (kiri) */
    .carousel-card {{
        background: rgba(25, 25, 35, 0.7);
        backdrop-filter: blur(12px);
        border-radius: 36px;
        padding: 1rem;
        border: 1px solid rgba(212,175,55,0.4);
        box-shadow: 0 20px 35px -10px rgba(0,0,0,0.3);
        height: 100%;
    }}
    .carousel-img {{
        border-radius: 24px;
        width: 100%;
        object-fit: cover;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        border: 1px solid rgba(212,175,55,0.3);
        transition: transform 0.3s ease;
    }}
    .carousel-btn {{
        background: rgba(212,175,55,0.2);
        border: 1px solid rgba(212,175,55,0.6);
        color: #D4AF37;
        font-size: 1.3rem;
        font-weight: bold;
        border-radius: 50px;
        padding: 0.25rem 1rem;
        transition: all 0.2s;
        cursor: pointer;
        text-align: center;
    }}
    .carousel-btn:hover {{
        background: #D4AF37;
        color: #1e2a3a;
        transform: scale(1.02);
    }}
    
    /* Grid 4 bagian (kanan) */
    .section-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
        height: 100%;
    }}
    .grid-card {{
        background: rgba(18, 22, 35, 0.65);
        backdrop-filter: blur(8px);
        border-radius: 28px;
        padding: 1rem 0.8rem;
        border: 1px solid rgba(212,175,55,0.3);
        transition: all 0.2s;
        height: 100%;
    }}
    .grid-card:hover {{
        border-color: #D4AF37;
        background: rgba(30, 35, 50, 0.75);
    }}
    .grid-title {{
        font-size: 1.2rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1rem;
        padding-bottom: 0.4rem;
        border-bottom: 2px solid #D4AF37;
        display: inline-block;
        width: 100%;
        color: #F5E7B2;
        letter-spacing: -0.2px;
    }}
    .list-link {{
        display: flex;
        align-items: center;
        gap: 0.8rem;
        margin: 0.8rem 0;
        padding: 0.4rem 0.6rem;
        border-radius: 20px;
        background: rgba(255,255,255,0.05);
        transition: 0.2s;
        text-decoration: none;
        color: #F0F0F0;
        font-weight: 500;
        font-size: 0.85rem;
    }}
    .list-link i {{
        width: 28px;
        font-size: 1.2rem;
        color: #D4AF37;
        text-align: center;
    }}
    .list-link:hover {{
        background: rgba(212,175,55,0.2);
        transform: translateX(5px);
        color: #FFFFFF;
    }}
    
    /* Running text marquee */
    .marquee-container {{
        background: rgba(0,0,0,0.6);
        backdrop-filter: blur(8px);
        border-radius: 50px;
        padding: 0.5rem 1rem;
        margin-top: 1.5rem;
        border: 1px solid #D4AF37;
        box-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }}
    .marquee {{
        width: 100%;
        white-space: nowrap;
        overflow: hidden;
        box-sizing: border-box;
        color: #F9E0A0;
        font-weight: 500;
        font-size: 0.9rem;
    }}
    .marquee span {{
        display: inline-block;
        padding-left: 100%;
        animation: marquee 20s linear infinite;
    }}
    @keyframes marquee {{
        0% {{ transform: translate(0, 0); }}
        100% {{ transform: translate(-100%, 0); }}
    }}
    
    /* Footer kecil */
    .footer {{
        text-align: center;
        margin-top: 0.8rem;
        font-size: 0.7rem;
        color: #CCCCCC;
    }}
    
    @media (max-width: 768px) {{
        .dashboard-title h1 {{ font-size: 1.8rem; }}
        .grid-title {{ font-size: 1rem; }}
        .list-link {{ font-size: 0.7rem; }}
        .section-grid {{ gap: 0.6rem; }}
    }}
</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
"""

st.markdown(custom_css, unsafe_allow_html=True)

# ==================== DATA LINK UNTUK 4 BAGIAN ====================
# 1. Konservasi Ekosistem
konservasi_ekosistem = [
    {"label": "LokaBeOn", "icon": "fa-solid fa-map", "url": "https://webgislokabeon2026.nonha-sdoc.workers.dev/"},
    {"label": "Anambas Dalam Data", "icon": "fa-solid fa-chart-line", "url": "https://linktr.ee/KonservasiAnambas"},
    {"label": "Pieh Dalam Data", "icon": "fa-solid fa-chart-simple", "url": "https://linktr.ee/KonsevasiPulauPieh"},
    {"label": "Landing Page KK Anambas", "icon": "fa-solid fa-leaf", "url": "https://sites.google.com/view/twp-anambas/home"},
    {"label": "Landing Page Pieh", "icon": "fa-solid fa-leaf", "url": "https://sites.google.com/view/twppieh"},
]

# 2. Konservasi Jenis Ikan Dilindungi
konservasi_ikan = [
    {"label": "ResPat BUAYA", "icon": "fa-solid fa-tree", "url": "https://lookerstudio.google.com/s/l64DGDDeTIQ"},
    {"label": "Kawasan Konservasi", "icon": "fa-solid fa-water", "url": "https://example.com/kkp"},
    {"label": "Jenis Ikan", "icon": "fa-solid fa-fish", "url": "https://example.com/jenis-ikan"},
    {"label": "PNBP", "icon": "fa-solid fa-hand-holding-heart", "url": "https://example.com/pnbp"},
]

# 3. Sumberdaya Kelautan
sumberdaya = [
    {"label": "Pulau-pulau kecil", "icon": "fa-solid fa-island-tropical", "url": "https://example.com/pulau-kecil"},
    {"label": "ALSE (Alat Serbu)", "icon": "fa-solid fa-fishing-rod", "url": "https://example.com/alse"},
    {"label": "Jasa Bahari", "icon": "fa-solid fa-ship", "url": "https://example.com/jasa-bahari"},
]

# 4. Dukungan Manajerial
dukungan = [
    {"label": "Sipintar", "icon": "fa-solid fa-laptop-code", "url": "https://sites.google.com/view/sipintar-lkkpn/home"},
    {"label": "PPID LPK", "icon": "fa-solid fa-folder-open", "url": "https://ppid.kkp.go.id/upt/loka-pengelolaan-kelautan-pekanbaru/"},
    {"label": "SIPPN", "icon": "fa-solid fa-network-wired", "url": "https://sippn.menpan.go.id/instansi/loka-pengelolaan-kelautan-pekanbaru-172582"},
    {"label": "VERIPERJAKE", "icon": "fa-solid fa-check-double", "url": "https://example.com/veriperjake"},
]

# ==================== DATA CAROUSEL GAMBAR KANTOR ====================
# Ganti dengan path gambar kantor anda (jpeg/png). Bisa juga URL gambar.
office_images = [
    "kantor1.jpg",   # Ganti dengan file gambar yang ada
    "kantor2.jpg",
    "kantor3.jpg",
    "kantor4.jpg"
]
# Jika file tidak ada, fallback ke gambar placeholder dari unsplash
for i, img in enumerate(office_images):
    if not Path(img).exists():
        office_images[i] = "https://images.unsplash.com/photo-1563533957184-4f20c01a7c3d?w=600&h=400&fit=crop"

# ==================== FUNGSI AMBIL DATA RUNNING TEXT DARI GOOGLE SHEETS ====================
@st.cache_data(ttl=60)  # cache 60 detik, update periodik
def get_running_text_from_sheets(sheet_url):
    """
    Ambil teks berjalan dari Google Sheet (publikasikan sebagai CSV).
    Contoh URL: https://docs.google.com/spreadsheets/d/e/2PACX-.../pub?output=csv
    Kolom pertama baris pertama dianggap sebagai teks marquee.
    """
    try:
        df = pd.read_csv(sheet_url, nrows=1)
        if not df.empty:
            first_cell = str(df.iloc[0,0])
            return first_cell.strip()
        else:
            return "Selamat datang di Dashboard Loka Pengelolaan Kelautan Pekanbaru | Konservasi & Dukungan Manajemen Terpadu"
    except Exception as e:
        st.error(f"Gagal membaca Google Sheets: {e}")
        return "📢 Informasi terkini akan muncul di sini. Pastikan URL Google Sheet sudah benar."

# ==================== SETTING GOOGLE SHEETS (GANTI DENGAN LINK PUBLIK ANDA) ====================
# Cara: Buka Google Sheet -> File -> Bagikan -> Publikasikan ke web (CSV)
# Masukkan URL lengkap di bawah
GOOGLE_SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT9Hhx8VzF9Wx12pP7dX6qZcV4yLrX1sLkQ/pub?output=csv"  # GANTI!

running_text = get_running_text_from_sheets(GOOGLE_SHEET_CSV_URL)

# ==================== TAMPILAN UTAMA ====================
# HEADER
st.markdown("""
    <div class="dashboard-title">
        <h1>Loka Pengelolaan Kelautan Pekanbaru</h1>
        <div class="dashboard-sub">🌊 Integrasi Data Konservasi, Sumberdaya Kelautan & Dukungan Manajemen</div>
    </div>
""", unsafe_allow_html=True)

# BAGIAN BODY: 1/3 CAROUSEL + 2/3 GRID 4 BAGIAN
left_col, right_col = st.columns([1, 2], gap="large")

# ---------- KIRI: CAROUSEL GAMBAR KANTOR ----------
with left_col:
    with st.container():
        st.markdown('<div class="carousel-card">', unsafe_allow_html=True)
        
        # Inisialisasi session state untuk index carousel
        if "carousel_idx" not in st.session_state:
            st.session_state.carousel_idx = 0
        
        # Tombol kiri/kanan
        col_prev, col_img, col_next = st.columns([1, 5, 1])
        with col_prev:
            if st.button("◀", key="prev", use_container_width=True):
                st.session_state.carousel_idx = (st.session_state.carousel_idx - 1) % len(office_images)
                st.rerun()
        with col_next:
            if st.button("▶", key="next", use_container_width=True):
                st.session_state.carousel_idx = (st.session_state.carousel_idx + 1) % len(office_images)
                st.rerun()
        
        # Tampilkan gambar
        current_img = office_images[st.session_state.carousel_idx]
        try:
            if current_img.startswith("http"):
                st.image(current_img, use_container_width=True, output_format="JPEG")
            else:
                if Path(current_img).exists():
                    st.image(current_img, use_container_width=True)
                else:
                    st.image("https://placehold.co/600x400/1e2a3a/D4AF37?text=Kantor+Loka", use_container_width=True)
        except:
            st.image("https://placehold.co/600x400/1e2a3a/D4AF37?text=Gambar+Kantor", use_container_width=True)
        
        st.caption(f"📍 Kantor Loka Pengelolaan Kelautan Pekanbaru • {st.session_state.carousel_idx+1}/{len(office_images)}")
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- KANAN: GRID 4 BAGIAN (2x2) ----------
with right_col:
    # Menggunakan grid CSS yang sudah didefinisikan
    st.markdown('<div class="section-grid">', unsafe_allow_html=True)
    
    # Bagian 1: Konservasi Ekosistem
    st.markdown('<div class="grid-card">', unsafe_allow_html=True)
    st.markdown('<div class="grid-title">🌿 Konservasi Ekosistem</div>', unsafe_allow_html=True)
    for item in konservasi_ekosistem:
        st.markdown(f'<a href="{item["url"]}" target="_blank" class="list-link"><i class="{item["icon"]}"></i> {item["label"]}</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Bagian 2: Konservasi Jenis Ikan Dilindungi
    st.markdown('<div class="grid-card">', unsafe_allow_html=True)
    st.markdown('<div class="grid-title">🐟 Konservasi Ikan Dilindungi</div>', unsafe_allow_html=True)
    for item in konservasi_ikan:
        st.markdown(f'<a href="{item["url"]}" target="_blank" class="list-link"><i class="{item["icon"]}"></i> {item["label"]}</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Bagian 3: Sumberdaya Kelautan
    st.markdown('<div class="grid-card">', unsafe_allow_html=True)
    st.markdown('<div class="grid-title">⛵ Sumberdaya Kelautan</div>', unsafe_allow_html=True)
    for item in sumberdaya:
        st.markdown(f'<a href="{item["url"]}" target="_blank" class="list-link"><i class="{item["icon"]}"></i> {item["label"]}</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Bagian 4: Dukungan Manajerial
    st.markdown('<div class="grid-card">', unsafe_allow_html=True)
    st.markdown('<div class="grid-title">📋 Dukungan Manajerial</div>', unsafe_allow_html=True)
    for item in dukungan:
        st.markdown(f'<a href="{item["url"]}" target="_blank" class="list-link"><i class="{item["icon"]}"></i> {item["label"]}</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== RUNNING TEXT MARQUEE (REALTIME DARI SPREADSHEET) ====================
# Gunakan komponen HTML marquee agar berjalan mulus
marquee_html = f"""
<div class="marquee-container">
    <div class="marquee">
        <span>{running_text} &nbsp;&nbsp; ✦ &nbsp;&nbsp; {running_text} &nbsp;&nbsp; ✦ &nbsp;&nbsp; {running_text}</span>
    </div>
</div>
"""
st.markdown(marquee_html, unsafe_allow_html=True)

# Tombol refresh manual untuk running text (jika ingin update segera)
if st.button("🔄 Refresh Informasi Terkini", key="refresh_marquee", help="Ambil data terbaru dari Google Sheets"):
    st.cache_data.clear()
    st.rerun()

# ==================== FOOTER ====================
st.markdown("""
    <div class="footer">
        © Loka Pengelolaan Kelautan Pekanbaru — Data tautan dapat disesuaikan di kode sumber. 
        <br>Running text diambil real-time dari Google Spreadsheet.
    </div>
""", unsafe_allow_html=True)

# Petunjuk singkat di sidebar (tidak mengganggu)
with st.sidebar:
    st.markdown("### ⚙️ Panduan Singkat")
    st.markdown("**Ganti Gambar Kantor:**\n - Letakkan file `kantor1.jpg` s.d `kantor4.jpg` di folder yang sama, atau ubah daftar `office_images`.\n\n**Ganti Running Text:**\n - Publikasikan Google Sheet ke web (CSV) dan ubah variabel `GOOGLE_SHEET_CSV_URL` di kode.\n\n**Sesuaikan Link:**\n - Edit dictionary di bagian `DATA LINK`.")
