# Soal baru bagian 1: Aspek Laboratorium DM (ldm) dan Ilmu Kedokteran Fisik & Rehabilitasi (kfr)
# Format: q(ppt, topik, stem, [[opsi, fakta/fungsi, alasan], ... kunci di indeks 0], pembahasan, poin_penting, tips, catatan)
N=[]
def q(c,sub,s,o,p,k="",t="",n=""):
    N.append(dict(c=c,sub=sub,s=s,o=o,p=p,k=k,t=t,n=n))

# ============================ ASPEK LABORATORIUM DM ============================
q("ldm","Definisi & klasifikasi","Menurut slide, diabetes melitus didefinisikan sebagai:",
[["Kelompok penyakit metabolik dengan karakteristik hiperglikemia akibat kelainan sekresi insulin, kerja insulin, atau keduanya","Definisi resmi yang dipakai slide (ADA/PERKENI).","Benar: mencakup DM tipe 1 (sekresi) dan tipe 2 (kerja ± sekresi)."],
 ["Penyakit infeksi pankreas yang menyebabkan hiperglikemia","Pankreatitis memang bisa menyebabkan DM, tetapi termasuk tipe spesifik lain.","Terlalu sempit dan bukan definisi umum DM."],
 ["Kelainan metabolik akibat gangguan sekresi insulin saja","Hanya menggambarkan defek sel β.","Mengabaikan resistensi insulin (kerja insulin) yang dominan pada DM tipe 2."],
 ["Destruksi autoimun sel β tanpa kelainan lain","Definisi DM tipe 1 autoimun.","Hanya satu subtipe, bukan definisi DM secara umum."],
 ["Gangguan metabolisme lemak primer yang menyebabkan dislipidemia","Dislipidemia bisa menyertai DM.","Ciri utama DM adalah hiperglikemia, bukan kelainan lemak primer."]],
"DM adalah sindrom hiperglikemia kronik. Mekanismenya bisa di \"pabrik\" (sekresi insulin oleh sel β), di \"kunci pintu\" (kerja insulin/resistensi), atau keduanya.",
"Definisi DM = hiperglikemia + kelainan sekresi insulin, kerja insulin, atau keduanya.",
"Pilihan yang menyebut hanya satu mekanisme (\"saja\") biasanya pengecoh untuk soal definisi.")

q("ldm","Definisi & klasifikasi","Remaja 16 tahun bertubuh normal dengan hiperglikemia ringan sejak usia 12 tahun. Ayah, kakek, dan bibinya juga menderita diabetes sejak usia muda (pola autosomal dominan). Autoantibodi negatif. Menurut klasifikasi etiologi di slide, kondisi ini termasuk:",
[["Tipe spesifik yang berkaitan dengan penyebab lain (diabetes monogenik/MODY)","MODY = maturity-onset diabetes of the young, mutasi gen tunggal, diturunkan autosomal dominan.","Benar: slide memasukkan sindroma diabetes monogenik (neonatal, MODY) ke tipe spesifik lain."],
 ["DM tipe 1 autoimun","Destruksi sel β autoimun dengan autoantibodi positif.","Autoantibodi negatif dan pola keturunan dominan tidak cocok."],
 ["DM tipe 1 idiopatik","Defisiensi insulin absolut tanpa bukti autoimun, sering dengan ketosis.","Pasien hiperglikemia ringan tanpa ketoasidosis dengan riwayat keluarga multigenerasi."],
 ["DM tipe 2","Resistensi insulin dengan defisiensi relatif, umumnya dewasa obesitas.","Usia sangat muda, tubuh normal, pola autosomal dominan lebih khas MODY."],
 ["DM gestasional","Didiagnosis pada trimester 2–3 kehamilan.","Pasien tidak hamil."]],
"Klasifikasi etiologi (slide): tipe 1 (autoimun/idiopatik), tipe 2, DM gestasional, dan tipe spesifik lain: monogenik (neonatal, MODY), penyakit eksokrin pankreas (fibrosis kistik, pankreatitis), akibat obat/zat kimia (glukokortikoid, terapi HIV/AIDS, pascatransplantasi).",
"MODY, fibrosis kistik, pankreatitis, dan DM karena steroid = tipe spesifik lain.",
"Petunjuk MODY: muda + bukan obesitas + autoantibodi negatif + riwayat keluarga beberapa generasi.")

q("ldm","Definisi & klasifikasi","Laki-laki 42 tahun pascatransplantasi ginjal mendapat prednison dosis tinggi jangka panjang. Tiga bulan kemudian GDP 140 mg/dL dan 152 mg/dL pada dua pemeriksaan. Menurut slide, jenis DM ini dikelompokkan sebagai:",
[["Tipe spesifik yang berkaitan dengan penyebab lain (akibat obat/zat kimia)","Glukokortikoid meningkatkan glukoneogenesis dan resistensi insulin.","Benar: slide menyebut penggunaan glukokortikoid pada terapi HIV/AIDS atau setelah transplantasi organ."],
 ["DM tipe 1","Destruksi sel β.","Tidak ada bukti autoimun; pencetusnya jelas obat."],
 ["DM tipe 2 murni","Resistensi insulin terkait gaya hidup.","Ada penyebab spesifik (steroid), sehingga klasifikasinya tipe spesifik lain."],
 ["Prediabetes","GDP 100–125 mg/dL.","GDP pasien ≥ 126 pada dua kali pemeriksaan."],
 ["DM gestasional","Pada kehamilan.","Tidak sesuai."]],
"Steroid ibarat \"menyuruh hati terus memproduksi gula\" sambil membuat otot malas menyerap glukosa.",
"Diagnosis GDP ≥ 126 mg/dL; bila ada penyebab obat → tipe spesifik lain.",
"Lihat penyebab yang jelas dulu: kalau ada obat, penyakit pankreas, atau gen tunggal, jawabannya tipe spesifik lain.")

q("ldm","Definisi & klasifikasi","Anak laki-laki 13 tahun, kurus, datang dengan poliuria, polidipsi, penurunan BB mendadak, dan napas Kussmaul. Pemeriksaan laboratorium yang paling mendukung etiologinya adalah:",
[["GADA positif dengan C-peptide rendah/tidak terdeteksi","Autoantibodi menandakan destruksi autoimun sel β; C-peptide rendah menandakan insulin endogen hampir habis.","Benar: khas DM tipe 1."],
 ["Autoantibodi negatif dengan C-peptide tinggi","Pola resistensi insulin (DM tipe 2).","Tidak cocok dengan anak kurus onset mendadak dengan ketoasidosis."],
 ["HbA1c 5,4% dengan GDP 92 mg/dL","Nilai normal.","Tidak menjelaskan gejala dan ketoasidosis."],
 ["Insulin endogen sangat tinggi","Hiperinsulinemia kompensasi pada DM tipe 2/insulinoma.","Pada tipe 1 insulin endogen rendah."],
 ["Glycated albumin rendah","Penanda kontrol glikemik 2–3 minggu.","Tidak menilai etiologi."]],
"Autoantibodi DM tipe 1 di slide: IAA (insulin autoantibody), GADA, IA-2A, ZnT8A. C-peptide dilepas bersama insulin endogen (1:1) sehingga menggambarkan cadangan insulin, tidak terganggu insulin suntik.",
"Tipe 1: onset mendadak, kurus, ketoasidosis sering, autoantibodi (+), insulin endogen rendah.",
"\"Kurus + muda + ketoasidosis\" → cari jawaban autoantibodi (+) dan C-peptide rendah.")

