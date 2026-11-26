# Simulator Blok 3.2 – FK UNWAHAS

Platform latihan & ujian berbasis HTML (satu file, tanpa backend) untuk Modul 3.2 Kelas B.
**742 soal** dari 20 PPT dosen + 1 kelompok recall UAM/UAS di luar PPT, termasuk 55 soal recall UAS 3.2 angkatan Cerebrum (6 asli, 49 direkonstruksi; `src/uas_cere.py`). Buka `index.html` atau GitHub Pages.

## Fitur
- **Mode CBT (ujian):** timer real-time, peta soal (dijawab/kosong/ragu), tandai ragu, sebelumnya/berikutnya, soal & opsi diacak, kirim otomatis saat waktu habis, konfirmasi sebelum kirim, skor otomatis, halaman hasil + review. Kunci tidak tampil sampai ujian selesai. Ujian yang sedang berjalan tetap tersimpan bila halaman ditutup/di-refresh.
- **Pilihan cakupan:** semua materi, per bagian (blok), per PPT, per subtopik, per tingkat kesulitan, soal yang pernah salah, remedial (salah + tebakan), belum pernah dikerjakan, bookmark, ditandai ragu. Filter jenis soal (asli/prediksi/baru/slide/reguler), jumlah soal, waktu per soal.
- **Mode belajar:** umpan balik langsung, pembahasan terstruktur (1 konsep · 2 kata kunci · 3 analisis kasus · 4 alasan kunci · 5 analisis opsi A–E · 6 clinical pearls · 7 referensi), bookmark, ulangi soal.
- **Tingkat keyakinan:** Yakin / Cukup yakin / Menebak (tombol 1–3), matriks interpretasi (benar-yakin = kuasai, salah-yakin = miskonsepsi, benar-menebak = rapuh, dst.) dan rekomendasi remedial.
- **Dashboard & analisis:** KPI, grafik riwayat, matriks keyakinan, PPT/topik terlemah, rekomendasi, bank soal salah, bookmark, riwayat ujian lengkap (bisa dibuka ulang).
- **Bank soal:** pencarian & filter (PPT, kesulitan, jenis kognitif, label).
- **Gambar soal (siap pakai):** field `img` dengan zoom/lightbox dan keterangan sumber; gambar diisi bertahap.
- Responsif (desktop/tablet/HP), tema terang/gelap, shortcut `A`–`E`, `1`–`3`, `←`/`→`, `F`, `B`.
- Data tersimpan di `localStorage` (kunci `sim-blok32-v2`, migrasi otomatis dari v1). Tidak ada sinkronisasi antarperangkat.

## Standar soal
5 opsi A–E (kecuali soal slide asli 2/4 opsi), satu jawaban terbaik, metadata kesulitan (`d`), jenis kognitif (`ty`: recall/understanding/application/analysis/integrated), konsep (`ks`), kata kunci (`kw`), analisis (`an`), referensi.
Desain **anti-clue** dicek otomatis: panjang opsi seimbang (rasio kunci/distraktor rata-rata 1,05), kunci tidak menonjol panjangnya (0%), posisi kunci A–E merata.
Soal asli/recall/slide **tidak diubah teksnya**; hanya ditambah metadata dan pembahasan.
PPT dosen adalah sumber utama; tambahan dari literatur dan koreksi slide ditandai di catatan soal.

Simulator praktikum: [`praktikum-neoplasma/`](praktikum-neoplasma/) — Praktikum Modul 3.2, dua praktikum dalam satu halaman dengan tombol pemilih: **Neoplasma** (32 soal gambar histopatologi) dan **Koagulasi** + POCT/glukosa urin (51 soal pre/post test), plus mode Gabungan. Link langsung: `#neoplasma`, `#koagulasi`; `praktikum-koagulasi/` mengalihkan ke sini. Dibangun ulang dengan `python3 src/praktikum_gabung.py`.

