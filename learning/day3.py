### 1
jumlah_jagung_awal = 2500
satu_resep = 125.5
banyak_resep = 15
sisa_jagung = jumlah_jagung_awal - (satu_resep * banyak_resep)

print("Jumlah Jagung Awal (kg):", jumlah_jagung_awal)
print("Satu Resep Pakan (kg):", satu_resep)
print("Banyak Resep Pakan:", banyak_resep)
print("Sisa Jagung (kg):", sisa_jagung)
print()


### 2
stok_terkini = 300
permintaan_masuk = 350

print("Stok Terkini (kg):", stok_terkini)
print("Permintaan Masuk (kg):", permintaan_masuk)
# Memeriksa apakah stok mencukupi untuk memenuhi permintaan
print("Memeriksa apakah stok mencukupi untuk memenuhi permintaan...")
if stok_terkini >= permintaan_masuk:
    print("Stok mencukupi untuk memenuhi permintaan.")
else:
    print("Stok tidak mencukupi, perlu restock.")
print()


### 3
sudah_langganan_lebih_dari_satu_tahun = False
total_pembelian_terakhir = 6000000

print("Sudah langganan lebih dari satu tahun:", sudah_langganan_lebih_dari_satu_tahun)
print("Total pembelian terakhir (IDR):", total_pembelian_terakhir)
# Memeriksa apakah pelanggan termasuk dalam VIP
print("Memeriksa apakah pelanggan termasuk dalam VIP...")
if sudah_langganan_lebih_dari_satu_tahun == True or total_pembelian_terakhir > 5000000:
    print("Pelanggan termasuk dalam VIP.")
print()

### Challenge
permintaan_masuk = {
    "kode_req": "REQ-004",
    "info_pelanggan": {
        "id": 2005,
        "nama": "Jaya Farm",
        "status_aktif": True
    },
    "bahan_yang_diminta": [
        'jagung', 'dedak', 'gandum', 'tepung tulang', 
        'jagung', 'gandum', 'premix vitamin'
    ],
    "butuh_segera": False
}

aturan1_terpenuhi = permintaan_masuk["info_pelanggan"]["status_aktif"]
aturan2_terpenuhi = len(set(permintaan_masuk["bahan_yang_diminta"])) <= 5
aturan3_terpenuhi = "premix vitamin" in permintaan_masuk["bahan_yang_diminta"]
print("Aturan 1 terpenuhi:", aturan1_terpenuhi)
print("Aturan 2 terpenuhi:", aturan2_terpenuhi)
print("Aturan 3 terpenuhi:", aturan3_terpenuhi)

apakah_disetujui = (
    aturan1_terpenuhi and
    aturan2_terpenuhi and
    aturan3_terpenuhi
)
print("Apakah permintaan disetujui?", apakah_disetujui)

hasil_validasi = {
    "kode_req": permintaan_masuk["kode_req"],
    "disetujui": apakah_disetujui,
}
print("Hasil Validasi Permintaan:", hasil_validasi)