q("ldm","Definisi & klasifikasi","Menurut tabel perbedaan DM tipe 1 dan tipe 2 di slide, pernyataan berikut benar, <b>KECUALI</b>:",
[["Konkordansi pada kembar identik DM tipe 1 lebih tinggi (90%) dibanding tipe 2 (50%)","Angka tertukar.","Benar sebagai jawaban: di slide tipe 1 = 50%, tipe 2 = 90%."],
 ["Ketoasidosis sering pada tipe 1 dan jarang pada tipe 2","Sesuai tabel.","Pernyataan benar, jadi bukan jawaban."],
 ["Autoantibodi biasanya ada pada tipe 1 dan tidak ada pada tipe 2","Sesuai tabel.","Pernyataan benar."],
 ["Insulin endogen tipe 2 bisa normal, menurun, atau meningkat","Sesuai tabel.","Pernyataan benar."],
 ["Tipe 2 meliputi sekitar 90–95% penderita diabetes di AS","Sesuai tabel.","Pernyataan benar."]],
"Paradoks yang sering ditanyakan: tipe 2 justru lebih \"genetik\" (konkordansi kembar 90%) walau dipicu gaya hidup, sedangkan tipe 1 butuh pemicu lingkungan tambahan (konkordansi 50%).",
"Konkordansi kembar identik: tipe 1 = 50%, tipe 2 = 90%.",
"Untuk soal KECUALI, cari angka yang dibalik.")

q("ldm","Kriteria diagnosis","Laki-laki 45 tahun tanpa keluhan menjalani medical check-up: GDP 118 mg/dL, glukosa 2 jam TTGO 160 mg/dL, HbA1c 6,1%. Interpretasi yang paling tepat adalah:",
[["Prediabetes (GDPT dan TGT)","Semua nilai berada di rentang prediabetes.","Benar: GDP 100–125, GD2PP 140–199, HbA1c 5,7–6,4%."],
 ["Normal","GDP < 100, GD2PP < 140, HbA1c < 5,7%.","Semua nilai pasien di atas normal."],
 ["Diabetes melitus","GDP ≥ 126, GD2PP ≥ 200, atau HbA1c ≥ 6,5%.","Tidak ada nilai yang mencapai ambang DM."],
 ["Prediabetes GDPT saja","Hanya GDP yang terganggu.","GD2PP 160 juga terganggu (TGT)."],
 ["DM gestasional","Pada kehamilan.","Pasien laki-laki."]],
"Tabel kriteria slide (ADA 2025/PERKENI 2021): GDP < 100 / 100–125 / ≥ 126; GD2PP < 140 / 140–199 / ≥ 200; HbA1c < 5,7 / 5,7–6,4 / ≥ 6,5%; GDS ≥ 200 + gejala klasik.",
"Hafal angka: 100–126 (GDP), 140–200 (TTGO), 5,7–6,5 (HbA1c).",
"Bandingkan tiap nilai ke tabel satu per satu; kategori tertinggi yang terpenuhi menentukan diagnosis.")

q("ldm","Kriteria diagnosis","Hasil TTGO seorang pasien: GDP 108 mg/dL dan glukosa 2 jam 214 mg/dL. Interpretasinya adalah:",
[["Diabetes melitus","GD2PP ≥ 200 mg/dL sudah memenuhi kriteria DM.","Benar: satu parameter yang memenuhi kriteria DM menentukan kategori tertinggi."],
 ["Prediabetes GDPT saja","GDP 100–125.","Mengabaikan GD2PP yang sudah ≥ 200."],
 ["Prediabetes TGT saja","GD2PP 140–199.","GD2PP pasien sudah 214."],
 ["Normal","Semua nilai normal.","Kedua nilai tidak normal."],
 ["Tidak dapat diinterpretasi karena kedua nilai tidak searah","Keliru.","Tiap parameter dinilai sendiri; yang tertinggi menentukan."]],
"GDP sering masih \"menutupi\" DM karena resistensi insulin perifer (otot) lebih dulu muncul daripada resistensi hepar. TTGO membuka kedok ini.",
"Satu kriteria DM terpenuhi → diagnosis DM (pada praktik dikonfirmasi ulang bila tanpa gejala).",
"Jangan terkecoh nilai yang \"lebih normal\"; ambil kategori terburuk.")

q("ldm","Kriteria diagnosis","Wanita 50 tahun <b>tanpa keluhan</b> diperiksa saat bakti sosial dengan glukometer kapiler; GDS 230 mg/dL. Sikap yang tepat menurut slide adalah:",
[["Belum bisa didiagnosis DM; perlu konfirmasi dengan plasma vena di laboratorium (GDP, TTGO, atau HbA1c)","GDS ≥ 200 hanya diagnostik bila disertai gejala klasik, dan POCT kapiler hanya untuk skrining.","Benar: dua syarat belum terpenuhi (tanpa gejala dan spesimen kapiler)."],
 ["Langsung didiagnosis DM karena GDS ≥ 200","Berlaku bila ada gejala klasik dan spesimen plasma vena.","Pasien tanpa gejala dan spesimennya kapiler."],
 ["Dinyatakan normal karena tanpa keluhan","Mengabaikan hasil abnormal.","Tetap perlu konfirmasi."],
 ["Didiagnosis prediabetes","Rentang GDS 140–199.","Nilai pasien 230 dan belum terkonfirmasi."],
 ["Langsung diberi insulin","Tatalaksana tanpa diagnosis.","Tidak tepat."]],
"Slide: diagnosis DM WAJIB memakai plasma vena di laboratorium standar; darah kapiler utuh (POCT) hanya untuk skrining massal atau pemantauan mandiri.",
"GDS ≥ 200 + gejala klasik (poliuria, polidipsi, polifagia, BB turun tanpa sebab) = DM.",
"Cek dua hal di soal GDS: ada gejala klasik? spesimennya vena atau kapiler?")

q("ldm","Kriteria diagnosis","Pasangan yang <b>benar</b> antara jenis prediabetes dan mekanisme yang dicerminkannya menurut slide adalah:",
[["IFG – resistensi insulin di hepar; IGT – resistensi insulin perifer (otot)","Saat puasa, glukosa dikendalikan produksi hati; setelah beban glukosa, ditentukan ambilan otot.","Benar: sesuai slide."],
 ["IFG – resistensi insulin otot; IGT – resistensi insulin hepar","Terbalik.","Tidak sesuai fisiologi puasa vs postprandial."],
 ["IFG – destruksi sel β; IGT – destruksi sel α","Keliru.","Bukan mekanisme prediabetes."],
 ["IFG – defisiensi insulin absolut; IGT – kelebihan glukagon","Keliru.","Tidak sesuai slide."],
 ["Keduanya mencerminkan gangguan ginjal","Keliru.","Tidak sesuai."]],
"Analogi: saat puasa, hati adalah \"keran\" glukosa; IFG = keran bocor (hati resisten). Setelah makan, otot adalah \"spons\" penyerap; IGT = spons tidak menyerap (otot resisten). Progresivitas prediabetes ke DM tipe 2 sekitar 5–10% per tahun.",
"IFG = hepar (puasa); IGT = otot (postprandial).",
"Puasa → Hati; Post-prandial → Perifer/otot.")

q("ldm","Pra-analitik & metode","Pasien DM memeriksa sendiri glukosa 2 jam setelah makan dengan glukometer kapiler: 235 mg/dL. Pada saat yang sama, plasma vena di laboratorium 185 mg/dL. Penjelasan yang paling tepat adalah:",
[["Glukosa post-prandial kapiler memang 20–70 mg/dL lebih tinggi daripada vena karena ambilan glukosa oleh jaringan","Darah kapiler lebih mendekati darah arteri; di vena glukosa sudah diambil jaringan.","Benar: sesuai tabel vena vs kapiler di slide."],
 ["Glukometer pasti rusak","Selisih ini fisiologis.","Tidak perlu menyimpulkan alat rusak."],
 ["Plasma vena selalu lebih tinggi daripada kapiler","Terbalik pada keadaan post-prandial.","Saat puasa nilainya hampir sama; post-prandial kapiler lebih tinggi."],
 ["Perbedaan disebabkan pasien belum puasa 8 jam","Pemeriksaan memang post-prandial.","Bukan penjelasan selisih vena-kapiler."],
 ["Darah kapiler tidak dipengaruhi hematokrit dan suhu","Keliru.","Slide: POCT dipengaruhi hematokrit, hipoperfusi, dan suhu."]],
"Tabel slide: puasa, kapiler sama atau sekitar 2–5 mg/dL lebih rendah dari plasma; post-prandial, kapiler 20–70 mg/dL lebih tinggi. Plasma vena: presisi tinggi (CV < 2%), gold standard diagnosis.",
"Diagnosis = plasma vena. POCT kapiler = skrining & pemantauan mandiri.",
"Post-prandial: kapiler > vena (ingat \"jaringan sudah makan sebagian gula di perjalanan\").")

