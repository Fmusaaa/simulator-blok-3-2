"""Bangun praktikum-koagulasi/index.html memakai mesin halaman praktikum-neoplasma.
Sumber: Petunjuk Praktikum Modul 3.2 (Koagulasi), catatan asistensi dr. Meta Safitri, Sp.PK, kisi-kisi pre/post test.
python3 src/praktikum_koagulasi.py"""
import json, re, collections

CATS = {
 "hemo": {"n": "Hemostasis & skrining", "c": "#3E3889"},
 "rl":   {"n": "Rumpel Leed", "c": "#C4426F"},
 "trom": {"n": "Jumlah trombosit", "c": "#2E8B7A"},
 "bt":   {"n": "Waktu perdarahan", "c": "#D08A1E"},
 "ct":   {"n": "Waktu pembekuan", "c": "#3E6FC4"},
 "bek":  {"n": "Retraksi, konsistensi, lisis", "c": "#7A3FA0"},
 "poct": {"n": "POCT & glukosa urin", "c": "#5D5A7A"},
}
Q = []
def q(c, s, opts, p, n=""):
    a = [i for i, o in enumerate(opts) if o[0].startswith('*')]
    assert len(a) == 1 and len(opts) == 5, s
    Q.append({"c": c, "s": s, "o": [[o[0].lstrip('*'), o[1], o[2]] for o in opts], "a": a[0], "p": p, "n": n})

# ---------------- Hemostasis & skrining ----------------
q("hemo", "Mekanisme hemostasis dipelihara oleh tiga komponen, yaitu…",
 [["*Pembuluh darah, trombosit, dan faktor koagulasi", "Tiga komponen menurut petunjuk praktikum.", "Benar."],
  ["Eritrosit, leukosit, dan trombosit", "Semua sel darah.", "Eritrosit dan leukosit bukan komponen hemostasis utama."],
  ["Hati, limpa, dan sumsum tulang belakang", "Organ pembentuk/penghancur sel darah.", "Bukan komponen mekanisme hemostasis."],
  ["Albumin, globulin, dan fibrinogen plasma", "Protein plasma.", "Hanya fibrinogen yang termasuk faktor koagulasi."],
  ["Plasmin, antitrombin, dan protein C saja", "Sistem antikoagulan/fibrinolitik.", "Bukan tiga komponen penjaga hemostasis."]],
 "Gagal hemostasis → perdarahan abnormal; gagal menjaga darah tetap cair → trombosis.")
q("hemo", "Pemeriksaan skrining koagulasi yang dikerjakan dalam praktikum Modul 3.2 adalah…",
 [["PPT, APTT, kadar fibrinogen, dan kadar D-dimer plasma", "Tes koagulasi laboratorium otomatis.", "PPT dan APTT tidak dipraktikumkan."],
  ["Rumpel Leed, PPT, APTT, dan agregasi trombosit", "Rumpel Leed dikerjakan di Skillab.", "PPT, APTT, dan agregasi tidak dipraktikumkan."],
  ["*Trombosit, waktu perdarahan & pembekuan, retraksi", "Skrining nomor 2–6 di petunjuk praktikum.", "Benar."],
  ["Hitung jenis leukosit, LED, hemoglobin, dan hematokrit", "Pemeriksaan hematologi rutin.", "Bukan skrining koagulasi."],
  ["Masa protrombin, INR, dan kadar faktor VIII", "Tes khusus.", "Tidak dipraktikumkan."]],
 "Skrining: Rumpel Leed (Skillab), jumlah trombosit, waktu perdarahan, waktu pembekuan, retraksi & konsistensi bekuan, lisis bekuan, PPT, APTT. Praktikum: nomor 2–6.",
 "Kisi-kisi pretest: “pemeriksaan koagulasi yang dilakukan, sebutkan 4”.")
q("hemo", "Pemeriksaan skrining hemostasis yang dipakai untuk persiapan pra-operasi adalah…",
 [["Retraksi bekuan, lisis bekuan, dan volume serum", "Menilai fungsi trombosit dan fibrinolisis.", "Tidak disebut untuk pra-operasi."],
  ["*Waktu perdarahan, waktu pembekuan, PPT, dan APTT", "Sesuai petunjuk praktikum.", "Benar."],
  ["Rumpel Leed dan konsistensi bekuan", "Skrining vaskuler/trombosit dan kualitas bekuan.", "Tidak disebut untuk pra-operasi."],
  ["Hitung trombosit metode Fonio saja", "Hitung trombosit tidak langsung.", "Tidak disebut untuk pra-operasi."],
  ["Glukosa darah sewaktu dengan POCT", "Pemeriksaan glukosa.", "Bukan skrining hemostasis."]],
 "Waktu perdarahan, waktu pembekuan, PPT, dan APTT dipakai untuk pra-operasi.")
q("hemo", "Tes yang terutama menilai aktivitas faktor-faktor koagulasi adalah…",
 [["Rumpel Leed", "Ketahanan kapiler (vaskuler + trombosit).", "Salah."],
  ["Waktu perdarahan metode Duke", "Hemostasis ekstravaskuler, pembuluh, trombosit.", "Salah."],
  ["Retraksi bekuan", "Fungsi trombosit.", "Salah."],
  ["*Waktu pembekuan (Lee and White)", "Ukuran aktivitas faktor koagulasi.", "Benar."],
  ["Hitung trombosit metode Brecher", "Jumlah trombosit.", "Salah."]],
 "Faktor koagulasi → waktu pembekuan. Trombosit & pembuluh → Rumpel Leed, waktu perdarahan, retraksi bekuan.")

