##Dictionary

# contoh data pelanggan disimpan dalam dictionary
data_pelanggan = {
    "nama": "CV Ternak Makmur",
    "id_pelanggan": 203,
    "alamat": "Jl. Pahlawan No.10",
    "produk_langganan": ["P-01", "P-02"],
    "aktif": True
}

print(data_pelanggan)

# mengakses nama pelanggan
print("Nama: ", data_pelanggan["nama"])

#mengubah alamat pelanggan
data_pelanggan["alamat"] = "Jl. Sudirman No.5"
print("Alamat Baru: ", data_pelanggan["alamat"])

# menambah data baru
data_pelanggan["telepon"] = "08123456789"
print(data_pelanggan)

#menghapus data produk langganan
del data_pelanggan["produk_langganan"]
print("Setelah menghapus produk langganan: ", data_pelanggan)
print()

##Set
# list bahan baku yang terdapat duplikat
bahan_mentah = ['Jagung', 'Dedak', 'Gandum', 'Jagung', 'Bekatul', 'Dedak']

# membuat set dari list bahan mentah
bahan_unik = set(bahan_mentah)

print("Bahan Unik: ", bahan_unik)

# menambah bahan baru
bahan_unik.add('kedelai')
print("Setelah penambahan: ", bahan_unik)
print()

#memeriksa apakah bahan ada dalam set
print("Apakah 'Jagung' ada dalam bahan unik? ", 'Jagung' in bahan_unik)
print()


##Latihan

# membuat dictionary untuk mendeskripsikan satu resep pakan
resep_pakan ={
    "id_resep": 101,
    "bahan": ['Jagung', 'Dedak', 'Gandum', 'Jagung'],
    "kadar_air": 12.5,
    "untuk_ternak": "Ayam",
}
print("Resep Pakan: ", resep_pakan)

# mengubah list bahan menjadi set untuk menghilangkan duplikat
resep_pakan["bahan"] = list(set(resep_pakan["bahan"]))
print("Bahan Unik: ", resep_pakan["bahan"])
print()

# manipulasi data resep

resep_pakan["kadar_air"] = 10.0
print("Kadar Air Baru: ", resep_pakan["kadar_air"])

resep_pakan["berat_total_kg"] = 1000
print("Berat Total (kg): ", resep_pakan["berat_total_kg"])


## Challenge for material day1 and day2

info_inti_pelanggan = (
    1002,
    "PT Sinar Ternak"
)

bahan_diajukan = ['jagung', 'dedak', 'tepung ikan', 'kalsium', 'dedak', 'mineral']
bahan_diajukan_unik = set(bahan_diajukan)
print("banyak bahan diajukan: ", len(bahan_diajukan_unik))

data_permintaan_lengkap = {
    "kode_permintaan": "REQ-003",
    f"pelanggan": info_inti_pelanggan,
    "detail_request": {
        "target_ternak": "Ayam Petelur",
        "target_bobot": 1.8,
    },
    "bahan_unik": list(bahan_diajukan_unik),
    "jumlah_bahan_unik": len(bahan_diajukan_unik),
    "status_permintaan": "Diproses"
}
print()

print("Data Permintaan Lengkap:")
print(data_permintaan_lengkap)