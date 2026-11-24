# Panduan mengelola bank soal

Sumber utama bank soal adalah `data/bank.json`. File di `content/*.txt` adalah arsip revisi v2. Setelah diterapkan, posisi kunci dan beberapa teks opsi masih diubah lagi oleh `balance.py` dan `fixopt.py`. Karena itu, **jangan menerapkan ulang file lama**. Selalu mulai dari `dump`.

## Alur kerja

```bash
# 1. Ambil soal satu PPT dalam format revisi
python3 tools/bank_tool.py dump tir > content/tir_edit.txt

# 2. Edit file tersebut (hapus blok yang tidak diubah), lalu terapkan
python3 tools/bank_tool.py apply content/tir_edit.txt

# 3. Ratakan posisi kunci A–E (hanya soal non-locked 5 opsi)
python3 tools/balance.py tir

# 4. Cek anti-clue; perbaiki soal yang kuncinya menonjol
python3 tools/bank_tool.py validate --ppt tir
python3 tools/showclue.py tir            # daftar soal "kunci menonjol"
python3 tools/fixopt.py perbaikan.txt    # baris: ID HURUF | teks opsi baru

# 5. Bangun & commit
python3 build.py
git add -A && git commit -m "Revisi soal PPT tir"
```

## Format blok revisi

```
#123 d=2 ty=application
s: stem baru (hanya soal non-locked; boleh HTML)
ks: konsep yang diuji
kw: kata kunci 1; kata kunci 2
an: analisis kasus / cara berpikir menuju jawaban
A: teks opsi || fakta tentang opsi || alasan benar/salah
B*: teks opsi kunci || fakta || alasan          (* = kunci)
C: = || fakta || alasan                         (= mempertahankan teks lama)
D: ...
E: ...
p: clinical pearl (menggantikan p lama)
n+: catatan tambahan (ditambahkan ke n lama)
ref: referensi khusus (default: judul PPT + dosen + topik)
```

- `d`: 1 mudah, 2 sedang, 3 sulit.
- `ty`: `recall`, `understanding`, `application`, `analysis`, `integrated`.
- Blok tanpa baris opsi hanya memperbarui metadata; opsi lama tetap dipakai.
- Field yang tidak ditulis tetap memakai nilai lama.

## Soal terkunci (tag `asli`, `rekon`, `slide`)

Teks stem dan opsi **tidak boleh diubah**, begitu juga jumlah opsi dan kunci. `apply` dan `fixopt` menolak perubahan itu. Untuk soal terkunci, yang boleh dilakukan:

- mengisi metadata (`d`, `ty`, `ks`, `kw`, `an`, `ref`);
- memperbaiki pembahasan opsi dengan menulis `A: = || fakta baru || alasan baru`.

## Aturan anti-clue (dicek `validate`)

| Metrik | Arti | Target |
|---|---|---|
| `kunci_terpanjang_%` | persentase soal yang kuncinya opsi terpanjang | ≈ 20% (setara peluang acak) |
| `kunci_menonjol_%` | kunci terpanjang unik, ≥ 1,2× opsi terpanjang kedua, dan selisih ≥ 8 karakter | **0%** |
| `rasio_panjang_rata2` | panjang kunci ÷ rata-rata panjang distraktor | ≈ 1,0 |
| `posisi_kunci` | sebaran huruf kunci | merata A–E |

Tips menulis soal:

- Tulis setidaknya satu distraktor yang sengaja lebih panjang dari kunci.
- Detail tambahan cukup ditulis di kolom fakta, jangan di teks opsi kunci.
- Semua opsi memakai pola tata bahasa yang sama.
- Hindari kata absolut ("selalu", "tidak pernah") yang hanya muncul di distraktor.

## Menambah gambar

Tambahkan field `img` pada soal, lalu simpan file gambarnya di folder `img/`:

```json
"img": {"src": "img/123.png", "cap": "Foto toraks PA", "credit": "PPT Radiologi, slide 14", "illus": false}
```

`illus: true` menandai gambar ilustrasi yang bukan dari PPT. Gambar bisa diperbesar (zoom) lewat lightbox.

## Menambah soal baru

Tambahkan objek baru ke `data/bank.json` dengan `id` unik (lanjutkan dari id terbesar), `ppt` yang sudah ada, `tag: "baru"`, 5 opsi, dan semua metadata. Setelah itu jalankan `validate`.
