# CASE-BASED REASONING - FUZZY LOGIC INFERENCE

## 📋 Deskripsi Proyek
Proyek ini mengimplementasikan sistem logika Fuzzy untuk memilih 5 restoran terbaik berdasarkan dataset 'restoran.csv'[cite: 1]. Sistem mengevaluasi aspek Pelayanan (1-100) dan Harga (25.000-55.000)[cite: 1].

## ⚙️ Spesifikasi Sistem
* **Bahasa**: Python 3.x[cite: 1]
* **Metode Fuzzy**: Sugeno (Weighted Average)[cite: 1]
* **Input**: 'restoran.csv' (Kolom: id Pelanggan, Pelayanan, harga)[cite: 1]
* **Output**: 'peringkat.csv' (5 Restoran Terbaik)[cite: 1]

## 🛠️ Alur Implementasi (Tanpa Library Fuzzy)
1. **Fuzzification**: Menghitung derajat keanggotaan menggunakan kurva Trapesium dan Segitiga[cite: 1].
2. **Inference**: Menerapkan 9 aturan (Rule-base) dengan operator MIN untuk menentukan fire strength[cite: 1].
3. **Defuzzification**: Menghitung skor kelayakan akhir secara manual dengan rumus rata-rata terbobot[cite: 1].

## 🚀 Cara Menjalankan
1. Pastikan file 'restoran.csv' berada di direktori yang sama dengan script ini[cite: 1].
2. Buka terminal atau CMD, lalu jalankan:

   `python Reasoning.py`
3. Hasil akan tampil di layar dan file 'peringkat.csv' akan tercipta secara otomatis[cite: 1].