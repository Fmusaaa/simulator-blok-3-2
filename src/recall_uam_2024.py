# Recall UAM 3.2 tahun 2024 ("Soal uam 3.2 aldosteron 2024")
# tag: 'asli' = soal & opsi utuh dari recall; 'rekon' = soal/opsi dilengkapi berdasarkan konteks
# q(ppt, tag, nomor_recall, stem, [[opsi,fakta,alasan] kunci di indeks 0], pembahasan, poin, tips, catatan)
U=[]
def q(c,tag,no,s,o,p,k="",t="",n=""):
    U.append(dict(c=c,tag=tag,no=no,s=s,o=o,p=p,k=k,t=t,n=n))

# ---------------- ADRENAL / STEROID ----------------
q("cush","asli","1, 47","Manakah bagian dari glandula suprarenalis yang menghasilkan hormon glukokortikoid?",
[["Korteks pars fasciculata","Zona tengah korteks adrenal, dirangsang ACTH, menghasilkan kortisol.","Benar."],
 ["Korteks pars glomerulosa","Zona terluar, menghasilkan mineralokortikoid (aldosteron).","Bukan glukokortikoid."],
 ["Korteks pars reticularis","Zona terdalam korteks, menghasilkan androgen adrenal (DHEA).","Bukan glukokortikoid."],
 ["Medulla","Menghasilkan katekolamin (epinefrin, norepinefrin).","Bukan steroid."],
 ["Korteks renalis","Bagian ginjal, bukan adrenal.","Organ yang berbeda."]],
"Urutan korteks adrenal dari luar ke dalam: glomerulosa (garam/aldosteron) → fasikulata (gula/kortisol) → retikularis (seks/androgen).",
"GFR = Garam, Fasikulata-gula, Retikularis-seks.","\"Makin dalam makin manis\": glomerulosa garam, fasikulata gula, retikularis seks.")

q("cush","asli","49","Obat kortikosteroid merupakan bentuk sintetis dari hormon steroid yang dihasilkan glandula suprarenalis. Bagian yang menghasilkan hormon <b>mineralokortikoid</b> adalah:",
[["Korteks pars glomerulosa","Menghasilkan aldosteron, dirangsang angiotensin II dan kalium.","Benar."],
 ["Korteks pars fasciculata","Menghasilkan kortisol.","Bukan mineralokortikoid."],
 ["Korteks pars reticularis","Menghasilkan androgen adrenal.","Bukan mineralokortikoid."],
 ["Medulla","Menghasilkan katekolamin.","Bukan steroid."],
 ["Korteks renalis","Bagian ginjal.","Bukan adrenal."]],
"Aldosteron bekerja di tubulus distal/duktus koligens: reabsorpsi Na⁺, sekresi K⁺ dan H⁺.",
"Glomerulosa = aldosteron.","Mineralokortikoid = \"mineral\" (Na, K) = zona terluar.")

q("cush","asli","50, 84","Korteks adrenal tersusun atas zona glomerulosa, fasikulata, dan retikularis. Hormon yang diproduksi zona <b>retikularis</b> adalah:",
[["Dehidroepiandrosteron (DHEA)","Androgen adrenal utama.","Benar."],
 ["Aldosteron","Produk zona glomerulosa.","Bukan retikularis."],
 ["Kortisol","Produk utama zona fasikulata.","Bukan retikularis (sebagian kecil saja)."],
 ["Epinefrin","Produk medula adrenal.","Bukan korteks."],
 ["Kortikosteron","Prekursor di jalur mineralokortikoid/glukokortikoid.","Bukan produk khas retikularis."]],
"Pada sindrom Cushing ACTH-dependent dan hiperplasia adrenal kongenital, androgen adrenal meningkat sehingga muncul hirsutisme dan akne.",
"Retikularis = androgen (DHEA, DHEA-S, androstenedion).","Soal \"androgen\" (no. 84 recall) jawabannya sama: zona retikularis.")

q("add","asli","15","Laki-laki 50 tahun dalam beberapa bulan merasa lemah, letih, lesu, kadang nyeri perut, dan ruas jari tangan serta bibirnya berwarna lebih gelap. Bagian adrenal yang predominan bertanggung jawab terhadap sintesis glukokortikoid adalah:",
[["Zona fasikulata","Sumber utama kortisol yang kurang pada penyakit Addison.","Benar."],
 ["Zona glomerulosa","Sumber aldosteron.","Bukan glukokortikoid."],
 ["Zona retikularis","Sumber androgen.","Bukan glukokortikoid."],
 ["Medula","Sumber katekolamin.","Bukan steroid."],
 ["Korteks adrenal (keseluruhan)","Benar secara umum, tetapi soal menanyakan bagian predominan.","Kurang spesifik dibanding zona fasikulata."]],
"Kasusnya penyakit Addison: lemas, nyeri perut, hiperpigmentasi lipatan jari dan mukosa bibir (ACTH/MSH tinggi karena kortisol rendah).",
"Hiperpigmentasi + lemas + nyeri perut = Addison; glukokortikoid = fasikulata.","Pilih jawaban paling spesifik (zona) daripada yang umum (korteks).")

q("add","asli","37","Manifestasi klinis yang terjadi akibat <b>kekurangan</b> hormon yang dihasilkan korteks adrenal zona fasikulata adalah:",
[["Penyakit Addison","Insufisiensi adrenal primer dengan defisiensi kortisol (± aldosteron).","Benar."],
 ["Sindrom Conn","Hiperaldosteronisme primer (kelebihan hormon zona glomerulosa).","Kelebihan, dan zonanya berbeda."],
 ["Sindrom Bartter","Tubulopati ginjal (defek kotransporter Na-K-2Cl di ansa Henle) dengan hipokalemia.","Bukan defisiensi hormon adrenal."],
 ["Sindrom Gitelman","Tubulopati ginjal (defek kotransporter NaCl tubulus distal).","Bukan defisiensi hormon adrenal."],
 ["Hiperplasia adrenal kongenital","Defek enzim (tersering 21-hidroksilase) dengan kortisol turun dan androgen naik.","Memang ada defisiensi kortisol, tetapi manifestasi yang ditanyakan adalah penyakit defisiensi kortisol klasik, yaitu Addison."]],
"Hormon zona fasikulata = kortisol. Defisiensinya = insufisiensi adrenal (Addison).",
"Kurang kortisol → Addison; kelebihan kortisol → Cushing.","Conn = kelebihan aldosteron; Bartter/Gitelman = penyakit tubulus ginjal.",
"HAK juga menyebabkan defisiensi kortisol; bila muncul sebagai opsi bersama Addison, pilih Addison sebagai jawaban paling tepat untuk \"kekurangan hormon zona fasikulata\".")

q("cush","asli","36","Pemeriksaan laboratorium hormon sebaiknya menyesuaikan irama sirkadian hormon tersebut. Kadar kortisol akan berada di puncak pada waktu:",
[["Pagi hari","Puncak kortisol sekitar pukul 06.00–08.00, terendah tengah malam.","Benar."],
 ["Sepanjang hari sama","Keliru.","Kortisol bersifat diurnal."],
 ["Siang hari","Kadar sudah menurun.","Bukan puncak."],
 ["Sore hari","Kadar rendah.","Bukan puncak."],
 ["Malam hari","Titik terendah (nadir) sekitar tengah malam.","Kebalikannya."]],
"Hilangnya nadir kortisol tengah malam adalah salah satu tanda sindrom Cushing. Itulah sebabnya pemeriksaan GDP juga dianjurkan pagi hari (meminimalkan variasi kortisol).",
"Kortisol: puncak pagi, nadir tengah malam.","Hormon \"bangun tidur\" = kortisol.")

q("ster","asli","42","Obat kortikosteroid memiliki efek glukokortikoid dan mineralokortikoid. Efek <b>mineralokortikoid</b> dari penggunaan kortikosteroid adalah:",
[["Hipokalemia","Retensi Na⁺ dan sekresi K⁺ di tubulus distal.","Benar."],
 ["Osteoporosis","Efek glukokortikoid (hambat osteoblas, kurangi absorpsi Ca).","Bukan mineralokortikoid."],
 ["Imunosupresi","Efek glukokortikoid.","Bukan mineralokortikoid."],
 ["Mempercepat pematangan tulang","Bukan efek khas; steroid justru menghambat pertumbuhan anak.","Tidak tepat."],
 ["Muncul akne","Efek dermatologik glukokortikoid/androgenik.","Bukan mineralokortikoid."]],
"Efek mineralokortikoid: retensi natrium dan air (edema, hipertensi), hipokalemia, alkalosis metabolik. Paling kuat pada fludrokortison dan hidrokortison; deksametason hampir tanpa efek mineralokortikoid.",
"Mineralokortikoid = Na naik, K turun, air tertahan.","Pilih opsi yang berhubungan dengan elektrolit.")

q("ster","asli","46","Glukokortikoid adalah hormon pengendali stres. Bila stres berlangsung terlalu lama sehingga glukokortikoid berlebihan, akibat yang dapat terjadi adalah:",
[["Depresi","Slide Steroid: ESO neuropsikiatrik berupa depresi pada pemakaian jangka panjang.","Benar menurut recall dan slide."],
 ["Hipotensi","Ciri defisiensi kortisol (Addison).","Kebalikannya."],
 ["Hiperkalemia","Ciri defisiensi aldosteron.","Kortisol berlebih justru cenderung hipokalemia."],
 ["Hipovolemia","Ciri insufisiensi adrenal.","Kortisol berlebih menyebabkan retensi cairan."],
 ["Hipertensi","Juga terjadi pada kortisol berlebih, tetapi slide menyebut hipertensi terutama pada dosis tinggi.","Lihat catatan: opsi ini juga bisa dibenarkan."]],
"Kortisol berlebih kronik memengaruhi hipokampus dan neurotransmiter sehingga timbul gangguan mood (depresi), di samping efek metabolik.",
"Kortisol berlebih jangka panjang: depresi, hipertensi, hiperglikemia, osteoporosis.","Kata \"stres\" dan \"jangka panjang\" mengarah ke efek neuropsikiatrik.",
"Soal ini ambigu: hipertensi juga akibat kortisol berlebih (Cushing). Recall memilih <b>depresi</b>, dan slide Steroid mencantumkan depresi sebagai efek jangka panjang, sedangkan hipertensi disebut \"hanya terjadi pada pemberian dosis tinggi\". Kalau di ujian pilihannya sama persis, depresi lebih aman.")