Dokumentasi: [`docs/BANK_GUIDE.md`](docs/BANK_GUIDE.md) (kelola bank soal) · [`docs/DEPLOY.md`](docs/DEPLOY.md) · [`docs/AUDIT.md`](docs/AUDIT.md).

## Simulator terpisah: Recall UAM 3.2 tahun 2024
`recall-uam-2024/index.html` – 70 soal (32 asli, 38 direkonstruksi) dari file "Soal uam 3.2 aldosteron 2024", dikelompokkan per PPT. Kunci dicek ke slide dosen; 8 kunci recall dikoreksi. Tidak digabung ke bank utama.
GitHub Pages: `/recall-uam-2024/`.

## Simulator terpisah: Soal angkatan (Articulatio vs Calcaneus)
`angkatan/index.html` – 351 soal dari 4 file angkatan, tidak digabung ke bank utama:
- Articulatio UAM 3.2 (99 soal; no. 62 duplikat no. 61) dan UAS 3.2 (100 soal) – kunci = stabilo di file angkatan.
- Calcaneus UAM 3.2 (53 soal dari recall: asli + direkonstruksi) dan UAS 3.2 (99 soal; no. 99–106 kosong di file) – kunci = cetak tebal di file angkatan.
- Tombol **Kunci angkatan / Kunci terverifikasi** untuk memilih kunci penilaian. 31 soal kuncinya beda; keduanya selalu ditampilkan di pembahasan beserta alasannya.
- Sumber data: `src/angkatan/k_*.py` (kunci + pembahasan per nomor), `src/angkatan/build_angkatan.py` → `data/angkatan.json`.
GitHub Pages: `/angkatan/`.

## Cara pakai
Buka `index.html` di browser, atau lewat GitHub Pages.

## Struktur
```
index.html            # simulator siap pakai (data sudah tertanam)
data/bank.json        # bank soal (ppts + qs)
src/app/              # platform v2: shell.html, base.css, app.css, app.js (simulator utama)
src/template.html     # tampilan lama (dipakai simulator recall 2024 & angkatan)
tools/                # bank_tool.py (validate/apply/dump), balance.py, fixopt.py, showclue.py
content/              # file revisi v2 per PPT (arsip; lihat docs/BANK_GUIDE.md)
src/build_bank.py     # gabung bank lama + soal baru -> data/bank.json
src/new1.py, new2.py  # soal baru (Aspek Lab DM, KFR, Respon Imun Non Infeksi, Hemodinamik, Tumor Marker 2026)
src/old_banks.json    # bank soal dari kuis-kuis sebelumnya
src/recall_uam_2024.py # recall UAM 3.2 tahun 2024
build.py              # template + data -> index.html dan recall-uam-2024/index.html
src/clean_opts.py     # hapus keterangan dalam kurung di opsi (dipindah ke pembahasan) saat build
data/recall_uam_2024.json # bank soal recall 2024
```

Bangun ulang setelah mengedit soal:
```bash
python3 tools/bank_tool.py validate && python3 build.py
```
`data/bank.json` adalah sumber utama. `src/build_bank.py` (lama) hanya jalan dengan `--force` karena akan menimpa revisi v2.

## Format soal (`data/bank.json`)
```json
{"id":1,"ppt":"ldm","topik":"Kriteria diagnosis","s":"stem (HTML)",
 "o":[["teks opsi","fungsi/fakta","alasan benar/salah"], ...],
 "a":0,"p":"pembahasan","k":"poin penting","t":"tips","n":"catatan slide","tag":"asli|rekon|slide|prediksi|baru|",
 "d":2,"ty":"application","ks":"konsep","kw":["kata kunci"],"an":"analisis","ref":"referensi",
 "img":{"src":"img/x.png","cap":"keterangan","credit":"sumber"}}
```

> Untuk belajar. Kunci disusun berdasarkan slide dosen; perbedaan dengan referensi ditandai di catatan soal.
