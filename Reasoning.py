import csv

# ==========================================================
# 1. FUZZIFICATION (Fungsi Keanggotaan Manual)
# ==========================================================

# Fungsi Segitiga/Trapesium untuk Kualitas Servis (1-100)
def f_servis_buruk(x):
# Mengimplementasikan rumus kurva untuk servis buruk
    if x <= 30: return 1
    elif 30 < x < 50: return (50 - x) / (20)
    return 0

# Mengimplementasikan rumus kurva untuk servis biasa (Segitiga/Trapesium)
def f_servis_biasa(x):
    if 35 < x <= 50: return (x - 35) / 15
    elif 50 < x <= 65: return 1
    elif 65 < x < 80: return (80 - x) / 15
    return 0

# Mengimplementasikan rumus kurva untuk servis bagus
def f_servis_bagus(x):
    # TODO : Lengkapi fungsi keanggotaan untuk servis bagus
    pass

# Fungsi untuk Harga (25.000 - 55.000)
def f_harga_murah(x):
    # TODO : Lengkapi fungsi keanggotaan untuk harga murah
    pass

def f_harga_sedang(x):
    # TODO : Lengkapi fungsi keanggotaan untuk harga sedang
    pass

def f_harga_mahal(x):
    # TODO : Lengkapi fungsi keanggotaan untuk harga mahal
    pass

# ==========================================================
# 2. INFERENSI & 3. DEFUZZIFICATION (Metode Sugeno)
# ==========================================================

def hitung_fuzzy(servis, harga):
    # TODO : Kerjakan bagian Inferensi dan Defuzzification di sini
    # 1. Panggil fungsi fuzzifikasi (s_buruk, s_biasa, dst)
    # 2. Tentukan Aturan (Rules) minimal 9 aturan
    # 3. Hitung nilai akhir dengan rumus Sugeno
    pass

# ==========================================================
# 3. PROSES DATA (Membaca & Menyimpan File)
# ==========================================================

def main():
    data_restoran = []
    
    try:
        # Membaca data tanpa library fuzzy[cite: 1]
        with open('restoran.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # TODO : Lengkapi pengambilan data dari kolom CSV di sini
                # id_val = row.get('id Pelanggan'), dsb.
                
                # --- Bagian Integrasi (Biarkan seperti ini) ---
                # Proses Fuzzification, Inferensi, dan Defuzzification
                # skor = hitung_fuzzy(servis, harga)
                
                pass # Hapus pass ini jika kode di atas sudah dilengkapi
            
    except FileNotFoundError:
        print("Error: File restoran.csv tidak ditemukan!")
        return
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return

# ==========================================================
# 4. BAGIAN OUTPUT (Menampilkan dan Menyimpan Hasil)
# ==========================================================

    # Sorting manual berdasarkan skor tertinggi[cite: 1]
    data_restoran.sort(key=lambda x: x['skor'], reverse=True)
    
    # Ambil 5 restoran terbaik[cite: 1]
    top_5 = data_restoran[:5]

    # Menampilkan ke layar dengan proteksi NoneType[cite: 1]
    print(f"{'ID':<5} | {'Servis':<10} | {'Harga':<10} | {'Skor':<10}")
    print("-" * 45)
    for r in top_5:
        # Menggunakan r['id'] karena sudah kita simpan di dictionary 'data_restoran' di atas
        print(f"{str(r['id']):<5} | {r['servis']:<10.1f} | {r['harga']:<10.0f} | {r['skor']:<10.2f}")

    # Simpan ke file peringkat.csv
    try:
        with open('peringkat.csv', mode='w', newline='') as file:
            # Pastikan fieldnames di sini SAMA PERSIS dengan key di dictionary data_restoran
            kolom = ['id', 'servis', 'harga', 'skor'] 
            writer = csv.DictWriter(file, fieldnames=kolom)
            
            writer.writeheader()
            writer.writerows(top_5)
        
        print("\nBerhasil! Hasil 5 terbaik disimpan di peringkat.csv")
    except Exception as e:
        print(f"Gagal menyimpan file: {e}")

if __name__ == "__main__":
    main()