# ---------------- DIABETES ----------------
q("ldm","rekon","3, 34","Pada pemeriksaan TTGO, beban glukosa yang dilarutkan dalam 250 cc air adalah:",
[["75 gram glukosa anhidrat","Standar WHO/ADA untuk dewasa.","Benar."],
 ["56 gram","Bukan dosis standar.","Keliru."],
 ["65 gram","Bukan dosis standar.","Keliru."],
 ["50 gram","Dosis glucose challenge test (skrining DMG satu langkah tanpa puasa).","Bukan TTGO diagnostik standar."],
 ["100 gram","Dosis TTGO 3 jam kriteria lama untuk DMG.","Bukan TTGO standar di slide."]],
"Slide: 75 g glukosa anhidrat dalam 250–300 mL air, diminum habis < 5 menit, ambil darah jam ke-2. Pada anak: 1,75 g/kgBB (maks. 75 g).",
"TTGO = 75 g / 250–300 mL / < 5 menit / 2 jam.","Angka 75 adalah jawaban paling sering keluar.",
"Dosis anak 1,75 g/kgBB adalah pelengkap dari literatur.")

q("ldm","asli","48","Wanita 50 tahun mengeluh mudah lelah, lemah, sering BAK malam hari, dan sering lapar. Glukosa darah puasa 118 mg/dL. Diagnosis yang paling tepat berdasarkan nilai tersebut adalah:",
[["Prediabetes (GDPT/IFG)","GDP 100–125 mg/dL.","Benar: belum mencapai ambang DM (≥ 126)."],
 ["DM tipe 1","Butuh kriteria DM dan bukti defisiensi insulin absolut.","GDP belum memenuhi kriteria DM."],
 ["DM tipe 2","Butuh GDP ≥ 126, GD2PP ≥ 200, HbA1c ≥ 6,5%, atau GDS ≥ 200 + gejala.","Belum terpenuhi."],
 ["Diabetes gestasional","Pada kehamilan.","Tidak sesuai."],
 ["DM tipe lain","Ada penyebab spesifik.","Tidak ada data."]],
"Walau ada keluhan yang mengarah ke DM, satu nilai GDP 118 baru masuk kategori prediabetes. Langkah berikutnya: periksa GDS/TTGO/HbA1c untuk memastikan.",
"GDP 100–125 = GDPT.","Hitung angka dulu, baru lihat gejala.")

q("ldm","asli","82","Wanita 26 tahun mengeluh polifagia, poliuria, dan polidipsia sejak 2 bulan. GDP 118 mg/dL. Hasil ini termasuk ciri:",
[["Prediabetes","GDP 100–125 mg/dL.","Benar berdasarkan angka GDP."],
 ["DM tipe 1","Perlu kriteria DM terpenuhi.","GDP belum ≥ 126."],
 ["DM tipe 2","Perlu kriteria DM terpenuhi.","GDP belum ≥ 126."],
 ["DM gestasional","Pada kehamilan.","Tidak ada data hamil."],
 ["DM tipe lain","Penyebab spesifik.","Tidak ada data."]],
"Gejala klasik hanya \"membantu\" bila dipasangkan dengan GDS ≥ 200. Dengan GDP 118, klasifikasinya prediabetes, lalu dikonfirmasi dengan GDS/TTGO/HbA1c karena gejala klasik membuat DM sangat mungkin.",
"Gejala klasik + GDS ≥ 200 = DM; gejala klasik + GDP 118 = belum memenuhi kriteria DM.","Jangan langsung menyimpulkan DM dari gejala; cocokkan angka dengan tabel.",
"Di praktik klinis, pasien ini perlu pemeriksaan ulang segera karena gejala klasik. Untuk soal pilihan ganda berdasarkan angka, jawabannya prediabetes.")

q("ldm","asli","45","Cut-off HbA1c untuk diagnosis diabetes melitus adalah:",
[["6,5%","HbA1c ≥ 6,5% (48 mmol/mol) = diagnosis DM.","Benar."],
 ["5,0%","Nilai normal.","Bukan cut-off."],
 ["5,5%","Masih normal (< 5,7%).","Bukan cut-off."],
 ["6,0%","Rentang prediabetes (5,7–6,4%).","Bukan cut-off DM."],
 ["7,0%","Target pengendalian HbA1c pasien DM (< 7%).","Bukan cut-off diagnosis."]],
"Rentang slide: normal < 5,7%; prediabetes 5,7–6,4%; DM ≥ 6,5%; target terapi < 7%.",
"5,7 dan 6,5 adalah dua angka batas; 7 adalah target terapi.","Bedakan \"cut-off diagnosis\" (6,5) dengan \"target terapi\" (7).",
"Recall menulis soal ini sebagai \"pada normalnya di-cut-off berapa\" dan catatan \"di PPT < 5,6 normalnya\". Batas normal yang benar adalah < 5,7%. Karena opsi 5,7 tidak ada, jawaban yang paling masuk akal adalah cut-off diagnosis DM 6,5%.")

q("ado","rekon","83","Pasien DM tipe 2 diberi obat yang menurunkan kadar glukosa postprandial dengan menghambat pemecahan karbohidrat di usus halus. Obat tersebut adalah:",
[["Akarbose (penghambat α-glukosidase)","Menghambat enzim α-glukosidase di brush border sehingga absorpsi glukosa melambat.","Benar."],
 ["Metformin","Menurunkan produksi glukosa hati, meningkatkan sensitivitas insulin.","Bukan di saluran cerna."],
 ["Glibenklamid","Sulfonilurea, merangsang sekresi insulin.","Bukan di saluran cerna."],
 ["Pioglitazon","Tiazolidindion, agonis PPAR-γ.","Bukan di saluran cerna."],
 ["Dapagliflozin","Penghambat SGLT2 di tubulus proksimal ginjal.","Bekerja di ginjal."]],
"Efek samping akarbose: flatulens, kembung, diare karena karbohidrat yang tidak tercerna difermentasi bakteri kolon. Bila hipoglikemia terjadi pada kombinasi dengan sulfonilurea/insulin, atasi dengan glukosa murni, bukan sukrosa.",
"Penghambat α-glukosidase = akarbose, miglitol; target glukosa postprandial.","\"Saluran cerna\" + \"pemecahan karbohidrat\" = akarbose.")

q("gdm","rekon","78","Pasien DM dengan kebutuhan energi total 2.000 kkal/hari. Menurut slide Tatalaksana Gizi pada DM, kebutuhan karbohidratnya per hari adalah:",
[["225–325 g/hari (45–65% energi ÷ 4 kkal/g)","2.000 × 45% = 900 kkal = 225 g; 2.000 × 65% = 1.300 kkal = 325 g.","Benar."],
 ["50–100 g/hari","Terlalu rendah.","Slide: pembatasan KH total < 130 g/hari tidak dianjurkan."],
 ["400–500 g/hari","Melebihi 65% energi.","Keliru."],
 ["100–150 g/hari","Dihitung dengan 9 kkal/g (kalori lemak).","Salah faktor konversi."],
 ["900–1.300 g/hari","Lupa membagi kkal dengan 4.","Itu nilai dalam kkal, bukan gram."]],
"Karbohidrat 4 kkal/g, protein 4 kkal/g, lemak 9 kkal/g. Slide: KH 45–65% total energi (utamakan berserat tinggi), sukrosa ≤ 5% energi, lemak 20–25% (tidak > 30%).",
"Gram KH = (% KH × total energi) ÷ 4.","Selalu ubah kkal ke gram dengan faktor 4 (KH/protein) atau 9 (lemak).",
"Soal recall no. 78 berbunyi \"rumus menghitung karbohidrat\", dan coretan di file menulis rumus Harris-Benedict (66 + 13,7 BB + 5 TB − 6,8 U). Rumus itu untuk energi basal laki-laki, bukan karbohidrat. Soal ini direkonstruksi ke perhitungan karbohidrat sesuai slide.")

# ---------------- LIPID ----------------
q("sm","rekon","4, 33","Apolipoprotein utama pada LDL yang dikenali reseptor LDL sehingga LDL dapat diambil oleh sel adalah:",
[["Apolipoprotein B (B-100)","Satu molekul per partikel LDL, ligan reseptor LDL.","Benar."],
 ["Apolipoprotein A","Apo A-I adalah protein utama HDL, mengaktifkan LCAT.","Bukan ligan reseptor LDL."],
 ["Apolipoprotein C","Apo C-II mengaktifkan lipoprotein lipase.","Bukan ligan reseptor LDL."],
 ["Apolipoprotein D","Apolipoprotein minor pada HDL.","Tidak sesuai."],
 ["Apolipoprotein E","Ligan reseptor untuk sisa kilomikron dan IDL.","Bukan untuk LDL."]],
"Apo B-48 ada pada kilomikron (usus), Apo B-100 pada VLDL, IDL, LDL (hati). Apo B menjadi target terapi (< 90 mg/dL pada DM).",
"LDL = Apo B-100; HDL = Apo A-I; aktivator LPL = Apo C-II; sisa kilomikron = Apo E.","Bila soal menyebut \"LDL\" atau \"reseptor LDL\", jawab Apo B.",
"Kalimat recall (\"yang mengikat lipoprotein itu apa\") tidak lengkap. Soal direkonstruksi ke konsep yang paling mungkin ditanyakan, dengan kunci recall Apo B.")

