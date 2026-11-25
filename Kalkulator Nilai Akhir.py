# Program KalkulaorNilaiAkhir
# Program ini digunakan untuk menghitung nilai yang dibutuhkan dan prioritas nilai yang dibutuhkan untuk mendapat indeks nilai yang diinginkan

# Kamus
# berjalan : Boolean
# pilihan : Strings
# Fungsi menampilkan menu
def menu_utama():
    # Algoritma
    print()
    print("======== Menu Utama ========")
    print("Pilihan Mata Kuliah yang Tersedia:")
    print("1. Matematika I")
    print("2. Fisika Dasar I")
    print("3. Kimia Dasar I")
    print("4. Berpikir Komputasional")
    print("5. Pengantar Prinsip Berkelanjutan")
    return
# Fungsi mata kuliah Matematika
def matematika():
    # Kamus
    # indeks : Char
    # PKH, KBF1, KBF2, proyek_mini, UTS, UAS : int
    # nilai_mtk : float
    
    # Algoritma
    print("======== Matematika Dasar I ========")
    PKH = int(input("Masukkan nilai tugas = "))
    KBF1 = int(input("Masukkan nilai KBF ke-1 = "))
    KBF2 = int(input("Masukkan nilai KBF ke-2 = "))
    proyek_mini = int(input("Masukkan nilai proyek mini = "))
    UTS = int(input("Masukkan nilai UTS = "))
    UAS = int(input("Masukkan nilai UAS = "))
    nilai = float(PKH * 0.1) + float(KBF1 * 0.5) + float(KBF2 * 0.5) + float(proyek_mini * 0.1) + float(UTS * 0.35) + float(UAS * 0.35)
   
    if nilai >= 80:
        indeks = 'A'
    elif nilai >= 73 and nilai < 80:
        indeks = 'AB'
    elif nilai >= 65 and nilai <73:
        indeks = 'B'
    elif nilai >= 57 and nilai <65:
        indeks = 'BC'
    elif nilai >= 50 and nilai <57:
        indeks = 'C'
    elif nilai >= 35 and nilai <50:
        indeks = 'D'
    elif nilai < 35:
        indeks = 'E'
        
    print("Indeks nilai Mata Kuliah Matematika I =", indeks)
    return
# Fungsi mata kuliah Fisika Dasar I
def fisika():
    # Kamus
    # indeks : Strings
    # AU1, AU2, AT, AK, LCE : int
    # nilai : float

    # Algoritma
    print("======== Fisika Dasar I ========")
    AU1 = int(input("Masukkan nilai Ujian I (AU1) = "))
    AU2 = int(input("Masukkan nilai Ujian II (AU2) = "))
    AT = int(input("Masukkan nilai tugas (AT) = "))
    AK = int(input("Masukkan nilai kuis (AK) = "))
    LCE = int(input("Masukkan nilai tugas besar (LCE) = "))
    nilai = float(AU1 * 0.3) + float(AU2 * 0.3) + float(AT * 0.15) + float(AK * 0.15) + float(LCE * 0.1)

    if nilai >= 75:
        indeks = 'A'
    elif nilai >= 68 and nilai < 75:
        indeks = 'AB'
    elif nilai >= 60 and nilai < 68:
        indeks = 'B'
    elif nilai >= 55 and nilai < 60:
        indeks = 'BC'
    elif nilai >= 50 and nilai < 55:
        indeks = 'C'
    elif nilai >= 45 and nilai < 50:
        indeks = 'D'
    elif nilai < 45:
        indeks = 'E'

    print("Indeks nilai Mata Kuliah Fisika Dasar I =", indeks)
    return
