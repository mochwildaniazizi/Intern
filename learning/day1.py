print("Hello, Pabrik ANH New Co!")
# This is a simple Python script to greet the company.

nama_produk = "Pakan A-101"
stok_kg = 500
kadar_protein = 21.5
sudah_diperiksa = True

print(f"Nama Produk: {nama_produk}")
print(f"Stok (kg): {stok_kg}")
print(f"Kadar Protein (%): {kadar_protein}")
print(f"Sudah Diperiksa: {sudah_diperiksa}")

bahan_utama = ["Jagung", "Dedak Padi", "Bungkil Kedelai"]
print("Bahan Utama nomor 1: ", bahan_utama[0]) # Output: Jagung
#tambah bahan utama baru
bahan_utama.append("Minyak Ikan")
#hapus bahan utama
bahan_utama.remove("Dedak Padi")
#cetak semua bahan utama
print("Bahan Utama:", bahan_utama)

#tuple untuk menyimpan informasi produk
info_produk = ("Pakan A-101", 500, 21.5, True)

#cetak tuple info_produk
print("Informasi Produk:", info_produk)

#mengakses elemen tuple
print("Kode Produk:", info_produk[0])  # Output: Pakan A-101
print("Berat (kg):", info_produk[1])  # Output: 500

#tes tambah data tuple
info_produk = info_produk + ("Kualitas Tinggi",)
print("Informasi Produk setelah penambahan:", info_produk)

#tes hapus data tuple
# Tidak bisa menghapus elemen dari tuple, karena tuple bersifat immutable
# Namun, kita bisa membuat tuple baru tanpa elemen yang ingin dihapus

info_produk = info_produk[:2] + info_produk[3:]
print("Informasi Produk setelah penghapusan:", info_produk)