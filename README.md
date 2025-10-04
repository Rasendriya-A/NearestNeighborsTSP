# Nearest Neighbor Algorithm for Traveling Salesman Problem (TSP)

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

Implementasi algoritma **Nearest Neighbor** untuk menyelesaikan masalah **Traveling Salesman Problem (TSP)** menggunakan Python. Program ini dibuat sebagai tugas mata kuliah **Sistem Cerdas** dengan fokus pada algoritma heuristik dan optimisasi.

## 📋 Deskripsi

**Traveling Salesman Problem (TSP)** adalah salah satu masalah optimisasi kombinatorial yang paling terkenal dalam ilmu komputer. Masalah ini bertujuan untuk menemukan rute terpendek yang mengunjungi semua kota tepat sekali dan kembali ke kota asal.

**Algoritma Nearest Neighbor** adalah algoritma heuristik sederhana yang menggunakan pendekatan greedy untuk menyelesaikan TSP dengan kompleksitas waktu O(n²).

### Cara Kerja Algoritma:
1. **Mulai** dari kota awal yang dipilih
2. **Pilih** kota terdekat yang belum dikunjungi dari posisi saat ini
3. **Pindah** ke kota terdekat tersebut
4. **Ulangi** langkah 2-3 sampai semua kota dikunjungi
5. **Kembali** ke kota awal

## 🚀 Fitur

- ✅ **Implementasi lengkap** algoritma Nearest Neighbor
- ✅ **Visualisasi grafik** rute TSP menggunakan matplotlib
- ✅ **Perhitungan jarak Euclidean** antar kota
- ✅ **Perbandingan multi-start** dari semua kota awal
- ✅ **Matriks jarak** antar semua kota
- ✅ **Output detail** langkah demi langkah algoritma
- ✅ **Analisis kompleksitas** dan performa
- ✅ **Format Jupyter Notebook** untuk pembelajaran interaktif

## 📊 Kompleksitas Algoritma

| Aspek | Kompleksitas | Keterangan |
|-------|--------------|------------|
| **Waktu** | **O(n²)** | Untuk setiap kota, periksa semua kota lain |
| **Ruang** | **O(n²)** | Menyimpan matriks jarak n×n |
| **Iterasi** | **n-1** | Pilih kota terdekat sebanyak (n-1) kali |

## 🛠️ Instalasi

### Persyaratan Sistem
- Python 3.7 atau lebih tinggi
- pip (Python package manager)

### Instalasi Dependencies
```bash
pip install numpy matplotlib jupyter
```

Atau menggunakan requirements file (jika tersedia):
```bash
pip install -r requirements.txt
```

## 📁 Struktur Project

```
NearestNeighborsTSP/
│
├── README.md                    # Dokumentasi project
├── NearestNeighbor.py          # Implementasi algoritma (Python script)
└── NearestNeighbor_TSP.ipynb   # Jupyter Notebook interaktif
```

## 💻 Cara Penggunaan

### 1. Menjalankan Python Script

```bash
# Clone repository
git clone https://github.com/Rasendriya-A/NearestNeighborsTSP.git
cd NearestNeighborsTSP

# Jalankan program
python NearestNeighbor.py
```

### 2. Menggunakan Jupyter Notebook

```bash
# Buka Jupyter Notebook
jupyter notebook

# Pilih file NearestNeighbor_TSP.ipynb
# Jalankan cell demi cell dengan Shift+Enter
```

### 3. Implementasi Custom

```python
from NearestNeighbor import NearestNeighborTSP

# Definisikan kota-kota dengan koordinat
cities = {
    'Jakarta': (0, 0),
    'Bandung': (3, 1),
    'Semarang': (5, 3),
    'Surabaya': (8, 2),
    'Yogyakarta': (4, -1)
}

# Buat objek TSP
tsp = NearestNeighborTSP(cities)

# Jalankan algoritma
route, distance = tsp.solve_nearest_neighbor('Jakarta')

# Visualisasi hasil
tsp.plot_route(route, "Rute TSP - Mulai dari Jakarta")

# Bandingkan dari semua kota awal
results = tsp.compare_all_starting_cities()
```

## 📈 Contoh Output

### Output Terminal:
```
=== Menjalankan Algoritma Nearest Neighbor ===
Kota awal: Jakarta

Langkah 1: Mulai dari kota Jakarta

Langkah 2:
   Posisi saat ini: Jakarta
   Kota yang sudah dikunjungi: ['Jakarta']
   Kota terdekat yang belum dikunjungi: Bandung
   Jarak dari Jakarta ke Bandung: 3.16
   Pindah ke Bandung
   Total jarak sejauh ini: 3.16

...

=== Hasil Akhir ===
Rute optimal: Jakarta → Bandung → Yogyakarta → Semarang → Surabaya → Jakarta
Total jarak: 18.75 unit
```

### Visualisasi:
Program akan menampilkan grafik yang menunjukkan:
- Titik-titik kota dengan koordinat
- Garis rute yang menghubungkan kota
- Nomor urutan kunjungan
- Kota awal/akhir yang dibedakan warnanya

## 🔍 Analisis Algoritma

### Keuntungan:
- **Sederhana**: Mudah dipahami dan diimplementasikan
- **Cepat**: Efisien untuk dataset kecil hingga menengah
- **Praktis**: Memberikan solusi yang cukup baik dalam waktu singkat
- **Deterministik**: Hasil konsisten untuk input yang sama

### Kekurangan:
- **Tidak Optimal**: Tidak menjamin solusi terbaik global
- **Greedy**: Keputusan lokal dapat menghasilkan solusi suboptimal
- **Sensitif**: Hasil bergantung pada pemilihan kota awal
- **Terjebak**: Bisa terjebak dalam optimum lokal

### Rekomendasi Optimisasi:
1. **Multi-Start Approach**: Jalankan dari semua kota awal dan pilih terbaik
2. **Local Search**: Tambahkan 2-opt atau 3-opt improvement
3. **Hybrid Algorithm**: Kombinasi dengan metaheuristic lain
4. **Parallel Processing**: Untuk dataset yang lebih besar

## 🧪 Testing dan Validasi

Program telah diuji dengan:
- **Dataset 5 kota**: Kota-kota Indonesia (Jakarta, Bandung, Semarang, Surabaya, Yogyakarta)
- **Dataset 8 kota**: Kota-kota Indonesia diperluas (+ Malang, Solo, Cirebon)
- **Perbandingan multi-start**: Algoritma dijalankan dari setiap kota sebagai titik awal