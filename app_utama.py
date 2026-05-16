import streamlit as st
import base64
from pathlib import Path

# ==================== KONFIGURASI HALAMAN ====================
st.set_page_config(
    page_title="Loka Dalam Genggaman",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== MEMBACA GAMBAR BACKGROUND (BASE64) ====================
background_image_path = Path("MRAP12.jpg")
background_base64 = ""

if background_image_path.exists():
    with open(background_image_path, "rb") as img_file:
        background_base64 = base64.b64encode(img_file.read()).decode()
else:
    st.warning("File MRAP12.jpg tidak ditemukan. Gunakan background default.")

# ==================== CSS KUSTOM (dengan blur keseluruhan background) ====================
if background_base64:
    bg_style = f"url('data:image/jpeg;base64,{background_base64}')"
else:
    bg_style = "linear-gradient(135deg, #0f2b3d, #1a4a6f)"

custom_css = f"""
<style>
    /* Reset & Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,600&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
    }}
    
    /* ----- BACKGROUND GAMBAR dengan BLUR TOTAL (pseudo-element) ----- */
    .stApp {{
        position: relative;
        background: {bg_style} no-repeat center center fixed;
        background-size: cover;
    }}
    
    /* Lapisan blur dan redup untuk background saja */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        backdrop-filter: blur(12px);   /* tingkat blur, bisa disesuaikan */
        background: rgba(0, 0, 0, 0.4); /* gelap transparan untuk efek mewah */
        z-index: 0;
        pointer-events: none;           /* agar tidak mengganggu klik */
    }}
    
    /* Semua konten utama harus berada di atas pseudo-element */
    .main > div {{
        position: relative;
        z-index: 1;
    }}
    
    /* Hapus overlay lama di .main (sudah tidak perlu) */
    /* .main { background: rgba(0, 0, 0, 0.5); backdrop-filter: blur(8px); } */
    
    /* Judul utama - mewah */
    .dashboard-title {{
        text-align: center;
        padding: 1rem 0 1rem 0;
        margin-bottom: 1.5rem;
    }}
    .dashboard-title h1 {{
        font-size: 2.4rem;
        font-weight: 700;
        background: linear-gradient(135deg, #F9D976, #F39F86, #D4AF37);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        text-shadow: 2px 2px 12px rgba(0,0,0,0.3);
        letter-spacing: -0.3px;
    }}
    .dashboard-title p {{
        color: #f0f0f0;
        font-size: 0.95rem;
        margin-top: -0.5rem;
        font-weight: 500;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.5);
    }}
    
    /* Card mewah transparan */
    .section-card {{
        background: rgba(20, 20, 30, 0.75);
        backdrop-filter: blur(8px);
        border-radius: 32px;
        padding: 1.2rem 1rem;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2), 0 0 0 1px rgba(212,175,55,0.2);
        height: 100%;
    }}
    
    .col-title {{
        font-size: 1.3rem;
        font-weight: 600;
        text-align: center;
        margin-bottom: 1.8rem;
        padding-bottom: 0.6rem;
        border-bottom: 2px solid #D4AF37;
        display: inline-block;
        width: auto;
        color: #F5E7B2;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }}
    
    .icon-card {{
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(4px);
        border-radius: 24px;
        padding: 1rem 0.5rem;
        margin: 0.8rem 0;
        text-align: center;
        transition: all 0.25s ease;
        border: 1px solid rgba(212,175,55,0.3);
        cursor: pointer;
    }}
    .icon-card:hover {{
        transform: translateY(-4px);
        background: rgba(212,175,55,0.2);
        border-color: #D4AF37;
    }}
    .icon-card a {{
        text-decoration: none;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0.7rem;
        color: #FFFFFF;
    }}
    .icon-card i {{
        font-size: 2.6rem;
        color: #D4AF37;
        transition: transform 0.2s;
        text-shadow: 0 0 5px rgba(0,0,0,0.5);
    }}
    .icon-card:hover i {{
        transform: scale(1.05);
        color: #F3D572;
    }}
    .icon-label {{
        font-weight: 500;
        font-size: 0.85rem;
        letter-spacing: 0.3px;
        color: #FAF7F0;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }}
    
    @media (max-width: 768px) {{
        .icon-card i {{ font-size: 2rem; }}
        .icon-label {{ font-size: 0.75rem; }}
        .col-title {{ font-size: 1.1rem; }}
    }}
    
    /* Media sosial */
    .social-container {{
        display: flex;
        justify-content: flex-end;
        gap: 1.2rem;
        margin: 2rem 1rem 1rem 1rem;
        flex-wrap: wrap;
    }}
    .social-icon {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 52px;
        height: 52px;
        border-radius: 50%;
        background: rgba(0,0,0,0.6);
        backdrop-filter: blur(4px);
        color: #D4AF37;
        text-decoration: none;
        font-size: 1.6rem;
        transition: all 0.25s ease;
        border: 1px solid rgba(212,175,55,0.5);
    }}
    .social-icon:hover {{
        transform: translateY(-4px);
        background: #D4AF37;
        color: #1e2a3a;
    }}
    .social-icon:hover::after {{
        content: attr(title);
        position: absolute;
        bottom: -34px;
        left: 50%;
        transform: translateX(-50%);
        background: #0f2b3d;
        color: #D4AF37;
        font-size: 0.75rem;
        padding: 4px 10px;
        border-radius: 30px;
        white-space: nowrap;
        font-family: 'Inter', sans-serif;
        pointer-events: none;
    }}
    .social-icon {{
        position: relative;
    }}
    @media (max-width: 768px) {{
        .social-icon {{ width: 44px; height: 44px; font-size: 1.4rem; }}
        .social-container {{ justify-content: center; }}
    }}
    
    .footer {{
        text-align: center;
        margin-top: 1rem;
        padding: 1rem;
        font-size: 0.75rem;
        color: #DDD;
        border-top: 1px solid rgba(212,175,55,0.4);
        background: rgba(0,0,0,0.3);
        border-radius: 20px;
        backdrop-filter: blur(4px);
    }}
</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
"""

st.markdown(custom_css, unsafe_allow_html=True)

# ==================== DATA IKON ====================
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
    {"label": "Jenis Ikan", "icon": "fa-solid fa-water", "url": "https://example.com/kkp"},
    {"label": "Pelayanan LPK Pekanbaru", "icon": "fa-solid fa-fish", "url": "https://dashboardapp-gwxpaouny5c3znvdudekvl.streamlit.app/"},
    {"label": "PNBP", "icon": "fa-solid fa-hand-holding-heart", "url": "https://example.com/berkelanjutan"},
    {"label": "SeaPark", "icon": "fa-solid fa-map-location-dot", "url": "https://seapark.kkp.go.id/"},
    {"label": "eSAJI", "icon": "fa-solid fa-map-location-dot", "url": "https://saji.kkp.go.id/"},
    {"label": "eSultan.2.0", "icon": "fa-solid fa-map-location-dot", "url": "https://sites.google.com/view/pelayananlpkpekanbaru/pelayanan-jenis-ikan/non-esaji"},
    {"label": "SOP Pelayanan", "icon": "fa-solid fa-map-location-dot", "url": "https://example.com/zona"},
]