q("sm","asli","30, 71","Jenis lipoprotein yang paling banyak terdapat dalam plasma (pada keadaan puasa) adalah:",
[["LDL","Pembawa utama kolesterol plasma (± 60–70% kolesterol total).","Benar."],
 ["Kilomikron","Lipoprotein terbesar, membawa lemak makanan; hilang dari plasma 12–14 jam setelah puasa.","Paling besar ukurannya, bukan paling banyak."],
 ["VLDL","Pembawa trigliserida endogen.","Jumlahnya lebih sedikit dari LDL."],
 ["HDL","Pembawa kolesterol balik ke hati (± 20–30%).","Lebih sedikit dari LDL."],
 ["IDL","Perantara VLDL → LDL, kadarnya sangat rendah.","Tidak sesuai."]],
"Bedakan \"paling besar\" (kilomikron) dan \"paling banyak di plasma\" (LDL).",
"Terbesar & paling ringan = kilomikron; terbanyak membawa kolesterol = LDL; terpadat/terkecil = HDL.","Perhatikan kata kunci ukuran vs jumlah.",
"<b>Koreksi kunci recall:</b> no. 30 menulis kilomikron, padahal coretan di file sudah membetulkan menjadi \"LDL yang benar\" (dan no. 71 menandai LDL). Kunci yang benar LDL.")

# ---------------- PATOLOGI KLINIK: elektrolit, AGD ----------------
q("el","asli","29","Elektrolit yang paling banyak berada di cairan ekstraseluler adalah:",
[["Natrium","Kation utama ekstrasel (135–145 mEq/L).","Benar."],
 ["Kalium","Kation utama intrasel.","Bukan ekstrasel."],
 ["Kalsium","Kadarnya kecil (± 2,2–2,6 mmol/L).","Tidak sesuai."],
 ["Klorida","Anion utama ekstrasel, tetapi kadarnya di bawah natrium.","Natrium tetap terbanyak."],
 ["Magnesium","Kation intrasel kedua terbanyak.","Tidak sesuai."]],
"Ekstrasel: Na⁺ dan Cl⁻, HCO₃⁻. Intrasel: K⁺, Mg²⁺, fosfat, protein.",
"Na = luar, K = dalam.","Ingat pompa Na-K: Na dipompa keluar, K masuk.")

q("el","asli","38","Pemeriksaan kalium harus memperhatikan faktor pra-analitik. Kondisi pra-analitik yang menyebabkan kadar kalium <b>tinggi palsu</b> adalah:",
[["Sampel hemolisis","Eritrosit pecah melepaskan K⁺ intrasel ke serum (pseudohiperkalemia).","Benar."],
 ["Sampel ikterik","Bilirubin tinggi terutama mengganggu metode kolorimetri tertentu.","Bukan penyebab klasik kalium tinggi palsu."],
 ["Sampel lipemik","Mengganggu pengukuran natrium dengan ISE indirek (pseudohiponatremia).","Bukan kalium tinggi palsu."],
 ["Antikoagulan heparin","Antikoagulan yang dianjurkan (Li-heparin).","Tidak menaikkan kalium."],
 ["Antikoagulan sitrat","Mengikat kalsium.","Tidak menaikkan kalium."]],
"Penyebab pseudohiperkalemia lain: kepalan tangan berulang saat sampling, tourniquet terlalu lama, darah lama tidak dipisah, trombositosis/leukositosis ekstrem, kontaminasi EDTA-K₂.",
"Hemolisis → K naik palsu; lipemik → Na turun palsu.","Hubungkan analit dengan isi sel: K banyak di eritrosit, jadi hemolisis menaikkan K.",
"<b>Koreksi kunci recall:</b> recall menulis jawaban B (ikterik), padahal coretan di file menandai C (hemolisis). Jawaban yang benar C. Hemolisis.")

q("agd","rekon","26","Sebelum pengambilan sampel AGD dari arteri radialis, dilakukan tes untuk menilai sirkulasi kolateral dari arteri ulnaris. Tes tersebut adalah:",
[["Tes Allen","Arteri radialis dan ulnaris ditekan, tangan mengepal hingga pucat, lalu tekanan a. ulnaris dilepas; warna kembali < 5–15 detik berarti kolateral adekuat.","Benar."],
 ["Tes Tourniquet (Rumple-Leede)","Uji kerapuhan kapiler pada DBD.","Bukan untuk AGD."],
 ["Tes Trendelenburg","Menilai insufisiensi katup vena.","Tidak sesuai."],
 ["Tes Phalen","Menilai carpal tunnel syndrome.","Tidak sesuai."],
 ["Tes Romberg","Menilai keseimbangan/propiosepsi.","Tidak sesuai."]],
"Slide AGD: lokasi sampling biasanya a. radialis; lakukan tes Allen untuk menilai kolateral.",
"AGD radialis → tes Allen dulu.","Allen = Arteri.",
"Batas waktu pemulihan warna (5–15 detik) adalah pelengkap dari literatur.")

q("agd","rekon","11, 27, 74","Menurut slide Pemeriksaan AGD, kontraindikasi pengambilan sampel darah arteri adalah:",
[["Sirkulasi arteri kolateral yang tidak adekuat (tes Allen abnormal)","Bila a. radialis rusak, tangan tidak mendapat suplai cukup.","Benar."],
 ["Pasien hiperkapnia kronik yang mendapat terapi O₂","Termasuk indikasi AGD di slide.","Bukan kontraindikasi."],
 ["Pasien kritis saat operasi toraks","Termasuk indikasi.","Bukan kontraindikasi."],
 ["Pasien yang direncanakan terapi O₂ jangka panjang","Termasuk indikasi.","Bukan kontraindikasi."],
 ["Pasien dengan gangguan asam-basa yang dicurigai","Indikasi utama AGD.","Bukan kontraindikasi."]],
"Kontraindikasi di slide: sirkulasi arteri kolateral tidak adekuat, gangguan pembekuan darah, terapi antikoagulan dosis sedang–tinggi, lokasi pascaoperasi/prosedur tertentu, ada penyakit di sekitar lokasi sampling.",
"Kontraindikasi AGD: kolateral buruk, koagulopati/antikoagulan, lokasi bermasalah.","Bedakan indikasi (kondisi pasien butuh AGD) dan kontraindikasi (risiko tindakan).",
"Slide menulis \"Tidak ada gangguan pembekuan darah\" di bawah judul kontraindikasi. Maksudnya justru <b>adanya</b> gangguan pembekuan darah merupakan kontraindikasi.")

q("agd","rekon","28","Antikoagulan yang digunakan pada spuit untuk pemeriksaan AGD adalah:",
[["Heparin (lithium/sodium heparin)","Tidak mengubah pH dan gas darah bila jumlahnya tepat.","Benar."],
 ["EDTA","Untuk hematologi rutin.","Mengubah pH dan tidak dipakai untuk AGD."],
 ["Sitrat","Untuk koagulasi.","Mengencerkan dan mengubah hasil."],
 ["Oksalat-fluorida","Untuk glukosa (menghambat glikolisis).","Tidak untuk AGD."],
 ["Tanpa antikoagulan","Darah membeku.","Sampel tidak bisa dianalisis."]],
"Heparin berlebih menyebabkan dilusi (PCO₂ dan HCO₃ turun palsu). Sampel dikirim segera tanpa gelembung udara, dalam es bila tertunda.",
"AGD = heparin.","Hafal pasangan: AGD–heparin, hematologi–EDTA, koagulasi–sitrat, glukosa–fluorida.")

# ---------------- PATOLOGI KLINIK: tiroid ----------------
q("tir","rekon","25","Kelenjar tiroid dipengaruhi hipotalamus dan hipofisis. Hormon yang dihasilkan hipofisis untuk merangsang tiroid adalah:",
[["TSH","Dari hipofisis anterior (tirotrop).","Benar."],
 ["TRH","Dari hipotalamus.","Bukan hipofisis."],
 ["T4 (tiroksin)","Dari kelenjar tiroid.","Bukan hipofisis."],
 ["Kalsitonin","Dari sel parafolikuler tiroid.","Bukan hipofisis."],
 ["ACTH","Dari hipofisis anterior, tetapi merangsang korteks adrenal.","Target berbeda."]],
"Aksis: TRH (hipotalamus) → TSH (hipofisis anterior) → T4/T3 (tiroid), dengan umpan balik negatif.",
"Hipotalamus = TRH; hipofisis = TSH.","Coretan \"TRH\" di file adalah jawaban untuk hipotalamus, bukan hipofisis.",
"Slide Pemeriksaan Tiroid menulis TRH \"distimulasi oleh TSH\"; yang benar TRH merangsang TSH.")

q("tir","asli","44","Hormon T3 dan T4 di plasma diangkut oleh protein pengikat. Protein pengangkut dengan persentase terbanyak adalah:",
[["Thyroxine binding globulin (TBG)","± 75% menurut slide.","Benar."],
 ["Thyroxine binding prealbumin (transtiretin)","± 20%.","Bukan terbanyak."],
 ["Thyroxine binding albumin","± 5%.","Bukan terbanyak."],
 ["Globulin (umum)","Tidak spesifik.","Kurang tepat."],
 ["Albumin","Kapasitas besar tetapi afinitas rendah (± 5%).","Bukan terbanyak."]],
"Perubahan TBG (kehamilan, estrogen menaikkan; androgen, sindroma nefrotik menurunkan) mengubah T4 total tanpa mengubah fT4. Karena itu fT4 lebih mencerminkan status tiroid.",
"TBG 75%, TBPA 20%, albumin 5%.","Urutan 75-20-5.")

q("tir","rekon","76","Gambaran laboratorium yang khas pada pasien hipertiroidisme primer (misalnya penyakit Graves) adalah:",
[["TSH(s) rendah, fT4 dan T3 tinggi","Hormon tiroid berlebih menekan TSH lewat umpan balik negatif.","Benar."],
 ["TSH tinggi, fT4 rendah","Pola hipotiroidisme primer.","Kebalikannya."],
 ["TSH tinggi, fT4 tinggi","Pola hipertiroidisme sekunder (TSHoma).","Bukan primer."],
 ["TSH rendah, fT4 rendah","Pola hipotiroidisme sekunder/sentral.","Tidak sesuai."],
 ["TSH tinggi, fT4 normal","Pola hipotiroidisme subklinis.","Tidak sesuai."]],
"Pemeriksaan tambahan: TRAb positif pada Graves (90–100%); di jaringan perifer BMR meningkat, kolesterol rendah, relaksasi refleks Achilles cepat.",
"Primer: TSH dan fT4 berlawanan arah.","Coretan recall \"TSH ↓, T3 & T4 ↑\" sudah benar.")