# ---------------- Rumpel Leed ----------------
q("rl", "Prinsip pemeriksaan Rumpel Leed adalah…",
 [["Mengukur waktu sejak luka standar sampai perdarahan berhenti", "Prinsip waktu perdarahan.", "Salah."],
  ["Menghitung trombosit di bilik hitung setelah sel lain dilisis", "Prinsip Brecher.", "Salah."],
  ["*Menguji ketahanan kapiler dengan membendung vena", "Darah menekan dinding kapiler.", "Benar."],
  ["Mengukur waktu darah lengkap membeku dalam tabung kaca", "Prinsip waktu pembekuan.", "Salah."],
  ["Menilai pengerutan bekuan dan serum yang terperas", "Prinsip retraksi bekuan.", "Salah."]],
 "Rumpel Leed = skrining kelainan vaskuler dan trombosit; alat: tensimeter + stetoskop.")
q("rl", "Pasien dengan TD 120/80 mmHg akan diperiksa Rumpel Leed. Cara pembendungan yang benar adalah…",
 [["*Bendung 100 mmHg (rata-rata sistol-diastol) selama 10 menit", "(120 + 80) ÷ 2 = 100 mmHg, maksimal 100 mmHg.", "Benar."],
  ["Bendung 120 mmHg (setinggi sistol) selama 5 menit", "Tekanan dan durasi salah.", "Salah."],
  ["Bendung 80 mmHg (setinggi diastol) selama 15 menit", "Tidak sesuai petunjuk.", "Salah."],
  ["Bendung 40 mmHg selama 10 menit seperti metode Ivy", "40 mmHg dipakai pada metode Ivy.", "Salah."],
  ["Bendung 150 mmHg selama 2 menit agar cepat terbaca", "Melebihi batas maksimal.", "Salah."]],
 "Bendung dengan rata-rata sistol & diastol, maksimal 100 mmHg, selama 10 menit. Bila rata-rata > 100 mmHg, bendung maksimal 90 mmHg.")
q("rl", "Rata-rata tekanan darah pasien adalah 110 mmHg. Pembendungan Rumpel Leed dilakukan pada tekanan…",
 [["110 mmHg sesuai rata-rata tekanan darah pasien", "Melebihi batas.", "Salah."],
  ["100 mmHg sebagai batas maksimal umum", "Ada aturan khusus bila rata-rata > 100.", "Kurang tepat."],
  ["*Maksimal 90 mmHg", "Aturan khusus bila rata-rata > 100 mmHg.", "Benar."],
  ["40 mmHg seperti pada metode Ivy", "Untuk waktu perdarahan.", "Salah."],
  ["Tidak boleh diperiksa sama sekali", "Tetap boleh dengan batas 90 mmHg.", "Salah."]],
 "Bila rata-rata TD > 100 mmHg → bendungan maksimal 90 mmHg.")
q("rl", "Area pembacaan hasil Rumpel Leed adalah…",
 [["Punggung tangan, di sekitar sendi metakarpofalangeal", "Bukan area baca.", "Salah."],
  ["*Volar lengan bawah ±4 cm di bawah lipat siku, penampang 5 cm", "Sesuai petunjuk.", "Benar."],
  ["Cuping telinga yang telah dipijat sampai hiperemis", "Lokasi tusukan metode Duke.", "Salah."],
  ["Ujung jari tengah atau jari manis tangan", "Lokasi tusukan kapiler/POCT.", "Salah."],
  ["Lengan atas tepat di bawah manset tensimeter", "Bukan area baca.", "Salah."]],
 "Baca di volar lengan bawah ±4 cm di bawah lipat siku, penampang 5 cm.")
q("rl", "Hasil Rumpel Leed dinyatakan POSITIF bila dalam 10 menit timbul petekie…",
 [["Kurang dari 5 buah pada area pembacaan", "Kriteria normal.", "Salah."],
  ["*10 buah atau lebih", "Kriteria positif.", "Benar."],
  ["Kurang dari 10 buah, bahkan setelah diulang", "Kriteria negatif.", "Salah."],
  ["Satu buah saja di mana pun pada lengan", "Tidak sesuai kriteria.", "Salah."],
  ["Hanya bila disertai hematoma di lengan atas", "Tidak sesuai kriteria.", "Salah."]],
 "Normal: tak ada perdarahan / petekie < 5. Positif: ≥ 10 petekie dalam 10 menit. Negatif: tidak ada atau < 10.")
q("rl", "Hal yang harus diperhatikan sebelum pemeriksaan Rumpel Leed untuk menghindari hasil positif palsu adalah…",
 [["Pasien harus puasa minimal 8 jam sebelum pemeriksaan", "Tidak diperlukan.", "Salah."],
  ["Pasien tidak boleh minum air sejak malam sebelumnya", "Tidak relevan.", "Salah."],
  ["Lengan harus dikompres hangat selama 10 menit", "Tidak disebut.", "Salah."],
  ["Pasien harus berbaring telentang selama 30 menit", "Tidak disebut.", "Salah."],
  ["*Bekas gigitan nyamuk atau noda hitam di volar lengan bawah", "Dapat terbaca sebagai petekie.", "Benar."]],
 "Cek bekas gigitan nyamuk/noda hitam sebelum pembendungan.")
