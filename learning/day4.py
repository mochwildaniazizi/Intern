# Input validasi dengan 0/1
apakah_disetujui = int(input("Apakah disetujui? (1=Ya, 0=Tidak): ")) == 1
aturan1_terpenuhi = int(input("Apakah pelanggan aktif? (1=Ya, 0=Tidak): ")) == 1
aturan2_terpenuhi = int(input("Apakah jumlah bahan tidak melebihi batas? (1=Ya, 0=Tidak): ")) == 1
aturan3_terpenuhi = int(input("Apakah bahan wajib ada? (1=Ya, 0=Tidak): ")) == 1

if apakah_disetujui == True:
    print("✅ Validasi Sukses. Permintaan REQ-004 diteruskan ke produksi.")
elif aturan1_terpenuhi == False:
    print("❌ Validasi Gagal: Pelanggan tidak aktif.")
elif aturan2_terpenuhi == False:
    print("❌ Validasi Gagal: Jumlah bahan melebihi batas.")
elif aturan3_terpenuhi == False:
    print("❌ Validasi Gagal: Bahan wajib tidak ada.")

print()

### Challenge

pesanan = {
    "id_pesanan": "ORD-005",
    "info_pelanggan": {
        "nama": "Maju Jaya Farm",
        "status": "VIP", # Coba ganti jadi "Reguler"
        "lokasi": "Luar Kota" # Coba ganti jadi "Dalam Kota"
    },
    "harga_barang": 750000
}

print(pesanan)

ongkir_normal = 50000
biaya_tambahan_luar_kota = 30000
if pesanan["harga_barang"] < 5000000:
    if pesanan["info_pelanggan"]["status"] == "VIP":
        if pesanan["info_pelanggan"]["lokasi"] == "Dalam Kota":
            ongkir = 0
        else:
            ongkir = 0.5 * ongkir_normal
    else:
        if pesanan["info_pelanggan"]["lokasi"] == "Dalam Kota":
            ongkir = ongkir_normal
        else:
            ongkir = ongkir_normal + biaya_tambahan_luar_kota
else:
    ongkir = 0

print("--- Rincian Pesanan ", pesanan["id_pesanan"], "---")
print("Status Pelanggan:", pesanan["info_pelanggan"]["status"])
print("Harga Barang (IDR):", pesanan["harga_barang"])
print("Biaya Ongkir (IDR):", ongkir)
print("------------------------------")
print("Total Harga (IDR):", pesanan["harga_barang"] + ongkir)