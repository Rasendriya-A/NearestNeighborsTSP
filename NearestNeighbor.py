"""
Implementasi Algoritma Nearest Neighbor untuk Traveling Salesman Problem (TSP)

Program ini mengimplementasikan algoritma Nearest Neighbor yang merupakan salah satu
algoritma heuristik untuk menyelesaikan masalah TSP. Algoritma ini bekerja dengan cara:
1. Mulai dari kota awal yang dipilih
2. Dari kota saat ini, pilih kota terdekat yang belum dikunjungi
3. Ulangi langkah 2 sampai semua kota dikunjungi
4. Kembali ke kota awal

Author: [Nama Mahasiswa]
Date: September 30, 2025
Subject: Sistem Cerdas
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from typing import List, Tuple, Dict

class NearestNeighborTSP:
    """
    Kelas untuk menyelesaikan TSP menggunakan algoritma Nearest Neighbor
    
    Attributes:
        cities (Dict[str, Tuple[float, float]]): Dictionary berisi nama kota dan koordinatnya
        distance_matrix (np.ndarray): Matriks jarak antar kota
        city_names (List[str]): List nama-nama kota
        num_cities (int): Jumlah kota
    """
    
    def __init__(self, cities: Dict[str, Tuple[float, float]]):
        """
        Inisialisasi objek NearestNeighborTSP
        
        Args:
            cities (Dict[str, Tuple[float, float]]): Dictionary dengan format:
                {'nama_kota': (koordinat_x, koordinat_y)}
        """
        self.cities = cities
        self.city_names = list(cities.keys())
        self.num_cities = len(cities)
        
        # Validasi input minimal 2 kota
        if self.num_cities < 2:
            raise ValueError("TSP memerlukan minimal 2 kota!")
        
        # Inisialisasi matriks jarak
        self.distance_matrix = self._calculate_distance_matrix()
        
        print(f"TSP telah diinisialisasi dengan {self.num_cities} kota:")
        for city, coord in cities.items():
            print(f"   {city}: {coord}")
    
    def _calculate_distance_matrix(self) -> np.ndarray:
        """
        Menghitung matriks jarak antar semua kota menggunakan jarak Euclidean
        
        Returns:
            np.ndarray: Matriks jarak simetris berukuran (n x n) dimana n = jumlah kota
                       distance_matrix[i][j] = jarak dari kota i ke kota j
        """
        # Inisialisasi matriks jarak dengan ukuran n x n
        matrix = np.zeros((self.num_cities, self.num_cities))
        
        # Hitung jarak untuk setiap pasangan kota
        for i in range(self.num_cities):
            for j in range(self.num_cities):
                if i != j:
                    # Ambil koordinat kota i dan j
                    city1_name = self.city_names[i]
                    city2_name = self.city_names[j]
                    coord1 = self.cities[city1_name]
                    coord2 = self.cities[city2_name]
                    
                    # Hitung jarak Euclidean antara kedua kota
                    distance = self._euclidean_distance(coord1, coord2)
                    matrix[i][j] = distance
                else:
                    # Jarak dari kota ke dirinya sendiri adalah 0
                    matrix[i][j] = 0
        
        return matrix
    
    def _euclidean_distance(self, coord1: Tuple[float, float], coord2: Tuple[float, float]) -> float:
        """
        Menghitung jarak Euclidean antara dua titik koordinat
        
        Formula: d = √((x2-x1)² + (y2-y1)²)
        
        Args:
            coord1 (Tuple[float, float]): Koordinat titik pertama (x1, y1)
            coord2 (Tuple[float, float]): Koordinat titik kedua (x2, y2)
            
        Returns:
            float: Jarak Euclidean antara kedua titik
        """
        x1, y1 = coord1
        x2, y2 = coord2
        
        # Rumus jarak Euclidean
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distance
    
    def solve_nearest_neighbor(self, start_city: str = None) -> Tuple[List[str], float]:
        """
        Menyelesaikan TSP menggunakan algoritma Nearest Neighbor
        
        Algoritma ini bekerja dengan prinsip greedy:
        1. Mulai dari kota awal (start_city)
        2. Dari kota saat ini, pilih kota terdekat yang belum dikunjungi
        3. Pindah ke kota terdekat tersebut
        4. Ulangi langkah 2-3 sampai semua kota dikunjungi
        5. Kembali ke kota awal
        
        Args:
            start_city (str, optional): Nama kota awal. Jika None, akan menggunakan kota pertama
            
        Returns:
            Tuple[List[str], float]: (rute_terpendek, total_jarak)
                - rute_terpendek: List nama kota dalam urutan kunjungan
                - total_jarak: Total jarak yang ditempuh
        """
        # Tentukan kota awal
        if start_city is None:
            start_city = self.city_names[0]
        elif start_city not in self.city_names:
            raise ValueError(f"Kota '{start_city}' tidak ditemukan!")
        
        print(f"\n=== Menjalankan Algoritma Nearest Neighbor ===")
        print(f"Kota awal: {start_city}")
        
        # Inisialisasi variabel untuk tracking
        current_city = start_city
        visited_cities = set([start_city])  # Set kota yang sudah dikunjungi
        route = [start_city]  # List rute perjalanan
        total_distance = 0.0  # Total jarak tempuh
        
        print(f"\nLangkah 1: Mulai dari kota {current_city}")
        
        # Lakukan algoritma nearest neighbor sampai semua kota dikunjungi
        step = 2
        while len(visited_cities) < self.num_cities:
            print(f"\nLangkah {step}:")
            print(f"   Posisi saat ini: {current_city}")
            print(f"   Kota yang sudah dikunjungi: {sorted(list(visited_cities))}")
            
            # Cari kota terdekat yang belum dikunjungi
            nearest_city, min_distance = self._find_nearest_unvisited_city(current_city, visited_cities)
            
            print(f"   Kota terdekat yang belum dikunjungi: {nearest_city}")
            print(f"   Jarak dari {current_city} ke {nearest_city}: {min_distance:.2f}")
            
            # Pindah ke kota terdekat
            route.append(nearest_city)
            visited_cities.add(nearest_city)
            total_distance += min_distance
            current_city = nearest_city
            
            print(f"   Pindah ke {nearest_city}")
            print(f"   Total jarak sejauh ini: {total_distance:.2f}")
            
            step += 1
        
        # Kembali ke kota awal
        distance_to_start = self.distance_matrix[self.city_names.index(current_city)][self.city_names.index(start_city)]
        route.append(start_city)
        total_distance += distance_to_start
        
        print(f"\nLangkah {step}: Kembali ke kota awal")
        print(f"   Jarak dari {current_city} ke {start_city}: {distance_to_start:.2f}")
        print(f"   Kembali ke {start_city}")
        
        print(f"\n=== Hasil Akhir ===")
        print(f"Rute optimal: {' → '.join(route)}")
        print(f"Total jarak: {total_distance:.2f} unit")
        
        return route, total_distance
    
    def _find_nearest_unvisited_city(self, current_city: str, visited_cities: set) -> Tuple[str, float]:
        """
        Mencari kota terdekat yang belum dikunjungi dari kota saat ini
        
        Args:
            current_city (str): Nama kota saat ini
            visited_cities (set): Set nama kota yang sudah dikunjungi
            
        Returns:
            Tuple[str, float]: (nama_kota_terdekat, jarak_ke_kota_terdekat)
        """
        current_index = self.city_names.index(current_city)
        min_distance = float('inf')
        nearest_city = None
        
        # Periksa jarak ke semua kota yang belum dikunjungi
        for i, city_name in enumerate(self.city_names):
            # Skip jika kota sudah dikunjungi
            if city_name in visited_cities:
                continue
            
            # Hitung jarak dari kota saat ini ke kota ini
            distance = self.distance_matrix[current_index][i]
            
            # Update jika menemukan kota yang lebih dekat
            if distance < min_distance:
                min_distance = distance
                nearest_city = city_name
        
        return nearest_city, min_distance
    
    def plot_route(self, route: List[str], title: str = "Rute TSP dengan Algoritma Nearest Neighbor"):
        """
        Menampilkan visualisasi rute TSP menggunakan matplotlib
        
        Args:
            route (List[str]): List nama kota dalam urutan kunjungan
            title (str): Judul grafik
        """
        # Buat figure dan axis
        plt.figure(figsize=(14, 10))
        
        # Ambil koordinat kota-kota dalam rute
        x_coords = []
        y_coords = []
        
        for city in route:
            coord = self.cities[city]
            x_coords.append(coord[0])
            y_coords.append(coord[1])
        
        # Plot titik-titik kota
        plt.scatter(x_coords[:-1], y_coords[:-1], c='red', s=150, zorder=5, label='Kota', edgecolor='black')
        plt.scatter(x_coords[0], y_coords[0], c='green', s=200, zorder=6, label='Kota Awal/Akhir', marker='s', edgecolor='black')
        
        # Plot garis rute
        plt.plot(x_coords, y_coords, 'b-', linewidth=3, alpha=0.7, label='Rute')
        
        # Tambahkan label nama kota
        for i, city in enumerate(route[:-1]):  # Exclude kota terakhir karena sama dengan awal
            plt.annotate(city, (x_coords[i], y_coords[i]), 
                        xytext=(8, 8), textcoords='offset points',
                        fontsize=11, ha='left', fontweight='bold',
                        bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
        
        # Tambahkan nomor urutan kunjungan
        for i in range(1, len(route) - 1):
            mid_x = (x_coords[i-1] + x_coords[i]) / 2
            mid_y = (y_coords[i-1] + y_coords[i]) / 2
            plt.annotate(f'{i}', (mid_x, mid_y), 
                        bbox=dict(boxstyle="circle", facecolor='yellow', alpha=0.8),
                        fontsize=10, ha='center', va='center', fontweight='bold')
        
        # Pengaturan grafik
        plt.title(title, fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Koordinat X', fontsize=14)
        plt.ylabel('Koordinat Y', fontsize=14)
        plt.grid(True, alpha=0.3)
        plt.legend(fontsize=12)
        
        # Atur batas axis agar plot terlihat jelas
        margin = 0.8
        plt.xlim(min(x_coords) - margin, max(x_coords) + margin)
        plt.ylim(min(y_coords) - margin, max(y_coords) + margin)
        
        # Tampilkan plot
        plt.tight_layout()
        plt.show()
    
    def print_distance_matrix(self):
        """
        Menampilkan matriks jarak antar kota dalam format yang mudah dibaca
        """
        print("\n=== Matriks Jarak Antar Kota ===")
        print("=" * 60)
        
        # Header kolom
        header = "Dari\\Ke".ljust(12)
        for city in self.city_names:
            header += city.ljust(12)
        print(header)
        print("-" * len(header))
        
        # Isi matriks
        for i, city_from in enumerate(self.city_names):
            row = city_from.ljust(12)
            for j, city_to in enumerate(self.city_names):
                distance = self.distance_matrix[i][j]
                if i == j:
                    row += "0.00".ljust(12)
                else:
                    row += f"{distance:.2f}".ljust(12)
            print(row)
    
    def compare_all_starting_cities(self) -> Dict[str, Tuple[List[str], float]]:
        """
        Mencoba algoritma Nearest Neighbor dari semua kota sebagai titik awal
        dan membandingkan hasilnya
        
        Returns:
            Dict[str, Tuple[List[str], float]]: Dictionary dengan format:
                {kota_awal: (rute, total_jarak)}
        """
        print("\n=== Perbandingan Hasil dari Semua Kota Awal ===")
        results = {}
        best_distance = float('inf')
        best_start_city = None
        
        for start_city in self.city_names:
            print(f"\n{'='*50}")
            print(f"Mulai dari {start_city}")
            print(f"{'='*50}")
            route, total_distance = self.solve_nearest_neighbor(start_city)
            results[start_city] = (route, total_distance)
            
            if total_distance < best_distance:
                best_distance = total_distance
                best_start_city = start_city
        
        print(f"\n=== Ringkasan Perbandingan ===")
        print("=" * 50)
        for start_city, (route, distance) in results.items():
            status = "TERBAIK" if start_city == best_start_city else ""
            print(f"{start_city:15}: {distance:8.2f} unit {status}")
        
        print(f"\nRute terbaik dimulai dari {best_start_city} dengan jarak {best_distance:.2f} unit")
        return results


# ========================================
# CONTOH PENGGUNAAN DAN TESTING PROGRAM
# ========================================

def main():
    """
    Fungsi utama untuk mendemonstrasikan penggunaan algoritma Nearest Neighbor
    """
    print("=" * 60)
    print("IMPLEMENTASI ALGORITMA NEAREST NEIGHBOR UNTUK TSP")
    print("=" * 60)
    
    # ==========================================
    # CONTOH 1: TSP dengan 5 kota sederhana
    # ==========================================
    print("\n>>> CONTOH 1: TSP dengan 5 Kota <<<")
    
    # Definisi koordinat kota-kota
    cities_example1 = {
        'Jakarta': (0, 0),      # Kota asal di koordinat (0, 0)
        'Bandung': (3, 1),      # Kota 150 km ke timur, 50 km ke utara
        'Semarang': (5, 3),     # Kota 250 km ke timur, 150 km ke utara
        'Surabaya': (8, 2),     # Kota 400 km ke timur, 100 km ke utara
        'Yogyakarta': (4, -1)   # Kota 200 km ke timur, 50 km ke selatan
    }
    
    print("Dataset Kota-kota Indonesia:")
    print("=" * 40)
    for city, coord in cities_example1.items():
        print(f"{city:12}: {coord}")
    
    # Buat objek TSP
    tsp1 = NearestNeighborTSP(cities_example1)
    
    # Tampilkan matriks jarak
    tsp1.print_distance_matrix()
    
    # Jalankan algoritma dari kota Jakarta
    print(f"\n{'='*50}")
    print("MENJALANKAN ALGORITMA NEAREST NEIGHBOR")
    print(f"{'='*50}")
    
    route1, distance1 = tsp1.solve_nearest_neighbor('Jakarta')
    
    # Visualisasi hasil
    tsp1.plot_route(route1, "TSP 5 Kota - Mulai dari Jakarta")
    
    # ==========================================
    # CONTOH 2: Perbandingan dari semua kota awal
    # ==========================================
    print(f"\n{'='*50}")
    print("PERBANDINGAN DARI SEMUA KOTA AWAL")
    print(f"{'='*50}")
    
    results = tsp1.compare_all_starting_cities()
    
    # Cari rute terbaik
    best_route = None
    best_distance = float('inf')
    best_start = None
    
    for start_city, (route, distance) in results.items():
        if distance < best_distance:
            best_distance = distance
            best_route = route
            best_start = start_city
    
    print(f"\n{'='*50}")
    print("HASIL TERBAIK")
    print(f"{'='*50}")
    print(f"Kota awal terbaik: {best_start}")
    print(f"Rute terbaik: {' → '.join(best_route)}")
    print(f"Jarak terbaik: {best_distance:.2f} unit")
    
    # Visualisasi rute terbaik
    tsp1.plot_route(best_route, f"Rute Terbaik TSP - Mulai dari {best_start}")
    
    # ==========================================
    # CONTOH 3: TSP dengan lebih banyak kota
    # ==========================================
    print(f"\n{'='*60}")
    print("CONTOH 2: TSP dengan 8 Kota")
    print(f"{'='*60}")
    
    # Dataset kota-kota besar Indonesia (koordinat relatif)
    cities_example2 = {
        'Jakarta': (0, 0),
        'Bandung': (2, 1),
        'Semarang': (6, 2),
        'Surabaya': (10, 1),
        'Yogyakarta': (5, -1),
        'Malang': (11, 0),
        'Solo': (7, 1),
        'Cirebon': (3, 2)
    }
    
    print("Dataset 8 Kota Indonesia:")
    print("=" * 40)
    for i, (city, coord) in enumerate(cities_example2.items(), 1):
        print(f"{i:2d}. {city:12}: {coord}")
    
    # Buat objek TSP baru
    tsp2 = NearestNeighborTSP(cities_example2)
    
    # Jalankan algoritma dari Jakarta
    route2, distance2 = tsp2.solve_nearest_neighbor('Jakarta')
    
    # Bandingkan semua titik awal
    results2 = tsp2.compare_all_starting_cities()
    
    # Cari yang terbaik
    best_route2 = None
    best_distance2 = float('inf')
    best_start2 = None
    
    for start_city, (route, distance) in results2.items():
        if distance < best_distance2:
            best_distance2 = distance
            best_route2 = route
            best_start2 = start_city
    
    print(f"\n{'='*50}")
    print("HASIL TERBAIK UNTUK 8 KOTA")
    print(f"{'='*50}")
    print(f"Kota awal terbaik: {best_start2}")
    print(f"Rute terbaik: {' → '.join(best_route2)}")
    print(f"Jarak terbaik: {best_distance2:.2f} unit")
    
    # Visualisasi
    tsp2.plot_route(best_route2, f"Rute Terbaik 8 Kota - Mulai dari {best_start2}")
    
    # ==========================================
    # ANALISIS KOMPLEKSITAS ALGORITMA
    # ==========================================
    print(f"\n{'='*60}")
    print("ANALISIS KOMPLEKSITAS ALGORITMA")
    print(f"{'='*60}")
    print("Kompleksitas Waktu Algoritma Nearest Neighbor:")
    print("- Worst Case: O(n²)")
    print("- Average Case: O(n²)")
    print("- Best Case: O(n²)")
    print()
    print("Kompleksitas Ruang: O(n²) untuk menyimpan matriks jarak")
    print()
    print("Keuntungan:")
    print("- Algoritma sederhana dan mudah diimplementasikan")
    print("- Cepat untuk dataset kecil hingga menengah")
    print("- Memberikan solusi yang cukup baik untuk banyak kasus")
    print()
    print("Kekurangan:")
    print("- Tidak selalu memberikan solusi optimal")
    print("- Hasil bergantung pada pemilihan kota awal")
    print("- Algoritma greedy yang bisa terjebak di solusi lokal")


if __name__ == "__main__":
    """
    Entry point program
    Jalankan fungsi main jika file ini dieksekusi langsung
    """
    main()