q("rl", "Rumpel Leed positif menunjukkan adanya…",
 [["Defisiensi faktor koagulasi jalur intrinsik", "Dinilai dengan waktu pembekuan/APTT.", "Salah."],
  ["Hiperaktivitas sistem fibrinolisis", "Dinilai dengan lisis bekuan.", "Salah."],
  ["*Gangguan vaskuler atau gangguan trombosit", "Arti klinis di petunjuk.", "Benar."],
  ["Hiperkoagulabilitas yang berisiko trombosis", "Tidak dinilai Rumpel Leed.", "Salah."],
  ["Kelebihan heparin di dalam darah", "Memperpanjang waktu pembekuan.", "Salah."]],
 "Kegunaan: menguji kapiler dan fungsi trombosit.")

# ---------------- Jumlah trombosit ----------------
q("trom", "Metode hitung trombosit secara langsung dan tak langsung adalah…",
 [["Langsung: Fonio; tak langsung: Brecher", "Tertukar.", "Salah."],
  ["*Langsung: Brecher dan Herwerden; tak langsung: Fonio", "Sesuai petunjuk.", "Benar."],
  ["Langsung: Duke; tak langsung: Ivy", "Metode waktu perdarahan.", "Salah."],
  ["Langsung: Lee and White; tak langsung: gelas arloji", "Metode waktu pembekuan.", "Salah."],
  ["Langsung: Benedict; tak langsung: Fehling", "Metode reduksi urin.", "Salah."]],
 "Langsung: Brecher, Herwerden (cara sama). Tak langsung: Fonio (hapusan dibandingkan eritrosit).")
q("trom", "Reagen pengencer yang dipakai pada hitung trombosit metode Brecher adalah…",
 [["Larutan Hayem", "Pengencer hitung eritrosit.", "Dipakai pada Fonio untuk hitung eritrosit."],
  ["Magnesium sulfat 14% steril", "Dipakai pada metode Fonio.", "Salah."],
  ["Larutan Turk", "Pengencer hitung leukosit.", "Salah."],
  ["*Amonium oksalat 1%", "Melisiskan sel lain kecuali trombosit.", "Benar."],
  ["Larutan Giemsa 1:9", "Pewarna hapusan.", "Salah."]],
 "R/ amonium oksalat 1 g + akuades ad 100 ml.", "Kisi-kisi pretest: “reagen yang dipakai dalam Brecher”.")
q("trom", "Pada metode Brecher, darah EDTA diisap dengan pipet eritrosit sampai tanda 0,5, lalu diencerkan sebanyak…",
 [["10 kali", "Faktor volume bilik hitung.", "Salah."],
  ["20 kali", "Pengenceran pipet leukosit.", "Salah."],
  ["100 kali", "Bila darah diisap sampai tanda 1.", "Salah."],
  ["*200 kali", "Darah sampai 0,5 dalam pipet eritrosit.", "Benar."],
  ["2000 kali", "Itu faktor pengali akhir.", "Salah."]],
 "Pengenceran 200× × faktor volume 10 = faktor pengali 2000.")
q("trom", "Bilik hitung yang sudah diisi pada metode Brecher diletakkan di atas kapas basah dalam piring petri tertutup selama 15–30 menit. Tujuannya adalah…",
 [["Agar trombosit melisis dan sel lain tetap utuh", "Kebalikan prinsip Brecher.", "Salah."],
  ["Agar darah membeku di dalam bilik hitung", "Darah sudah diencerkan antikoagulan.", "Salah."],
  ["*Agar trombosit mengendap dan cairan tidak menguap", "Kapas basah menjaga kelembapan.", "Benar."],
  ["Agar warna trombosit lebih kontras saat diamati", "Tidak memakai pewarna.", "Salah."],
  ["Agar suhu sampel mencapai 37 °C", "Tidak dipanaskan.", "Salah."]],
 "Trombosit kecil dan ringan; perlu waktu mengendap ke satu bidang fokus.")
q("trom", "Pada metode Brecher, trombosit dihitung pada seluruh bidang baca eritrosit dengan pembesaran 400×. Bila didapat 120 trombosit, jumlah trombosit adalah…",
 [["24.000/µl", "Dikali 200.", "Faktor volume terlewat."],
  ["120.000/µl", "Dikali 1000.", "Salah faktor."],
  ["*240.000/µl", "120 × 2000.", "Benar dan masih normal."],
  ["480.000/µl", "Dikali 4000.", "Salah faktor."],
  ["1.200.000/µl", "Dikali 10.000.", "Salah faktor."]],
 "Brecher: hasil × 2000 = trombosit/µl darah.")
q("trom", "Faktor pengali 2000 pada metode Brecher berasal dari…",
 [["Pengenceran 20× dikali faktor volume 100", "Angka salah.", "Salah."],
  ["Pengenceran 2000× tanpa koreksi volume", "Pengenceran hanya 200×.", "Salah."],
  ["*Pengenceran 200× dikali faktor volume 10", "Volume hitung 1 mm² × 0,1 mm = 0,1 µl.", "Benar."],
  ["Jumlah kotak besar (9) dikali pengenceran 200", "Tidak sesuai.", "Salah."],
  ["Pembesaran mikroskop 400× dikali 5", "Pembesaran tidak masuk rumus.", "Salah."]],
 "Volume = luas × kedalaman; kedalaman 0,1 mm → faktor volume 10. 200 × 10 = 2000.")