q("ldm","Pra-analitik & metode","Persiapan pasien untuk pemeriksaan glukosa darah puasa yang <b>benar</b> menurut slide adalah:",
[["Puasa tanpa asupan kalori 8–12 jam, air putih boleh, darah diambil pagi pukul 07.00–09.00","Air putih mencegah hemokonsentrasi; pagi hari meminimalkan variasi sirkadian kortisol.","Benar: sesuai slide."],
 ["Puasa 4 jam, boleh minum teh manis","Masih ada asupan kalori.","Puasa terlalu singkat dan teh manis mengandung gula."],
 ["Puasa 24 jam tanpa minum sama sekali","Berlebihan.","Dehidrasi menyebabkan hemokonsentrasi; puasa > 12 jam juga tidak dianjurkan."],
 ["Puasa 8 jam, darah diambil sore hari","Waktu tidak ideal.","Kortisol bervariasi sirkadian; slide menganjurkan pagi."],
 ["Tidak perlu puasa","Itu untuk GDS.","GDP mensyaratkan puasa."]],
"Kortisol adalah hormon kontra-insulin dengan puncak pagi. Pengambilan sampel pada jam yang konsisten membuat hasil bisa dibandingkan.",
"GDP: puasa 8–12 jam, air putih boleh, pagi 07.00–09.00.",
"Pilihan dengan angka \"8–12 jam\" + \"air putih boleh\" hampir selalu benar.")

q("ldm","Pra-analitik & metode","Seorang pasien menjalani TTGO. Ia puasa 10 jam dan diberi 75 g glukosa anhidrat dalam 250 mL air yang diminum habis dalam 3 menit. Selama menunggu 2 jam, ia merokok dan berjalan-jalan di halaman rumah sakit. Menurut protokol slide, hal yang membuat hasil TTGO kurang valid adalah:",
[["Merokok dan aktivitas fisik selama menunggu 2 jam","Rokok (stres simpatis) dan olahraga (ambilan glukosa otot) mengubah kadar glukosa.","Benar: slide mensyaratkan pasien istirahat/duduk, tidak merokok atau berolahraga."],
 ["Volume air 250 mL","Sesuai protokol 250–300 mL.","Bukan kesalahan."],
 ["Glukosa diminum dalam 3 menit","Sesuai protokol (< 5 menit).","Bukan kesalahan."],
 ["Puasa 10 jam","Sesuai rentang 8–12 jam.","Bukan kesalahan."],
 ["Beban 75 g glukosa anhidrat","Sesuai protokol.","Bukan kesalahan."]],
"Protokol TTGO slide: (1) diet karbohidrat cukup ≥ 150 g/hari selama 3 hari; (2) puasa 8–12 jam, ambil GDP; (3) 75 g glukosa anhidrat dalam 250–300 mL air, habis < 5 menit; (4) istirahat 2 jam tanpa merokok/olahraga, ambil GD2PP. Indikasi: kasus borderline, skrining DMG, evaluasi riwayat prediabetes.",
"Angka TTGO: 3 hari, 150 g, 8–12 jam, 75 g, 250–300 mL, < 5 menit, 2 jam.",
"Kalau soal menyebut kegiatan pasien selama menunggu, itulah kesalahannya.")

q("ldm","Pra-analitik & metode","Seorang wanita akan menjalani TTGO besok pagi. Tiga hari terakhir ia diet sangat rendah karbohidrat (± 50 g/hari) untuk menurunkan berat badan. Kemungkinan pengaruhnya terhadap hasil TTGO adalah:",
[["Hasil bisa positif palsu (glukosa 2 jam tinggi palsu) karena slide mensyaratkan diet karbohidrat cukup ≥ 150 g/hari selama 3 hari","Diet rendah karbohidrat menurunkan kesiapan sekresi insulin dan sensitivitas terhadap beban glukosa.","Benar: syarat persiapan TTGO tidak terpenuhi."],
 ["Hasil pasti lebih rendah dari sebenarnya","Kebalikannya.","Toleransi glukosa justru tampak lebih buruk."],
 ["Tidak berpengaruh karena pasien tetap puasa","Keliru.","Persiapan 3 hari termasuk syarat protokol."],
 ["Hanya memengaruhi HbA1c","Keliru.","HbA1c mencerminkan 2–3 bulan, bukan 3 hari."],
 ["Membuat TTGO tidak perlu dilakukan","Keliru.","Tes perlu ditunda dan diulang dengan persiapan benar."]],
"Analogi: pabrik insulin yang tiga hari \"libur\" karena jarang ada gula akan kaget saat tiba-tiba datang 75 g glukosa, sehingga responnya lambat.",
"Persiapan TTGO: karbohidrat ≥ 150 g/hari selama 3 hari sebelumnya.",
"Kesalahan persiapan TTGO cenderung membuat hasil tampak lebih buruk (positif palsu).",
"Mekanisme positif palsu adalah pelengkap fisiologi; slide hanya mencantumkan syarat diet 150 g/hari.")

q("ldm","HbA1c","Pembentukan HbA1c yang benar menurut slide adalah:",
[["Reaksi kondensasi non-enzimatik glukosa dengan gugus amino terminal valin pada rantai β hemoglobin A0, irreversibel, selama masa hidup eritrosit (± 120 hari)","Glukosa + Hb → basa Schiff (reversibel) → produk Amadori (stabil).","Benar: sesuai slide."],
 ["Reaksi enzimatik reversibel yang mencerminkan glukosa 1 hari terakhir","Keliru: glikasi bersifat non-enzimatik.","Tidak sesuai."],
 ["Ikatan glukosa dengan rantai α hemoglobin, mencerminkan 24 jam","Keliru.","HbA1c terbentuk di valin N-terminal rantai β."],
 ["Ikatan glukosa dengan albumin, mencerminkan 2–3 minggu","Itu glycated albumin.","Bukan HbA1c."],
 ["Ikatan glukosa dengan hemoglobin F, mencerminkan 1 tahun","Keliru.","HbA1c dari HbA0 dewasa."]],
"Analogi: glukosa seperti \"gula yang menempel\" di eritrosit dan tidak bisa dicuci. Makin lama dan makin tinggi kadar gula, makin banyak yang menempel, sampai eritrosit dibuang (± 120 hari).",
"HbA1c: non-enzimatik, valin N-terminal rantai β HbA0, irreversibel, ± 120 hari, menilai 8–12 minggu terakhir.",
"\"Non-enzimatik\" dan \"irreversibel\" adalah kata kunci HbA1c.")

q("ldm","HbA1c","Wanita 28 tahun dengan talasemia β mayor yang rutin transfusi tiap 4 minggu juga menderita DM. Pemeriksaan untuk memantau kontrol glikemiknya yang paling tepat adalah:",
[["Glycated albumin (GA)","Glikasi albumin tidak bergantung pada umur eritrosit; menggambarkan 2–3 minggu terakhir.","Benar: slide menyarankan GA bila HbA1c tidak dapat dipakai."],
 ["HbA1c tetap tiap 3 bulan","Tidak andal pada hemoglobinopati dan transfusi.","Slide menyebut HbA1c tidak dapat dipakai pada kondisi ini."],
 ["C-peptide","Menilai cadangan insulin endogen.","Bukan penanda kontrol glikemik."],
 ["Autoantibodi GADA","Menilai etiologi autoimun.","Bukan pemantauan."],
 ["Kolesterol total","Profil lipid.","Tidak menilai glikemik."]],
"Slide: HbA1c tidak dapat dipakai pada anemia, hemoglobinopati, riwayat transfusi 2–3 bulan terakhir, keadaan yang memengaruhi umur eritrosit, dan gangguan fungsi ginjal. Alternatifnya glycated albumin (atau fruktosamin).",
"HbA1c tidak andal bila umur eritrosit berubah → pakai glycated albumin.",
"Kata \"transfusi\", \"talasemia\", \"anemia\", atau \"gagal ginjal\" pada soal HbA1c → jawabannya GA.")

