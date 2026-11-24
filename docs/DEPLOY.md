# Deploy (GitHub Pages)

Simulator adalah file HTML statis tanpa backend.

1. Bangun ulang setelah ada perubahan:
   ```bash
   python3 tools/bank_tool.py validate   # harus "error": 0
   python3 build.py                      # index.html, recall-uam-2024/, angkatan/
   ```
2. Commit lalu push ke `main`:
   ```bash
   git add -A && git commit -m "…" && git push origin main
   ```
3. GitHub Pages (Settings → Pages → Deploy from branch `main` / root) menerbitkan:
   - `https://fmusaaa.github.io/simulator-blok-3-2/`: simulator utama
   - `/recall-uam-2024/`: recall UAM 2024
   - `/angkatan/`: soal angkatan

   Pembaruan biasanya tampil 1–2 menit setelah push. Bila browser masih menampilkan versi lama, lakukan hard refresh.

## Uji cepat sebelum push

Uji end-to-end dengan Playwright (skrip di luar repo, `t2.js`) mencakup:

- mode belajar dengan keyakinan;
- bookmark;
- ujian dengan timer dan resume setelah reload;
- auto-submit saat waktu habis;
- hasil dan review ujian;
- riwayat;
- pencarian bank soal;
- tampilan HP tanpa scroll horizontal.

Tanpa Playwright, cukup buka `index.html` di browser dan periksa console untuk memastikan tidak ada error.

## Data pengguna

Progres disimpan di `localStorage` browser dengan kunci `sim-blok32-v2`. Data dari versi lama (`sim-blok32-v1`) dimigrasikan otomatis. Data tidak berpindah antarperangkat dan hilang bila data situs dihapus. Mengganti versi simulator tidak menghapus progres, selama kunci penyimpanannya tetap sama.
