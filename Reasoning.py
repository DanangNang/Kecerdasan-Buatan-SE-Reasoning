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
    if x <= 70: return 0
    elif 70 < x < 90: return (x - 70) / 20
    elif x >= 90: return 1
    return 0

# Fungsi untuk Harga (25.000 - 55.000)
def f_harga_murah(x):
    if x <= 30000: return 1
    elif 30000 < x < 40000: return (40000 - x) / 10000
    return 0

def f_harga_sedang(x):
    if 35000 < x <= 45000: return (x - 35000) / 10000
    elif 45000 < x <= 50000: return 1
    elif 50000 < x < 55000: return (55000 - x) / 5000
    return 0

def f_harga_mahal(x):
    if x < 45000: return 0
    elif 45000 <= x < 55000: return (x - 45000) / 10000
    elif x >= 55000: return 1
    return 0

# ==========================================================
# 2. INFERENSI 
# ==========================================================
# 3. DEFUZZIFICATION (Metode Sugeno)
# ==========================================================

def hitung_fuzzy(servis, harga):
    # 1. Fuzzifikasi Input Servis
    servis_buruk = f_servis_buruk(servis)
    servis_biasa = f_servis_biasa(servis)
    servis_bagus = f_servis_bagus(servis)
    
    # 2. Fuzzifikasi Input Harga
    harga_murah = f_harga_murah(harga)
    harga_sedang = f_harga_sedang(harga)
    harga_mahal = f_harga_mahal(harga)
    
    # 3. Inferensi dengan 9 Rules (Sugeno)
    # Rule output (Sugeno) berupa nilai crisp
    rules = []
    
    # Rule 1: Jika Servis Buruk DAN Harga Murah MAKA Output = 50
    alpha_1 = min(servis_buruk, harga_murah)
    if alpha_1 > 0:
        rules.append((alpha_1, 50))
    
    # Rule 2: Jika Servis Buruk DAN Harga Sedang MAKA Output = 30
    alpha_2 = min(servis_buruk, harga_sedang)
    if alpha_2 > 0:
        rules.append((alpha_2, 30))
    
    # Rule 3: Jika Servis Buruk DAN Harga Mahal MAKA Output = 10
    alpha_3 = min(servis_buruk, harga_mahal)
    if alpha_3 > 0:
        rules.append((alpha_3, 10))
    
    # Rule 4: Jika Servis Biasa DAN Harga Murah MAKA Output = 70
    alpha_4 = min(servis_biasa, harga_murah)
    if alpha_4 > 0:
        rules.append((alpha_4, 70))
    
    # Rule 5: Jika Servis Biasa DAN Harga Sedang MAKA Output = 50
    alpha_5 = min(servis_biasa, harga_sedang)
    if alpha_5 > 0:
        rules.append((alpha_5, 50))
    
    # Rule 6: Jika Servis Biasa DAN Harga Mahal MAKA Output = 30
    alpha_6 = min(servis_biasa, harga_mahal)
    if alpha_6 > 0:
        rules.append((alpha_6, 30))
    
    # Rule 7: Jika Servis Bagus DAN Harga Murah MAKA Output = 90
    alpha_7 = min(servis_bagus, harga_murah)
    if alpha_7 > 0:
        rules.append((alpha_7, 90))
    
    # Rule 8: Jika Servis Bagus DAN Harga Sedang MAKA Output = 70
    alpha_8 = min(servis_bagus, harga_sedang)
    if alpha_8 > 0:
        rules.append((alpha_8, 70))
    
    # Rule 9: Jika Servis Bagus DAN Harga Mahal MAKA Output = 50
    alpha_9 = min(servis_bagus, harga_mahal)
    if alpha_9 > 0:
        rules.append((alpha_9, 50))
    
    # 4. Defuzzifikasi menggunakan Metode Sugeno (Weighted Average)
    if not rules:
        return 50  # Default jika tidak ada rule yang aktif
    
    total_weight = sum(alpha for alpha, _ in rules)
    if total_weight == 0:
        return 50
    
    output = sum(alpha * value for alpha, value in rules) / total_weight
    return output

# ==========================================================
# 4. PROSES DATA (Membaca & Menyimpan File)
# ==========================================================

def main():
    data_restoran = []
    
    try:
        with open('restoran.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # 1. Pastikan nama kolom di row.get() sesuai dengan header di file CSV kamu
                # Jika di CSV kolomnya masih 'id Pelanggan', ganti di sini
                id_val = row.get('id Pelanggan') or row.get('id_restoran')
                servis_val = row.get('Pelayanan')
                harga_val = row.get('harga')
                
                if id_val is None or servis_val is None or harga_val is None:
                    continue
                
                servis = float(servis_val)
                harga = float(harga_val)
                
                skor = hitung_fuzzy(servis, harga)
                
                # 2. KRUSIAL: Simpan dengan key 'id_restoran' agar bisa dipanggil nanti
                # Jika x nya ingin diambil dari servis buruk dan harga mahal
                # if servis <= 50 and harga >= 45000: (Hapus Komen ini)
                data_restoran.append({
                    'id_restoran': id_val, # Pastikan key ini tertulis tepat seperti ini
                    'servis': servis,
                    'harga': harga,
                    'skor': skor
                })
    except Exception as e:
        print(f"Terjadi kesalahan pembacaan: {e}")
        return

    # 3. Sorting berdasarkan skor
    data_restoran.sort(key=lambda x: x['skor'], reverse=True)
    top_5 = data_restoran[:10]

    # 4. Bagian Output (Print)
    print(" ")
    print(" == 10 RESTORAN TERBAIK DI BANDUNG == ")
    print(f"\n{'No':<4} | {'ID':<12} | {'Servis':<10} | {'Harga':<10} | {'Skor':<10}")
    print("-" * 55)
    
    for i, r in enumerate(top_5, 1):
        # Panggil menggunakan key yang sama persis yaitu 'id_restoran'
        print(f"{i:<4} | {str(r['id_restoran']):<12} | {r['servis']:<10.1f} | {r['harga']:<10.0f} | {r['skor']:<10.2f}")

    # 5. Simpan ke File peringkat.csv
    try:
        with open('peringkat.csv', mode='w', newline='') as file:
            kolom = ['no', 'id_restoran', 'servis', 'harga', 'skor'] 
            writer = csv.DictWriter(file, fieldnames=kolom)
            writer.writeheader()
            
            data_dengan_nomor = []
            for i, r in enumerate(top_5, 1):
                row_baru = r.copy()
                row_baru['no'] = i
                data_dengan_nomor.append(row_baru)
            
            writer.writerows(data_dengan_nomor)
        print("\nBerhasil! Hasil 10 terbaik disimpan di peringkat.csv")
    except Exception as e:
        print(f"Gagal menyimpan file: {e}")
        
    print(" ")

if __name__ == "__main__":
    main()