q("ldm","HbA1c","Pasien DM tipe 2 baru mengganti terapi. Dokter ingin menilai efek perubahan terapi tersebut dengan HbA1c. Menurut slide, frekuensi pemeriksaan yang tepat adalah:",
[["Setiap 3 bulan; bila sasaran tercapai dan stabil, minimal 2 kali setahun","HbA1c menggambarkan efek terapi 8–12 minggu sebelumnya.","Benar: sesuai slide."],
 ["Setiap minggu","Terlalu sering.","HbA1c belum berubah bermakna dalam seminggu."],
 ["Setiap bulan","Frekuensi pemeriksaan glukosa darah, bukan HbA1c.","Slide: glukosa darah setidaknya sebulan sekali."],
 ["Setiap tahun","Terlalu jarang untuk evaluasi terapi baru.","Tidak sesuai."],
 ["Cukup sekali saat diagnosis","Keliru.","HbA1c adalah alat pemantauan berkala."]],
"Karena HbA1c merekam rata-rata glukosa ± 3 bulan, memeriksanya lebih sering tidak memberi informasi baru.",
"HbA1c tiap 3 bulan (stabil: ≥ 2x/tahun); glukosa darah ≥ 1x/bulan.",
"Hubungkan frekuensi dengan umur eritrosit 120 hari.")

q("ldm","HbA1c","Menurut data UKPDS 35 yang ditampilkan di slide, setiap penurunan rata-rata HbA1c 1% memberikan penurunan risiko <b>terbesar</b> pada:",
[["Amputasi atau penyakit pembuluh darah tepi yang fatal (43%)","Angka tertinggi di slide.","Benar."],
 ["Komplikasi mikrovaskular (37%)","Angka kedua tertinggi.","Bukan yang terbesar."],
 ["Kematian terkait diabetes (21%)","Sesuai slide.","Lebih kecil dari 43%."],
 ["Serangan jantung (14%)","Sesuai slide.","Lebih kecil."],
 ["Stroke (12%)","Penurunan terkecil di slide.","Bukan yang terbesar."]],
"UKPDS 35 (Stratton dkk, BMJ 2000): HbA1c turun 1% → kematian terkait DM −21%, mikrovaskular −37%, infark −14%, amputasi/PAD fatal −43%, stroke −12%.",
"Urutan: amputasi 43 > mikrovaskular 37 > kematian 21 > jantung 14 > stroke 12.",
"Jembatan: \"4-3-2-1-1\" (43, 37, 21, 14, 12).")

q("ldm","Pemantauan & sasaran","Pasien DM tipe 2 kontrol rutin. Menurut tabel sasaran pengendalian PERKENI di slide, nilai berikut menunjukkan sasaran sudah tercapai, <b>KECUALI</b>:",
[["Glukosa darah kapiler 2 jam setelah makan 210 mg/dL","Sasaran 1–2 jam setelah makan < 180 mg/dL.","Benar sebagai jawaban: belum tercapai."],
 ["HbA1c 6,8%","Sasaran < 7% atau individual.","Sudah tercapai."],
 ["Glukosa kapiler sebelum makan 110 mg/dL","Sasaran 80–130 mg/dL.","Sudah tercapai."],
 ["Tekanan darah 132/84 mmHg","Sasaran sistolik < 140, diastolik < 90.","Sudah tercapai."],
 ["IMT 22 kg/m²","Sasaran 18,5–22,9.","Sudah tercapai."]],
"Sasaran slide: IMT 18,5–22,9; TD < 140/< 90; HbA1c < 7% atau individual; kapiler puasa/sebelum makan 80–130; 1–2 jam setelah makan < 180; LDL < 100 (< 70 bila risiko tinggi PKV); TG < 150; Apo-B < 90.",
"Kapiler: preprandial 80–130, postprandial < 180, HbA1c < 7%.",
"Cek tiap angka ke tabel sasaran; yang keluar rentang adalah jawabannya.",
"Koreksi slide: sasaran HDL tertulis \"< 40 (laki-laki), < 50 (perempuan)\". Yang benar secara klinis adalah HDL > 40 mg/dL pada laki-laki dan > 50 mg/dL pada perempuan, karena HDL rendah adalah faktor risiko.")

q("ldm","Pemantauan & sasaran","Pasien DM dengan riwayat infark miokard (risiko tinggi penyakit kardiovaskular). Menurut sasaran pengendalian di slide, target LDL-C dan Apo-B yang tepat adalah:",
[["LDL < 70 mg/dL dan Apo-B < 90 mg/dL","Target lipid ketat untuk risiko tinggi PKV.","Benar: sesuai tabel slide."],
 ["LDL < 100 mg/dL","Target LDL umum tanpa risiko tinggi PKV.","Pasien berisiko tinggi, jadi target lebih ketat."],
 ["LDL < 130 mg/dL","Terlalu longgar.","Tidak sesuai."],
 ["LDL < 160 mg/dL","Ambang LDL \"tinggi\" pada klasifikasi.","Bukan target terapi."],
 ["Apo-B < 150 mg/dL","Terlalu longgar.","Slide: Apo-B < 90."]],
"Apo-B adalah protein pada setiap partikel aterogenik (LDL, VLDL, IDL); semakin banyak Apo-B, semakin banyak \"truk\" pembawa kolesterol ke dinding arteri.",
"LDL < 100 (umum), < 70 (risiko tinggi PKV); Apo-B < 90.",
"Riwayat infark/stroke = risiko tinggi → pilih angka paling ketat.")

q("ldm","Komplikasi & kegawatdaruratan","Laki-laki 68 tahun DM tipe 2 dibawa dengan penurunan kesadaran setelah 5 hari diare. Lab: glukosa plasma 760 mg/dL, Na 146 mEq/L, pH arteri 7,35, bikarbonat 23 mEq/L, keton urin sedikit. Diagnosis yang paling tepat adalah:",
[["Hiperglikemia hiperosmolar (HHS)","Glukosa > 600, pH > 7,30, bikarbonat > 18, keton sedikit, osmolalitas efektif > 320.","Benar: osmolalitas efektif = 2 × 146 + 760/18 = 292 + 42 = 334 mOsm/kg."],
 ["Ketoasidosis diabetik ringan","pH 7,25–7,30, bikarbonat 15–18, keton positif.","pH dan bikarbonat pasien normal, keton hanya sedikit."],
 ["Ketoasidosis diabetik berat","pH < 7,00, bikarbonat < 10.","Tidak sesuai."],
 ["Hipoglikemia level 3","Glukosa rendah dengan gangguan kognitif berat.","Glukosa pasien sangat tinggi."],
 ["Asidosis laktat","pH rendah dengan laktat tinggi.","pH pasien normal."]],
"HHS khas pada lansia DM tipe 2 dengan dehidrasi berat. Insulin masih cukup untuk mencegah ketosis berat, tetapi tidak cukup mencegah hiperglikemia ekstrem.",
"HHS: glukosa > 600, pH > 7,30, HCO3 > 18, keton sedikit, osmolalitas efektif > 320 mOsm/kg.",
"Osmolalitas efektif = 2 × Na + glukosa/18 (urea tidak dihitung).")

