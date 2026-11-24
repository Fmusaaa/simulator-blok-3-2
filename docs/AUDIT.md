# Audit & perubahan v2

## Temuan audit (sebelum v2)

| Aspek | Temuan |
|---|---|
| Petunjuk panjang opsi | 71% soal non-asli punya kunci sebagai opsi terpanjang; rasio panjang kunci/distraktor 1,7 (soal angkatan asli: 33%) |
| Pembahasan opsi | 658/687 soal hanya berisi "Salah." / "Tidak sesuai." untuk distraktor |
| Jumlah opsi | 32 soal < 5 opsi |
| Metadata | Belum ada tingkat kesulitan, jenis kognitif, konsep, atau kata kunci |
| Ujian | Hilang bila halaman di-refresh; riwayat hanya menyimpan persentase |
| Fitur | Belum ada tingkat keyakinan, bookmark, bank soal salah, dashboard, pengaturan |
| Penyimpanan | `localStorage` tanpa pengaman kuota |

## Hasil v2

### Bank soal

- Semua 687 soal punya metadata `d`, `ty`, `ks`, `kw`, dan `an`.
- 602 soal non-locked direvisi, baik opsi maupun pembahasannya. Semua soal non-locked kini 5 opsi.
- 85 soal terkunci (64 asli, 21 contoh soal slide) tidak diubah teksnya; hanya ditambah metadata (dan sebagian pembahasan).

| Metrik anti-clue | Sebelum | Sesudah |
|---|---|---|
| Kunci = opsi terpanjang | 71% | 17,9% |
| Kunci menonjol (≥ 1,2× opsi terpanjang kedua) | tidak diukur | 0% |
| Rasio panjang kunci/distraktor | 1,7 | 1,05 |
| Posisi kunci A/B/C/D/E | condong A | 134/139/144/133/137 |

Sebaran kesulitan: 384 mudah, 277 sedang, 26 sulit.

Jenis kognitif: 321 recall, 96 understanding, 239 application, 26 analysis, 5 integrated.

### Koreksi isi yang ditemukan saat revisi

- Lokasi SGLT2 ditulis tubulus distal; yang benar tubulus proksimal (#378).
- Istilah slide yang keliru dicatat di field `n`, tanpa mengubah kunci slide. Contoh: TSH "di hipotalamus" (#397) dan "penyumbatan" pada hiperemia (#667).
- Simbol "<" pada rentang nilai (misalnya "pH 7,00–< 7,24") sempat terhapus oleh filter tag HTML; filter sudah diperbaiki di tools dan app.
- Build tidak lagi menghapus keterangan dalam kurung di opsi simulator utama, karena keseimbangan panjang opsi sudah dijaga oleh validator.

### Platform

Platform ditulis ulang di `src/app/` (vanilla JS, satu file HTML hasil build). Fitur:

- Mode CBT dan mode belajar.
- Pilihan cakupan: 10 mode.
- Tingkat keyakinan dengan matriks interpretasi.
- Dashboard, analisis, bank soal salah, remedial otomatis, bookmark, riwayat lengkap.
- Resume ujian setelah reload, termasuk kirim otomatis bila waktu habis selama halaman tertutup.
- Pengaturan dan reset data.
- Lightbox gambar soal.

## QA

Uji Playwright (desktop dan HP), tanpa error JavaScript di console:

- alur belajar dan keyakinan;
- bookmark;
- ujian dengan timer, reload, resume, kirim otomatis setelah waktu habis;
- hasil dan review ujian;
- riwayat;
- pencarian bank soal;
- tampilan HP tanpa scroll horizontal.

## Batasan yang diketahui

- Penyimpanan hanya `localStorage`: tidak ada sinkronisasi atau ekspor, sesuai keputusan pengguna.
- Gambar soal belum diisi; fiturnya sudah siap.
- Rujukan per soal masih berupa default: judul PPT, dosen, dan topik. Nomor slide spesifik belum dicantumkan.
