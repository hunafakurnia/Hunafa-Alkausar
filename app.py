import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Form Data Mahasiswa",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Aplikasi Data Mahasiswa")
st.write("Silakan isi data di bawah ini.")

# Sidebar
st.sidebar.header("Menu")
menu = st.sidebar.radio("Pilih Halaman", ["Input Data", "Data Mahasiswa"])

# Session State
if "data" not in st.session_state:
    st.session_state.data = []

if menu == "Input Data":

    with st.form("form_mahasiswa"):

        col1, col2 = st.columns(2)

        with col1:
            nama = st.text_input("Nama Lengkap")
            umur = st.number_input("Umur", 17, 60, 20)
            jk = st.radio(
                "Jenis Kelamin",
                ["Laki-laki", "Perempuan"]
            )
            jurusan = st.selectbox(
                "Jurusan",
                [
                    "Teknik Informatika",
                    "Sistem Informasi",
                    "Manajemen",
                    "Akuntansi"
                ]
            )

        with col2:
            semester = st.slider("Semester", 1, 8, 1)
            tanggal = st.date_input("Tanggal Lahir")
            nilai = st.slider("Nilai", 0, 100, 80)
            hobi = st.multiselect(
                "Hobi",
                [
                    "Membaca",
                    "Olahraga",
                    "Musik",
                    "Coding",
                    "Game",
                    "Traveling"
                ]
            )

        alamat = st.text_area("Alamat")

        foto = st.file_uploader(
            "Upload Foto",
            type=["jpg", "jpeg", "png"]
        )

        setuju = st.checkbox(
            "Saya menyatakan data yang diisi benar."
        )

        simpan = st.form_submit_button("💾 Simpan Data")

    if simpan:

        if nama == "":
            st.error("Nama wajib diisi.")
        elif not setuju:
            st.warning("Centang persetujuan terlebih dahulu.")
        else:

            st.session_state.data.append({
                "Nama": nama,
                "Umur": umur,
                "Jenis Kelamin": jk,
                "Jurusan": jurusan,
                "Semester": semester,
                "Tanggal Lahir": tanggal,
                "Nilai": nilai,
                "Hobi": ", ".join(hobi),
                "Alamat": alamat
            })

            st.success("Data berhasil disimpan.")

            if foto:
                st.image(foto, width=180)

            st.subheader("Ringkasan Data")

            st.write(f"**Nama :** {nama}")
            st.write(f"**Umur :** {umur} Tahun")
            st.write(f"**Jurusan :** {jurusan}")
            st.write(f"**Semester :** {semester}")
            st.write(f"**Nilai :** {nilai}")

elif menu == "Data Mahasiswa":

    st.header("📋 Data Mahasiswa")

    if len(st.session_state.data) == 0:
        st.info("Belum ada data.")
    else:
        df = pd.DataFrame(st.session_state.data)

        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇ Download CSV",
            csv,
            "data_mahasiswa.csv",
            "text/csv"
        )

        st.metric("Jumlah Mahasiswa", len(df))

        st.bar_chart(df.set_index("Nama")["Nilai"])