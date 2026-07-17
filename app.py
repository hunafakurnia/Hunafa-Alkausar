import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os

# =====================================
# KONFIGURASI HALAMAN
# =====================================
st.set_page_config(
    page_title="MindCare Dashboard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)
# =====================================
# CSS
# =====================================

st.markdown("""
<style>

.main{
    background-color:#F8F9FA;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

h1,h2,h3{
    color:#0F172A;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:15px;
    padding:15px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.15);
}

.stButton > button{
    width:100%;
    background:#2563EB;
    color:white;
    border:none;
    border-radius:10px;
    height:45px;
    font-size:17px;
}

.stButton > button:hover{
    background:#1D4ED8;
}

</style>
""", unsafe_allow_html=True)
# =====================================
# SESSION STATE
# =====================================

if "hasil" not in st.session_state:
    st.session_state.hasil = []
# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("🧠 MindCare")

menu = st.sidebar.radio(
    "Pilih Menu",
    [
        "🏠 Home",
        "📚 Edukasi",
        "📝 Self Check",
        "📊 Dashboard"
    ]
)
# =====================================
# HOME
# =====================================

if menu == "🏠 Home":

    st.title("🧠 MindCare Dashboard")

    st.write("""
    Selamat datang di **MindCare**.

    Aplikasi ini membantu pengguna melakukan
    pemeriksaan kondisi mental secara sederhana.

    **Fitur**
    - Edukasi Mental Health
    - Self Check
    - Dashboard
    - Grafik Interaktif
    """)

    col1,col2 = st.columns([2,1])

    with col1:

        st.success("""
        Kesehatan mental sama pentingnya
        dengan kesehatan fisik.
        """)

    with col2:

        try:
            st.image("yamal.jpg", use_container_width=True)

        except:
            st.info("Tambahkan gambar yamal.jpg")
# =====================================
# HALAMAN EDUKASI
# =====================================

elif menu == "📚 Edukasi":

    st.title("📚 Edukasi Kesehatan Mental")

    st.info("""
    **Apa itu kesehatan mental?**

    Kesehatan mental adalah kondisi ketika seseorang mampu
    mengelola emosi, menghadapi tekanan hidup, bekerja secara
    produktif, dan berinteraksi dengan orang lain secara sehat.
    """)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("😊 Cara Menjaga Kesehatan Mental")

        st.success("""
        ✔ Tidur 7–8 jam setiap malam

        ✔ Olahraga minimal 30 menit

        ✔ Konsumsi makanan bergizi

        ✔ Luangkan waktu bersama keluarga

        ✔ Kurangi penggunaan media sosial

        ✔ Lakukan hobi yang disukai

        ✔ Bersyukur setiap hari

        ✔ Meditasi atau relaksasi
        """)

    with col2:

        st.subheader("⚠ Tanda-Tanda Gangguan Mental")

        st.warning("""
        • Sulit tidur

        • Mudah marah

        • Sulit berkonsentrasi

        • Kehilangan semangat

        • Merasa cemas berlebihan

        • Menarik diri dari lingkungan

        • Nafsu makan berubah

        • Merasa putus asa terus-menerus
        """)

    st.divider()

    st.subheader("💡 Tips Mengurangi Stres")

    tips = [
        "🧘 Meditasi selama 10–15 menit.",
        "🚶 Berjalan santai di pagi atau sore hari.",
        "🎵 Dengarkan musik yang menenangkan.",
        "📖 Membaca buku favorit.",
        "📵 Batasi penggunaan media sosial.",
        "☕ Istirahat sejenak saat bekerja atau belajar.",
        "👨‍👩‍👧 Habiskan waktu bersama keluarga atau teman.",
        "🌳 Luangkan waktu di alam terbuka."
    ]

    for tip in tips:
        st.write(tip)

    st.divider()

    st.subheader("🌈 Kutipan Motivasi")

    st.success(
        "\"Merawat kesehatan mental adalah bentuk kepedulian terhadap diri sendiri. "
        "Meminta bantuan saat dibutuhkan adalah tindakan yang berani.\""
    )
# =====================================
# SELF CHECK
# =====================================

elif menu == "📝 Self Check":

    st.title("📝 Self Check Kesehatan Mental")

    st.write("Jawablah setiap pertanyaan sesuai kondisi Anda selama **2 minggu terakhir**.")

    st.divider()

    nama = st.text_input("👤 Nama")

    umur = st.number_input(
        "Umur",
        min_value=10,
        max_value=100,
        value=20
    )

    jenis_kelamin = st.selectbox(
        "Jenis Kelamin",
        [
            "Laki-laki",
            "Perempuan"
        ]
    )

    st.divider()

    st.subheader("Jawab Pertanyaan Berikut")

    st.caption("0 = Tidak Pernah | 1 = Jarang | 2 = Kadang | 3 = Sering | 4 = Sangat Sering")

    q1 = st.slider("1. Saya merasa sedih.",0,4,0)
    q2 = st.slider("2. Saya merasa cemas.",0,4,0)
    q3 = st.slider("3. Saya sulit tidur.",0,4,0)
    q4 = st.slider("4. Saya mudah marah.",0,4,0)
    q5 = st.slider("5. Saya sulit berkonsentrasi.",0,4,0)
    q6 = st.slider("6. Saya kehilangan semangat.",0,4,0)
    q7 = st.slider("7. Saya merasa lelah sepanjang hari.",0,4,0)
    q8 = st.slider("8. Saya kehilangan minat melakukan aktivitas.",0,4,0)
    q9 = st.slider("9. Saya merasa kesepian.",0,4,0)
    q10 = st.slider("10. Saya merasa kewalahan menghadapi masalah.",0,4,0)

    skor = (
        q1+q2+q3+q4+q5+
        q6+q7+q8+q9+q10
    )

    st.divider()

    if st.button("💾 Simpan Hasil"):

        if nama == "":
            st.warning("Silakan masukkan nama terlebih dahulu.")

        else:

            if skor <= 10:

                kategori = "😊 Baik"

                warna = "success"

                pesan = """
Kondisi Anda terlihat cukup baik.

Tetap jaga pola tidur, olahraga teratur,
makan bergizi, dan luangkan waktu untuk beristirahat.
"""

            elif skor <= 20:

                kategori = "🙂 Ringan"

                warna = "info"

                pesan = """
Anda mulai menunjukkan beberapa tanda stres.

Cobalah mengurangi aktivitas yang melelahkan,
istirahat yang cukup, dan berbicara dengan orang yang dipercaya.
"""

            elif skor <= 30:

                kategori = "😟 Sedang"

                warna = "warning"

                pesan = """
Anda mengalami tingkat stres yang cukup tinggi.

Pertimbangkan untuk berkonsultasi dengan guru BK,
konselor, psikolog, atau tenaga profesional bila kondisi ini berlanjut.
"""

            else:

                kategori = "🔴 Tinggi"

                warna = "error"

                pesan = """
Hasil self-check menunjukkan tingkat stres yang tinggi.

Ini bukan diagnosis medis.

Apabila kondisi ini berlangsung lama atau mengganggu aktivitas sehari-hari,
pertimbangkan untuk berkonsultasi dengan psikolog atau psikiater.

Jika Anda merasa tidak aman atau memiliki keinginan untuk menyakiti diri sendiri,
segera hubungi orang yang Anda percaya atau layanan darurat di wilayah Anda.
"""

            data = {
                "Tanggal": datetime.now().strftime("%d-%m-%Y"),
                "Nama": nama,
                "Umur": umur,
                "Jenis Kelamin": jenis_kelamin,
                "Skor": skor,
                "Kategori": kategori
            }

            st.session_state.hasil.append(data)

            st.success("Data berhasil disimpan.")

            st.divider()

            st.subheader("📋 Hasil Pemeriksaan")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Skor", skor)

            with col2:
                st.metric("Kategori", kategori)

            if warna == "success":
                st.success(pesan)

            elif warna == "info":
                st.info(pesan)

            elif warna == "warning":
                st.warning(pesan)

            else:
                st.error(pesan)
# =====================================
# DASHBOARD
# =====================================

elif menu == "📊 Dashboard":

    st.title("📊 Dashboard MindCare")

    # ==========================
    # Belum ada data
    # ==========================
    if len(st.session_state.hasil) == 0:

        st.warning("Belum ada data pemeriksaan.")

    else:

        # Membuat DataFrame
        df = pd.DataFrame(st.session_state.hasil)

        # ==========================
        # Statistik
        # ==========================

        total = len(df)
        rata = round(df["Skor"].mean(), 2)
        skor_tertinggi = df["Skor"].max()
        skor_terendah = df["Skor"].min()

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Pemeriksaan", total)
        col2.metric("Rata-rata Skor", rata)
        col3.metric("Skor Tertinggi", skor_tertinggi)
        col4.metric("Skor Terendah", skor_terendah)

        st.divider()

        # ==========================
        # Filter Nama
        # ==========================

        nama = st.selectbox(
            "Filter Nama",
            ["Semua"] + list(df["Nama"].unique())
        )

        if nama != "Semua":
            df = df[df["Nama"] == nama]

        st.dataframe(df, use_container_width=True)

        st.divider()

        # ==========================
        # Grafik
        # ==========================

        col1, col2 = st.columns(2)

        with col1:

            fig1 = px.bar(
                df,
                x="Nama",
                y="Skor",
                color="Kategori",
                title="Skor Setiap Pengguna",
                text="Skor"
            )

            fig1.update_layout(
                template="plotly_white"
            )

            st.plotly_chart(fig1, use_container_width=True)

        with col2:

            fig2 = px.pie(
                df,
                names="Kategori",
                title="Persentase Kategori"
            )

            st.plotly_chart(fig2, use_container_width=True)

        st.divider()

        # ==========================
        # Grafik Histogram
        # ==========================

        fig3 = px.histogram(
            df,
            x="Skor",
            nbins=10,
            color="Kategori",
            title="Distribusi Skor"
        )

        st.plotly_chart(fig3, use_container_width=True)

        st.divider()

        # ==========================
        # Download CSV
        # ==========================

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name="hasil_mindcare.csv",
            mime="text/csv"
        )

        # ==========================
        # Hapus Data
        # ==========================

        if st.button("🗑️ Hapus Semua Data"):

            st.session_state.hasil = []

            st.success("Semua data berhasil dihapus.")

            st.rerun()
# =====================================
# FUNGSI PENYIMPANAN DATA
# =====================================

FILE_DATA = "data_mindcare.csv"


def simpan_data(data):

    df_baru = pd.DataFrame([data])

    if os.path.exists(FILE_DATA):

        df_lama = pd.read_csv(FILE_DATA)

        df = pd.concat(
            [df_lama, df_baru],
            ignore_index=True
        )

    else:

        df = df_baru


    df.to_csv(
        FILE_DATA,
        index=False
    )


def baca_data():

    if os.path.exists(FILE_DATA):

        return pd.read_csv(FILE_DATA)

    else:

        return pd.DataFrame()