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

nomor = 1
print("Daftar Bahan yang Diminta: ")
for bahan in permintaan_masuk["bahan_yang_diminta"]:
    print(f"{nomor}.", bahan)
    nomor = nomor + 1


### Challenge

batch_permintaan = [
    { # Seharusnya Lolos
        "kode_req": "REQ-101",
        "pelanggan": {"nama": "Jaya Farm", "status_aktif": True},
        "bahan": ['jagung', 'dedak', 'premix vitamin']
    },
    { # Seharusnya Gagal: Pelanggan tidak aktif
        "kode_req": "REQ-102",
        "pelanggan": {"nama": "Mundur Jaya", "status_aktif": False},
        "bahan": ['jagung', 'dedak', 'premix vitamin']
    },
    { # Seharusnya Gagal: Bahan lebih dari 3
        "kode_req": "REQ-103",
        "pelanggan": {"nama": "Ternak Sejahtera", "status_aktif": True},
        "bahan": ['jagung', 'dedak', 'gandum', 'mineral']
    },
    { # Seharusnya Gagal: Tidak ada premix vitamin
        "kode_req": "REQ-104",
        "pelanggan": {"nama": "Sumber Pangan", "status_aktif": True},
        "bahan": ['gandum', 'bekatul']
    }
]

aturan1_terpenuhi = [batch_permintaan[i]["pelanggan"]["status_aktif"] for i in range(len(batch_permintaan))]
aturan2_terpenuhi = [len(set(batch_permintaan[i]["bahan"])) <= 3 for i in range(len(batch_permintaan))]
aturan3_terpenuhi = ["premix vitamin" in batch_permintaan[i]["bahan"] for i in range(len(batch_permintaan))]

permintaan_disetujui = []
permintaan_ditolak = []

for jumlah_batch_permintaan in range(len(batch_permintaan)):
    apakah_disetujui = (
        aturan1_terpenuhi[jumlah_batch_permintaan] and
        aturan2_terpenuhi[jumlah_batch_permintaan] and
        aturan3_terpenuhi[jumlah_batch_permintaan]
    )
        
    if apakah_disetujui:
        permintaan_disetujui.append(batch_permintaan[jumlah_batch_permintaan]['kode_req'])
    elif not aturan1_terpenuhi[jumlah_batch_permintaan]:
        permintaan_ditolak.append((batch_permintaan[jumlah_batch_permintaan]['kode_req'], "Pelanggan tidak aktif"))
    elif not aturan2_terpenuhi[jumlah_batch_permintaan]:
        permintaan_ditolak.append((batch_permintaan[jumlah_batch_permintaan]['kode_req'], "Bahan lebih dari 3"))
    elif not aturan3_terpenuhi[jumlah_batch_permintaan]:
        permintaan_ditolak.append((batch_permintaan[jumlah_batch_permintaan]['kode_req'], "Bahan wajib tidak ada"))

    print()

print("--- Laporan Validasi Batch ---")
print("Total Permintaan Diproses:", len(batch_permintaan))
print("Total Permintaan Disetujui:", len(permintaan_disetujui))
print("Total Permintaan Ditolak:", len(permintaan_ditolak))
print()
print("--- Daftar Permintaan Disetujui ---")
for kode in permintaan_disetujui:
    print(f"- {kode}")
print()
print("--- Rincian Permintaan Ditolak ---")
for kode, alasan in permintaan_ditolak:
    print(f"- {kode}: {alasan}")