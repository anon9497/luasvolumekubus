# Impor modul math untuk menggunakan konstanta pi
import math

# Fungsi untuk menghitung luas permukaan kubus
def luas_permukaan_kubus(s):
    # Rumus luas permukaan kubus = 6 * s**2
    return 6 * s**2

# Fungsi untuk menghitung volume kubus
def volume_kubus(s):
    # Rumus volume kubus = s**3
    return s**3

# Contoh penggunaan fungsi
# Masukkan panjang sisi kubus
s = float(input("Masukkan panjang sisi kubus: "))
# Panggil fungsi luas_permukaan_kubus dan volume_kubus
# Cetak hasilnya dengan pembulatan dua angka di belakang koma
print(f"Luas permukaan kubus = {round(luas_permukaan_kubus(s), 2)}")
print(f"Volume kubus = {round(volume_kubus(s), 2)}")