q("trom", "Ukuran bilik hitung Neubauer Improved adalah…",
 [["Luas 1 × 1 mm², kedalaman 1 mm", "Tidak sesuai.", "Salah."],
  ["*Luas 3 × 3 mm², kedalaman 0,1 mm", "9 kotak besar @ 1 × 1 mm².", "Benar."],
  ["Luas 3 × 3 mm², kedalaman 0,01 mm", "Kedalaman salah.", "Salah."],
  ["Luas 5 × 5 mm², kedalaman 0,1 mm", "Luas salah.", "Salah."],
  ["Luas 9 × 9 mm², kedalaman 0,2 mm", "Tidak sesuai.", "Salah."]],
 "Kotak sedang: ¼ × ¼ mm² (sudut) dan 1/5 × 1/5 mm² (tengah); kotak kecil: 1/20 × 1/20 mm².")
q("trom", "Pada metode Fonio, magnesium sulfat 14% diteteskan di ujung jari sebelum ditusuk. Fungsinya adalah…",
 [["Sebagai pewarna trombosit pada hapusan", "Pewarnanya Giemsa.", "Salah."],
  ["Melisiskan eritrosit agar trombosit terlihat", "Fungsi amonium oksalat (Brecher).", "Salah."],
  ["Sebagai desinfektan pengganti alkohol", "Ujung jari dibersihkan alkohol dulu.", "Salah."],
  ["*Mencegah trombosit menggumpal (antikoagulan)", "Darah langsung bercampur MgSO₄ saat keluar.", "Benar."],
  ["Mempercepat pembekuan agar luka cepat menutup", "Kebalikannya.", "Salah."]],
 "Reagen Fonio: MgSO₄ 14% steril, Giemsa (1:9), Hayem (hitung eritrosit).")
q("trom", "Hitung trombosit metode Fonio: 60 trombosit per 1000 eritrosit, jumlah eritrosit (Hayem) 5.000.000/µl. Jumlah trombosit adalah…",
 [["30.000/µl", "Salah hitung.", "Salah."],
  ["120.000/µl", "Salah hitung.", "Salah."],
  ["250.000/µl", "Memakai 50 trombosit.", "Salah."],
  ["*300.000/µl", "(5.000.000 ÷ 1000) × 60.", "Benar."],
  ["3.000.000/µl", "Lupa dibagi 1000 dengan benar.", "Salah."]],
 "Fonio: (eritrosit/µl ÷ 1000) × trombosit per 1000 eritrosit.")
q("trom", "Nilai normal hitung trombosit metode Fonio adalah…",
 [["5–10 trombosit per 1000 eritrosit", "Terlalu rendah.", "Salah."],
  ["10–20 trombosit per 100 eritrosit", "Tidak sesuai.", "Salah."],
  ["*40–60 trombosit per 1000 eritrosit", "Sesuai petunjuk.", "Benar."],
  ["150–450 trombosit per 1000 eritrosit", "Rancu dengan nilai per µl.", "Salah."],
  ["400–600 trombosit per 1000 eritrosit", "Terlalu tinggi.", "Salah."]],
 "Normal Fonio: 40–60 per 1000 eritrosit.")
q("trom", "Nilai rujukan jumlah trombosit menurut petunjuk praktikum Modul 3.2 adalah…",
 [["50.000–100.000/µl", "Trombositopenia.", "Salah."],
  ["100.000–150.000/µl", "Trombositopenia ringan.", "Salah."],
  ["*150.000–450.000/µl", "Angka modul (slide: 150.000–400.000).", "Benar."],
  ["500.000–1.000.000/µl", "Trombositosis.", "Salah."],
  ["4.000–10.000/µl", "Rentang leukosit.", "Salah."]],
 "Modul: 150.000–450.000/µl; slide asistensi: 150.000–400.000/µl.",
 "Konfirmasi ke asisten angka mana yang dipakai di tes.")
q("trom", "Jumlah trombosit di bawah normal disebut trombositopenia. Contoh penyakitnya adalah…",
 [["Polisitemia vera (primer)", "Penyebab trombositosis.", "Salah."],
  ["Leukemia mieloid kronik (CML)", "Penyebab trombositosis.", "Salah."],
  ["Osteomielofibrosis primer", "Penyebab trombositosis.", "Salah."],
  ["Osteomielosklerosis", "Penyebab trombositosis.", "Salah."],
  ["*Purpura trombositopenik idiopatik", "Contoh di petunjuk.", "Benar."]],
 "Trombositopenia: ITP, simtomatik (alergi, penekanan sumsum tulang), toksik (benzene, sitostatika, sinar X).",
 "Kisi-kisi pretest: “kekurangan trombosit namanya apa dan contoh penyakitnya”.")
q("trom", "Penyebab trombositopenia toksik yang disebut dalam petunjuk praktikum adalah…",
 [["Polisitemia dan leukemia mieloid kronik", "Penyebab trombositosis.", "Salah."],
  ["*Keracunan benzene, sitostatika, sinar X", "Trombositopenia toksika.", "Benar."],
  ["Alergi dan penekanan sumsum tulang", "Trombositopenia simtomatik.", "Kurang tepat."],
  ["Defisiensi faktor VIII dan IX", "Hemofilia, trombosit normal.", "Salah."],
  ["Penggunaan heparin dosis terapeutik", "Tidak disebut di petunjuk.", "Salah."]],
 "Trombositopenia: ITP; simtomatik (alergi, penekanan sumsum); toksik (benzene, sitostatika, sinar X).")