# ---------------- TUMOR MARKER ----------------
q("tm","rekon","12, 52","Laki-laki 34 tahun mengeluh benjolan leher kiri sejak 6 bulan, mobile, tidak nyeri, disertai pembesaran KGB. USG: massa solid soliter 3 × 4 cm. Biopsi: karsinoma tiroid. Petanda tumor yang tepat diperiksa (sesuai opsi) adalah:",
[["Kalsitonin","Slide: meningkat berhubungan dengan Ca tiroid, berkorelasi dengan ukuran tumor dan metastasis, untuk monitoring terapi dan rekurensi (khas karsinoma meduler).","Benar sesuai opsi recall."],
 ["Kalsium ion","Elektrolit, bukan petanda tumor.","Tidak sesuai."],
 ["Kalsium serum","Elektrolit.","Tidak sesuai."],
 ["AFP","Petanda HCC dan tumor sel germinal.","Tidak sesuai."],
 ["PSA","Petanda kanker prostat.","Tidak sesuai."]],
"Slide Tumor Marker: kalsitonin terkait Ca tiroid (monitoring dan rekurensi); tiroglobulin juga marker Ca tiroid.",
"Ca tiroid meduler → kalsitonin; Ca tiroid berdiferensiasi (papiler/folikuler) → tiroglobulin (pascatiroidektomi).","Bila opsinya hanya kalsium vs kalsitonin, pilih kalsitonin.",
"Recall no. 52 menampilkan opsi kalsitonin vs tiroglobulin, dan penulis recall ragu. Secara klinis, laki-laki muda dengan metastasis KGB lebih khas karsinoma papiler (marker: tiroglobulin, dipakai setelah tiroidektomi total). Kalsitonin khas karsinoma meduler. Karena slide menyebut keduanya, kunci recall (kalsitonin) diikuti, tetapi siapkan alasan ini kalau keluar opsi tiroglobulin.")

q("tm","asli","31","Pemeriksaan petanda tumor yang digunakan untuk <b>memperkirakan respons terapi</b> dalam merencanakan pengobatan pasien (misalnya terapi trastuzumab/Herceptin pada kanker payudara) adalah:",
[["HER2/neu","Slide: pemeriksaan HER2/neu untuk memperkirakan respons terapi Herceptin pada kanker payudara.","Benar."],
 ["CEA","Untuk monitoring terapi dan rekurensi Ca kolorektal.","Bukan prediktor respons terapi target."],
 ["PSA","Diagnosis dan monitoring Ca prostat.","Tidak sesuai."],
 ["CA 19-9","Ca pankreas/hepatobilier.","Tidak sesuai."],
 ["CA 125","Ca ovarium.","Tidak sesuai."]],
"Slide Fungsi Tumor Marker: \"memperkirakan respons terapi\" dicontohkan dengan reseptor estrogen (respons antiestrogen) dan HER2/neu (respons Herceptin).",
"Prediksi respons terapi: ER (tamoksifen), HER2 (trastuzumab).","\"Memperkirakan respons terapi\" ≠ \"memantau efektivitas terapi\".",
"<b>Koreksi kunci recall:</b> recall menandai A (CEA). Sesuai slide, yang dipakai untuk memperkirakan respons terapi adalah HER2/neu (B). CEA dipakai untuk pemantauan efektivitas terapi, fungsi yang berbeda di slide.")

q("tm","asli","32, 73","Petanda tumor yang memiliki spesifisitas tinggi untuk neoplasma ovarium adalah:",
[["CA 125","Ditemukan Bast 1983 untuk Ca ovarium, cut-off 35 U/mL.","Benar."],
 ["PSA","Ca prostat.","Tidak sesuai."],
 ["CEA","Ca kolorektal.","Tidak sesuai."],
 ["AFP","HCC, tumor sel germinal (bisa ovarium yolk sac tumor).","Bukan marker utama epitelial ovarium."],
 ["IgG","Imunoglobulin, bukan petanda tumor.","Tidak sesuai."]],
"CA 125 juga meningkat pada endometriosis, kehamilan awal, sirosis, dan Ca pankreas/paru/kolorektal, jadi tetap perlu korelasi klinis.",
"Ovarium = CA 125.","Hafal pasangan organ–marker.")

q("tm","asli","35","Pemeriksaan laboratorium petanda tumor sebagian besar menggunakan metode:",
[["Immunoassay (ELISA, RIA, IRMA, CLIA, FPIA)","Berdasarkan reaksi antigen–antibodi.","Benar."],
 ["Kolorimetri","Untuk analit kimia klinik (glukosa, kolesterol).","Tidak sesuai."],
 ["Flowsitometri","Untuk imunofenotiping sel.","Tidak sesuai."],
 ["Koagulometri","Untuk PT/aPTT.","Tidak sesuai."],
 ["Kromatografi","Untuk pemisahan senyawa (obat, hormon tertentu).","Bukan metode utama."]],
"Slide: sampel serum/plasma, diperiksa serial dengan metode dan laboratorium yang sama.",
"Tumor marker = immunoassay.","Marker berupa protein/antigen, jadi diukur dengan antibodi.")

q("tm","rekon","51","Petanda tumor berupa glikoprotein yang secara normal diproduksi sel hepatosit imatur pada fetus dan strukturnya homolog dengan albumin adalah:",
[["AFP (alfa-fetoprotein)","Marker HCC dan tumor sel germinal.","Benar."],
 ["CEA","Antigen onkofetal kolorektal.","Bukan dari hepatosit fetus."],
 ["hCG","Dari sinsitiotrofoblas.","Tidak sesuai."],
 ["CA 19-9","Marker pankreas.","Tidak sesuai."],
 ["PSA","Dari epitel prostat.","Tidak sesuai."]],
"AFP meningkat pada keganasan (HCC, tumor sel germinal, metastasis hati) dan nonkeganasan (kehamilan, sirosis, hepatitis).",
"AFP = hati fetus = HCC.","\"Fetus + hepatosit\" → AFP.")

q("tm","rekon","53","Petanda tumor yang kadarnya dapat meningkat pada perokok sehingga menjadi faktor interferensi adalah:",
[["CEA","Slide: merokok meningkatkan CEA.","Benar."],
 ["PSA","Meningkat setelah colok dubur/manipulasi transuretra.","Tidak sesuai."],
 ["CA 19-9","Meningkat pada penyakit reumatik.","Tidak sesuai."],
 ["AFP","Meningkat pada kehamilan, hepatitis.","Tidak sesuai."],
 ["CA 125","Meningkat pada endometriosis, kehamilan awal.","Tidak sesuai."]],
"Riwayat klinis (merokok, CKD, kolestasis, reumatik, prosedur) wajib diketahui sebelum menyimpulkan keganasan dari tumor marker.",
"Rokok → CEA.","\"Perokok\" pada soal tumor marker hampir selalu CEA.")

q("tm","asli","72","Tumor marker yang paling sering dipakai secara luas dalam praktik klinis adalah:",
[["CEA","Marker paling luas dipakai, terutama pemantauan Ca kolorektal; meningkat pada banyak keganasan GI, paru, payudara.","Benar menurut recall."],
 ["PSA","Spesifik organ prostat.","Pemakaian terbatas pada pria."],
 ["CA 15-3","Monitoring Ca payudara.","Pemakaian lebih terbatas."],
 ["CA 19-9","Pankreas/hepatobilier.","Pemakaian lebih terbatas."],
 ["CA 125","Ovarium.","Pemakaian lebih terbatas."]],
"CEA ditemukan Gold & Freedman (1965), glikoprotein onkofetal.",
"CEA = marker serbaguna.","Bila soal menanyakan \"paling sering/umum\", pilih CEA.",
"Soal ini tidak tertera di slide secara eksplisit; kunci mengikuti recall dan literatur umum.")

# ---------------- PATOLOGI ANATOMI: hemodinamik, hemostasis ----------------
q("hemo","rekon","6, 81","Pasien gagal jantung kongestif mengalami edema tungkai dan efusi. Mekanisme utama yang mendasari edema pada pasien ini adalah:",
[["Peningkatan tekanan hidrostatik (kongesti vena) disertai retensi natrium dan air","Curah jantung turun → aliran balik vena terhambat; RAAS dan ADH aktif.","Benar."],
 ["Penurunan tekanan onkotik akibat proteinuria","Mekanisme sindroma nefrotik.","Bukan mekanisme utama gagal jantung."],
 ["Obstruksi limfatik","Limfedema lokal.","Tidak sesuai."],
 ["Peningkatan permeabilitas akibat inflamasi","Edema radang (eksudat).","Tidak sesuai."],
 ["Peningkatan tekanan onkotik plasma","Justru menarik cairan masuk pembuluh.","Kebalikannya."]],
"Slide: gagal jantung → curah jantung turun → volume arteri efektif turun → RAAS & ADH → retensi Na & air → volume plasma naik → tekanan kapiler naik → transudasi → edema.",
"Gagal jantung = hidrostatik ↑ (kongesti) + retensi Na.","Coretan recall \"kongesti\" mengarah ke jawaban ini.",
"Soal recall menyebut \"penumpukan cairan di jantung\". Bila maksudnya cairan di kantong perikardium, istilahnya hidroperikardium. Soal direkonstruksi ke mekanisme edema pada penyakit jantung (sesuai recall no. 81).")