q("ldm","Komplikasi & kegawatdaruratan","Wanita 22 tahun DM tipe 1 datang dengan muntah, nyeri perut, dan mengantuk tetapi masih bisa diajak bicara. Lab: glukosa 420 mg/dL, pH 7,12, bikarbonat 12 mEq/L, Na 134, Cl 100 mEq/L, keton serum positif. Klasifikasi yang tepat adalah:",
[["Ketoasidosis diabetik sedang","pH 7,00–< 7,24, bikarbonat 10–< 15, anion gap > 12, status mental sadar/mengantuk.","Benar: anion gap = 134 − (100 + 12) = 22."],
 ["Ketoasidosis diabetik ringan","pH 7,25–7,30, bikarbonat 15–18, sadar.","pH dan bikarbonat pasien lebih rendah."],
 ["Ketoasidosis diabetik berat","pH < 7,00, bikarbonat < 10, stupor/koma.","Pasien belum masuk kriteria berat."],
 ["HHS","Glukosa > 600, pH > 7,30, keton sedikit.","Tidak sesuai."],
 ["Hipoglikemia level 2","Glukosa < 54 mg/dL.","Glukosa pasien tinggi."]],
"Tabel DKA vs HHS (Kitabchi, ADA 2009) di slide. Keton diperiksa dengan reaksi nitroprusida. Anion gap = Na − (Cl + HCO3).",
"DKA ringan/sedang/berat ditentukan terutama oleh pH, bikarbonat, dan status mental.",
"Hafalkan pasangan pH–HCO3: ringan 7,25–7,30/15–18, sedang 7,00–7,24/10–15, berat < 7,00/< 10.")

q("ldm","Komplikasi & kegawatdaruratan","Pasien DM pengguna sulfonilurea mendadak gemetar, berkeringat dingin, dan berdebar. Glukosa plasma 50 mg/dL. Ia masih sadar dan bisa minum teh manis sendiri. Menurut klasifikasi ADA di slide, hipoglikemia ini termasuk:",
[["Level 2 (sedang)","Glukosa < 54 mg/dL, signifikan secara klinis.","Benar: angka < 54 menentukan level 2 walaupun pasien masih mandiri."],
 ["Level 1 (ringan)","Glukosa 54–69 mg/dL.","Nilai pasien di bawah 54."],
 ["Level 3 (berat)","Gangguan kognitif/fisik berat yang memerlukan bantuan orang lain, tanpa ambang angka.","Pasien masih bisa menolong diri sendiri."],
 ["Normal","Glukosa ≥ 70 mg/dL.","Tidak sesuai."],
 ["Hiperglikemia reaktif","Keliru.","Tidak sesuai."]],
"Level 1 dan 2 ditentukan oleh angka; level 3 ditentukan oleh klinis (butuh bantuan orang lain), berapa pun angkanya.",
"Level 1: 54–69; level 2: < 54; level 3: butuh bantuan orang lain.",
"Bila pasien pingsan atau butuh bantuan → level 3 tanpa melihat angka.")

q("ldm","Komplikasi & kegawatdaruratan","Pasien DM lansia ditemukan keluarganya bingung dan tidak bisa makan sendiri; keluarga memberinya larutan gula. Glukosa plasma saat diperiksa 58 mg/dL (setelah diberi gula). Klasifikasi hipoglikemianya adalah:",
[["Level 3 (berat)","Ditentukan oleh gangguan kognitif berat yang membutuhkan bantuan orang lain.","Benar: level 3 tidak memakai ambang angka."],
 ["Level 1 karena glukosa 58 mg/dL","Hanya melihat angka.","Mengabaikan kriteria klinis level 3."],
 ["Level 2","Glukosa < 54.","Kriteria klinis lebih menentukan."],
 ["Bukan hipoglikemia","Keliru.","Ada gejala neuroglikopenia dan butuh bantuan."],
 ["HHS","Glukosa > 600.","Tidak sesuai."]],
"Glukosa yang diukur setelah diberi gula bisa \"menyamarkan\" beratnya episode. Yang dinilai adalah kondisi saat episode: butuh bantuan orang lain.",
"Level 3 = definisi fungsional, bukan angka.",
"Kata kunci \"butuh bantuan orang lain\" → level 3.")

q("ldm","Komplikasi & kegawatdaruratan","Menurut gambar komplikasi di slide, yang termasuk komplikasi <b>mikrovaskular</b> diabetes adalah:",
[["Retinopati, nefropati (penyakit ginjal diabetik), dan neuropati","Kerusakan pembuluh darah kecil.","Benar."],
 ["Penyakit jantung koroner dan stroke","Komplikasi makrovaskular, ± 65% kematian terkait diabetes.","Bukan mikrovaskular."],
 ["Amputasi tungkai non-traumatik","Slide memasukkannya ke makrovaskular (> 60% amputasi non-traumatik).","Bukan mikrovaskular menurut slide."],
 ["Penyakit arteri perifer","Makrovaskular.","Tidak sesuai."],
 ["Hipertensi esensial","Bukan komplikasi mikrovaskular.","Tidak sesuai."]],
"Slide: retinopati penyebab kebutaan baru usia 20–74 tahun; DM penyebab utama gagal ginjal (44% kasus baru 2002); 60–70% pasien mengalami kerusakan saraf.",
"Mikro: mata, ginjal, saraf. Makro: jantung, otak, tungkai.",
"Jembatan mikro: \"RNN\" (Retina, Nefron, Neuron).",
"Pada literatur, amputasi sering disebabkan gabungan neuropati (mikro) dan penyakit arteri perifer (makro). Slide menempatkannya di sisi makrovaskular.")

q("ldm","Pemeriksaan lab","Pasien DM yang sudah mendapat insulin suntik ingin dinilai sisa fungsi sel β-nya. Pemeriksaan yang paling tepat adalah:",
[["C-peptide","Dilepas setara dengan insulin endogen dan tidak terdapat dalam insulin suntik.","Benar: slide memasukkan C-peptide sebagai pemeriksaan cadangan insulin."],
 ["Kadar insulin serum","Ikut terukur dari insulin eksogen.","Tidak bisa membedakan insulin endogen dan suntik."],
 ["HbA1c","Kontrol glikemik jangka menengah.","Tidak menilai sel β."],
 ["Glukosa darah sewaktu","Nilai sesaat.","Tidak menilai sel β."],
 ["Fruktosamin","Kontrol glikemik 2–3 minggu.","Tidak menilai sel β."]],
"Proinsulin dipecah menjadi insulin + C-peptide dalam jumlah setara. Insulin suntik tidak mengandung C-peptide, jadi C-peptide murni menggambarkan produksi tubuh sendiri.",
"C-peptide = cadangan insulin endogen.",
"Kata \"sudah mendapat insulin\" + \"fungsi sel β\" → C-peptide.")

q("ldm","Definisi & klasifikasi","Menurut data IDF Diabetes Atlas ed. 11 (2025) di slide, jumlah penderita DM di dunia pada 2024 dan prediksinya pada 2050 adalah:",
[["589 juta (2024) menjadi 853 juta (2050)","Angka di slide pendahuluan.","Benar."],
 ["463 juta menjadi 700 juta","Angka IDF edisi 9 (2019).","Bukan angka slide."],
 ["537 juta menjadi 783 juta","Angka IDF edisi 10 (2021).","Bukan angka slide."],
 ["853 juta menjadi 589 juta","Terbalik.","Tren justru meningkat."],
 ["20 juta menjadi 35 juta","Angka kasus kanker baru (Globocan).","Bukan DM."]],
"Slide juga menekankan bahwa sebagian besar pasien tidak sadar menderita DM sehingga datang dengan komplikasi, dan biaya terbesar adalah perawatan komplikasi.",
"IDF 2025: 589 juta → 853 juta.",
"Pilih tren yang meningkat; hati-hati angka dari edisi IDF lama.")