# Fungsi mata kuliah Kimia Dasar I
def kimia():
    # Kamus
    # indeks : Strings
    # tugas, kuis1, kuis2, UTS, UAS : int
    # kuis, nilai : float

    # Algoritma
    print("======== Kimia Dasar I ========")
    tugas = int(input("Masukkan nilai tugas = "))
    kuis1 = int(input("Masukkan nilai kuis ke-1 = "))
    kuis2 = int(input("Masukkan nilai kuis ke-2 = "))
    UTS = int(input("Masukkan nilai UTS = "))
    UAS = int(input("Masukkan nilai UAS = "))
    kuis = float(kuis1 + kuis2) / 2
    nilai = float(tugas * 0.05) + float(kuis * 0.25) + float(UTS * 0.35) + float(UAS * 0.35)

    if nilai >= 75:
        indeks = 'A'
    elif nilai >= 68 and nilai < 75:
        indeks = 'AB'
    elif nilai >= 60 and nilai < 68:
        indeks = 'B'
    elif nilai >= 53 and nilai < 60:
        indeks = 'BC'
    elif nilai >= 45 and nilai < 53:
        indeks = 'C'
    elif nilai >= 38 and nilai < 45:
        indeks = 'D'
    elif nilai < 38:
        indeks = 'E'

    print("Indeks nilai Mata Kuliah Kimia Dasar I =", indeks)
    return
# Fungsi mata kuliah Berpikir Komputasional
def berpikir_komputasional():
    # Kamus
    # indeks : Strings
    # UTS, projek1, projek2, kuis, praktikum, tugas_kelas : int
    # nilai : float

    # Algoritma
    print("======== Berpikir Komputasional ========")
    UTS = int(input("Masukkan nilai UTS = "))
    projek1 = int(input("Masukkan nilai Projek I = "))
    projek2 = int(input("Masukkan nilai Projek II = "))
    kuis = int(input("Masukkan nilai kuis = "))
    praktikum = int(input("Masukkan nilai praktikum = "))
    tugas_kelas = int(input("Masukkan nilai tugas kelas = "))
    nilai = float(UTS * 0.35) + float(projek1 * 0.25) + float(projek2 * 0.25) + float(kuis * 0.05) + float(praktikum * 0.1) + float(tugas_kelas * 0.025)

    if nilai >= 80:
        indeks = 'A'
    elif nilai >= 73 and nilai < 80:
        indeks = 'AB'
    elif nilai >= 65 and nilai < 73:
        indeks = 'B'
    elif nilai >= 57 and nilai < 65:
        indeks = 'BC'
    elif nilai >= 50 and nilai < 57:
        indeks = 'C'
    elif nilai >= 35 and nilai < 50:
        indeks = 'D'
    elif nilai < 35:
        indeks = 'E'

    print("Indeks nilai Mata Kuliah Berpikir Komputasional =", indeks)
    return
# Fungsi mata kuliah Pengantar Prinsip Berkelanjutan
def berkelanjutan():
    # Kamus
    # indeks : Strings
    # kuis, tugas_kelompok, UTS, laporan, media : int
    # nilai : float

    # Algoritma
    print("======== Pengantar Prinsip Berkelanjutan ========")
    kuis = int(input("Masukkan nilai kuis online = "))
    tugas_kelompok = int(input("Masukkan nilai tugas kelas berkelompok = "))
    UTS = int(input("Masukkan nilai UTS = "))
    laporan = int(input("Masukkan nilai activity reports = "))
    media = int(input("Masukkan nilai popular media = "))
    nilai = float(kuis * 0.1) + float(tugas_kelompok * 0.1) + float(UTS * 0.3) + float(laporan * 0.35) + float(media * 0.15)

    if nilai >= 80:
        indeks = 'A'
    elif nilai >= 73 and nilai < 80:
        indeks = 'AB'
    elif nilai >= 65 and nilai < 73:
        indeks = 'B'
    elif nilai >= 57 and nilai < 65:
        indeks = 'BC'
    elif nilai >= 50 and nilai < 57:
        indeks = 'C'
    elif nilai >= 35 and nilai < 50:
        indeks = 'D'
    elif nilai < 35:
        indeks = 'E'

    print("Indeks nilai Mata Kuliah Pengantar Prinsip Berkelanjutan =", indeks)
    return
    
# Program Utama
berjalan = True

while berjalan:
    menu_utama()
    pilihan = str(input("Mata Kuliah yang dipilih (1-5): "))
    
    if pilihan == "1":
        matematika()
    elif pilihan == "2":
        fisika()
    elif pilihan == "3":
        kimia()
    elif pilihan == "4":
        berpikir_komputasional()
    elif pilihan == "5":
        berkelanjutan()
    else:
        print("Mata Kuliah yang dipilih tidak valid, silahkan pilih Mata Kuliah yang disediakan")