q("trom", "Catatan teknis mikroskop saat menghitung trombosit adalah…",
 [["Kondensor dinaikkan maksimal agar cahaya terang", "Kebalikannya.", "Salah."],
  ["Memakai lensa objektif 100× dengan minyak imersi", "Hitung Brecher memakai 400×.", "Salah."],
  ["*Kondensor diturunkan dan dilakukan blank out", "Trombosit tampak seperti bintang, gerak Brown.", "Benar."],
  ["Diafragma dibuka penuh dan memakai filter biru", "Tidak disebut.", "Salah."],
  ["Bilik hitung diamati tanpa kaca penutup", "Tidak benar.", "Salah."]],
 "Trombosit 2–4 µm (kadang 7 µm), dinding teratur, tengah terang, latar remang-remang, tampak seperti bintang.")

# ---------------- Waktu perdarahan ----------------
q("bt", "Dua metode pemeriksaan waktu perdarahan adalah…",
 [["Brecher dan Fonio", "Metode hitung trombosit.", "Salah."],
  ["Lee and White dan gelas arloji", "Metode waktu pembekuan.", "Salah."],
  ["*Duke dan Ivy", "Sesuai petunjuk.", "Benar."],
  ["Benedict dan Fehling", "Metode reduksi urin.", "Salah."],
  ["Rumpel Leed dan Hess", "Uji ketahanan kapiler.", "Salah."]],
 "Waktu perdarahan menilai faktor hemostasis ekstravaskuler; dinding vaskuler dan trombosit juga berpengaruh.",
 "Kisi-kisi pretest: “sebutkan dua metode tes perdarahan”.")
q("bt", "Lokasi tusukan dan kedalaman tusukan pada metode Duke adalah…",
 [["Volar lengan bawah, 3 mm, dengan manset 40 mmHg", "Itu metode Ivy.", "Salah."],
  ["Ujung jari tengah, 1 mm, tanpa bendungan", "Lokasi pungsi kapiler.", "Salah."],
  ["*Cuping telinga, 2–3 mm, tanpa bendungan", "Sesuai petunjuk.", "Benar."],
  ["Tumit, 5 mm, dengan bendungan 100 mmHg", "Tidak sesuai.", "Salah."],
  ["Volar lengan bawah, 5 mm, dengan manset 100 mmHg", "Tidak sesuai.", "Salah."]],
 "Duke: cuping telinga dipijat hingga hiperemis, alkohol, tusuk 2–3 mm, isap dengan kertas saring tiap ½ menit.")
q("bt", "Pada metode Duke, darah yang keluar diisap dengan kertas saring setiap…",
 [["5 detik, dengan kertas saring menekan luka", "Kertas tidak boleh menyentuh luka.", "Salah."],
  ["*½ menit, tanpa menyentuh luka", "Sesuai petunjuk.", "Benar."],
  ["2 menit, dengan kertas saring menekan luka", "Interval dan cara salah.", "Salah."],
  ["5 menit, tanpa menyentuh luka", "Interval terlalu lama.", "Salah."],
  ["Sekali saja di akhir, saat darah berhenti", "Tidak sesuai.", "Salah."]],
 "Stopwatch dijalankan saat darah keluar dan dihentikan saat darah tidak dapat diisap lagi.")
q("bt", "Pemeriksaan waktu perdarahan metode Duke dinyatakan berhasil bila…",
 [["Darah langsung berhenti dalam 30 detik pertama", "Tidak sesuai.", "Salah."],
  ["Bercak pada kertas saring makin lama makin besar", "Tidak sesuai.", "Salah."],
  ["Kertas saring menyentuh luka di setiap isapan", "Dilarang.", "Salah."],
  ["Tusukan dilakukan di dua tempat pada cuping yang sama", "Kontrol di cuping telinga lain.", "Salah."],
  ["*Bercak pertama berdiameter 3–4 mm", "Syarat keberhasilan di petunjuk.", "Benar."]],
 "Lakukan juga di cuping telinga yang lain sebagai kontrol.")
q("bt", "Nilai normal waktu perdarahan metode Duke adalah…",
 [["*1–3 menit", "Sesuai petunjuk.", "Benar."],
  ["9–15 menit", "Normal waktu pembekuan Lee and White.", "Salah."],
  ["10–20 detik", "Terlalu singkat.", "Salah."],
  ["½–1 jam", "Waktu serum mulai keluar pada retraksi bekuan.", "Salah."],
  ["24–72 jam", "Rentang lisis bekuan.", "Salah."]],
 "Duke 1–3 menit; Lee and White 9–15 menit.")
q("bt", "Perbedaan utama metode Ivy dibandingkan metode Duke adalah…",
 [["Ivy memakai darah vena 5 ml dalam tiga tabung", "Itu Lee and White.", "Salah."],
  ["Ivy di cuping telinga, Duke di lengan bawah", "Tertukar.", "Salah."],
  ["Ivy tidak memakai kertas saring untuk mengisap darah", "Ivy juga memakai kertas saring.", "Salah."],
  ["*Ivy di volar lengan bawah dengan bendungan 40 mmHg", "Tusuk ±3 jari di bawah lipat siku, 3 mm.", "Benar."],
  ["Ivy memakai amonium oksalat sebagai pengencer", "Itu Brecher.", "Salah."]],
 "Duke: cuping telinga tanpa bendungan. Ivy: lengan bawah dengan manset 40 mmHg.")
q("bt", "Sebelum pemeriksaan waktu perdarahan, pasien perlu ditanya tentang obat yang dapat memperpanjang perdarahan, misalnya…",
 [["Vitamin C dan zat besi oral", "Tidak disebut.", "Salah."],
  ["Parasetamol dan antasida", "Tidak disebut.", "Salah."],
  ["*Aspirin dan antikoagulan", "Juga sulfonamid dan antineoplastik.", "Benar."],
  ["Vitamin K dan asam traneksamat oral", "Justru prohemostatik.", "Salah."],
  ["Oralit dan probiotik untuk diare", "Tidak disebut.", "Salah."]],
 "Obat yang memperpanjang waktu perdarahan: tiazid, sulfonamid, antineoplastik, antikoagulan, antiinflamasi, aspirin.")