# ============================ ILMU KEDOKTERAN FISIK & REHABILITASI ============================
q("kfr","Konsep dasar","Laki-laki 55 tahun, sopir angkot, mengalami stroke dengan kelemahan lengan dan tungkai kanan. Ia kini tidak bisa berjalan dan mandi sendiri, serta tidak bisa lagi bekerja sebagai sopir untuk menafkahi keluarga. Menurut definisi di slide, \"tidak bisa lagi bekerja sebagai sopir\" termasuk:",
[["Handicap","Keterbatasan memenuhi peran sosial normal (pekerjaan) akibat impairment dan disabilitas.","Benar: slide menyebut handicap pada tingkat pekerjaan/peran sosial."],
 ["Impairment","Gangguan struktur/faal tingkat organ (hemiparesis kanan).","Kelemahan anggota gerak adalah impairment, bukan kehilangan peran kerja."],
 ["Disabilitas","Terbatasnya kemampuan melakukan aktivitas normal (gangguan AKS), misalnya tidak bisa berjalan dan mandi.","Disabilitas pada tingkat aktivitas, bukan peran sosial."],
 ["Cacat sekunder","Cacat akibat imobilisasi (dekubitus, kontraktur).","Tidak sesuai."],
 ["Cacat primer","Cacat langsung akibat penyakit (hemiplegi).","Kehilangan pekerjaan adalah dampak sosial, bukan cacat primer."]],
"Tiga tingkat (Braddom): impairment (organ) → disabilitas (aktivitas/AKS) → handicap (peran sosial, pekerjaan, sesuai usia, jenis kelamin, dan sosiokultural).",
"Organ = impairment; AKS = disabilitas; peran/pekerjaan = handicap.",
"Tanyakan: yang rusak organnya, aktivitasnya, atau perannya di masyarakat?")

q("kfr","Konsep dasar","Pada pasien stroke yang sama, \"tidak mampu mandi dan berjalan sendiri\" dikategorikan sebagai:",
[["Disabilitas","Terbatasnya kemampuan melakukan aktivitas normal akibat impairment (gangguan AKS).","Benar."],
 ["Impairment","Gangguan tingkat organ.","Mandi dan berjalan adalah aktivitas, bukan struktur organ."],
 ["Handicap","Gangguan peran sosial.","Tidak tepat untuk aktivitas pribadi."],
 ["Cacat sekunder","Akibat imobilisasi.","Tidak sesuai."],
 ["Pencegahan tingkat pertama","Upaya sebelum penyakit terjadi.","Bukan kategori dampak."]],
"Aktivitas Kehidupan Sehari-hari (AKS/ADL) menurut slide: personal, vokasional, avokasional, dan instrumental.",
"Gangguan AKS = disabilitas.",
"Mandi, makan, berpakaian, berjalan → disabilitas.")

q("kfr","Konsep dasar","Pasien cedera medula spinalis yang dirawat lama di tempat tidur mengalami luka dekubitus di sakrum dan kontraktur lutut. Menurut slide, luka dan kontraktur ini termasuk:",
[["Cacat sekunder","Disebabkan imobilisasi atau pembatasan sebagai bagian pengobatan, atau kelalaian perawatan.","Benar: contoh slide meliputi ulkus dekubitus, kontraktur, atrofi otot, dan osteoporosis."],
 ["Cacat primer","Disebabkan langsung oleh proses patologis (paraplegi pada cedera medula spinalis).","Dekubitus bukan akibat langsung cedera, tetapi akibat imobilisasi."],
 ["Impairment primer","Istilah tidak tepat.","Tidak sesuai klasifikasi slide."],
 ["Handicap","Gangguan peran sosial.","Tidak sesuai."],
 ["Efek samping fisioterapi","Keliru.","Fisioterapi justru mencegahnya."]],
"Cacat sekunder sebenarnya bisa dicegah. Itulah alasan rehabilitasi dimulai sedini mungkin, sejak fase akut.",
"Primer: hemiplegi (stroke), paraplegi (SCI). Sekunder: dekubitus, kontraktur, atrofi, osteoporosis.",
"Kalau penyebabnya \"lama berbaring\" → cacat sekunder.")

q("kfr","Konsep dasar","Seorang pasien pascastroke hari ke-2 di ICU sudah mulai diposisikan dan digerakkan pasif oleh tim rehabilitasi untuk mencegah kontraktur. Menurut konsep pencegahan cacat di slide, hal ini menunjukkan prinsip:",
[["Rehabilitasi dilakukan sedini mungkin, sejak stadium akut, bersama disiplin ilmu lain","Dua prinsip utama pencegahan cacat di slide.","Benar."],
 ["Rehabilitasi baru dimulai setelah pasien pulang","Kebalikan prinsip.","Terlambat mencegah cacat sekunder."],
 ["Rehabilitasi hanya oleh fisioterapis sendiri","Bertentangan dengan pendekatan tim.","Tidak tepat."],
 ["Rehabilitasi hanya untuk pasien kronis","Keliru.","Justru dimulai di fase akut."],
 ["Pencegahan tingkat pertama","Mencegah penyakit terjadi (vaksinasi, edukasi).","Stroke sudah terjadi."]],
"Keuntungan menurut slide: masa perawatan lebih singkat, pengiriman pasien ke pusat rehabilitasi berkurang, dan penanganan komprehensif lewat pendekatan tim.",
"Prinsip: sedini mungkin + pendekatan tim.",
"Rehabilitasi di fase akut = mencegah cacat sekunder.")

q("kfr","Konsep dasar","Pasien diabetes dengan neuropati ringan mendapat edukasi perawatan kaki dan sepatu khusus agar tidak terjadi ulkus yang membatasi fungsi berjalan. Menurut slide, upaya ini termasuk pencegahan:",
[["Tingkat kedua","Dilakukan sesudah ada kelainan/penyakit, ditujukan mencegah timbulnya pembatasan fungsional (cacat ringan).","Benar."],
 ["Tingkat pertama","Mencegah kelainan/penyakit terjadi (vaksinasi, edukasi umum).","Penyakit (DM, neuropati) sudah ada."],
 ["Tingkat ketiga","Segera setelah pembatasan fungsional menetap, untuk mencegah cacat lebih berat.","Belum ada pembatasan fungsional menetap."],
 ["Rehabilitasi vokasional","Persiapan kerja.","Tidak sesuai."],
 ["Paliatif","Perawatan akhir hayat.","Tidak sesuai."]],
"Pencegahan tingkat 1: sebelum penyakit. Tingkat 2: setelah penyakit, sebelum/saat cacat ringan. Tingkat 3: setelah cacat menetap, agar tidak lebih berat.",
"Ada penyakit tapi belum ada cacat menetap → tingkat kedua.",
"Tentukan posisi pasien di timeline: sehat → sakit → cacat ringan → cacat menetap.")

q("kfr","Konsep dasar","Menurut slide, rehabilitasi dikatakan berhasil bila terdapat hal berikut, <b>KECUALI</b>:",
[["Penyakit dasar sembuh total tanpa sisa","Bukan kriteria keberhasilan rehabilitasi.","Benar sebagai jawaban: rehabilitasi bisa berhasil walau gejala sisa tetap ada."],
 ["Pemulihan kondisi fisik","Kriteria di slide.","Benar, bukan jawaban."],
 ["Pemulihan kondisi psikologis","Kriteria di slide.","Benar, bukan jawaban."],
 ["Latihan pravokasional untuk mempersiapkan bekerja","Kriteria di slide.","Benar, bukan jawaban."],
 ["Resosialisasi","Kriteria di slide.","Benar, bukan jawaban."]],
"Tujuan rehabilitasi bukan selalu menyembuhkan, tetapi mengembalikan atau mempertahankan fungsi agar AKS berjalan dan pasien mandiri.",
"Empat kriteria berhasil: fisik, psikologis, pravokasional, resosialisasi.",
"Rehabilitasi = fungsi, bukan kesembuhan penyakit.")

