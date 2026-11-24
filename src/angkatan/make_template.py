import os,re
D=os.path.dirname(os.path.abspath(__file__))
T=open(os.path.join(D,'..','template.html')).read()
def R(a,b,cnt=1):
    global T
    assert T.count(a)>=1, a[:60]
    T=T.replace(a,b) if cnt==0 else T.replace(a,b,cnt)
R('setTheme(ST.theme);','setTheme(ST.theme);\nfunction applyKM(){QS.forEach(function(q){q.a=(ST.km!=="ver"&&q.r!=null)?q.r:q.v;});}\napplyKM();')
# panel angkatan + mode kunci
R("""     '</div>'+
     (ST.hist.length?""","""     '</div>'+
     '<div class="row" style="margin-top:10px">'+['Articulatio','Calcaneus'].map(function(a){var n=QS.filter(function(q){return PBY[q.ppt].bagian==='Angkatan '+a;}).length;return '<button class="btn" data-ang="'+a+'">Semua soal '+a+' ('+n+')</button>';}).join('')+'</div>'+
     '<div style="margin-top:14px"><div class="small muted" style="font-weight:700;margin-bottom:6px">Kunci yang dipakai untuk menilai</div><div class="row">'+
       '<button class="btn sm'+(ST.km!=="ver"?' pri':'')+'" data-km="ref">Kunci angkatan</button><button class="btn sm'+(ST.km==="ver"?' pri':'')+'" data-km="ver">Kunci terverifikasi</button></div>'+
       '<div class="small muted" style="margin-top:6px">'+QS.filter(function(q){return q.r!=null&&q.r!==q.v;}).length+' soal punya kunci angkatan yang berbeda dengan hasil verifikasi. Dua-duanya selalu ditampilkan di pembahasan.</div></div>'+
     (ST.hist.length?""")
R("""    var id;
    if((id=b.getAttribute("data-pr")))""","""    var id;
    if((id=b.getAttribute("data-km"))){ ST.km=id; applyKM(); save(); home(); return; }
    if((id=b.getAttribute("data-ang"))){ var a=id; startPractice(QS.filter(function(q){return PBY[q.ppt].bagian==='Angkatan '+a;}),"Semua soal "+a,false); return; }
    if((id=b.getAttribute("data-pr")))""")
R("dari PPT yang dipilih","dari set soal yang dipilih")
R("PPT yang diikutkan","Set soal yang diikutkan")
R("Latihan per PPT","Latihan per set soal")
R('ask("Belum ada PPT dipilih","Pilih minimal satu PPT untuk simulasi."','ask("Belum ada set dipilih","Pilih minimal satu set soal untuk simulasi."')
R("Analisis per PPT","Analisis per set soal"); R("<th>PPT</th>","<th>Set</th>",0)
# pill label
i=T.index('(q.tag==="asli"?'); j=T.index("(it.fl?'<span class=\"pill pred\">Ditandai ragu",i)
T=T[:i]+"""(q.lbl?'<span class="pill '+(q.tag==="rekon"?'pred':'asli')+'">'+esc(q.lbl)+' · no. '+esc(q.no)+'</span>':'')+
     """+T[j:]
# explain baru
i=T.index('function explain(it){'); j=T.index('/* ================= HASIL')
T=T[:i]+r'''function explain(it){
  var q=it.q, mine=it.ans, ok=mine===q.a, kpos=it.ord.indexOf(q.a), diff=q.r!=null&&q.r!==q.v, h='<div class="expl">';
  if(mine===null) h+='<div class="verdict na">Tidak dijawab. Kunci: '+LET[kpos]+'. '+q.o[q.a][0]+'</div>';
  else h+='<div class="verdict '+(ok?'ok':'no')+'">'+(ok?'Benar! ':'Belum tepat. ')+'Kunci jawaban: '+LET[kpos]+'. '+q.o[q.a][0]+'</div>';
  if(diff) h+='<div class="note"><b>Kunci angkatan vs kunci terverifikasi:</b> file angkatan menandai <b>'+LET[it.ord.indexOf(q.r)]+'. '+q.o[q.r][0]+'</b>, hasil verifikasi <b>'+LET[it.ord.indexOf(q.v)]+'. '+q.o[q.v][0]+'</b>. Nilai sesi ini memakai '+(ST.km==="ver"?'kunci terverifikasi':'kunci angkatan')+' (bisa diganti di beranda).</div>';
  else if(q.r==null) h+='<div class="note">File angkatan tidak menandai jawaban untuk soal ini, jadi kunci diambil dari hasil verifikasi.</div>';
  if(mine!==null&&!ok){ var mp=it.ord.indexOf(mine);
    if(diff&&mine===q.v) h+='<div class="mistake"><b>Pilihanmu ('+LET[mp]+') sama dengan kunci terverifikasi</b>, tapi berbeda dengan kunci angkatan. Untuk ujian, pahami alasan di catatan di bawah.</div>';
    else h+='<div class="mistake"><b>Kenapa pilihanmu ('+LET[mp]+') keliru:</b> '+q.o[mine][1]+'</div>'; }
  h+='<div class="blk"><h4>Pembahasan</h4><div class="body">'+q.o[q.v][1]+(q.p?'<div style="margin-top:6px">'+q.p+'</div>':'')+'</div></div>';
  h+='<div class="blk"><h4>Pembahasan semua opsi</h4>';
  it.ord.forEach(function(oi,k){
    var good=oi===q.a, me=oi===mine;
    var tags=(good?'<em class="g">Kunci</em>':'')+(diff&&oi===q.r&&!good?'<em class="m">Kunci angkatan</em>':'')+(diff&&oi===q.v&&!good?'<em class="m">Terverifikasi</em>':'')+(me&&!good?'<em class="b">Pilihanmu</em>':'')+(me&&good?'<em class="m">Pilihanmu</em>':'');
    h+='<div class="optx'+(good?' good':'')+(me&&!good?' mine':'')+'"><div class="h">'+LET[k]+'. '+q.o[oi][0]+tags+'</div><p>'+q.o[oi][1]+'</p></div>';
  });
  h+='</div>';
  if(q.n) h+='<div class="note"><b>Catatan:</b> '+q.n+'</div>';
  h+='</div>';
  return h;
}

'''+T[j:]
R('"Latihan semua soal ("+(CUSTOM?"urut per PPT":"urut nomor recall")+")"','"Latihan semua soal (urut set & nomor)"')
R("QS.slice().sort(function(x,y){return (x.ord||0)-(y.ord||0)||PIDX[x.ppt]-PIDX[y.ppt]||x.id-y.id;})","QS.slice()")
R('Tiap soal ada kunci, pembahasan semua opsi, poin penting, dan catatan bila slide berbeda dengan referensi.','Tiap soal ada kunci, pembahasan semua opsi, dan catatan bila kunci angkatan perlu dikoreksi.')
open(os.path.join(D,'template_angkatan.html'),'w').write(T)
print('ok')