# ---------------- Waktu pembekuan ----------------
q("ct", "Dua metode pemeriksaan waktu pembekuan menurut petunjuk praktikum adalah…",
 [["Duke dan Ivy (luka standar)", "Waktu perdarahan.", "Salah."],
  ["*Gelas arloji; Lee and White", "Lee and White yang dipraktikumkan.", "Benar."],
  ["Brecher dan Herwerden", "Hitung trombosit.", "Salah."],
  ["PPT dan APTT (plasma sitrat)", "Tes koagulasi plasma.", "Salah."],
  ["Rumpel Leed dan Hess", "Uji kapiler.", "Salah."]],
 "Lee and White memakai darah lengkap: kasar tetapi masih dianggap yang terbaik.")
q("ct", "Pada metode Lee and White, darah vena 5 ml dimasukkan ke dalam…",
 [["Satu tabung berisi EDTA", "Antikoagulan mencegah pembekuan.", "Salah."],
  ["Dua tabung masing-masing 2,5 ml", "Tidak sesuai.", "Salah."],
  ["*Tiga tabung: 1,5 + 1,5 ml + sisa", "Tabung III sebagai kontrol.", "Benar."],
  ["Tiga tabung berisi sitrat, masing-masing 1,5 ml", "Antikoagulan tidak dipakai.", "Salah."],
  ["Lima tabung masing-masing 1 ml", "Tidak sesuai.", "Salah."]],
 "Tabung bersih dan kering; darah dimasukkan perlahan dengan tabung miring.")
q("ct", "Tabung I membeku dalam 8 menit dan tabung II dalam 11 menit. Waktu pembekuan metode Lee and White adalah…",
 [["8 menit (tabung tercepat)", "Bukan cara penilaian.", "Salah."],
  ["11 menit (tabung terlama)", "Bukan cara penilaian.", "Salah."],
  ["*9,5 menit, masih normal", "(8 + 11) ÷ 2.", "Benar; normal 9–15 menit."],
  ["19 menit, memanjang", "Dijumlahkan, bukan dirata-rata.", "Salah."],
  ["3 menit (selisih kedua tabung)", "Bukan cara penilaian.", "Salah."]],
 "Waktu pembekuan = rata-rata tabung I dan II.")
q("ct", "Nilai normal waktu pembekuan metode Lee and White adalah…",
 [["1–3 menit", "Normal waktu perdarahan Duke.", "Salah."],
  ["3–5 menit", "Tidak sesuai petunjuk.", "Salah."],
  ["*9–15 menit", "Sesuai petunjuk.", "Benar."],
  ["20–30 menit", "Memanjang.", "Salah."],
  ["½–2 jam", "Rentang retraksi bekuan.", "Salah."]],
 "Memanjang → koagulopati atau inhibitor dalam darah (misal heparin).",
 "Kisi-kisi pretest: “waktu pembekuan Lee and White”.")
q("ct", "Waktu pembekuan Lee and White yang memanjang menunjukkan…",
 [["Trombositopenia berat pada ITP akut", "Memengaruhi waktu perdarahan.", "Kurang tepat."],
  ["Gangguan ketahanan kapiler", "Dinilai Rumpel Leed.", "Salah."],
  ["Fibrinolisis yang berlebihan", "Dinilai lisis bekuan.", "Salah."],
  ["Polisitemia dengan hiperviskositas", "Tidak disebut.", "Salah."],
  ["*Koagulopati atau inhibitor (heparin)", "Arti klinis di petunjuk.", "Benar."]],
 "Waktu pembekuan = ukuran aktivitas faktor koagulasi.")
q("ct", "Pada pengambilan darah untuk Lee and White, tusukan tidak boleh berulang dan pengambilan tidak boleh lebih dari 30 detik. Alasannya adalah…",
 [["Agar pasien tidak merasa nyeri berlebihan", "Bukan alasan teknis di petunjuk.", "Kurang tepat."],
  ["Agar volume darah cukup untuk tiga tabung", "Tidak berkaitan dengan waktu.", "Salah."],
  ["Agar trombosit tidak lisis selama pengambilan", "Tidak disebut.", "Salah."],
  ["*Mencegah bekuan dini oleh cairan jaringan", "Sesuai catatan petunjuk.", "Benar."],
  ["Agar darah tidak tercampur antikoagulan", "Tidak memakai antikoagulan.", "Salah."]],
 "Tromboplastin jaringan dari tusukan berulang memicu jalur ekstrinsik → waktu memendek palsu.")

# ---------------- Retraksi, konsistensi, lisis ----------------
q("bek", "Pemeriksaan retraksi bekuan digunakan untuk menguji…",
 [["Aktivitas faktor koagulasi", "Dinilai waktu pembekuan.", "Salah."],
  ["*Fungsi trombosit", "Bekuan mengerut dan serum terperas.", "Benar."],
  ["Ketahanan dinding kapiler", "Dinilai Rumpel Leed.", "Salah."],
  ["Aktivitas sistem fibrinolisis", "Dinilai lisis bekuan.", "Salah."],
  ["Kadar fibrinogen plasma", "Tidak disebut.", "Salah."]],
 "Selain trombosit, permukaan yang bersinggungan dengan bekuan dan faktor lain membantu retraksi.")