kolom3_data = [
    {"label": "Sipintar", "icon": "fa-solid fa-ship", "url": "https://sites.google.com/view/sipintar-lkkpn/home"},
    {"label": "PPID LPK", "icon": "fa-solid fa-eye", "url": "https://ppid.kkp.go.id/upt/loka-pengelolaan-kelautan-pekanbaru/"},
    {"label": "SIPPN", "icon": "fa-solid fa-eye", "url": "https://sippn.menpan.go.id/instansi/loka-pengelolaan-kelautan-pekanbaru-172582"},
    {"label": "Koordinasi Instansi", "icon": "fa-solid fa-handshake", "url": "https://example.com/koordinasi"},
    {"label": "Sistem Pelaporan", "icon": "fa-solid fa-file-alt", "url": "https://example.com/pelaporan"},
    {"label": "Emergency Response", "icon": "fa-solid fa-life-ring", "url": "https://example.com/emergency"},
]

social_media = [
    {"label": "Hotline WA", "icon": "fab fa-whatsapp", "url": "https://wa.me/628116666642"},
    {"label": "Instagram", "icon": "fab fa-instagram", "url": "https://www.instagram.com/lokapkpekanbaru?igsh=YTN3OGRvd3ZrZXF1"},
    {"label": "Facebook", "icon": "fab fa-facebook-f", "url": "https://www.facebook.com/LPKPekanbaru.477456"},
    {"label": "TikTok", "icon": "fab fa-tiktok", "url": "https://www.tiktok.com/@lokapkpekanbaru?_r=1&_t=ZS-966OrjUjiPx"},
    {"label": "Twitter", "icon": "fab fa-twitter", "url": "https://x.com/lokapkpekanbaru?s=21"},
    {"label": "YouTube", "icon": "fab fa-youtube", "url": "https://youtube.com/@lokapkpekanbaru?si=1n9Cvsn5Ic2BDORL"},
    {"label": "Website", "icon": "fas fa-globe", "url": "https://ppid.kkp.go.id/upt/loka-pengelolaan-kelautan-pekanbaru/"},
]

# ==================== FUNGSI RENDER ====================
def render_column(icon_list, column_title):
    st.markdown(f"""
        <div style="text-align: center;">
            <div class="col-title">{column_title}</div>
        </div>
    """, unsafe_allow_html=True)
    for item in icon_list:
        card_html = f"""
        <div class="icon-card">
            <a href="{item['url']}" target="_blank" rel="noopener noreferrer">
                <i class="{item['icon']}"></i>
                <span class="icon-label">{item['label']}</span>
            </a>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)

def render_social_media(social_list):
    social_list_reversed = list(reversed(social_list))
    html_parts = ['<div class="social-container">']
    for soc in social_list_reversed:
        url = soc["url"].replace('"', '&quot;')
        html_parts.append(f'''
            <a href="{url}" target="_blank" rel="noopener noreferrer" class="social-icon" title="{soc['label']}">
                <i class="{soc['icon']}"></i>
            </a>
        ''')
    html_parts.append('</div>')
    st.markdown(''.join(html_parts), unsafe_allow_html=True)

# ==================== TAMPILAN UTAMA ====================
st.markdown("""
    <div class="dashboard-title">
        <h1>🌊 Loka Pengelolaan Kelautan Pekanbaru</h1>
        <p>Dashboard terintegrasi untuk perlindungan, pemanfaatan, dan dukungan manajemen</p>
    </div>
""", unsafe_allow_html=True)

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

render_social_media(social_media)

st.markdown("""
    <div class="footer">
        Dashboard Konservasi & Dukman — Data tautan dapat diperbarui di file app.py (bagian DATA IKON dan DATA MEDIA SOSIAL)
    </div>
""", unsafe_allow_html=True)