q("kfr","Sejarah","Menurut slide, tokoh yang mendirikan pusat rehabilitasi di Solo pada tahun 1951 adalah:",
[["Prof. dr. Soeharso (ahli bedah)","Pelopor rehabilitasi medik di Indonesia.","Benar."],
 ["Prof. dr. Kariadi","Nama RSUP di Semarang tempat PRU/IRM didirikan tahun 1978.","Bukan pendiri pusat rehabilitasi Solo."],
 ["dr. Cipto Mangunkusumo","Tokoh pergerakan nasional.","Tidak terkait."],
 ["dr. Soetomo","Tokoh Budi Utomo.","Tidak terkait."],
 ["Prof. dr. Sardjito","Rektor pertama UGM.","Tidak terkait."]],
"Slide: rehabilitasi berkembang setelah PD I (ortopedi, fisioterapi, terapi okupasi); diakui sebagai spesialisasi tahun 1947 di AS; di Indonesia Prof. dr. Soeharso (1951, Solo); 1978 PRU (Preventive Rehabilitation Unit)/IRM di RSUP Dr. Kariadi.",
"Soeharso 1951 Solo; AS 1947; Kariadi 1978.",
"Soal sejarah biasanya menanyakan tahun atau tokoh; hafal pasangan Soeharso–Solo–1951.")

q("kfr","Tim rehabilitasi","Anggota tim rehabilitasi medik yang bertugas melakukan assessment, menegakkan diagnosis rehabilitasi, menyusun program, dan mengevaluasi adalah:",
[["Dokter spesialis kedokteran fisik dan rehabilitasi (SpKFR)","Pemimpin tim yang menyusun program rehabilitasi.","Benar."],
 ["Fisioterapis","Melaksanakan terapi fisik (panas, dingin, air, listrik, latihan).","Bukan yang menegakkan diagnosis rehabilitasi."],
 ["Okupasi terapis","Melatih AKS dengan aktivitas.","Tidak sesuai."],
 ["Pekerja sosial medik","Menangani masalah sosial pasien.","Tidak sesuai."],
 ["Psikolog","Menangani aspek psikis.","Tidak sesuai."]],
"Tim KFR (slide): SpKFR, fisioterapis, okupasi terapis, terapis wicara, ortotis-prostetis, pekerja sosial medik, dan psikolog.",
"SpKFR = assessment, diagnosis rehabilitasi, program, evaluasi.",
"\"Diagnosis\" dan \"program\" → dokter SpKFR.")

q("kfr","Tim rehabilitasi","Pasien nyeri punggung bawah mendapat terapi traksi lumbal dan microwave diathermy. Anggota tim yang melaksanakan terapi dengan perantaraan unsur fisika ini adalah:",
[["Fisioterapis","Pengobatan fisik dengan panas, dingin, air, arus listrik, pemijatan, manipulasi, dan latihan.","Benar: traksi dan diatermi adalah modalitas fisioterapi."],
 ["Okupasi terapis","Terapi dengan aktivitas permainan/pekerjaan dan latihan AKS.","Bukan modalitas fisik."],
 ["Ortotis","Membuat alat bantu/penguat.","Tidak sesuai."],
 ["Terapis wicara","Gangguan bicara, bahasa, menelan.","Tidak sesuai."],
 ["Pekerja sosial","Masalah sosial.","Tidak sesuai."]],
"Tujuan fisioterapi (slide): menghilangkan/mengurangi nyeri, mencegah dan mengoreksi kecacatan, memperbaiki sirkulasi darah, memulihkan kekuatan, mobilitas, dan koordinasi. Alat di slide: traksi lumbal, microwave diathermy, parallel bar, ergocycle, shoulder wheel.",
"Fisioterapi = unsur fisika + latihan.",
"Alat fisik (panas, listrik, traksi) → fisioterapis.")

q("kfr","Tim rehabilitasi","Pasien pascastroke dilatih memakai baju, makan dengan sendok yang dimodifikasi, dan menyusun balok mainan untuk melatih koordinasi tangan. Anggota tim yang bertanggung jawab adalah:",
[["Okupasi terapis","Mengarahkan pasien pada aktivitas selektif: permainan/pekerjaan, latihan AKS, penilaian pravokasional.","Benar."],
 ["Fisioterapis","Tujuan sama, tetapi caranya dengan modalitas fisik dan latihan gerak.","Kegiatan berupa aktivitas sehari-hari dan permainan adalah ciri okupasi terapi."],
 ["Terapis wicara","Bicara, bahasa, dan menelan.","Tidak sesuai."],
 ["Psikolog","Masalah psikis.","Tidak sesuai."],
 ["Prostetis","Alat ganti anggota tubuh.","Tidak sesuai."]],
"Slide: tujuan okupasi terapi sama dengan fisioterapi, hanya caranya berbeda, yaitu melalui aktivitas permainan/pekerjaan, latihan AKS, dan penilaian pravokasional.",
"Aktivitas sehari-hari & permainan → okupasi terapi.",
"Bedakan \"latihan gerak/modalitas fisik\" (fisioterapi) dengan \"latihan melakukan aktivitas\" (okupasi).")

q("kfr","Tim rehabilitasi","Pasien diamputasi di bawah lutut akibat ulkus diabetik. Ia membutuhkan kaki palsu. Ahli yang membuat dan mengajarkan pemakaian alat tersebut adalah:",
[["Prostetis","Ahli teknik pembuatan dan pemakaian alat ganti/palsu (protesis).","Benar."],
 ["Ortotis","Ahli alat bantu/penguat (ortosis) seperti brace dan splint.","Ortosis tidak menggantikan anggota tubuh yang hilang."],
 ["Fisioterapis","Melatih kekuatan dan berjalan.","Ikut melatih, tetapi bukan pembuat alat."],
 ["Okupasi terapis","Latihan AKS.","Bukan pembuat protesis."],
 ["Pekerja sosial","Masalah sosial.","Tidak sesuai."]],
"Protesis = alat GANTI (anggota tubuh hilang): protesis atas/bawah siku, atas/bawah lutut. Ortosis = alat BANTU/penguat (anggota tubuh masih ada).",
"Hilang → protesis/prostetis; masih ada tapi lemah → ortosis/ortotis.",
"Jembatan: \"Pro-\" = pengganti (palsu), \"Orto-\" = meluruskan/menguatkan.")

q("kfr","Tim rehabilitasi","Menurut slide, perbedaan brace dan splint adalah:",
[["Brace kaku dan bersendi; splint kaku dan tidak bersendi","Keduanya ortosis (alat bantu/penguat).","Benar."],
 ["Brace tidak bersendi; splint bersendi","Terbalik.","Tidak sesuai slide."],
 ["Brace adalah protesis; splint adalah ortosis","Keliru.","Keduanya ortosis."],
 ["Brace untuk anggota gerak atas saja","Keliru.","Tidak dibatasi lokasi."],
 ["Splint untuk mengganti anggota tubuh yang hilang","Itu protesis.","Keliru."]],
"Macam ortosis di slide: brace (kaku, bersendi), splint (kaku, tidak bersendi), orthopedic shoes (koreksi kaki, mengurangi nyeri). Tujuan ortosis/protesis: mencegah kecacatan, mengoreksi kecacatan, memperbaiki/mengembalikan fungsi.",
"Brace = bersendi; splint = tanpa sendi.",
"\"Brace\" dan \"Bersendi\" sama-sama huruf B.")

q("kfr","Tim rehabilitasi","Pasien pascastroke bicara pelo (cadel, tidak jelas) walaupun mengerti pembicaraan dan bisa memilih kata dengan benar. Menurut slide, gangguan ini termasuk gangguan bicara aspek:",
[["Artikulasi (disartria)","Gangguan koordinasi otot bicara sehingga pengucapan tidak jelas.","Benar: slide menyebut artikulasi: pelo/disartria."],
 ["Bahasa (afasia)","Gangguan memahami atau menyusun bahasa.","Pasien masih mengerti dan memilih kata dengan benar."],
 ["Irama (gagap, latah)","Gangguan kelancaran.","Tidak sesuai."],
 ["Phonasi (suara lemah)","Gangguan produksi suara.","Masalah utamanya kejelasan pengucapan."],
 ["Disfagia","Gangguan menelan.","Tidak sesuai."]],
"Terapi wicara (slide) menangani gangguan bicara (irama: gagap, latah; intonasi; phonasi: suara lemah/kecil; artikulasi: pelo/disartria), bahasa (afasia), dan menelan (disfagia).",
"Pelo = disartria (artikulasi); afasia = bahasa; disfagia = menelan.",
"Pasien mengerti tapi pengucapannya kacau → disartria; tidak mengerti/tak bisa menyusun kata → afasia.")