q("bek", "Hasil retraksi bekuan dinyatakan normal bila…",
 [["Serum tidak tampak sampai lebih dari 2 jam", "Kriteria abnormal.", "Salah."],
  ["Bekuan langsung melisis dalam 1 jam", "Tidak sesuai.", "Salah."],
  ["Bekuan tetap cair setelah 24 jam", "Tidak terbentuk bekuan.", "Salah."],
  ["*Serum keluar ½ jam; sempurna ≤ 24 jam", "Sesuai petunjuk (inkubasi 37 °C).", "Benar."],
  ["Volume serum terperas kurang dari 10%", "Normal volume serum 40–60%.", "Salah."]],
 "Abnormal: lebih dari 2 jam serum tidak tampak.")
q("bek", "Gambaran konsistensi bekuan yang normal adalah…",
 [["Rapuh, berlubang, dan mudah hancur", "Abnormal.", "Salah."],
  ["Cair dan tidak berbentuk", "Abnormal.", "Salah."],
  ["*Licin, kompak, tidak berlubang, kenyal", "Sesuai petunjuk.", "Benar."],
  ["Keras seperti batu dan kering", "Tidak sesuai.", "Salah."],
  ["Bergranula halus dan berwarna kuning", "Tidak sesuai.", "Salah."]],
 "Konsistensi diperiksa dengan menekan bekuan di piring petri memakai dasar tabung reaksi.")
q("bek", "Bekuan sisa pemeriksaan waktu pembekuan diinkubasi 37 °C minimal 24 jam untuk menilai lisis bekuan. Hasil normal adalah…",
 [["Lisis terjadi dalam 30 menit", "Terlalu cepat (hiperfibrinolisis).", "Salah."],
  ["Lisis terjadi dalam 2 jam", "Terlalu cepat.", "Salah."],
  ["Bekuan tidak pernah lisis", "Tidak sesuai.", "Salah."],
  ["Lisis terjadi dalam 12 jam", "Tidak sesuai petunjuk.", "Salah."],
  ["*Lisis terjadi dalam 72 jam", "Sesuai petunjuk.", "Benar."]],
 "Lisis bekuan menilai fibrinolisis (tidak dipraktikumkan, tetapi bisa keluar di tes).")
q("bek", "Volume serum yang terperas dari bekuan dinyatakan normal bila…",
 [["5–10% dari volume semula", "Terlalu sedikit.", "Salah."],
  ["*40–60% dari volume semula", "Sesuai petunjuk.", "Benar."],
  ["80–100% dari volume semula", "Terlalu banyak.", "Salah."],
  ["Tidak ada serum yang terperas sama sekali", "Abnormal.", "Salah."],
  ["Sama dengan volume plasma darah EDTA", "Tidak sesuai.", "Salah."]],
 "Bandingkan volume semula dengan cairan yang terperas dari bekuan.")

# ---------------- POCT & glukosa urin ----------------
q("poct", "Kepanjangan POCT adalah…",
 [["Point of Clinical Treatment", "Salah.", "Salah."],
  ["Portable Oxidase Colorimetric Test", "Salah.", "Salah."],
  ["*Point of Care Testing", "Pemeriksaan di dekat pasien.", "Benar."],
  ["Primary Outpatient Clinical Test", "Salah.", "Salah."],
  ["Plasma Oxidation Capillary Test", "Salah.", "Salah."]],
 "POCT: pemeriksaan laboratorium sederhana di samping pasien (misal glukometer).",
 "Kisi-kisi PK glukosa urin dan POCT.")
q("poct", "Reagen yang terdapat pada strip glukosa POCT (per 100 strip) menurut slide asistensi adalah…",
 [["Amonium oksalat 1% dan larutan Hayem", "Reagen hitung trombosit/eritrosit.", "Salah."],
  ["Tembaga sulfat dan natrium sitrat", "Komponen reagen Benedict.", "Salah."],
  ["Heksokinase dan NADP (metode laboratorium)", "Metode laboratorium lain.", "Tidak disebut di slide."],
  ["*Glucose oxidase dan ferricyanide", "GOD 100 unit; ferricyanide 7,8 mg.", "Benar."],
  ["Magnesium sulfat dan Giemsa", "Reagen Fonio.", "Salah."]],
 "Strip glukometer memakai enzim glucose oxidase dengan mediator ferricyanide.")
q("poct", "Sampel darah yang digunakan pada pemeriksaan glukosa dengan POCT adalah…",
 [["Plasma sitrat dari darah vena", "Untuk tes koagulasi.", "Salah."],
  ["Serum yang dipisahkan dengan sentrifugasi", "Untuk pemeriksaan laboratorium.", "Salah."],
  ["*Darah kapiler segar dari tusukan jari", "Jari tengah atau jari manis.", "Benar."],
  ["Darah arteri radialis", "Untuk analisis gas darah.", "Salah."],
  ["Darah EDTA yang disimpan 24 jam", "Glikolisis menurunkan glukosa.", "Salah."]],
 "Bersihkan jari dengan alkohol dan tunggu kering; air hangat membantu vasodilatasi.")
q("poct", "Pada pemeriksaan glukosa POCT, tes harus diulang bila…",
 [["Hasil 90–140 mg/dL", "Rentang wajar.", "Salah."],
  ["Hasil ditampilkan tanpa angka desimal", "Satuan mg/dL memang tanpa desimal.", "Salah."],
  ["Meter berbunyi bip saat darah menyentuh strip", "Normal.", "Salah."],
  ["*Hasil < 20 atau > 600 mg/dL, atau tampil HI/LO", "Di luar rentang ukur alat.", "Benar."],
  ["Pasien belum makan siang", "Tidak membuat hasil invalid.", "Salah."]],
 "Laporkan dalam mg/dL tanpa desimal; ubah satuan bila tampil mmol/L.")
