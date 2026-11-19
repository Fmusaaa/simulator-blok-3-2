# Simulator Blok 3.2 – FK UNWAHAS

Simulator ujian blok berbasis HTML (satu file, tanpa backend) untuk Modul 3.2 Kelas B.

**687 soal** dikelompokkan per judul asli PPT dosen (20 PPT) + 1 kelompok recall UAM 3.2 yang topiknya di luar PPT tersebut.

## Fitur
- **Latihan per PPT** – jawaban langsung dinilai, pembahasan muncul.
- **Simulasi ujian** – soal diambil proporsional dari PPT yang dipilih, diacak, timer per soal, peta nomor, tandai ragu, konfirmasi sebelum kirim. Kunci baru tampil setelah ujian dikirim.
- **Hasil** – skor, analisis per PPT & per topik, daftar soal salah/kosong, rekomendasi materi, ulangi soal salah.
- **Pembahasan** – kunci, alasan, pembahasan tiap opsi A–E (fungsi/fakta + kenapa benar/salah), poin penting, tips, dan catatan bila slide berbeda dengan referensi.
- Progres disimpan di `localStorage` browser. Tema terang/gelap. Shortcut: `A`–`E`, `←`/`→`, `F`.
- Label soal: **SOAL ASLI** (recall UAM 3.2), **PREDIKSI**, **SOAL BARU**.

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
src/template.html     # tampilan & logika (placeholder __BANK__)
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
python3 src/build_bank.py && python3 build.py
```

## Format soal (`data/bank.json`)
```json
{"id":1,"ppt":"ldm","topik":"Kriteria diagnosis","s":"stem (HTML)",
 "o":[["teks opsi","fungsi/fakta","alasan benar/salah"], ...],
 "a":0,"p":"pembahasan","k":"poin penting","t":"tips","n":"catatan slide","tag":"asli|prediksi|baru|"}
```

> Untuk belajar. Kunci disusun berdasarkan slide dosen; perbedaan dengan referensi ditandai di catatan soal.