q("kfr","Tim rehabilitasi","Tugas pekerja sosial medik dalam tim rehabilitasi menurut slide meliputi hal berikut, <b>KECUALI</b>:",
[["Melakukan psikoanalisis untuk mengatasi masalah psikis pasien","Tugas psikolog.","Benar sebagai jawaban."],
 ["Mengumpulkan data latar belakang sosial pasien","Tugas pekerja sosial.","Bukan jawaban."],
 ["Menjadi penghubung antara staf RS, keluarga, dan masyarakat","Tugas pekerja sosial.","Bukan jawaban."],
 ["Memanfaatkan sumber bantuan di masyarakat (lembaga sosial pemerintah/swasta)","Tugas pekerja sosial.","Bukan jawaban."],
 ["Melakukan kunjungan rumah atau ke tempat kerja bila perlu","Tugas pekerja sosial.","Bukan jawaban."]],
"Tujuh tugas pekerja sosial di slide: kumpul data sosial, penghubung, bimbingan/motivasi sosial, memecahkan masalah sosial, memanfaatkan sumber bantuan, tindak lanjut, kunjungan rumah/tempat kerja.",
"Sosial = lingkungan rumah, kerja, masyarakat; psikolog = kondisi jiwa pasien.",
"\"Psikoanalisis\" selalu milik psikolog.")

q("kfr","Tim rehabilitasi","Seminggu setelah kecelakaan yang menyebabkan amputasi, pasien merasa panik, cemas, dan putus asa. Keluarga diminta menenangkan dan memberi keyakinan. Menurut slide, pasien berada pada fase psikologis:",
[["Fase shock mental","Segera setelah serangan: panik, cemas, putus asa; perlu dukungan keluarga.","Benar."],
 ["Fase penolakan","Fase akut, masih panik dan putus asa; perlu dorongan melakukan aktivitas ringan.","Mirip, tetapi penekanan slide pada dorongan aktivitas ringan, bukan sekadar menenangkan."],
 ["Fase penyesuaian","Pemulihan awal: cemas, pahit, depresi; diberi aktivitas baru yang menantang.","Belum sampai fase ini."],
 ["Fase penerimaan","Pemulihan lanjut: gairah hidup naik; dilatih bekerja mencapai sasaran.","Tidak sesuai."],
 ["Fase vokasional","Bukan fase psikologis di slide.","Tidak sesuai."]],
"Urutan fase (slide): shock mental → penolakan → penyesuaian (adjustment) → penerimaan. Psikolog membantu pasien melewati tiap fase.",
"Shock (menenangkan) → penolakan (aktivitas ringan) → penyesuaian (aktivitas menantang) → penerimaan (bekerja ke sasaran).",
"Perhatikan intervensi yang diminta soal: \"menenangkan dan memberi keyakinan\" = shock mental.",
"Fase shock dan penolakan di slide gejalanya sangat mirip; yang membedakan adalah waktunya (segera setelah serangan vs fase akut) dan intervensinya.")

q("kfr","Tim rehabilitasi","Beberapa bulan setelah stroke, pasien mulai bersemangat dan antusias berlatih. Psikolog melatihnya bekerja untuk mencapai sasaran yang telah ditentukan. Fase ini adalah:",
[["Fase penerimaan","Pemulihan lanjut, gairah hidup meningkat.","Benar."],
 ["Fase penyesuaian","Pemulihan awal dengan cemas dan depresi.","Pasien sudah bersemangat."],
 ["Fase penolakan","Masih panik dan putus asa.","Tidak sesuai."],
 ["Fase shock mental","Segera setelah serangan.","Tidak sesuai."],
 ["Fase depresi berat","Bukan nama fase di slide.","Tidak sesuai."]],
"Fase penerimaan adalah target akhir: pasien menerima keadaannya dan bekerja sama dengan tim.",
"Gairah hidup naik = penerimaan.",
"Urutkan emosi: panik → menolak → sedih/cemas → menerima.")

q("kfr","Asesmen & AKS","Untuk menilai faktor <b>fungsi</b> pada pasien nyeri bahu (nyeri dan keterbatasan gerak sendi), alat ukur yang tercantum di slide adalah:",
[["Visual Analog Scale (VAS) dan Range of Motion (ROM)","VAS mengukur intensitas nyeri; ROM mengukur luas gerak sendi.","Benar: tercantum di kolom tindakan faktor fungsi."],
 ["Kuesioner ADL dan uji jalan","Mengukur faktor aktivitas.","Bukan faktor fungsi."],
 ["Skor kualitas hidup","Faktor organisasi/partisipasi.","Tidak sesuai."],
 ["Analisis kehidupan sosial","Faktor lingkungan.","Tidak sesuai."],
 ["Anamnesis epidemiologi","Faktor individu.","Tidak sesuai."]],
"Slide memetakan deskripsi penyakit ke lima faktor: fungsi, aktivitas, organisasi, lingkungan, individu. Tindakan untuk fungsi: VAS, ROM, tes isokinetik; aktivitas: tes koordinasi, kuesioner ADL, uji jalan, uji performa.",
"Fungsi → VAS, ROM, isokinetik.",
"Nyeri dan gerak sendi adalah \"fungsi tubuh\", bukan aktivitas.")

q("kfr","Asesmen & AKS","Lansia pascastroke sudah mampu mandi dan makan sendiri, tetapi belum mampu berbelanja ke pasar, menggunakan telepon, dan mengatur uang. Kemampuan yang belum pulih termasuk AKS:",
[["Instrumental","Aktivitas kompleks untuk hidup mandiri di masyarakat (belanja, telepon, keuangan, memasak).","Benar."],
 ["Personal","Perawatan diri dasar (mandi, makan, berpakaian, toileting).","Pasien sudah mampu AKS personal."],
 ["Vokasional","Aktivitas terkait pekerjaan.","Belanja dan telepon bukan pekerjaan."],
 ["Avokasional","Aktivitas waktu luang/rekreasi.","Tidak sesuai."],
 ["Disabilitas vokasional","Bukan istilah di slide.","Tidak sesuai."]],
"Slide mencantumkan empat jenis AKS: personal, vokasional, avokasional, instrumental.",
"Personal = mengurus diri; instrumental = mengurus urusan rumah tangga & komunitas.",
"Uang, telepon, belanja, obat → instrumental.",
"Definisi tiap jenis AKS adalah pelengkap; slide hanya menyebutkan keempat jenisnya.")

q("kfr","Konsep dasar","Menurut slide, definisi rehabilitasi medik adalah:",
[["Pelayanan kesehatan yang bertujuan mengembangkan fungsi fisik dan psikis individu, dan bila perlu mengembangkan mekanisme kompensasinya agar dapat mandiri","Definisi rehabilitasi medik.","Benar."],
 ["Upaya menyembuhkan penyakit dasar dengan obat","Pengobatan kuratif.","Bukan definisi rehabilitasi medik."],
 ["Pelayanan khusus pasien lanjut usia","Terlalu sempit.","Rehabilitasi untuk semua usia."],
 ["Upaya menempatkan pasien di panti sosial","Keliru.","Tujuannya kemandirian dan partisipasi."],
 ["Tindakan operasi untuk mengoreksi cacat","Tindakan bedah.","Bukan definisi."]],
"Slide membedakan rehabilitasi (semua upaya mengurangi dampak disabilitas dan handicap agar penyandang cacat berpartisipasi aktif di keluarga dan masyarakat) dan rehabilitasi medik (pelayanan kesehatan untuk mengembangkan fungsi fisik dan psikis serta mekanisme kompensasi agar mandiri).",
"Kata kunci: fungsi fisik + psikis + kompensasi + mandiri.",
"Jawaban rehabilitasi selalu berorientasi \"fungsi\" dan \"mandiri\".")