q("poct", "Glukosa darah sewaktu dikatakan memenuhi kriteria diabetes melitus bila…",
 [["≥ 126 mg/dL tanpa melihat gejala", "Angka itu untuk GDP.", "Salah."],
  ["≥ 140 mg/dL disertai gejala klasik", "Ambang TGT 2 jam.", "Salah."],
  ["≥ 180 mg/dL tanpa melihat gejala", "Target postprandial, bukan diagnosis.", "Salah."],
  ["*≥ 200 mg/dL disertai gejala klasik", "Poliuria, polidipsia, polifagia, BB turun.", "Benar."],
  ["≥ 250 mg/dL tanpa gejala", "Bukan kriteria.", "Salah."]],
 "Diagnosis DM wajib dengan plasma vena; POCT kapiler untuk skrining/pemantauan.")
q("poct", "Glukosa darah puasa dikatakan memenuhi kriteria diabetes melitus bila…",
 [["≥ 100 mg/dL", "Batas bawah GDPT.", "Salah."],
  ["≥ 110 mg/dL", "Kriteria lama.", "Salah."],
  ["*≥ 126 mg/dL", "Setelah puasa ≥ 8 jam.", "Benar."],
  ["≥ 140 mg/dL", "Ambang TTGO 2 jam (TGT).", "Salah."],
  ["≥ 200 mg/dL", "Ambang GDS atau TTGO 2 jam.", "Salah."]],
 "GDP 100–125 = GDPT (prediabetes); ≥ 126 = DM.")
q("poct", "Pada uji reduksi urin metode Benedict, 5 ml reagen Benedict dicampur dengan…",
 [["*5–8 tetes urin, lalu dipanaskan 5 menit", "Sesuai slide asistensi.", "Benar."],
  ["5 ml urin tanpa pemanasan", "Tidak sesuai.", "Salah."],
  ["1 tetes urin, didiamkan 30 menit", "Tidak sesuai.", "Salah."],
  ["5–8 tetes darah kapiler, lalu disentrifus", "Bukan bahan pemeriksaan.", "Salah."],
  ["Larutan Fehling 1 dan 2 sama banyak", "Itu metode Fehling.", "Salah."]],
 "Benedict: biru → hijau → kuning/jingga → merah bata; makin merah makin tinggi gula pereduksi.")
q("poct", "Hasil uji Benedict yang menunjukkan kadar gula pereduksi paling tinggi berwarna…",
 [["Biru jernih", "Negatif.", "Salah."],
  ["Hijau", "Positif lemah.", "Salah."],
  ["Kuning", "Positif sedang.", "Salah."],
  ["Jingga", "Positif kuat.", "Kurang tepat."],
  ["*Merah bata", "Paling banyak endapan Cu₂O.", "Benar."]],
 "Gula pereduksi mereduksi Cu²⁺ (biru) menjadi Cu₂O (merah bata).")

# ---------------- balance key positions + build ----------------
cnt = collections.Counter()
for i, x in enumerate(Q):
    tgt = min(range(5), key=lambda k: (cnt[k], (k - i) % 5))
    key = x["o"][x["a"]]; rest = [o for j, o in enumerate(x["o"]) if j != x["a"]]
    x["o"] = rest[:tgt] + [key] + rest[tgt:]; x["a"] = tgt; cnt[tgt] += 1
for i, x in enumerate(Q, 1):
    x["num"] = i
print("posisi kunci", dict(sorted(cnt.items())))
L = lambda s: len(s)
mon = [x["num"] for x in Q if (lambda l, k: k == l[-1] and k >= 1.2 * l[-2] and k - l[-2] >= 8)(sorted(L(o[0]) for o in x["o"]), L(x["o"][x["a"]][0]))]
print("kunci menonjol", mon)

tpl = open('praktikum-neoplasma/index.html').read()
def sub(old, new, count=1):
    global tpl
    assert old in tpl, old[:60]
    tpl = tpl.replace(old, new, count)
qs_json = json.dumps(Q, ensure_ascii=False)
tpl = re.sub(r'const CATS=\{.*?\};\n', lambda m: 'const CATS=' + json.dumps(CATS, ensure_ascii=False) + ';\n', tpl, count=1, flags=re.S)
tpl = re.sub(r'const QS=\[.*?\];\n', lambda m: 'const QS=' + qs_json + ';\n', tpl, count=1, flags=re.S)
sub('const KEY="prak-neoplasma-32-v1"', 'const KEY="prak-koagulasi-32-v1"')
sub('<title>Praktikum Neoplasma Modul 3.2</title>', '<title>Praktikum Koagulasi Modul 3.2</title>')
sub('<h1>Praktikum Neoplasma 3.2</h1><p id="sub">24 gambar, 32 soal</p>', f'<h1>Praktikum Koagulasi 3.2</h1><p id="sub">Pre/post test, {len(Q)} soal</p>')
sub('placeholder="mis. griseofulvin, Th2, nekrosis"', 'placeholder="mis. Brecher, Duke, Lee and White"')
assert 'data:image' not in tpl
import os; os.makedirs('praktikum-koagulasi', exist_ok=True)
open('praktikum-koagulasi/index.html', 'w').write(tpl)
print(len(Q), 'soal ->', len(tpl), 'byte')
