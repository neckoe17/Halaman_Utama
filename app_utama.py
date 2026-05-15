import streamlit as st

# ==================== KONFIGURASI HALAMAN ====================
st.set_page_config(
    page_title="Loka Dalam Genggaman",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== CSS KUSTOM (ELEGAN & MINIMALIS) ====================
custom_css = """
<style>
    /* Reset & Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Background utama - putih bersih dengan aksen gold */
    .main {
        background: linear-gradient(135deg, #f9fafb 0%, #ffffff 100%);
    }
    
    /* Judul utama */
    .dashboard-title {
        text-align: center;
        padding: 1rem 0 1rem 0;
        margin-bottom: 1.5rem;
    }
    .dashboard-title h1 {
        font-size: 2.2rem;
        font-weight: 600;
        background: linear-gradient(120deg, #1e2a3a, #2c3e50);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        letter-spacing: -0.5px;
    }
    .dashboard-title p {
        color: #5d6e7e;
        font-size: 0.9rem;
        margin-top: -0.5rem;
    }
    
    /* Container kolom - luxury card effect */
    .section-card {
        background: rgba(255,255,255,0.85);
        backdrop-filter: blur(2px);
        border-radius: 32px;
        padding: 1.2rem 1rem;
        box-shadow: 0 8px 20px rgba(0,0,0,0.02), 0 2px 6px rgba(0,0,0,0.03);
        transition: all 0.2s ease;
        border: 1px solid rgba(212, 175, 55, 0.15);
        height: 100%;
    }
    
    /* Judul kolom */
    .col-title {
        font-size: 1.3rem;
        font-weight: 600;
        text-align: center;
        margin-bottom: 1.8rem;
        padding-bottom: 0.6rem;
        border-bottom: 2px solid #d4af37;
        display: inline-block;
        width: auto;
        color: #2c3e4e;
        letter-spacing: -0.3px;
    }
    
    /* Kartu ikon */
    .icon-card {
        background: white;
        border-radius: 24px;
        padding: 1rem 0.5rem;
        margin: 0.8rem 0;
        text-align: center;
        transition: all 0.25s ease;
        box-shadow: 0 2px 8px rgba(0,0,0,0.02);
        border: 1px solid #eef2f5;
        cursor: pointer;
    }
    .icon-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 15px 30px -12px rgba(0,0,0,0.1);
        border-color: rgba(212, 175, 55, 0.4);
        background: #fefef7;
    }
    
    /* Link (seluruh area kartu) */
    .icon-card a {
        text-decoration: none;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0.7rem;
        color: #2c3e50;
    }
    
    /* Gaya ikon */
    .icon-card i {
        font-size: 2.6rem;
        color: #d4af37;
        transition: transform 0.2s;
    }
    .icon-card:hover i {
        transform: scale(1.05);
        color: #b88d2c;
    }
    
    /* Label teks */
    .icon-label {
        font-weight: 500;
        font-size: 0.85rem;
        letter-spacing: 0.3px;
        color: #3a5468;
    }
    
    /* Responsive: kolom Streamlit otomatis */
    @media (max-width: 768px) {
        .icon-card i { font-size: 2rem; }
        .icon-label { font-size: 0.75rem; }
        .col-title { font-size: 1.1rem; }
    }
    
    /* Footer minimal */
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        font-size: 0.75rem;
        color: #8a9aa8;
        border-top: 1px solid #e9ecef;
    }
</style>

<!-- Font Awesome 6 (Free) -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
"""

st.markdown(custom_css, unsafe_allow_html=True)

# ==================== DATA IKON (MUDAH DIUPDATE) ====================
# Struktur: setiap kolom berisi list of dict
# Setiap dict: {"label": "Nama Ikon", "icon": "fa-solid fa-...", "url": "https://..."}

kolom1_data = [
    {"label": "ResPat BUAYA", "icon": "fa-solid fa-tree", "url": "https://lookerstudio.google.com/s/l64DGDDeTIQ"},
    {"label": "LokaBeOn", "icon": "fa-solid fa-tree", "url": "https://webgislokabeon2026.nonha-sdoc.workers.dev/"},
    {"label": "Anambas Dalam Data", "icon": "fa-solid fa-leaf", "url": "https://linktr.ee/KonservasiAnambas"},
    {"label": "Pieh Dalam Data", "icon": "fa-solid fa-gavel", "url": "https://linktr.ee/KonsevasiPulauPieh"},
    {"label": "Landing Page KK Anambas", "icon": "fa-solid fa-gavel", "url": "https://sites.google.com/view/twp-anambas/home"},
    {"label": "Landing Page KK Pieh", "icon": "fa-solid fa-gavel", "url": "https://sites.google.com/view/twppieh"},
]

kolom2_data = [
    {"label": "Kawasan Konservasi", "icon": "fa-solid fa-water", "url": "https://example.com/kkp"},
    {"label": "Jenis Ikan", "icon": "fa-solid fa-fish", "url": "https://dashboardapp-gwxpaouny5c3znvdudekvl.streamlit.app/"},
    {"label": "PNBP", "icon": "fa-solid fa-hand-holding-heart", "url": "https://example.com/berkelanjutan"},
    {"label": "SeaPark", "icon": "fa-solid fa-map-location-dot", "url": "https://seapark.kkp.go.id/"},
    {"label": "eSAJI", "icon": "fa-solid fa-map-location-dot", "url": "https://saji.kkp.go.id/"},
    {"label": "eSultan.2.0", "icon": "fa-solid fa-map-location-dot", "url": "https://sites.google.com/view/pelayananlpkpekanbaru/pelayanan-jenis-ikan/non-esaji"},
    {"label": "SOP Pelayanan", "icon": "fa-solid fa-map-location-dot", "url": "https://example.com/zona"},
]

kolom3_data = [
    {"label": "Sipintar", "icon": "fa-solid fa-ship", "url": "https://sites.google.com/view/sipintar-lkkpn/home"},
    {"label": "PPID LPK", "icon": "fa-solid fa-eye", "url": "https://ppid.kkp.go.id/upt/loka-pengelolaan-kelautan-pekanbaru/"},
    {"label": "SIPPN", "icon": "fa-solid fa-radar", "url": "https://sippn.menpan.go.id/instansi/loka-pengelolaan-kelautan-pekanbaru-172582"},
    {"label": "Koordinasi Instansi", "icon": "fa-solid fa-handshake", "url": "https://example.com/koordinasi"},
    {"label": "Sistem Pelaporan", "icon": "fa-solid fa-file-alt", "url": "https://example.com/pelaporan"},
    {"label": "Emergency Response", "icon": "fa-solid fa-life-ring", "url": "https://example.com/emergency"},
]

# ==================== FUNGSI RENDER KOLOM ====================
def render_column(icon_list, column_title):
    """Menerima list ikon dan judul kolom, lalu render HTML/CSS melalui markdown"""
    # Judul kolom dengan style kustom
    st.markdown(f"""
        <div style="text-align: center;">
            <div class="col-title">{column_title}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Looping setiap ikon
    for item in icon_list:
        label = item["label"]
        icon_class = item["icon"]
        url = item["url"]
        
        card_html = f"""
        <div class="icon-card">
            <a href="{url}" target="_blank" rel="noopener noreferrer">
                <i class="{icon_class}"></i>
                <span class="icon-label">{label}</span>
            </a>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)

# ==================== TAMPILAN UTAMA ====================
# Header
st.markdown("""
    <div class="dashboard-title">
        <h1>🌊 Loka Pengelolaan Kelautan Pekanbaru</h1>
        <p>Dashboard terintegrasi untuk perlindungan, pemanfaatan, dan dukungan manajemen</p>
    </div>
""", unsafe_allow_html=True)

# Membuat 3 kolom dengan rasio lebar seimbang
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    with st.container():
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        render_column(kolom1_data, "🛡️ Perlindungan & Pelestarian")
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        render_column(kolom2_data, "🐟 Pemanfaatan & Jenis Ikan")
        st.markdown('</div>', unsafe_allow_html=True)

with col3:
    with st.container():
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        render_column(kolom3_data, "⚙️ Dukman (Dukungan Manajemen)")
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        Dashboard Konservasi & Dukman — Data tautan dapat diperbarui di file app.py (bagian DATA IKON)
    </div>
""", unsafe_allow_html=True)