q("hemo","rekon","84","Yang dimaksud dengan edema adalah:",
[["Meningkatnya cairan di ruang interstisial","Bisa terjadi karena tekanan hidrostatik naik, tekanan onkotik turun, obstruksi limfe, retensi Na, atau inflamasi.","Benar."],
 ["Meningkatnya volume darah setempat karena dilatasi arteriol","Definisi hiperemia.","Tidak sesuai."],
 ["Ekstravasasi darah dari pembuluh","Definisi perdarahan.","Tidak sesuai."],
 ["Penumpukan cairan di dalam sel","Degenerasi hidropik (jejas sel), bukan edema interstisial.","Tidak sesuai."],
 ["Bekuan darah dalam pembuluh","Definisi trombus.","Tidak sesuai."]],
"Slide: tubuh 60% air (2/3 intrasel, 1/3 ekstrasel, sebagian besar interstisial). Edema dinamai sesuai lokasi: hidrotoraks, hidroperikardium, asites; anasarka = edema berat menyeluruh.",
"Edema = cairan interstisial ↑.","Pisahkan definisi (apa) dari mekanisme (kenapa).",
"Recall menjawab dengan mekanisme (\"peningkatan hidrostatik dan penurunan onkotik\"); itu penyebab, bukan definisi.")

q("hemo","rekon","21","Hemostasis terbagi menjadi fase primer dan sekunder. Yang termasuk mekanisme hemostasis <b>sekunder</b> adalah:",
[["Kaskade koagulasi hingga terbentuk fibrin","Faktor jaringan, kompleks fosfolipid, aktivasi trombin, polimerisasi fibrin.","Benar."],
 ["Adhesi trombosit melalui vWF","Hemostasis primer.","Tidak sesuai."],
 ["Agregasi trombosit membentuk sumbat","Hemostasis primer.","Tidak sesuai."],
 ["Vasokonstriksi refleks","Tahap awal (endotelin, refleks neurogenik).","Bukan hemostasis sekunder."],
 ["Pelepasan t-PA dan trombomodulin","Kontraregulasi antitrombosis.","Tidak sesuai."]],
"Urutan slide: vasokonstriksi → hemostasis primer (sumbat trombosit) → hemostasis sekunder (fibrin) → kontraregulasi antitrombosis.",
"Primer = trombosit; sekunder = fibrin/koagulasi.","Kata \"fibrin\" atau \"faktor pembekuan\" → sekunder.")

q("hemo","rekon","23","Faktor pembekuan darah yang mengawali jalur <b>ekstrinsik</b> bersama faktor jaringan adalah:",
[["Faktor VII","Faktor jaringan (tromboplastin) + VIIa mengaktifkan faktor X.","Benar."],
 ["Faktor XII (Hageman)","Awal jalur intrinsik.","Tidak sesuai."],
 ["Faktor VIII","Jalur intrinsik (kofaktor IXa).","Tidak sesuai."],
 ["Faktor IX","Jalur intrinsik.","Tidak sesuai."],
 ["Faktor XIII","Menstabilkan fibrin (ikatan silang).","Tidak sesuai."]],
"Jalur ekstrinsik dinilai dengan PT; intrinsik dengan aPTT. Faktor VII punya waktu paruh terpendek, sehingga PT paling cepat memanjang pada defisiensi vitamin K/warfarin.",
"Ekstrinsik = TF + VII (PT); intrinsik = XII, XI, IX, VIII (aPTT).","\"Ekstrinsik = Tujuh\" (eks-TUJUH).")

q("hemo","asli","40","Komponen yang mempunyai peranan penting dalam hemostasis adalah:",
[["Endotel pembuluh darah","Utuh: antitrombotik; setelah jejas: protrombotik (vWF, faktor jaringan).","Benar."],
 ["Eosinofil","Berperan pada alergi dan parasit.","Tidak sesuai."],
 ["Tunika media","Otot polos untuk vasokonstriksi, tetapi bukan komponen utama di slide.","Kurang tepat."],
 ["Tunika adventisia","Jaringan ikat luar.","Tidak sesuai."],
 ["Matriks ekstraseluler","Terpapar saat jejas untuk adhesi trombosit, tetapi pengatur utamanya endotel.","Kurang tepat."]],
"Slide: hemostasis dan trombosis bergantung pada dinding pembuluh darah (endotel), trombosit, dan kaskade pembekuan.",
"Tiga pilar: endotel, trombosit, faktor koagulasi.","Pilih komponen dinding yang langsung bersentuhan dengan darah: endotel.")

# ---------------- IMUNOLOGI ----------------
q("rinf","asli","13, 50b","Mekanisme imunologi yang mendasari reaksi kulit pada tes tuberkulin (Mantoux) adalah:",
[["Hipersensitivitas tipe IV (tipe lambat)","Th1 → IFN-γ → aktivasi makrofag (tipe IVa); indurasi muncul 48–72 jam.","Benar."],
 ["Hipersensitivitas tipe I","IgE, reaksi cepat.","Tidak sesuai."],
 ["Hipersensitivitas tipe II","IgG terhadap sel.","Tidak sesuai."],
 ["Hipersensitivitas tipe III","Kompleks imun.","Tidak sesuai."],
 ["Reaksi anafilaktik","Bentuk berat tipe I.","Tidak sesuai."]],
"Slide Respon Imun Non Infeksi: tipe IVa (Th1, IFN-γ, makrofag) contohnya reaksi tuberkulin dan dermatitis kontak.",
"Tuberkulin = DTH = tipe IV.","Reaksi yang dibaca setelah 2–3 hari → tipe IV.")

q("imun","asli","41","Nekrosis fibrinoid pada arteritis sering ditemukan pada SLE. Mekanisme yang mendasari kelainan ini adalah:",
[["Hipersensitivitas tipe III","Kompleks imun (anti-dsDNA–DNA) mengendap di dinding pembuluh, mengaktifkan komplemen.","Benar."],
 ["Reaksi anafilaktik","Tipe I.","Tidak sesuai."],
 ["Hipersensitivitas tipe I","IgE.","Tidak sesuai."],
 ["Hipersensitivitas tipe IV","Sel T.","Tidak sesuai."],
 ["Hipersensitivitas tipe II","Antibodi terhadap antigen sel (pada SLE menyebabkan anemia hemolitik autoimun, trombositopenia).","Bukan mekanisme vaskulitis fibrinoid."]],
"Nekrosis fibrinoid = deposit kompleks imun + fibrin di dinding pembuluh, tampak eosinofilik terang. Slide Respon Imun: SLE (dsDNA, Sm, histon) → deposisi kompleks imun tipe III.",
"Nekrosis fibrinoid ↔ kompleks imun ↔ tipe III.","Vaskulitis + SLE → tipe III.")

q("rinf","asli","39","Monosit yang berada di hepar (sistem retikuloendotelial) disebut:",
[["Sel Kupffer","Makrofag hati.","Benar."],
 ["Makrofag alveolar","Makrofag paru.","Lokasi berbeda."],
 ["Histiosit","Makrofag jaringan ikat.","Lokasi berbeda."],
 ["Osteoklas","Makrofag tulang.","Lokasi berbeda."],
 ["Mikroglia","Makrofag otak.","Lokasi berbeda."]],
"Slide: makrofag berasal dari monosit darah, hidup 60–120 hari di jaringan ikat; histiosit, makrofag alveolar, Kupffer, osteoklas, mikroglia.",
"Kupffer = hati.","Coretan di file: makrofag (paru), Kupffer (hati), histiosit (jaringan), osteoklas (tulang), mikroglia (otak).")

q("rinf","asli","54, 80","Sel imun yang bekerja menjembatani sistem imun <b>bawaan (innate)</b> dan <b>adaptif</b> adalah:",
[["Sel NK (termasuk sel NKT)","Pada diagram \"Innate vs Adaptive Immunity\", sel NKT dan sel T γδ berada di perbatasan kedua sistem.","Benar menurut recall."],
 ["Limfosit B","Sel imun adaptif murni.","Tidak menjembatani."],
 ["Makrofag","Imun bawaan; berperan sebagai APC.","Lihat catatan."],
 ["Sel dendritik","Imun bawaan; APC profesional yang mengaktifkan sel T naif.","Lihat catatan."],
 ["Granulosit","Imun bawaan murni.","Tidak menjembatani."]],
"Diagram klasik (Dranoff, Nat Rev Cancer 2004) yang sering dipakai di slide: innate (makrofag, sel dendritik, sel mast, granulosit, sel NK), adaptif (sel B, sel T), dan di tengahnya sel NKT dan sel T γδ.",
"Sel di perbatasan innate–adaptif: NKT, T γδ.","Coretan recall \"NK cell / T cell\" merujuk ke sel NKT.",
"Soal ambigu. Kalau soal menanyakan \"penghubung\" lewat presentasi antigen, jawabannya <b>sel dendritik</b> (APC profesional). Kalau mengacu diagram slide yang menempatkan sel di tengah kedua sistem, jawabannya <b>sel NK(T)</b>, seperti kunci recall. Baca kalimat soalnya dengan teliti.")

q("rinf","rekon","55","Sel yang bekerja pada sistem imun <b>nonspesifik</b> (bawaan) adalah:",
[["Makrofag","Fagosit innate, tersedia sebelum infeksi, tanpa memori.","Benar."],
 ["Limfosit B","Imun adaptif (humoral).","Spesifik."],
 ["Sel plasma","Penghasil antibodi spesifik.","Spesifik."],
 ["Limfosit T sitotoksik","Imun adaptif (seluler).","Spesifik."],
 ["Limfosit T helper","Imun adaptif.","Spesifik."]],
"Komponen innate: barier fisik/kimia, fagosit (neutrofil, makrofag), sel NK, sel dendritik, komplemen, sel mast.",
"Innate = cepat, umum, tanpa memori.","Semua limfosit B/T dan sel plasma = adaptif.")

