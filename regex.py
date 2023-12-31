import re
import numpy

def idRegex(text):
    teks = text
    kunci = "2141"
    pola_nim = re.compile(r'\b' + re.escape(kunci) + r'\d+\b')

    hasil_nim = pola_nim.search(teks)
    NIM="Tidak Ditemukan"

    if hasil_nim:
        nim_ditemukan = hasil_nim.group()
        NIM=nim_ditemukan

    # nama
    pola_nama = re.compile(r'\b([A-Z\s]+)\n')

    # Temukan semua kecocokan yang sesuai dengan pola
    hasil = pola_nama.search(teks)

    # Ambil hasil ekstraksi nama
    nama = "Tidak ditemukan"
    if hasil:
        nama = hasil.group(1).strip()
        # print(nama)
        
    # TTL

    pola_tanggal_tempat = re.compile(r'\b\n([A-Z][A-Z\s,]+)\s+(\d+\s+[A-Za-z]+\s+\d{4})')

    # Temukan semua kecocokan yang sesuai dengan pola
    hasil_ttl = pola_tanggal_tempat.search(teks)

    # Ambil hasil ekstraksi tanggal dan tempat
    ttl = "Tidak ditemukan"
    if hasil_ttl:
        tempat = hasil_ttl.group(1).strip()
        tanggal = hasil_ttl.group(2).strip()
        ttl = tempat+tanggal

    # Prodi
    # Definisikan pola regex untuk mengekstrak "DAV T. INFORMATIKA"
    pola_nama_program = re.compile(r'\b([A-Z]+\s[A-Z]+\.\s[A-Z\s]+)\b\n\n')

    # Temukan semua kecocokan yang sesuai dengan pola
    hasil_prodi = pola_nama_program.search(teks)

    nama_program = "Tidak ditemukan"
    # Ambil hasil ekstraksi "DAV T. INFORMATIKA"
    if hasil_prodi:
        nama_program = hasil_prodi.group(1).strip()

    result = {
        "NIM": NIM,
        'NAMA' : nama,
        'TTL' : ttl,
        'PRODI' : nama_program
    }
    return result