q("rinf","rekon","56","Pada inflamasi, pattern recognition receptors (PRRs) mengenali pola molekuler tertentu. Pada penyakit <b>non-infeksi</b>, aktivasi PRR dipicu oleh:",
[["DAMPs (damage-associated molecular patterns)","Molekul dari sel rusak/nekrosis (ATP, HMGB1, asam urat, DNA).","Benar."],
 ["PAMPs (pathogen-associated molecular patterns)","Dari mikroba (LPS, peptidoglikan).","Itu pada infeksi."],
 ["Imunoglobulin E","Pada alergi tipe I.","Bukan ligan PRR."],
 ["Komplemen C3b","Opsonin.","Bukan ligan PRR."],
 ["MHC kelas I","Presentasi antigen ke CD8.","Bukan ligan PRR."]],
"Inflamasi steril (trauma, iskemia, gout, autoimun) dipicu DAMPs; inflamasi infeksi dipicu PAMPs.",
"Infeksi = PAMPs; non-infeksi = DAMPs.","D untuk Damage (kerusakan sel sendiri).")

q("rinf","rekon","57","Salah satu tanda kardinal inflamasi yang terjadi akibat keluarnya eksudat cairan ke jaringan adalah:",
[["Tumor (pembengkakan)","Peningkatan permeabilitas → eksudat → edema.","Benar."],
 ["Rubor (kemerahan)","Akibat vasodilatasi/hiperemia.","Bukan karena eksudat."],
 ["Kalor (panas)","Akibat peningkatan aliran darah.","Tidak sesuai."],
 ["Dolor (nyeri)","Akibat bradikinin, PGE2, dan tekanan.","Tidak sesuai."],
 ["Functio laesa","Hilangnya fungsi.","Tidak sesuai."]],
"Lima tanda kardinal: rubor, kalor, tumor, dolor, functio laesa (Celsus–Virchow).",
"Eksudat → tumor (bengkak).","Pasangkan tiap tanda dengan mekanismenya.")

q("rinf","asli","17, 58, 79","Mediator kimia inflamasi yang berasal dari protein plasma yang diproduksi di hepar adalah:",
[["Bradikinin","Dari HMWK plasma (disintesis hati) yang dipecah kalikrein.","Benar."],
 ["Histamin","Dari sel mast, basofil, trombosit.","Mediator yang berasal dari sel."],
 ["Serotonin","Dari trombosit.","Mediator yang berasal dari sel."],
 ["Lisozim","Dari granula neutrofil dan makrofag.","Berasal dari sel."],
 ["Nitric oxide","Dari endotel dan makrofag.","Berasal dari sel."]],
"Mediator yang berasal dari plasma (prekursornya disintesis hati): sistem kinin (bradikinin), komplemen, sistem koagulasi/fibrinolisis. Mediator dari sel: histamin, serotonin, metabolit asam arakidonat, sitokin, NO.",
"Mediator dari plasma/hati: kinin, komplemen, koagulasi.","Kalau sumbernya \"hepar\", cari protein plasma (bradikinin, komplemen).")

q("rinf","rekon","59","Mediator kimia berikut yang segera meningkatkan permeabilitas vaskular pada fase awal inflamasi akut adalah:",
[["Histamin","Amin vasoaktif dari sel mast; kontraksi endotel venula → celah.","Benar."],
 ["Leukotrien B4","Kemotaksis neutrofil.","Bukan peningkat permeabilitas utama."],
 ["IL-8","Kemoatraktan neutrofil.","Tidak sesuai."],
 ["Lipoksin","Antiinflamasi.","Kebalikannya."],
 ["Tromboksan A2","Vasokonstriksi dan agregasi trombosit.","Tidak sesuai."]],
"Slide: yang meningkatkan permeabilitas = histamin, serotonin, bradikinin, leukotrien C4/D4/E4.",
"Permeabilitas: histamin, serotonin, bradikinin, LTC4–E4.","Histamin = mediator pertama yang dilepas (preformed).",
"Recall menduga \"serotonin\". Serotonin memang meningkatkan permeabilitas, tetapi pada manusia histamin adalah mediator utama fase awal. Bila opsinya hanya serotonin, jawaban serotonin juga dibenarkan.")

# ---------------- FARMAKOLOGI TIROID ----------------
q("ftr","rekon","18","Obat yang digunakan untuk menurunkan sintesis hormon pada hipertiroidisme adalah:",
[["Propiltiourasil (PTU) dan metimazol (tiamazol)","Tionamida, menghambat tiroid peroksidase.","Benar."],
 ["Levotiroksin","Terapi hipotiroidisme.","Kebalikannya."],
 ["Kalsitriol","Vitamin D aktif.","Tidak sesuai."],
 ["Prednison","Glukokortikoid.","Bukan OAT utama."],
 ["Furosemid","Diuretik loop.","Tidak sesuai."]],
"PTU dipilih pada kehamilan trimester I dan krisis tiroid (juga menghambat konversi T4→T3 perifer); metimazol pada umumnya (sekali sehari, risiko hepatotoksik lebih rendah).",
"OAT = PTU, metimazol, karbimazol.","Coretan recall \"PTU & metimazol\" sudah benar.")

q("ftr","rekon","75","Pasien hipotiroid yang minum levotiroksin (LT4) dianjurkan tidak meminumnya bersamaan dengan suplemen kalsium atau zat besi. Alasannya adalah:",
[["Kalsium dan besi mengikat levotiroksin di usus sehingga absorpsinya menurun","Interaksi farmakokinetik (kelasi/adsorpsi).","Benar."],
 ["Levotiroksin merusak suplemen","Keliru.","Tidak sesuai."],
 ["Kombinasi menyebabkan hipertiroid","Keliru.","Justru kadar LT4 turun."],
 ["Suplemen meningkatkan metabolisme LT4 di hati","Itu efek penginduksi enzim (rifampisin, fenitoin).","Bukan mekanisme kalsium/besi."],
 ["Suplemen menghambat sekresi TSH","Keliru.","Tidak sesuai."]],
"Levotiroksin diminum pagi saat perut kosong, 30–60 menit sebelum makan, dan dipisah ± 4 jam dari kalsium, besi, antasida, sukralfat, atau kolestiramin.",
"LT4: perut kosong, pisahkan dari Ca, Fe, antasida.","\"Mengganggu penyerapan\" (seperti coretan recall) = jawaban.")

q("ktp","asli","8","Pasien tirotoksikosis datang dengan takikardia. Dokter memberikan obat untuk mengurangi takikardia tersebut. Jenis obat yang diberikan adalah:",
[["Antagonis β-adrenergik (propranolol)","Memblok efek simpatis; propranolol juga menghambat konversi T4→T3 perifer.","Benar."],
 ["Agonis α-adrenergik","Vasokonstriktor/antihipertensi sentral.","Tidak menurunkan takikardia tirotoksik."],
 ["Agonis β-adrenergik","Menaikkan denyut jantung.","Kebalikannya."],
 ["Antagonis α-adrenergik","Vasodilator, bisa memicu refleks takikardia.","Tidak sesuai."],
 ["Agonis muskarinik","Efek parasimpatis; tidak dipakai untuk takikardia.","Tidak sesuai."]],
"Propranolol = terapi simptomatik tirotoksikosis (palpitasi, tremor, cemas), bukan penurun sintesis hormon.",
"Takikardia → β-bloker.","Beta-1 ada di jantung; blok beta = denyut turun.")

# ---------------- KFR ----------------
q("kfr","rekon","9","Pasien pascastroke menjalani fisioterapi. Menurut slide, tujuan/manfaat terapi fisik (fisioterapi) adalah berikut ini, <b>KECUALI</b>:",
[["Menyembuhkan penyebab dasar stroke","Bukan tujuan fisioterapi.","Benar sebagai jawaban."],
 ["Menghilangkan atau mengurangi nyeri","Tujuan fisioterapi.","Bukan jawaban."],
 ["Mencegah dan mengoreksi kecacatan","Tujuan fisioterapi.","Bukan jawaban."],
 ["Memperbaiki sirkulasi darah","Tujuan fisioterapi.","Bukan jawaban."],
 ["Memulihkan kekuatan, mobilitas, dan koordinasi","Tujuan fisioterapi.","Bukan jawaban."]],
"Fisioterapi: pengobatan fisik dengan perantaraan unsur fisika (panas, dingin, air, arus listrik), pemijatan, manipulasi, dan latihan.",
"Fisioterapi = mengembalikan fungsi, bukan menyembuhkan penyakit dasar.","Coretan recall \"memulihkan fungsi otot\" termasuk tujuan fisioterapi.",
"Recall tidak menyertakan opsi; soal direkonstruksi menjadi format KECUALI sesuai daftar tujuan di slide KFR.")

# ---------------- HEMATOLOGI / PK lain (di luar 20 PPT) ----------------
q("lain","asli","14, 43","Defisiensi faktor IX akan bermanifestasi sebagai penyakit:",
[["Hemofilia B (Christmas disease)","X-linked resesif, aPTT memanjang, PT normal.","Benar."],
 ["Hemofilia A","Defisiensi faktor VIII.","Faktor berbeda."],
 ["Hemofilia C","Defisiensi faktor XI.","Faktor berbeda."],
 ["Penyakit von Willebrand","Defisiensi/defek vWF.","Tidak sesuai."],
 ["Lupus eritematosus sistemik","Penyakit autoimun.","Tidak sesuai."]],
"A = VIII (tersering), B = IX, C = XI (autosomal, ras Yahudi Ashkenazi).",
"A-8, B-9, C-11.","Urut abjad = urut angka (8, 9, lalu 11).")

q("lain","rekon","22","Ion kalsium (Ca²⁺) dalam kaskade pembekuan darah dikenal sebagai faktor:",
[["Faktor IV","Kofaktor di banyak tahap kaskade.","Benar."],
 ["Faktor I","Fibrinogen.","Tidak sesuai."],
 ["Faktor II","Protrombin.","Tidak sesuai."],
 ["Faktor III","Faktor jaringan (tromboplastin).","Tidak sesuai."],
 ["Faktor V","Proakselerin.","Tidak sesuai."]],
"Itulah alasan sitrat dan EDTA berfungsi sebagai antikoagulan: keduanya mengikat kalsium.",
"I fibrinogen, II protrombin, III faktor jaringan, IV kalsium.","Coretan recall \"diPPT\" (sitrat) membantu: sitrat mengikat Ca = faktor IV.")

q("lain","asli","24","Komponen utama yang berperan dalam proses fibrinolisis di antara pilihan berikut adalah:",
[["Inhibitor plasmin","Pengatur fibrinolisis (α2-antiplasmin, PAI-1); satu-satunya opsi yang termasuk sistem plasmin.","Benar sesuai opsi recall."],
 ["Trombin","Mengubah fibrinogen menjadi fibrin (koagulasi).","Bukan fibrinolisis."],
 ["Protrombin","Prekursor trombin.","Bukan fibrinolisis."],
 ["Fibrinogen","Prekursor fibrin.","Bukan fibrinolisis."],
 ["Tromboplastin","Faktor jaringan, memulai jalur ekstrinsik.","Bukan fibrinolisis."]],
"Fibrinolisis: plasminogen → (t-PA/u-PA) → plasmin → memecah fibrin menjadi FDP/D-dimer. Dikendalikan PAI-1 dan α2-antiplasmin.",
"Komponen fibrinolisis: plasminogen, plasmin, t-PA, PAI-1, α2-antiplasmin.","Pilih satu-satunya opsi yang mengandung kata \"plasmin\".",
"Komponen utama fibrinolisis sebenarnya plasmin(ogen) dan t-PA. Kalau di ujian muncul opsi \"plasmin\" atau \"plasminogen\", pilih itu.")

# ---------------- ONKOLOGI / NEOPLASMA ----------------
q("lain","asli","5","Untuk menghindari kesalahan pembelahan, sel memiliki mekanisme checkpoint. Checkpoint utama yang memastikan DNA tidak rusak sebelum sel memasuki fase sintesis terletak pada:",
[["Akhir G1 (G1/S, restriction point)","Diatur p53 dan Rb; DNA rusak → sel berhenti di G1 untuk diperbaiki atau apoptosis.","Benar menurut kunci recall."],
 ["Akhir G0","G0 adalah fase istirahat, bukan checkpoint.","Tidak sesuai."],
 ["Akhir mitosis","Bukan checkpoint klasik.","Tidak sesuai."],
 ["Akhir sintesis","Checkpoint intra-S ada, tetapi bukan jawaban utama.","Kurang tepat."],
 ["Awal mitosis (G2/M)","Juga checkpoint, memeriksa DNA sudah tereplikasi sempurna.","Lihat catatan."]],
"Checkpoint siklus sel: G1/S (paling penting, terkait p53/Rb), G2/M, dan spindle (metafase–anafase). Mutasi p53 menghilangkan G1/S checkpoint sehingga sel dengan DNA rusak terus membelah (dasar karsinogenesis).",
"G1/S = restriction point, dijaga p53 & Rb.","Bila hanya boleh satu, pilih G1/S.",
"Soal recall asli menanyakan \"di mana saja\" checkpoint terjadi. Awal mitosis (G2/M) juga benar. Penulis recall awalnya menandai \"awal mitosis\", lalu membetulkan menjadi \"akhir G1\". Kalau soal di ujian memungkinkan dua jawaban, keduanya checkpoint.")

q("lain","rekon","7","Neoplasma ovarium yang tersusun dari dua atau lebih lapisan embrional (ektoderm, mesoderm, endoderm), misalnya berisi rambut, gigi, dan kelenjar sebasea, adalah:",
[["Teratoma (kista dermoid/teratoma kistik matur)","Tumor sel germinal dengan jaringan dari ≥ 2 lapisan germinal.","Benar."],
 ["Kistadenoma serosum","Tumor epitel permukaan.","Satu jenis jaringan."],
 ["Tumor Krukenberg","Metastasis (biasanya dari lambung) ke ovarium, sel signet ring.","Tidak sesuai."],
 ["Fibroma ovarium","Tumor stroma.","Tidak sesuai."],
 ["Disgerminoma","Tumor sel germinal primitif, satu jenis sel.","Tidak mengandung beberapa lapisan."]],
"Teratoma matur ovarium jinak; teratoma imatur (jaringan neuroepitel embrional) ganas.",
"Banyak lapisan germinal = teratoma.","Rambut + gigi di ovarium = kista dermoid.")

q("lain","rekon","19","Yang termasuk ciri tumor ganas adalah:",
[["Bermetastasis","Kriteria pasti keganasan.","Benar."],
 ["Tumbuh lambat","Ciri tumor jinak.","Tidak sesuai."],
 ["Berkapsul","Ciri tumor jinak.","Tidak sesuai."],
 ["Tidak infiltratif","Ciri tumor jinak.","Tidak sesuai."],
 ["Berdiferensiasi baik","Ciri tumor jinak (ganas cenderung anaplastik).","Tidak sesuai."]],
"Ganas: tumbuh cepat, tidak berkapsul, infiltratif/invasif, metastasis, anaplasia, mitosis atipik.",
"Metastasis = tanda keganasan paling pasti.","Opsi \"tidak\", \"lambat\", \"berkapsul\" = jinak.")

q("lain","asli","16","Pasien kanker stadium IV dengan keadaan umum buruk dan anemia berat. Pilihan terapi yang paling tepat adalah:",
[["Paliatif","Meningkatkan kualitas hidup, mengurangi gejala.","Benar."],
 ["Radioterapi kuratif","Membutuhkan keadaan umum memadai.","Tidak tepat."],
 ["Kemoterapi","Toksik, butuh status performa baik dan Hb cukup.","Tidak tepat."],
 ["Pembedahan","Stadium IV dengan KU buruk tidak operabel.","Tidak tepat."],
 ["Transplantasi","Tidak relevan.","Tidak tepat."]],
"Terapi paliatif tidak berarti \"tidak berbuat apa-apa\": tatalaksana nyeri, transfusi, nutrisi, psikososial, dan spiritual.",
"Stadium IV + KU buruk → paliatif.","Kata \"keadaan umum buruk\" menutup pilihan terapi agresif.")

q("lain","asli","20","Sel kanker menekan sel T sitotoksik melalui jalur PD-1/PD-L1. Obat yang bekerja menghambat PD-1 adalah:",
[["Nivolumab","Antibodi monoklonal anti-PD-1 (immune checkpoint inhibitor).","Benar."],
 ["Rituximab","Anti-CD20 (limfoma sel B).","Tidak sesuai."],
 ["Trastuzumab","Anti-HER2/neu.","Tidak sesuai."],
 ["Siklosporin","Penghambat kalsineurin (imunosupresan).","Kebalikannya."],
 ["Imatinib","Penghambat tirosin kinase BCR-ABL (LMK).","Tidak sesuai."]],
"Anti-PD-1: nivolumab, pembrolizumab. Anti-PD-L1: atezolizumab. Anti-CTLA-4: ipilimumab. Mekanisme ini sejalan dengan fase \"escape\" imunoediting tumor.",
"-mab = antibodi; nivolumab & pembrolizumab = anti-PD-1.","Hafal target: rituximab CD20, trastuzumab HER2, imatinib BCR-ABL.")

q("lain","rekon","10, 70","Pada staging kanker paru (TNM), metastasis ke kelenjar getah bening mediastinal <b>kontralateral</b> atau supraklavikula diklasifikasikan sebagai:",
[["N3","KGB mediastinal/hilus kontralateral atau skalenus/supraklavikula.","Benar."],
 ["N0","Tanpa metastasis KGB regional.","Tidak sesuai."],
 ["N1","KGB peribronkial/hilus ipsilateral.","Tidak sesuai."],
 ["N2","KGB mediastinal ipsilateral/subkarina.","Tidak sesuai."],
 ["N4","Tidak ada kategori N4 pada ca paru.","Tidak sesuai."]],
"Semakin jauh dan menyeberang garis tengah, semakin tinggi N.",
"Paru: N1 hilus ipsilateral, N2 mediastinum ipsilateral, N3 kontralateral/supraklavikula.","\"Kontralateral\" → N3.",
"Recall no. 10 tidak lengkap (\"Kelenjar limfe... TNM berapa?\"); digabung dengan no. 70 yang menyebut nodul kontralateral = N3.")

# ---------------- RADIOLOGI ----------------
q("lain","rekon","2, 64","Perlengkapan radiologi yang berfungsi mencegah radiasi hambur mencapai film adalah:",
[["Grid","Kisi timbal yang menyerap radiasi hambur sebelum mencapai film.","Benar."],
 ["Intensifying screen","Mengubah sinar-X menjadi cahaya untuk menurunkan dosis.","Bukan untuk radiasi hambur."],
 ["Marker","Penanda kanan/kiri.","Tidak sesuai."],
 ["Konus (cone)","Membatasi luas lapangan berkas primer, sehingga mengurangi radiasi hambur yang terbentuk.","Mengurangi pembentukan, tetapi yang mencegahnya mencapai film adalah grid."],
 ["Kaset","Wadah film.","Tidak sesuai."]],
"Radiasi hambur menurunkan kontras gambar (kabur keabuan).",
"Grid = penyaring radiasi hambur di depan film.","Kata kunci \"ketika mencapai film\" → grid.")

q("lain","rekon","61","Sifat sinar-X yang dapat bertebaran ke segala arah setelah mengenai suatu objek disebut:",
[["Radiasi hambur (scatter)","Interaksi Compton menghasilkan foton yang berbelok arah.","Benar."],
 ["Radiasi primer","Berkas langsung dari tabung.","Tidak menyebar ke segala arah."],
 ["Radiasi bocor","Radiasi yang lolos dari rumah tabung.","Tidak sesuai."],
 ["Fluoresensi","Kemampuan membuat zat tertentu berpendar.","Tidak sesuai."],
 ["Ionisasi","Kemampuan mengionkan atom.","Tidak sesuai."]],
"Radiasi hambur adalah sumber utama dosis bagi petugas, sehingga dipakai apron timbal dan jarak.",
"Hambur = scatter = ke segala arah.","\"Bertebaran\" = hambur.")

q("lain","asli","62","Pada foto rontgen, gambaran yang tampak opak (radiopak, putih) menunjukkan material:",
[["Tulang","Densitas tinggi (kalsium) menyerap sinar-X paling banyak.","Benar."],
 ["Lemak","Lebih lusen dari jaringan lunak.","Tidak sesuai."],
 ["Jantung dan pembuluh darah","Densitas jaringan lunak/cairan (abu-abu).","Kurang opak dibanding tulang."],
 ["Gas","Paling lusen (hitam).","Kebalikannya."],
 ["Otot","Jaringan lunak (abu-abu).","Tidak sesuai."]],
"Urutan densitas dari lusen ke opak: udara → lemak → jaringan lunak/cairan → tulang → logam.",
"Opak = putih = tulang/logam; lusen = hitam = udara.","Hafal lima densitas dasar radiologi.")

q("lain","rekon","63","Semakin besar jarak antara sumber sinar-X dengan objek, maka hasil gambarannya:",
[["Magnifikasi semakin kecil","Berkas makin sejajar sehingga bayangan mendekati ukuran asli.","Benar."],
 ["Magnifikasi semakin besar","Terjadi bila jarak sumber–objek kecil atau objek–film besar.","Kebalikannya."],
 ["Relatif sama","Keliru.","Jarak memengaruhi magnifikasi."],
 ["Gambar menjadi lebih kabur","Ketajaman justru membaik.","Tidak sesuai."],
 ["Dosis pasien meningkat","Dosis per luas menurun dengan jarak (hukum kuadrat terbalik).","Tidak sesuai."]],
"Itulah alasan foto toraks PA dibuat dengan jarak 180 cm dan dada menempel kaset: jantung tidak tampak membesar palsu.",
"Sumber–objek jauh + objek–film dekat = magnifikasi minimal.","Bayangkan senter: makin jauh senter, bayangan tangan makin mirip ukuran aslinya.")

q("lain","rekon","65","Prinsip proteksi radiasi ALARA (as low as reasonably achievable) merupakan penerapan asas:",
[["Optimisasi","Dosis ditekan serendah mungkin yang masih wajar dengan memperhatikan faktor sosial-ekonomi.","Benar."],
 ["Justifikasi","Paparan hanya dilakukan bila manfaat lebih besar dari risiko.","Asas berbeda."],
 ["Limitasi dosis","Dosis tidak boleh melebihi nilai batas dosis.","Asas berbeda."],
 ["Kalibrasi","Bukan asas proteksi radiasi.","Tidak sesuai."],
 ["Dekontaminasi","Bukan asas proteksi radiasi.","Tidak sesuai."]],
"Tiga asas proteksi radiasi (ICRP): justifikasi, optimisasi (ALARA), limitasi dosis. Teknik praktis: waktu, jarak, perisai.",
"ALARA = optimisasi.","\"As low as\" = mengoptimalkan, bukan membatasi.")

q("lain","rekon","66","Pada foto toraks ditemukan massa mediastinum yang berisi bayangan gigi dan kalsifikasi, khas teratoma. Lokasi massa ini paling sering di mediastinum:",
[["Anterior","Lokasi khas 4T: timoma, teratoma (tumor sel germinal), tiroid retrosternal, \"terrible\" limfoma.","Benar."],
 ["Superior","Bisa terdapat struma retrosternal, tetapi bukan lokasi khas teratoma.","Kurang tepat."],
 ["Media","Kista bronkogenik, limfadenopati, aneurisma.","Tidak sesuai."],
 ["Posterior","Tumor neurogenik (schwannoma, neurofibroma).","Tidak sesuai."],
 ["Paru perifer","Bukan mediastinum.","Tidak sesuai."]],
"Ditemukannya gigi (dan lemak) dalam massa mediastinum hampir patognomonik untuk teratoma matur.",
"Mediastinum anterior = 4T.","Gigi di mediastinum → teratoma → anterior.",
"<b>Koreksi kunci recall:</b> recall menjawab \"mediastinum media\" (dengan tanda ragu \"idk\"), dan coretan di file menulis \"superior\". Teratoma klasik terletak di <b>mediastinum anterior</b>.")

q("lain","rekon","67","Nodul milier pada foto toraks (misalnya TB milier) berukuran:",
[["1–3 mm (sangat kecil, seperti biji milet)","Nodul kecil-kecil difus di kedua lapangan paru.","Benar."],
 ["5–10 mm","Nodul kecil biasa.","Terlalu besar."],
 ["1–3 cm","Nodul soliter/koin.","Terlalu besar."],
 ["> 3 cm","Disebut massa.","Tidak sesuai."],
 ["Tidak dapat dilihat pada foto polos","Keliru.","Milier tampak sebagai bintik halus difus."]],
"Penyebab pola milier: TB milier, metastasis (Ca tiroid, ginjal), sarkoidosis, pneumokoniosis.",
"Milier = ≤ 3 mm, difus, seragam.","\"Milet\" = biji jewawut yang kecil.",
"Recall menulis \"< 2 mm\". Literatur radiologi umumnya menyebut 1–3 mm; jawaban recall termasuk dalam rentang ini.")

q("lain","rekon","68","Tumor ganas primer pleura yang berhubungan erat dengan paparan asbes adalah:",
[["Mesotelioma maligna","Berasal dari sel mesotel pleura; latensi 20–40 tahun setelah paparan asbes.","Benar."],
 ["Metastasis pleura","Tumor sekunder dari organ lain (paru, payudara).","Bukan tumor primer."],
 ["Adenokarsinoma paru","Tumor primer paru, bukan pleura.","Tidak sesuai."],
 ["Limfoma","Tumor limfoid.","Tidak sesuai."],
 ["Fibroma pleura soliter","Tumor jinak/borderline pleura.","Tidak terkait asbes."]],
"Asbes juga menyebabkan asbestosis (fibrosis interstisial) dan plak pleura, serta meningkatkan risiko karsinoma bronkogenik.",
"Asbes → mesotelioma (pleura).","Mesotel = lapisan pleura.",
"<b>Koreksi recall:</b> recall menulis \"metastase pada pleura disebut mesotelioma\". Itu keliru: mesotelioma adalah tumor <b>primer</b> pleura, bukan metastasis. Soal direkonstruksi ke konsep yang benar.")

q("lain","rekon","69","Pada foto vertebra pria 70 tahun ditemukan lesi osteoblastik multipel. Keganasan primer yang paling mungkin adalah:",
[["Karsinoma prostat","Metastasis tulang tersering bersifat osteoblastik (sklerotik).","Benar."],
 ["Karsinoma ginjal","Metastasis litik.","Tidak sesuai."],
 ["Karsinoma tiroid","Metastasis litik.","Tidak sesuai."],
 ["Mieloma multipel","Lesi litik \"punched-out\".","Tidak sesuai."],
 ["Karsinoma paru","Umumnya litik.","Tidak sesuai."]],
"Osteoblastik: prostat (pria), payudara (bisa campuran). Litik: ginjal, tiroid, paru, mieloma.",
"Pria + osteoblastik vertebra = Ca prostat.","Prostat = \"Putih\" (sklerotik).")

# ---------------- K3 & KESEHATAN LINGKUNGAN ----------------
q("lain","rekon","60","Penyakit yang ditularkan melalui air yang tercemar (misalnya kolera, tifoid, hepatitis A) dan dapat menimbulkan wabah disebut:",
[["Water-borne disease","Ditularkan melalui air minum yang tercemar.","Benar."],
 ["Water-washed disease","Akibat kurangnya air untuk kebersihan (skabies, trakoma).","Tidak sesuai."],
 ["Water-based disease","Agen hidup sebagian siklusnya di hewan air (schistosomiasis).","Tidak sesuai."],
 ["Water-related vector disease","Vektor berkembang biak di air (malaria, DBD).","Tidak sesuai."],
 ["Air-borne disease","Ditularkan lewat udara.","Tidak sesuai."]],
"Klasifikasi Bradley: water-borne, water-washed, water-based, water-related insect vector.",
"Diminum = water-borne.","Bedakan \"diminum\" (borne), \"kurang air\" (washed), \"inang air\" (based), \"vektor\" (related).")

q("lain","rekon","77","Asbestosis pada pekerja pabrik termasuk penyakit akibat kerja yang disebabkan faktor bahaya:",
[["Kimia (debu/serat)","Debu dan serat termasuk faktor kimia di lingkungan kerja.","Benar."],
 ["Fisik","Kebisingan, getaran, radiasi, iklim kerja, pencahayaan.","Tidak sesuai."],
 ["Biologi","Mikroorganisme, hewan, tumbuhan.","Tidak sesuai."],
 ["Ergonomi","Posisi dan beban kerja.","Tidak sesuai."],
 ["Psikososial","Stres kerja, beban mental.","Tidak sesuai."]],
"Pneumokoniosis (asbestosis, silikosis, antrakosis) disebabkan inhalasi debu di tempat kerja.",
"Debu & serat = faktor kimia.","Coretan recall \"kimia\" sudah benar.")

q("lain","rekon","85","Dokter K3 mengunjungi pabrik untuk mengamati proses dan cara kerja serta mengidentifikasi potensi bahaya secara langsung di lapangan. Kegiatan ini disebut:",
[["Walk-through survey (penilaian/survei tempat kerja)","Survei awal untuk mengenali bahaya potensial.","Benar."],
 ["Medical check-up berkala","Pemeriksaan kesehatan pekerja.","Bukan menilai tempat kerja."],
 ["Surveilans epidemiologi","Pengumpulan data penyakit berkelanjutan.","Tidak sesuai."],
 ["Rehabilitasi kerja","Pemulihan pekerja yang sakit.","Tidak sesuai."],
 ["Audit keuangan","Tidak terkait.","Tidak sesuai."]],
"Langkah identifikasi bahaya: walk-through survey → pengukuran lingkungan kerja → penilaian risiko → pengendalian (hierarki: eliminasi, substitusi, rekayasa, administrasi, APD).",
"Melihat langsung proses kerja = walk-through survey.","Recall menyebut \"penilaian pabrik\"; itu nama lain kegiatan ini.",
"Opsi asli recall tidak lengkap; kunci recall \"b. penilaian pabrik\". Soal direkonstruksi dengan istilah baku.")
