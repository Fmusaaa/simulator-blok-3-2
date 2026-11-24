(function(){
"use strict";
/* =====================================================================
   Simulator Blok 3.2 — Medical Exam & Learning Platform (v2)
   Data bank: <script id="bank"> (dibangun dari data/bank.json oleh build.py)
   Penyimpanan: localStorage (KEY), migrasi otomatis dari versi lama (OLDKEY)
   ===================================================================== */
const BANK=JSON.parse(document.getElementById("bank").textContent);
const PPTS=BANK.ppts, QS=BANK.qs, QBY={}, PBY={}, PIDX={};
QS.forEach(q=>{QBY[q.id]=q;});
PPTS.forEach((p,i)=>{PBY[p.id]=p;PIDX[p.id]=i;});
const BAGS=[...new Set(PPTS.map(p=>p.bagian))];
const LET="ABCDEFGH", KEY="__KEY__", OLDKEY="__OLDKEY__";
const DIFF={1:"Mudah",2:"Sedang",3:"Sulit"};
const TYPE={recall:"Recall",understanding:"Pemahaman",application:"Aplikasi klinis",analysis:"Analisis",integrated:"Kasus terintegrasi"};
const CONF={y:"Yakin",c:"Cukup yakin",g:"Menebak"};
const TAGL={asli:"SOAL ASLI · recall UAM 3.2",rekon:"Direkonstruksi",prediksi:"Prediksi",baru:"Soal baru",slide:"Contoh soal slide dosen"};
const $=id=>document.getElementById(id);
const esc=s=>String(s==null?"":s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const strip=s=>String(s||"").replace(/<[a-zA-Z\/][^>]*>/g," ").replace(/\s+/g," ").trim();
const pc=(a,b)=>b?Math.round(a/b*100):0;
const shuffle=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));const t=a[i];a[i]=a[j];a[j]=t;}return a;};
const fmt=s=>{s=Math.max(0,Math.round(s));const h=Math.floor(s/3600),m=Math.floor(s%3600/60),x=s%60;return (h?h+":":"")+String(m).padStart(2,"0")+":"+String(x).padStart(2,"0");};
const dstr=t=>{const d=new Date(t),p=x=>String(x).padStart(2,"0");return d.getFullYear()+"-"+p(d.getMonth()+1)+"-"+p(d.getDate())+" "+p(d.getHours())+":"+p(d.getMinutes());};
const accCls=r=>r>=0.8?"g":r>=0.6?"w":"b";
const accTxt=r=>r>=0.8?"good-t":r>=0.6?"warn-t":"bad-t";

/* ---------------- penyimpanan ---------------- */
const ST={v:2,stats:{},flags:{},bm:{},hist:[],cm:{},active:null,set:{},setup:{}};
function emptyCm(){return {y:{ok:0,no:0},c:{ok:0,no:0},g:{ok:0,no:0}};}
(function load(){
  try{
    let raw=localStorage.getItem(KEY);
    if(raw){ Object.assign(ST,JSON.parse(raw)); }
    else if(OLDKEY&&(raw=localStorage.getItem(OLDKEY))){
      const o=JSON.parse(raw);
      ST.stats=o.stats||{}; ST.flags=o.flags||{};
      if(o.theme) ST.set.theme=o.theme;
      (o.hist||[]).forEach((h,i)=>ST.hist.push({id:"old"+i,date:h.date,mode:"exam",title:"Simulasi ujian (versi lama)",n:h.n,ok:Math.round(h.pct*h.n/100),blank:0,pct:h.pct,legacy:true}));
      ST.migrated=true;
    }
  }catch(e){}
  ST.set=Object.assign({conf:true,shuf:true,tpq:72,theme:null},ST.set||{});
  ST.cm=Object.assign(emptyCm(),ST.cm||{});
  ST.bm=ST.bm||{}; ST.flags=ST.flags||{}; ST.hist=ST.hist||[]; ST.setup=ST.setup||{};
})();
let storageOk=true;
function save(){
  try{localStorage.setItem(KEY,JSON.stringify(ST));storageOk=true;}
  catch(e){
    storageOk=false;
    // kosongkan detail riwayat lama bila kuota penuh, lalu coba lagi
    try{ST.hist.slice(0,-10).forEach(h=>{delete h.items;});localStorage.setItem(KEY,JSON.stringify(ST));storageOk=true;}catch(e2){}
  }
}
function setTheme(t){ if(t) document.documentElement.setAttribute("data-theme",t); else document.documentElement.removeAttribute("data-theme"); }
setTheme(ST.set.theme);
$("themeBtn").onclick=()=>{
  const cur=document.documentElement.getAttribute("data-theme");
  const dark=cur?cur==="dark":window.matchMedia("(prefers-color-scheme: dark)").matches;
  ST.set.theme=dark?"light":"dark"; setTheme(ST.set.theme); save();
};

/* ---------------- statistik ---------------- */
const stat=id=>ST.stats[id]||null;
function record(q,ans,conf){
  const s=ST.stats[q.id]||{n:0,c:0,w:0,last:null};
  const ok=ans===q.a;
  s.n++; if(ok) s.c++; else s.w++; s.last=ok?1:0; s.la=ans; s.lc=conf||null; s.ts=Date.now();
  ST.stats[q.id]=s;
  if(conf&&ST.cm[conf]) ST.cm[conf][ok?"ok":"no"]++;
}
function status(q){const s=stat(q.id);return !s?"new":s.last===1?"ok":"no";}
const isWrong=q=>{const s=stat(q.id);return !!s&&s.last===0;};
const isWeakOk=q=>{const s=stat(q.id);return !!s&&s.last===1&&s.lc==="g";};
function agg(list){
  let n=0,done=0,ok=0;
  list.forEach(q=>{n++;const s=stat(q.id);if(s){done++;if(s.last===1)ok++;}});
  return {n,done,ok,acc:done?ok/done:0};
}
function groupBy(list,keyFn){const m=new Map();list.forEach(q=>{const k=keyFn(q);if(!m.has(k))m.set(k,[]);m.get(k).push(q);});return m;}

/* ---------------- modal, toast, lightbox ---------------- */
let mCb=null;
function ask(title,body,yes,yesLabel,noLabel){
  $("mTitle").textContent=title; $("mBody").innerHTML=body; $("mYes").textContent=yesLabel||"Ya";
  $("mNo").textContent=noLabel||"Batal"; $("mNo").classList.toggle("hide",noLabel===false);
  mCb=yes; $("modal").classList.add("show"); setTimeout(()=>$("mYes").focus(),30);
}
$("mNo").onclick=()=>{$("modal").classList.remove("show");mCb=null;};
$("mYes").onclick=()=>{$("modal").classList.remove("show");const f=mCb;mCb=null;if(f)f();};
function info(title,body){ask(title,body,null,"Oke",false);}
let lbScale=1;
function openLB(src,cap){
  $("lbImg").src=src; $("lbCap").innerHTML=cap||""; lbScale=1; applyLB(); $("lb").classList.add("show");
}
function applyLB(){
  const img=$("lbImg"), st=$("lbStage");
  if(lbScale===0){ img.style.width=""; img.style.maxWidth="100%"; img.style.maxHeight=(st.clientHeight-20)+"px"; $("lbZ").textContent="Pas"; return; }
  img.style.maxWidth="none"; img.style.maxHeight="none";
  img.style.width=(img.naturalWidth*lbScale||"")+"px"; $("lbZ").textContent=Math.round(lbScale*100)+"%";
}
$("lbIn").onclick=()=>{lbScale=Math.min((lbScale||1)*1.25,6);applyLB();};
$("lbOut").onclick=()=>{lbScale=Math.max((lbScale||1)/1.25,.2);applyLB();};
$("lbFit").onclick=()=>{lbScale=0;applyLB();};
$("lbX").onclick=()=>$("lb").classList.remove("show");
$("lbImg").onload=()=>{lbScale=0;applyLB();};
document.addEventListener("click",e=>{
  const im=e.target.closest(".qfig img,.qimg");
  if(im){e.preventDefault();e.stopPropagation();const cap=im.closest("figure")?im.closest("figure").querySelector("figcaption"):null;openLB(im.src,cap?cap.innerHTML:(im.alt||""));}
},true);

/* ---------------- navigasi ---------------- */
const IC={
 dashboard:'<path d="M3 13h8V3H3zm10 8h8V11h-8zM3 21h8v-6H3zm10-18v6h8V3z"/>',
 ujian:'<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2.5M9 2h6"/>',
 belajar:'<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M8 7h8M8 11h6"/>',
 bank:'<path d="M4 6h16M4 12h16M4 18h10"/>',
 salah:'<circle cx="12" cy="12" r="9"/><path d="M15 9l-6 6M9 9l6 6"/>',
 bookmark:'<path d="M6 3h12v18l-6-4-6 4z"/>',
 riwayat:'<path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5M12 7v5l3 2"/>',
 analisis:'<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
 setelan:'<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>'
};
const NAV=[["dashboard","Dashboard"],["ujian","Mode CBT"],["belajar","Mode belajar"],["bank","Bank soal"],"-",["salah","Soal salah"],["bookmark","Bookmark"],["riwayat","Riwayat ujian"],["analisis","Analisis"],"-",["setelan","Pengaturan"]];
const svg=k=>'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'+IC[k]+'</svg>';
function renderNav(cur){
  const wr=QS.filter(q=>isWrong(q)).length, bm=Object.keys(ST.bm).filter(id=>QBY[id]).length;
  const cnt={salah:wr,bookmark:bm,riwayat:ST.hist.length};
  $("nav").innerHTML=NAV.map(x=>x==="-"?'<div class="sep"></div>':'<a href="#'+x[0]+'" class="'+(cur===x[0]?"on":"")+'">'+svg(x[0])+x[1]+(cnt[x[0]]?'<span class="cnt">'+cnt[x[0]]+'</span>':'')+'</a>').join("");
  $("bnav").innerHTML=NAV.filter(x=>x!=="-").map(x=>'<a href="#'+x[0]+'" class="'+(cur===x[0]?"on":"")+'">'+svg(x[0])+({"Riwayat ujian":"Riwayat","Mode CBT":"CBT","Mode belajar":"Belajar"}[x[1]]||x[1])+'</a>').join("");
}

/* ---------------- sesi (ujian / belajar) ---------------- */
let S=null, TIMER=null;
function makeItems(list,shufOpt){
  return list.map(q=>{const ord=q.o.map((_,i)=>i); if(shufOpt) shuffle(ord); return {id:q.id,ord,ans:null,conf:null,fl:!!ST.flags[q.id],struck:{},pend:null};});
}
function persist(){
  if(!S){ST.active=null;save();return;}
  if(S.done){ST.active=null;save();return;}
  ST.active={mode:S.mode,title:S.title,items:S.items.map(x=>({id:x.id,ord:x.ord,ans:x.ans,conf:x.conf,fl:x.fl})),cur:S.cur,t0:S.t0,limit:S.limit||0,src:S.src||""};
  save();
}
function startSession(mode,list,title,opts){
  opts=opts||{};
  if(!list.length){info("Tidak ada soal","Tidak ada soal yang cocok dengan pilihan ini.");return;}
  const begin=()=>{
    S={mode,title,items:makeItems(list,opts.shuf!==false),cur:0,done:false,t0:Date.now(),limit:opts.limit||0,src:opts.src||""};
    persist(); location.hash="soal"; render();
  };
  if(ST.active&&ST.active.mode==="exam"&&!(S&&S.done)) ask("Ada ujian yang belum selesai","Memulai sesi baru akan membatalkan ujian \""+esc(ST.active.title)+"\" (tidak dinilai). Lanjutkan?",begin,"Mulai baru");
  else begin();
}
function resumeActive(){
  const a=ST.active; if(!a) return false;
  const items=a.items.filter(x=>QBY[x.id]).map(x=>{const q=QBY[x.id];let ord=x.ord;if(!ord||ord.length!==q.o.length) ord=q.o.map((_,i)=>i);return {id:x.id,ord,ans:x.ans,conf:x.conf||null,fl:!!x.fl,struck:{},pend:null};});
  if(!items.length){ST.active=null;save();return false;}
  S={mode:a.mode,title:a.title,items,cur:Math.min(a.cur||0,items.length-1),done:false,t0:a.t0,limit:a.limit||0,src:a.src||""};
  if(S.mode==="exam"&&S.limit&&remaining()<=0){ finishExam(true); return true; }
  location.hash="soal"; render(); return true;
}
const remaining=()=>S&&S.limit?S.limit-(Date.now()-S.t0)/1000:Infinity;
function startTimer(){
  stopTimer();
  if(!S||S.mode!=="exam"||!S.limit||S.done) return;
  const tick=()=>{
    if(!S||S.done){stopTimer();return;}
    const left=remaining(), t=fmt(left);
    ["tmr","topTimer"].forEach(id=>{const el=$(id);if(el){el.textContent="⏱ "+t;el.classList.toggle("low",left<=60);}});
    if(left<=0){stopTimer();finishExam(true);}
  };
  $("topTimer").classList.remove("hide"); tick(); TIMER=setInterval(tick,1000);
}
function stopTimer(){ if(TIMER){clearInterval(TIMER);TIMER=null;} $("topTimer").classList.add("hide"); }

/* ---------------- tampilan soal ---------------- */
function metaPills(q,full){
  const p=PBY[q.ppt];
  let h='<span class="pill">'+esc(p.title)+'</span><span class="pill">'+esc(q.topik)+'</span>';
  if(q.tag&&TAGL[q.tag]) h+='<span class="pill '+(q.tag==="asli"||q.tag==="rekon"?"asli":q.tag==="prediksi"?"pred":"baru")+'">'+TAGL[q.tag]+(q.src==="uam2024"?" (2024)":"")+'</span>';
  if(full!==false){
    if(q.d) h+='<span class="pill d'+q.d+'">'+DIFF[q.d]+'</span>';
    if(q.ty) h+='<span class="pill">'+TYPE[q.ty]+'</span>';
  }
  return h;
}
function figure(q){
  if(!q.img) return "";
  const im=Array.isArray(q.img)?q.img:[q.img];
  return im.map(x=>'<figure class="qfig"><img src="'+esc(x.src)+'" alt="'+esc(x.alt||x.cap||"Gambar soal")+'" loading="lazy"><figcaption>'+esc(x.cap||"")+(x.credit?' <i>Sumber: '+esc(x.credit)+'</i>':'')+(x.illus?' <b>[Ilustrasi tambahan, bukan dari soal asli]</b>':'')+' · ketuk untuk perbesar</figcaption></figure>').join("");
}
function render(){
  if(!S){route();return;}
  if(S.done){results();return;}
  renderNav("");
  const it=S.items[S.cur], q=QBY[it.id], exam=S.mode==="exam";
  const answered=it.ans!==null, reveal=!exam&&answered&&!it.pend;
  const nAns=S.items.filter(x=>x.ans!==null).length;
  let h='<div class="qbar"><span class="pill brand">'+(exam?"Mode CBT":"Mode belajar")+'</span><b style="font-size:15px">'+esc(S.title)+'</b><div class="sp"></div>'+
    '<span class="muted small">'+nAns+'/'+S.items.length+' dijawab</span>'+
    (exam&&S.limit?'<span class="pill timer" id="tmr"></span>':'')+
    '<button class="btn sm mob-map" id="mapT">Peta soal</button>'+
    (exam?'<button class="btn sm pri" id="endB">Kirim & akhiri</button>':'<button class="btn sm" id="endB">Selesai</button>')+'</div>';
  h+='<div class="layout"><div><div class="qcard">';
  h+='<div class="row" style="justify-content:space-between;margin-bottom:6px"><div class="qnum" style="margin:0">Soal '+(S.cur+1)+' dari '+S.items.length+'</div>'+
     '<button class="btn sm bmk'+(ST.bm[q.id]?" on":"")+'" id="bmB" title="Bookmark (B)">'+(ST.bm[q.id]?"★ Tersimpan":"☆ Bookmark")+'</button></div>';
  h+='<div class="metarow">'+metaPills(q,!exam)+(it.fl?'<span class="pill pred">Ditandai ragu</span>':'')+'</div>';
  h+='<div class="stem">'+q.s+'</div>'+figure(q)+'<div class="opts">';
  const lock=reveal;
  it.ord.forEach((oi,k)=>{
    let cls="opt";
    if(lock){ if(oi===q.a) cls+=" ok"; else if(oi===it.ans) cls+=" no"; }
    else if(it.ans===oi||it.pend===oi) cls+=" sel";
    if(it.struck[oi]) cls+=" struck";
    if(lock) cls+=" locked";
    h+='<div class="'+cls+'" data-o="'+oi+'" role="button" tabindex="0" aria-label="Opsi '+LET[k]+'"><span class="L">'+LET[k]+'</span><span class="T">'+q.o[oi][0]+'</span>'+(lock?'':'<button class="x" data-x="'+oi+'" title="Coret opsi" aria-label="Coret opsi">✕</button>')+'</div>';
  });
  h+='</div>';
  // confidence
  if(!exam&&it.pend!==null&&it.pend!==undefined){
    h+='<div class="conf"><div class="q">Seberapa yakin dengan jawaban '+LET[it.ord.indexOf(it.pend)]+'? (jawaban dinilai setelah dipilih)</div><div class="row">'+
       Object.keys(CONF).map((k,i)=>'<button class="btn" data-cf="'+k+'">'+(i+1)+' · '+CONF[k]+'</button>').join("")+'</div>'+
       '<div class="small muted" style="margin-top:6px">Ganti pilihan dengan mengetuk opsi lain. Tingkat keyakinan dipakai untuk analisis pemahaman & remedial.</div></div>';
  }
  if(exam&&answered&&ST.set.conf){
    h+='<div class="conf"><div class="q">Tingkat keyakinan (opsional)</div><div class="row">'+Object.keys(CONF).map(k=>'<button class="btn sm'+(it.conf===k?" on":"")+'" data-cf="'+k+'">'+CONF[k]+'</button>').join("")+'</div></div>';
  }
  if(reveal) h+=explain(q,it);
  h+='<div class="qnav"><button class="btn" id="prevB" '+(S.cur===0?"disabled":"")+'>← Sebelumnya</button><button class="btn" id="flagB">'+(it.fl?"Hapus tanda ragu":"Tandai ragu")+'</button><div class="sp"></div><button class="btn pri" id="nextB">'+(S.cur===S.items.length-1?(exam?"Kirim & akhiri":"Selesai"):"Berikutnya →")+'</button></div>';
  h+='<div class="small muted" style="margin-top:10px">Pintasan: <kbd>A</kbd>–<kbd>E</kbd> pilih · <kbd>1</kbd>–<kbd>3</kbd> keyakinan · <kbd>←</kbd><kbd>→</kbd> pindah · <kbd>F</kbd> ragu · <kbd>B</kbd> bookmark</div>';
  h+='</div></div><aside class="side" id="side"><div class="panel" style="padding:14px"><div style="font-weight:700;margin-bottom:6px">Peta soal</div>'+
     '<div class="legend">'+(exam?'<span><i></i>Belum</span><span><i style="background:var(--brand-soft);border-color:var(--brand)"></i>Dijawab</span>':'<span><i></i>Belum</span><span><i style="background:var(--good-soft);border-color:var(--good)"></i>Benar</span><span><i style="background:var(--bad-soft);border-color:var(--bad)"></i>Salah</span>')+'<span><i style="background:var(--flag);border-color:var(--flag)"></i>Ragu</span></div>'+
     '<div class="map" id="map">'+S.items.map((x,i)=>{
        let c=""; if(x.ans!==null){ c=exam?"ans":(x.ans===QBY[x.id].a?"ok":"no"); }
        if(i===S.cur) c+=" cur"; if(x.fl) c+=" fl";
        return '<button class="'+c+'" data-go="'+i+'" aria-label="Soal '+(i+1)+'">'+(i+1)+'</button>';}).join("")+'</div>'+
     '<div class="small muted" style="margin-top:8px">'+(exam?'Kunci & pembahasan tampil setelah ujian dikirim. Jawaban tersimpan otomatis — aman bila halaman tertutup.':'Progres tersimpan otomatis.')+'</div></div></aside></div>';
  $("app").innerHTML=h;
  persist();
  bindQuiz();
  if(exam&&S.limit) startTimer(); else stopTimer();
}
function bindQuiz(){
  const it=S.items[S.cur];
  $("app").onclick=e=>{
    const x=e.target.closest("[data-x]");
    if(x){e.stopPropagation();const oi=+x.getAttribute("data-x");it.struck[oi]=!it.struck[oi];render();return;}
    const cf=e.target.closest("[data-cf]"); if(cf){setConf(cf.getAttribute("data-cf"));return;}
    const o=e.target.closest("[data-o]"); if(o){choose(+o.getAttribute("data-o"));return;}
    const g=e.target.closest("[data-go]"); if(g){S.cur=+g.getAttribute("data-go");render();window.scrollTo(0,0);return;}
  };
  $("prevB").onclick=()=>go(-1);
  $("nextB").onclick=()=>{ if(S.cur===S.items.length-1) endAsk(); else go(1); };
  $("flagB").onclick=toggleFlag;
  $("bmB").onclick=toggleBm;
  $("endB").onclick=endAsk;
  const mt=$("mapT"); if(mt) mt.onclick=()=>{$("side").classList.toggle("show");$("side").scrollIntoView({behavior:"smooth"});};
}
function go(d){const n=S.cur+d;if(n<0||n>=S.items.length)return;S.cur=n;render();window.scrollTo(0,0);}
function toggleFlag(){const it=S.items[S.cur];it.fl=!it.fl;if(it.fl)ST.flags[it.id]=1;else delete ST.flags[it.id];save();render();}
function toggleBm(id){id=typeof id==="number"||typeof id==="string"?id:S.items[S.cur].id;if(ST.bm[id])delete ST.bm[id];else ST.bm[id]=Date.now();save();if(S&&!S.done&&location.hash==="#soal")render();}
function choose(oi){
  const it=S.items[S.cur];
  if(S.mode==="exam"){ it.ans=(it.ans===oi?null:oi); if(it.ans===null) it.conf=null; render(); return; }
  if(it.ans!==null) return;            // belajar: sudah dinilai
  if(ST.set.conf){ it.pend=oi; render(); return; }
  commit(it,oi,null);
}
function commit(it,oi,conf){
  const q=QBY[it.id];
  it.ans=oi; it.conf=conf; it.pend=null;
  record(q,oi,conf); save(); render();
}
function setConf(k){
  const it=S.items[S.cur];
  if(S.mode==="exam"){ if(it.ans===null) return; it.conf=(it.conf===k?null:k); render(); return; }
  if(it.pend!==null&&it.pend!==undefined) commit(it,it.pend,k);
}
function endAsk(){
  const n=S.items.length, a=S.items.filter(x=>x.ans!==null).length, f=S.items.filter(x=>x.fl).length;
  if(S.mode==="exam"){
    ask("Kirim jawaban dan akhiri ujian?",'Dijawab <b>'+a+'</b> dari '+n+' soal'+(n-a?' · <b>'+(n-a)+'</b> belum dijawab':'')+(f?' · <b>'+f+'</b> ditandai ragu':'')+'.<br>Setelah dikirim, jawaban tidak bisa diubah.',()=>finishExam(false),"Ya, kirim");
  } else {
    const fin=()=>finishLearn();
    if(a<n) ask("Akhiri sesi belajar?",(n-a)+' soal belum dijawab. Hasil dihitung dari soal yang sudah dijawab.',fin,"Akhiri");
    else fin();
  }
}
function histEntry(timeout){
  const items=S.items, ok=items.filter(x=>x.ans===QBY[x.id].a).length, ans=items.filter(x=>x.ans!==null).length;
  const exam=S.mode==="exam", denom=exam?items.length:Math.max(ans,1);
  return {id:"h"+Date.now(),date:dstr(Date.now()),mode:S.mode,title:S.title,n:items.length,ans,ok,blank:items.length-ans,pct:pc(ok,denom),
    dur:Math.round((Date.now()-S.t0)/1000),limit:S.limit||0,timeout:!!timeout,
    items:items.map(x=>[x.id,x.ord.join(""),x.ans,x.conf,x.fl?1:0])};
}
function finishExam(timeout){
  stopTimer(); if(!S) return;
  S.items.forEach(it=>{ if(it.ans!==null) record(QBY[it.id],it.ans,it.conf); });
  S.timeout=!!timeout; S.done=true;
  const h=histEntry(timeout); ST.hist.push(h); if(ST.hist.length>60) ST.hist=ST.hist.slice(-60);
  S.hid=h.id; ST.active=null; save();
  if(timeout) setTimeout(()=>info("Waktu habis","Jawaban dikirim otomatis. Soal yang belum dijawab dihitung kosong."),50);
  location.hash="hasil"; results();
}
function finishLearn(){
  stopTimer(); S.done=true;
  if(S.items.some(x=>x.ans!==null)){ const h=histEntry(false); ST.hist.push(h); if(ST.hist.length>60) ST.hist=ST.hist.slice(-60); S.hid=h.id; }
  ST.active=null; save(); location.hash="hasil"; results();
}

/* ---------------- pembahasan ---------------- */
function explain(q,it){
  const mine=it?it.ans:null, ok=mine===q.a, ord=it?it.ord:q.o.map((_,i)=>i), kpos=ord.indexOf(q.a);
  let h='<div class="expl">';
  if(it){
    if(mine===null) h+='<div class="verdict na">Tidak dijawab. Kunci: '+LET[kpos]+'</div>';
    else h+='<div class="verdict '+(ok?"ok":"no")+'">'+(ok?"Benar! ":"Belum tepat. ")+'Kunci jawaban: '+LET[kpos]+'. '+q.o[q.a][0]+
      (it.conf?' <span class="confpill '+it.conf+'">'+CONF[it.conf]+'</span>':'')+'</div>';
    if(it.conf) h+='<div class="small muted">'+confNote(ok,it.conf)+'</div>';
  } else h+='<div class="verdict ok">Kunci jawaban: '+LET[kpos]+'. '+q.o[q.a][0]+'</div>';
  if(q.ks) h+='<div class="blk"><h4>1 · Konsep yang diuji</h4><div class="body">'+q.ks+'</div></div>';
  if(q.kw&&q.kw.length) h+='<div class="blk"><h4>2 · Kata kunci pada soal</h4><div class="kw">'+q.kw.map(k=>'<span>'+esc(k)+'</span>').join("")+'</div></div>';
  if(q.an) h+='<div class="blk"><h4>3 · Analisis kasus</h4><div class="body">'+q.an+'</div></div>';
  h+='<div class="blk"><h4>'+(q.ks?"4 · ":"")+'Kenapa jawaban '+LET[kpos]+' paling tepat</h4><div class="body">'+q.o[q.a][2]+(q.o[q.a][1]?'<div style="margin-top:6px" class="muted">'+q.o[q.a][1]+'</div>':'')+'</div></div>';
  if(mine!==null&&it&&!ok){const mp=ord.indexOf(mine);h+='<div class="mistake"><b>Kenapa pilihanmu ('+LET[mp]+') keliru:</b> '+q.o[mine][2]+(q.o[mine][1]?'<br><span class="muted">Faktanya: '+q.o[mine][1]+'</span>':'')+'</div>';}
  h+='<div class="blk"><h4>'+(q.ks?"5 · ":"")+'Analisis opsi '+LET[0]+'–'+LET[ord.length-1]+'</h4>';
  ord.forEach((oi,k)=>{
    const good=oi===q.a, me=oi===mine;
    h+='<div class="optx'+(good?" good":"")+(me&&!good?" mine":"")+'"><div class="h">'+LET[k]+'. '+q.o[oi][0]+(good?'<em class="g">Kunci</em>':'')+(me&&!good?'<em class="b">Pilihanmu</em>':'')+(me&&good?'<em class="m">Pilihanmu</em>':'')+'</div>'+
       (q.o[oi][1]?'<p><b>Fakta:</b> '+q.o[oi][1]+'</p>':'')+'<p><b>'+(good?"Kenapa benar:":"Kenapa salah:")+'</b> '+q.o[oi][2]+'</p></div>';
  });
  h+='</div>';
  const pearls=[q.p,q.k].filter(Boolean);
  if(pearls.length) h+='<div class="pearl"><b>'+(q.ks?"6 · ":"")+'Clinical pearls:</b> '+pearls.join(" ")+'</div>';
  if(q.t) h+='<div class="tip"><b>Tips menjawab:</b> '+q.t+'</div>';
  if(q.n) h+='<div class="note"><b>Catatan (slide dosen vs referensi):</b> '+q.n+'</div>';
  const p=PBY[q.ppt];
  h+='<div class="ref"><b>'+(q.ks?"7 · ":"")+'Referensi:</b> '+(q.ref?q.ref:'PPT “'+esc(p.title)+'”'+(p.dosen?' ('+esc(p.dosen)+')':'')+' — topik '+esc(q.topik)+'.')+'</div>';
  h+='</div>';
  return h;
}
function confNote(ok,c){
  if(ok&&c==="y") return "Benar + yakin → pemahaman baik.";
  if(ok&&c==="c") return "Benar + cukup yakin → hampir kuat; ulangi sekali lagi nanti.";
  if(ok&&c==="g") return "Benar + menebak → konsep belum dikuasai. Soal ini masuk daftar remedial.";
  if(!ok&&c==="y") return "Salah + yakin → kemungkinan miskonsepsi. Baca analisis opsi dengan teliti.";
  if(!ok&&c==="c") return "Salah + cukup yakin → konsep masih rancu; bandingkan dengan opsi kunci.";
  return "Salah + menebak → materi perlu dipelajari ulang.";
}

/* ---------------- hasil sesi ---------------- */
let resFilter="all";
function results(){
  stopTimer(); renderNav("");
  const items=S.items, exam=S.mode==="exam";
  const Q=x=>QBY[x.id];
  const ans=items.filter(x=>x.ans!==null), ok=items.filter(x=>x.ans===Q(x).a), wrong=ans.filter(x=>x.ans!==Q(x).a);
  const denom=exam?items.length:Math.max(ans.length,1), pct=pc(ok.length,denom);
  const col=pct>=80?"var(--good)":pct>=60?"var(--warn)":"var(--bad)";
  const dur=S.durSec!=null?S.durSec:Math.round((Date.now()-S.t0)/1000);
  let h='<div class="page-h"><div><h1>'+(exam?"Hasil ujian":"Hasil sesi belajar")+'</h1><p>'+esc(S.title)+(S.timeout?" · waktu habis, dikirim otomatis":"")+(S.fromHist?" · dari riwayat":"")+'</p></div></div>';
  h+='<div class="panel"><div class="score"><div class="ring" style="background:conic-gradient('+col+' '+pct*3.6+'deg,var(--soft) 0)"><div style="width:84px;height:84px;border-radius:50%;background:var(--paper);display:grid;place-items:center">'+pct+'%</div></div>'+
     '<div><div class="row"><span class="pill">'+items.length+' soal</span><span class="pill baru">Benar '+ok.length+'</span><span class="pill" style="background:var(--bad-soft);color:var(--bad)">Salah '+wrong.length+'</span><span class="pill">Kosong '+(items.length-ans.length)+'</span><span class="pill">Durasi '+fmt(dur)+'</span></div>'+
     '<div class="small muted" style="margin-top:6px">'+(exam?"Skor = benar ÷ seluruh soal.":"Skor = benar ÷ soal yang dijawab.")+'</div></div></div>';
  // keyakinan sesi ini
  const cm=emptyCm(); let anyConf=false;
  ans.forEach(x=>{if(x.conf){anyConf=true;cm[x.conf][x.ans===Q(x).a?"ok":"no"]++;}});
  h+='<div class="row" style="margin-top:14px"><button class="btn pri" id="rvFirst">Tinjau semua pembahasan</button><button class="btn" id="rvWrong" '+(wrong.length||items.length-ans.length?"":"disabled")+'>Ulangi salah & kosong</button><button class="btn" id="rvRem">Remedial (salah + menebak)</button><a class="btn" href="#dashboard">Dashboard</a></div></div>';
  if(anyConf) h+='<div class="panel mt"><h2>Analisis keyakinan sesi ini</h2>'+cmTable(cm)+'</div>';
  // per PPT dan kesulitan
  const per=groupBy(items.map(Q),q=>q.ppt), perD=groupBy(items.map(Q),q=>q.d||0);
  const row=(label,list)=>{const n=list.length,c=list.filter(q=>{const x=items.find(i=>i.id===q.id);return x.ans===q.a;}).length,r=n?c/n:0;return '<div class="hbar"><span class="t" title="'+esc(label)+'">'+esc(label)+'</span><span class="bar"><i class="'+accCls(r)+'" style="width:'+pc(c,n)+'%"></i></span><span class="v '+accTxt(r)+'">'+c+'/'+n+'</span></div>';};
  h+='<div class="cols2"><div class="panel mt"><h2>Per topik (PPT)</h2>'+[...per.entries()].sort((a,b)=>PIDX[a[0]]-PIDX[b[0]]).map(([k,l])=>row(PBY[k].title,l)).join("")+'</div>'+
     '<div class="panel mt"><h2>Per tingkat kesulitan</h2>'+[1,2,3,0].filter(d=>perD.has(d)).map(d=>row(d?DIFF[d]:"Belum diklasifikasi",perD.get(d))).join("")+'</div></div>';
  // tinjauan
  const filt={all:"Semua",no:"Salah",blank:"Kosong",fl:"Ragu",g:"Menebak"};
  h+='<div class="panel mt"><h2>Tinjauan soal</h2><div class="tabs" id="rfTabs">'+Object.keys(filt).map(k=>'<button data-rf="'+k+'" class="'+(resFilter===k?"on":"")+'">'+filt[k]+'</button>').join("")+'</div><div id="rfList"></div></div>';
  $("app").innerHTML=h;
  const list=()=>{
    const sel=items.map((x,i)=>({x,i})).filter(({x})=>{const q=Q(x);
      if(resFilter==="no") return x.ans!==null&&x.ans!==q.a; if(resFilter==="blank") return x.ans===null;
      if(resFilter==="fl") return x.fl; if(resFilter==="g") return x.conf==="g"; return true;});
    $("rfList").innerHTML=sel.length?sel.map(({x,i})=>{const q=Q(x),st=x.ans===null?"":x.ans===q.a?"ok":"no";
      return '<details class="wrong-item" style="padding:0"><summary class="qrow" style="margin:0;border:none;cursor:pointer;list-style:none"><span class="st '+st+'"></span><span class="tx"><b>'+(i+1)+'.</b> '+esc(strip(q.s).slice(0,180))+(strip(q.s).length>180?"…":"")+'<div class="m">'+esc(PBY[q.ppt].title)+' · '+esc(q.topik)+(x.conf?' · <span class="confpill '+x.conf+'">'+CONF[x.conf]+'</span>':'')+'</div></span></summary><div style="padding:0 14px 14px"><div class="stem">'+q.s+'</div>'+figure(q)+explain(q,x)+'</div></details>';}).join(""):'<div class="empty">Tidak ada soal di filter ini.</div>';
  };
  list();
  $("rfTabs").onclick=e=>{const b=e.target.closest("[data-rf]");if(!b)return;resFilter=b.getAttribute("data-rf");document.querySelectorAll("#rfTabs button").forEach(x=>x.classList.toggle("on",x===b));list();};
  $("app").onclick=null;
  $("rvFirst").onclick=()=>{S.cur=0;S.review=true;reviewMode();};
  $("rvWrong").onclick=()=>startSession("learn",items.filter(x=>x.ans!==Q(x).a).map(Q),"Ulangi soal salah & kosong",{shuf:ST.set.shuf});
  $("rvRem").onclick=()=>{const l=items.filter(x=>x.ans!==Q(x).a||x.conf==="g").map(Q);startSession("learn",l,"Remedial sesi ini",{shuf:ST.set.shuf});};
  window.scrollTo(0,0);
}
/* tinjauan satu per satu setelah selesai (kunci terbuka) */
function reviewMode(){
  const it=S.items[S.cur], q=QBY[it.id];
  renderNav("");
  let h='<div class="qbar"><span class="pill brand">Tinjauan</span><b>'+esc(S.title)+'</b><div class="sp"></div><button class="btn sm" id="backRes">← Kembali ke hasil</button></div>';
  h+='<div class="layout"><div><div class="qcard"><div class="row" style="justify-content:space-between"><div class="qnum">Soal '+(S.cur+1)+' dari '+S.items.length+'</div><button class="btn sm bmk'+(ST.bm[q.id]?" on":"")+'" id="bmB">'+(ST.bm[q.id]?"★ Tersimpan":"☆ Bookmark")+'</button></div>'+
     '<div class="metarow">'+metaPills(q)+'</div><div class="stem">'+q.s+'</div>'+figure(q)+'<div class="opts">'+
     it.ord.map((oi,k)=>'<div class="opt locked'+(oi===q.a?" ok":oi===it.ans?" no":"")+'"><span class="L">'+LET[k]+'</span><span class="T">'+q.o[oi][0]+'</span></div>').join("")+'</div>'+explain(q,it)+
     '<div class="qnav"><button class="btn" id="prevB" '+(S.cur===0?"disabled":"")+'>← Sebelumnya</button><div class="sp"></div><button class="btn pri" id="nextB" '+(S.cur===S.items.length-1?"disabled":"")+'>Berikutnya →</button></div></div></div>'+
     '<aside class="side" style="display:block"><div class="panel" style="padding:14px"><div class="map">'+S.items.map((x,i)=>{const c=x.ans===null?"":x.ans===QBY[x.id].a?"ok":"no";return '<button class="'+c+(i===S.cur?" cur":"")+(x.fl?" fl":"")+'" data-go="'+i+'">'+(i+1)+'</button>';}).join("")+'</div></div></aside></div>';
  $("app").innerHTML=h;
  $("backRes").onclick=()=>results();
  $("prevB").onclick=()=>{S.cur--;reviewMode();window.scrollTo(0,0);};
  $("nextB").onclick=()=>{S.cur++;reviewMode();window.scrollTo(0,0);};
  $("bmB").onclick=()=>{toggleBm(q.id);reviewMode();};
  $("app").onclick=e=>{const g=e.target.closest("[data-go]");if(g){S.cur=+g.getAttribute("data-go");reviewMode();}};
}

/* ---------------- tabel keyakinan ---------------- */
function cmTable(cm){
  const cell=(k,okk)=>{const v=cm[k][okk],t=cm[k].ok+cm[k].no;const cls=okk==="ok"?(k==="y"?"c-good":k==="c"?"c-warn":"c-warn"):(k==="y"?"c-bad":"c-warn");return '<div class="'+cls+'"><b>'+v+'</b>'+pc(v,t)+'%</div>';};
  return '<div class="cmx"><div class="h"></div>'+Object.keys(CONF).map(k=>'<div class="h" style="text-align:center">'+CONF[k]+'</div>').join("")+
    '<div class="h">Benar</div>'+cell("y","ok")+cell("c","ok")+cell("g","ok")+
    '<div class="h">Salah</div>'+cell("y","no")+cell("c","no")+cell("g","no")+'</div>'+
    '<ul class="small muted" style="margin:10px 0 0;padding-left:18px"><li><b>Benar + yakin</b>: pemahaman baik.</li><li><b>Benar + menebak</b>: belum menguasai — ikut remedial.</li><li><b>Salah + yakin</b>: kemungkinan miskonsepsi — prioritas ditinjau.</li><li><b>Salah + menebak</b>: materi perlu dipelajari ulang.</li></ul>';
}

/* ---------------- penyaring soal (dipakai CBT, belajar, bank) ---------------- */
function scopeList(sc){
  // sc: {mode, bag[], ppt[], sub[] (ppt||topik), diff[], src}
  let L=QS.slice();
  if(sc.mode==="bag") L=L.filter(q=>sc.bag.includes(PBY[q.ppt].bagian));
  if(sc.mode==="ppt") L=L.filter(q=>sc.ppt.includes(q.ppt));
  if(sc.mode==="sub") L=L.filter(q=>sc.sub.includes(q.ppt+"||"+q.topik));
  if(sc.mode==="diff") L=L.filter(q=>sc.diff.includes(String(q.d||0)));
  if(sc.mode==="wrong") L=L.filter(isWrong);
  if(sc.mode==="rem") L=L.filter(q=>isWrong(q)||isWeakOk(q));
  if(sc.mode==="bm") L=L.filter(q=>ST.bm[q.id]);
  if(sc.mode==="flag") L=L.filter(q=>ST.flags[q.id]);
  if(sc.mode==="new") L=L.filter(q=>!stat(q.id));
  if(sc.tag&&sc.tag!=="all") L=L.filter(q=>(q.tag||"")===sc.tag);
  return L;
}
const SCOPES={
  all:["Seluruh materi","Semua soal Blok 3.2"],
  bag:["Mata kuliah","Patologi Klinik, Gizi, PA, …"],
  ppt:["Topik (PPT)","Pilih judul PPT dosen"],
  sub:["Subtopik","Subtopik di dalam PPT"],
  diff:["Tingkat kesulitan","Mudah / sedang / sulit"],
  wrong:["Soal yang pernah salah","Jawaban terakhir salah"],
  rem:["Remedial","Salah + benar tapi menebak"],
  new:["Belum dikerjakan","Soal yang belum pernah dijawab"],
  bm:["Bookmark","Soal yang kamu simpan"],
  flag:["Ditandai ragu","Soal bertanda ragu"]
};
function scopeUI(kind){
  const sc=ST.setup[kind]=Object.assign({mode:"all",bag:[],ppt:[],sub:[],diff:[],tag:"all",subP:PPTS[0].id,n:kind==="ujian"?"50":"20",ord:"rnd"},ST.setup[kind]||{});
  const modes=kind==="ujian"?["all","bag","ppt","sub","diff","wrong","rem"]:["all","bag","ppt","sub","diff","new","wrong","rem","bm","flag"];
  const cnt=m=>scopeList({mode:m,bag:BAGS,ppt:PPTS.map(p=>p.id),sub:[],diff:["1","2","3","0"]}).length;
  let h='<div class="field"><label>'+(kind==="ujian"?"Ujian berdasarkan":"Sumber soal")+'</label><div class="modes">'+modes.map(m=>{const c=["all","bag","ppt","sub","diff"].includes(m)?null:cnt(m);return '<button class="mode'+(sc.mode===m?" on":"")+'" data-mode="'+m+'" '+(c===0?"disabled":"")+'><b>'+SCOPES[m][0]+(c!=null?' ('+c+')':'')+'</b><span>'+SCOPES[m][1]+'</span></button>';}).join("")+'</div></div>';
  h+='<div id="scopeSub"></div>';
  h+='<div class="setgrid"><div class="field"><label for="scTag">Jenis soal</label><select id="scTag">'+[["all","Semua jenis"],["asli","Soal asli recall UAM"],["","Bank reguler"],["baru","Soal baru"],["prediksi","Prediksi"],["slide","Contoh soal slide dosen"]].map(([v,l])=>'<option value="'+v+'"'+(sc.tag===v?" selected":"")+'>'+l+'</option>').join("")+'</select></div>'+
     '<div class="field"><label for="scN">Jumlah soal</label><select id="scN">'+["10","20","30","50","100","all"].map(v=>'<option value="'+v+'"'+(sc.n===v?" selected":"")+'>'+(v==="all"?"Semua yang cocok":v)+'</option>').join("")+'</select></div>';
  if(kind==="ujian") h+='<div class="field"><label for="scT">Waktu per soal</label><select id="scT">'+[[0,"Tanpa batas waktu"],[60,"60 detik"],[72,"72 detik (±1,2 mnt)"],[90,"90 detik"],[120,"2 menit"]].map(([v,l])=>'<option value="'+v+'"'+(+ST.set.tpq===v?" selected":"")+'>'+l+'</option>').join("")+'</select></div>';
  else h+='<div class="field"><label for="scO">Urutan</label><select id="scO"><option value="rnd"'+(sc.ord==="rnd"?" selected":"")+'>Acak</option><option value="seq"'+(sc.ord==="seq"?" selected":"")+'>Urut per PPT & subtopik</option></select></div>';
  h+='</div>';
  h+='<div class="go-bar"><span class="n" id="scCount"></span><div class="sp"></div><button class="btn pri" id="scGo">'+(kind==="ujian"?"Mulai ujian":"Mulai belajar")+'</button></div>';
  return h;
}
function scopeSubUI(kind){
  const sc=ST.setup[kind];
  const chip=(attr,val,label,on,c)=>'<span class="chip'+(on?" on":"")+'" data-'+attr+'="'+esc(val)+'">'+esc(label)+(c!=null?'<small>'+c+'</small>':'')+'</span>';
  if(sc.mode==="bag") return '<div class="field"><label>Mata kuliah</label><div class="chips">'+BAGS.map(b=>chip("bag",b,b,sc.bag.includes(b),QS.filter(q=>PBY[q.ppt].bagian===b).length)).join("")+'</div></div>';
  if(sc.mode==="ppt") return '<div class="field"><label>Topik (PPT) <button class="btn sm ghost" data-all="ppt">Semua</button><button class="btn sm ghost" data-none="ppt">Kosongkan</button></label><div class="chips tall">'+PPTS.map(p=>chip("ppt",p.id,p.title,sc.ppt.includes(p.id),QS.filter(q=>q.ppt===p.id).length)).join("")+'</div></div>';
  if(sc.mode==="sub"){
    const subs=[...groupBy(QS.filter(q=>q.ppt===sc.subP),q=>q.topik).entries()];
    return '<div class="setgrid"><div class="field"><label for="subP">PPT</label><select id="subP">'+PPTS.map(p=>'<option value="'+p.id+'"'+(sc.subP===p.id?" selected":"")+'>'+esc(p.title)+'</option>').join("")+'</select></div></div>'+
      '<div class="field"><label>Subtopik (bisa pilih lebih dari satu, lintas PPT)</label><div class="chips tall">'+subs.map(([t,l])=>chip("sub",sc.subP+"||"+t,t,sc.sub.includes(sc.subP+"||"+t),l.length)).join("")+'</div>'+(sc.sub.length?'<div class="small muted" style="margin-top:4px">'+sc.sub.length+' subtopik terpilih</div>':'')+'</div>';
  }
  if(sc.mode==="diff"){
    const c=d=>QS.filter(q=>String(q.d||0)===d).length;
    return '<div class="field"><label>Tingkat kesulitan</label><div class="chips">'+[["1","Mudah"],["2","Sedang"],["3","Sulit"]].concat(c("0")?[["0","Belum diklasifikasi"]]:[]).map(([v,l])=>chip("diff",v,l,sc.diff.includes(v),c(v))).join("")+'</div></div>';
  }
  return "";
}
function bindScope(kind){
  const sc=ST.setup[kind];
  const pick=()=>{
    let L=scopeList(sc);
    return L;
  };
  const refresh=()=>{
    $("scopeSub").innerHTML=scopeSubUI(kind);
    const L=pick(), n=sc.n==="all"?L.length:Math.min(+sc.n,L.length);
    let t=L.length?n+' soal'+(n<L.length?' dari '+L.length+' yang cocok':''):'Tidak ada soal yang cocok';
    if(kind==="ujian"&&+ST.set.tpq&&n) t+=' · waktu '+fmt(n*ST.set.tpq);
    $("scCount").textContent=t; $("scGo").disabled=!n; save();
    const sp=$("subP"); if(sp) sp.onchange=()=>{sc.subP=sp.value;refresh();};
  };
  $("app").onclick=e=>{
    const m=e.target.closest("[data-mode]"); if(m&&!m.disabled){sc.mode=m.getAttribute("data-mode");document.querySelectorAll("[data-mode]").forEach(b=>b.classList.toggle("on",b===m));refresh();return;}
    for(const k of ["bag","ppt","sub","diff"]){const c=e.target.closest("[data-"+k+"]");if(c){const v=c.getAttribute("data-"+k),a=sc[k],i=a.indexOf(v);if(i>=0)a.splice(i,1);else a.push(v);refresh();return;}}
    const al=e.target.closest("[data-all]"); if(al){sc.ppt=PPTS.map(p=>p.id);refresh();return;}
    const no=e.target.closest("[data-none]"); if(no){sc.ppt=[];refresh();return;}
  };
  $("scTag").onchange=e=>{sc.tag=e.target.value;refresh();};
  $("scN").onchange=e=>{sc.n=e.target.value;refresh();};
  if($("scT")) $("scT").onchange=e=>{ST.set.tpq=+e.target.value;refresh();};
  if($("scO")) $("scO").onchange=e=>{sc.ord=e.target.value;refresh();};
  $("scGo").onclick=()=>{
    let L=pick(); if(!L.length) return;
    const seq=kind!=="ujian"&&sc.ord==="seq";
    L=shuffle(L.slice()); if(sc.n!=="all") L=L.slice(0,+sc.n);
    if(seq) L.sort((a,b)=>PIDX[a.ppt]-PIDX[b.ppt]||a.id-b.id); else if(kind==="ujian") shuffle(L);
    const desc=scopeDesc(sc);
    if(kind==="ujian") startSession("exam",L,"Ujian · "+desc,{limit:(+ST.set.tpq||0)*L.length,shuf:true,src:"ujian"});
    else startSession("learn",L,"Belajar · "+desc,{shuf:ST.set.shuf,src:"belajar"});
  };
  refresh();
}
function scopeDesc(sc){
  const lim=(a,f)=>a.length>2?a.length+" pilihan":a.map(f).join(", ");
  switch(sc.mode){
    case "bag": return lim(sc.bag,x=>x)||"mata kuliah";
    case "ppt": return lim(sc.ppt,x=>PBY[x].title)||"topik";
    case "sub": return lim(sc.sub,x=>x.split("||")[1])||"subtopik";
    case "diff": return "kesulitan "+sc.diff.map(d=>d==="0"?"belum diklasifikasi":DIFF[d].toLowerCase()).join("/");
    default: return SCOPES[sc.mode][0].toLowerCase();
  }
}

/* ---------------- halaman ---------------- */
function pageDashboard(){
  const done=QS.filter(q=>stat(q.id)), okN=done.filter(q=>stat(q.id).last===1).length;
  const attempts=Object.values(ST.stats).reduce((a,s)=>a+(s.n||0),0);
  const exams=ST.hist.filter(h=>h.mode==="exam"), avg=exams.length?Math.round(exams.reduce((a,h)=>a+h.pct,0)/exams.length):null;
  const wr=QS.filter(isWrong), weakOk=QS.filter(isWeakOk);
  let h='<div class="page-h"><div><h1>Dashboard</h1><p>'+QS.length+' soal · '+PPTS.length+' PPT · '+BAGS.length+' mata kuliah</p></div></div>';
  if(ST.active) h+='<div class="banner'+(ST.active.mode==="exam"?" warn":"")+'"><div style="flex:1;min-width:200px"><b>'+(ST.active.mode==="exam"?"Ujian belum selesai":"Lanjutkan sesi belajar")+'</b><div class="small muted">'+esc(ST.active.title)+' · '+ST.active.items.filter(x=>x.ans!==null).length+'/'+ST.active.items.length+' dijawab'+(ST.active.mode==="exam"&&ST.active.limit?' · sisa waktu '+fmt(ST.active.limit-(Date.now()-ST.active.t0)/1000):'')+'</div></div><button class="btn pri" id="resB">Lanjutkan</button><button class="btn ghost sm" id="resX">Buang</button></div>';
  if(ST.migrated) h+='<div class="banner"><div style="flex:1">Progres dari versi lama (statistik per soal, tanda ragu, riwayat skor) sudah dipindahkan otomatis.</div><button class="btn sm" id="migX">Oke</button></div>';
  h+='<div class="kpis">'+
    kpi(done.length+'<small class="muted" style="font-size:13px"> / '+QS.length+'</small>',"Soal sudah dikerjakan")+
    kpi(okN,"Benar (jawaban terakhir)")+kpi(done.length-okN,"Salah (jawaban terakhir)")+
    kpi(done.length?pc(okN,done.length)+"%":"–","Akurasi")+kpi(avg!=null?avg+"%":"–","Rata-rata skor ujian ("+exams.length+")")+kpi(attempts,"Total percobaan menjawab")+'</div>';
  h+='<div class="cols2"><div class="panel mt"><h2>Mulai</h2><div class="rec"><span class="ico">⏱</span><div class="b"><b>Simulasi CBT</b><div class="small muted">Timer, peta soal, tanpa kunci sampai dikirim.</div></div><a class="btn pri sm" href="#ujian">Mode CBT</a></div>'+
     '<div class="rec"><span class="ico">✎</span><div class="b"><b>Mode belajar</b><div class="small muted">Langsung dinilai + pembahasan lengkap.</div></div><a class="btn sm" href="#belajar">Belajar</a></div>'+
     '<div class="rec"><span class="ico">↻</span><div class="b"><b>Remedial otomatis</b><div class="small muted">'+wr.length+' salah + '+weakOk.length+' benar-tapi-menebak.</div></div><button class="btn sm" id="remB" '+(wr.length+weakOk.length?"":"disabled")+'>Mulai</button></div></div>'+
     '<div class="panel mt"><h2>Rekomendasi belajar</h2>'+recommendations()+'</div></div>';
  h+='<div class="panel mt"><h2>Perkembangan skor ujian</h2>'+histChart(exams)+'</div>';
  const cmT=Object.values(ST.cm).reduce((a,v)=>a+v.ok+v.no,0);
  h+='<div class="cols2"><div class="panel mt"><h2>Analisis keyakinan</h2>'+(cmT?cmTable(ST.cm):'<div class="empty">Belum ada data. Pilih tingkat keyakinan saat menjawab di mode belajar/CBT.</div>')+'</div>'+
     '<div class="panel mt"><h2>Materi masih lemah</h2>'+weakList(6)+'<div style="margin-top:8px"><a href="#analisis" class="small">Lihat analisis lengkap →</a></div></div></div>';
  $("app").innerHTML=h;
  if($("resB")){$("resB").onclick=resumeActive;$("resX").onclick=()=>ask("Buang sesi ini?",ST.active.mode==="exam"?"Ujian yang belum dikirim tidak akan dinilai.":"Jawaban yang sudah dinilai tetap tercatat di statistik.",()=>{ST.active=null;save();route();},"Buang");}
  if($("migX")) $("migX").onclick=()=>{delete ST.migrated;save();route();};
  $("remB").onclick=()=>startRemedial();
  bindRecs();
}
const kpi=(v,l)=>'<div class="kpi"><b>'+v+'</b><span>'+l+'</span></div>';
function startRemedial(){
  // prioritas: salah+yakin (miskonsepsi), salah lain, benar+menebak
  const pri=q=>{const s=stat(q.id);if(s.last===0&&s.lc==="y")return 0;if(s.last===0)return 1;return 2;};
  const L=QS.filter(q=>isWrong(q)||isWeakOk(q)).sort((a,b)=>pri(a)-pri(b)||PIDX[a.ppt]-PIDX[b.ppt]);
  startSession("learn",L.slice(0,40),"Remedial otomatis",{shuf:ST.set.shuf,src:"remedial"});
}
function topicRows(){
  const m=groupBy(QS,q=>q.ppt+"||"+q.topik);
  return [...m.entries()].map(([k,l])=>{const a=agg(l);return {k,ppt:k.split("||")[0],topik:k.split("||")[1],...a};});
}
function weakList(n){
  const rows=topicRows().filter(r=>r.done>=3&&r.acc<0.6).sort((a,b)=>a.acc-b.acc).slice(0,n);
  if(!rows.length) return '<div class="empty">Belum ada subtopik lemah (butuh ≥3 soal dikerjakan per subtopik dengan akurasi &lt;60%).</div>';
  return rows.map(r=>'<div class="hbar"><span class="t" title="'+esc(r.topik)+'">'+esc(r.topik)+'<br><span class="small muted">'+esc(PBY[r.ppt].title)+'</span></span><span class="bar"><i class="'+accCls(r.acc)+'" style="width:'+Math.round(r.acc*100)+'%"></i></span><span class="v '+accTxt(r.acc)+'">'+Math.round(r.acc*100)+'%</span></div>').join("");
}
function recommendations(){
  const recs=[];
  const miscon=QS.filter(q=>{const s=stat(q.id);return s&&s.last===0&&s.lc==="y";});
  if(miscon.length) recs.push(["!","<b>"+miscon.length+" soal salah padahal yakin</b> — tanda miskonsepsi. Tinjau dulu.","rec-mis","Tinjau"]);
  const weak=topicRows().filter(r=>r.done>=3&&r.acc<0.6).sort((a,b)=>a.acc-b.acc)[0];
  if(weak) recs.push(["↓","Subtopik terlemah: <b>"+esc(weak.topik)+"</b> ("+Math.round(weak.acc*100)+"%, "+esc(PBY[weak.ppt].title)+").","rec-sub|"+weak.k,"Belajar"]);
  const pptCov=PPTS.map(p=>({p,a:agg(QS.filter(q=>q.ppt===p.id))})).filter(x=>x.a.n).sort((a,b)=>a.a.done/a.a.n-b.a.done/b.a.n)[0];
  if(pptCov&&pptCov.a.done<pptCov.a.n) recs.push(["○","Cakupan terendah: <b>"+esc(pptCov.p.title)+"</b> ("+pptCov.a.done+"/"+pptCov.a.n+" soal dikerjakan).","rec-ppt|"+pptCov.p.id,"Kerjakan"]);
  const g=QS.filter(isWeakOk);
  if(g.length) recs.push(["?","<b>"+g.length+" soal benar tapi menebak</b> — perkuat konsepnya.","rec-guess","Ulangi"]);
  const lastExam=ST.hist.filter(h=>h.mode==="exam").slice(-1)[0];
  if(!lastExam) recs.push(["⏱","Belum pernah simulasi CBT. Coba 50 soal dengan timer.","rec-exam","Mulai"]);
  if(!recs.length) return '<div class="empty">Kerjakan beberapa soal dulu untuk mendapat rekomendasi.</div>';
  return recs.map(r=>'<div class="rec"><span class="ico">'+r[0]+'</span><div class="b">'+r[1]+'</div><button class="btn sm" data-rec="'+esc(r[2])+'">'+r[3]+'</button></div>').join("");
}
function bindRecs(){
  document.querySelectorAll("[data-rec]").forEach(b=>b.onclick=()=>{
    const [k,v]=b.getAttribute("data-rec").split(/\|(.+)/);
    if(k==="rec-mis") startSession("learn",QS.filter(q=>{const s=stat(q.id);return s&&s.last===0&&s.lc==="y";}),"Tinjau miskonsepsi",{shuf:ST.set.shuf});
    if(k==="rec-sub") startSession("learn",QS.filter(q=>q.ppt+"||"+q.topik===v),"Belajar · "+v.split("||")[1],{shuf:ST.set.shuf});
    if(k==="rec-ppt") startSession("learn",QS.filter(q=>q.ppt===v&&!stat(q.id)),"Belajar · "+PBY[v].title+" (belum dikerjakan)",{shuf:ST.set.shuf});
    if(k==="rec-guess") startSession("learn",QS.filter(isWeakOk),"Perkuat soal tebakan",{shuf:ST.set.shuf});
    if(k==="rec-exam"){ST.setup.ujian=Object.assign(ST.setup.ujian||{},{mode:"all",n:"50"});location.hash="ujian";}
  });
}
function histChart(exams){
  const pts=exams.slice(-20);
  if(pts.length<1) return '<div class="empty">Belum ada riwayat ujian. Grafik muncul setelah ujian pertama.</div>';
  const W=640,H=200,pl=34,pr=12,pt=12,pb=28, n=pts.length;
  const x=i=>pl+(n===1?(W-pl-pr)/2:i*(W-pl-pr)/(n-1)), y=v=>pt+(100-v)*(H-pt-pb)/100;
  let s='<svg class="histline" viewBox="0 0 '+W+' '+H+'" role="img" aria-label="Grafik skor ujian">';
  [0,50,60,80,100].forEach(v=>{s+='<line x1="'+pl+'" x2="'+(W-pr)+'" y1="'+y(v)+'" y2="'+y(v)+'" stroke="var(--line)" stroke-dasharray="'+(v===80||v===60?"4 4":"0")+'"/><text x="'+(pl-6)+'" y="'+(y(v)+4)+'" text-anchor="end">'+v+'</text>';});
  s+='<polyline fill="none" stroke="var(--brand)" stroke-width="2.5" points="'+pts.map((h,i)=>x(i)+","+y(h.pct)).join(" ")+'"/>';
  pts.forEach((h,i)=>{s+='<circle cx="'+x(i)+'" cy="'+y(h.pct)+'" r="4" fill="var(--paper)" stroke="var(--brand)" stroke-width="2"><title>'+esc(h.date+" · "+h.pct+"% · "+h.n+" soal")+'</title></circle>';
    if(n<=12||i===n-1) s+='<text x="'+x(i)+'" y="'+(H-8)+'" text-anchor="middle">'+esc(h.date.slice(5,10))+'</text>';});
  s+='<text x="'+x(n-1)+'" y="'+(y(pts[n-1].pct)-9)+'" text-anchor="middle" style="font-weight:700;fill:var(--ink)">'+pts[n-1].pct+'%</text></svg>';
  return s+'<div class="small muted">20 ujian terakhir. Garis putus-putus: 60% dan 80%.</div>';
}

function pageSetup(kind){
  const ujian=kind==="ujian";
  let h='<div class="page-h"><div><h1>'+(ujian?"Mode CBT":"Mode belajar")+'</h1><p>'+(ujian?"Simulasi ujian berbasis komputer: timer berjalan, kunci & pembahasan baru terbuka setelah ujian dikirim, jawaban terkirim otomatis saat waktu habis.":"Setiap jawaban langsung dinilai lalu dibahas lengkap: konsep, kata kunci, analisis, alasan tiap opsi, clinical pearls, dan referensi.")+'</p></div></div>';
  h+='<div class="panel">'+scopeUI(kind)+'</div>';
  if(!ujian){
    h+='<div class="sect-t"><h2>Belajar per PPT</h2><span class="muted small">Ketuk judul untuk melihat subtopik</span></div>';
    BAGS.forEach(b=>{
      h+='<div class="bagian-h">'+esc(b)+'</div><div class="grid">';
      PPTS.filter(p=>p.bagian===b).forEach(p=>{
        const L=QS.filter(q=>q.ppt===p.id), a=agg(L);
        h+='<div class="card"><h3>'+esc(p.title)+'</h3><div class="meta">'+esc(p.dosen||"")+(p.dosen?" · ":"")+L.length+' soal · '+a.done+' dikerjakan'+(a.done?' · akurasi '+Math.round(a.acc*100)+'%':'')+'</div><div class="bar"><i style="width:'+pc(a.done,a.n)+'%"></i></div>'+
           '<div class="row"><button class="btn sm pri" data-lp="'+p.id+'">Belajar</button><button class="btn sm" data-lpn="'+p.id+'" '+(a.done<a.n?"":"disabled")+'>Yang belum</button><button class="btn sm ghost" data-tp="'+p.id+'">Subtopik ▾</button></div>'+
           '<div class="topics" id="tp-'+p.id+'">'+[...groupBy(L,q=>q.topik).entries()].map(([t,l])=>{const x=agg(l);return '<div><a href="#" data-lt="'+esc(p.id+"||"+t)+'">'+esc(t)+'</a><span class="muted">'+x.done+'/'+x.n+(x.done?' · '+Math.round(x.acc*100)+'%':'')+'</span></div>';}).join("")+'</div></div>';
      });
      h+='</div>';
    });
  }
  $("app").innerHTML=h;
  bindScope(kind);
  if(!ujian){
    const base=$("app").onclick;
    $("app").onclick=e=>{
      const a=e.target.closest("[data-lp]"); if(a){const id=a.getAttribute("data-lp");startSession("learn",shuffle(QS.filter(q=>q.ppt===id)),"Belajar · "+PBY[id].title,{shuf:ST.set.shuf});return;}
      const b=e.target.closest("[data-lpn]"); if(b){const id=b.getAttribute("data-lpn");startSession("learn",shuffle(QS.filter(q=>q.ppt===id&&!stat(q.id))),"Belajar · "+PBY[id].title+" (belum dikerjakan)",{shuf:ST.set.shuf});return;}
      const t=e.target.closest("[data-tp]"); if(t){$("tp-"+t.getAttribute("data-tp")).classList.toggle("open");return;}
      const lt=e.target.closest("[data-lt]"); if(lt){e.preventDefault();const k=lt.getAttribute("data-lt");startSession("learn",QS.filter(q=>q.ppt+"||"+q.topik===k),"Belajar · "+k.split("||")[1],{shuf:ST.set.shuf});return;}
      base(e);
    };
  }
}

/* bank soal */
const BF={q:"",ppt:"",d:"",ty:"",st:"",tag:"all",page:0,open:null};
function pageBank(){
  let h='<div class="page-h"><div><h1>Bank soal</h1><p>Telusuri, saring, dan buka pembahasan soal mana pun. Data soal ada di <code>data/bank.json</code> (lihat panduan pengelolaan bank soal).</p></div></div>';
  h+='<div class="panel"><div class="row"><input class="searchbox" id="bfQ" placeholder="Cari kata di soal/opsi/subtopik…" value="'+esc(BF.q)+'"></div><div class="setgrid" style="margin-top:6px">'+
    sel("bfP","Topik (PPT)",[["","Semua PPT"]].concat(PPTS.map(p=>[p.id,p.title])),BF.ppt)+
    sel("bfD","Kesulitan",[["","Semua"],["1","Mudah"],["2","Sedang"],["3","Sulit"],["0","Belum diklasifikasi"]],BF.d)+
    sel("bfY","Jenis kognitif",[["","Semua"]].concat(Object.entries(TYPE)).concat([["-","Belum diklasifikasi"]]),BF.ty)+
    sel("bfS","Status",[["","Semua"],["new","Belum dikerjakan"],["ok","Benar"],["no","Salah"],["g","Benar tapi menebak"],["bm","Bookmark"],["fl","Ragu"]],BF.st)+
    sel("bfT","Jenis soal",[["all","Semua"],["asli","Soal asli"],["","Bank reguler"],["baru","Soal baru"],["prediksi","Prediksi"],["slide","Contoh slide"]],BF.tag)+
    '</div></div><div id="bfOut" class="mt"></div>';
  $("app").innerHTML=h;
  const upd=()=>{
    const qq=BF.q.toLowerCase().trim();
    const L=QS.filter(q=>{
      if(BF.ppt&&q.ppt!==BF.ppt) return false;
      if(BF.d&&String(q.d||0)!==BF.d) return false;
      if(BF.ty&&(BF.ty==="-"?!!q.ty:q.ty!==BF.ty)) return false;
      if(BF.tag!=="all"&&(q.tag||"")!==BF.tag) return false;
      if(BF.st){const s=status(q); if(BF.st==="bm"){if(!ST.bm[q.id])return false;} else if(BF.st==="fl"){if(!ST.flags[q.id])return false;} else if(BF.st==="g"){if(!isWeakOk(q))return false;} else if(s!==BF.st) return false;}
      if(qq){const t=(strip(q.s)+" "+q.o.map(o=>strip(o[0])).join(" ")+" "+q.topik).toLowerCase(); if(!qq.split(/\s+/).every(w=>t.includes(w))) return false;}
      return true;});
    const per=25, pages=Math.max(1,Math.ceil(L.length/per)); BF.page=Math.min(BF.page,pages-1);
    let o='<div class="row" style="margin-bottom:8px"><b>'+L.length+' soal</b><div class="sp"></div><button class="btn sm pri" id="bfLearn" '+(L.length?"":"disabled")+'>Belajar dari hasil ini</button><button class="btn sm" id="bfExam" '+(L.length?"":"disabled")+'>Ujian dari hasil ini</button></div>';
    o+=L.slice(BF.page*per,BF.page*per+per).map(q=>{const s=stat(q.id),st=status(q);
      return '<div class="qrow"><span class="st '+st+'" title="'+(st==="new"?"Belum":st==="ok"?"Benar":"Salah")+'"></span><div class="tx"><b>#'+q.id+'</b> '+esc(strip(q.s).slice(0,200))+(strip(q.s).length>200?"…":"")+
        '<div class="m">'+esc(PBY[q.ppt].title)+' · '+esc(q.topik)+(q.d?' · '+DIFF[q.d]:'')+(q.ty?' · '+TYPE[q.ty]:'')+(q.tag&&TAGL[q.tag]?' · '+TAGL[q.tag]:'')+(s?' · dijawab '+s.n+'×':'')+'</div>'+
        (BF.open===q.id?'<div style="margin-top:10px"><div class="stem">'+q.s+'</div>'+figure(q)+explain(q,null)+'</div>':'')+
        '</div><div class="ac"><button class="btn sm" data-bo="'+q.id+'">'+(BF.open===q.id?"Tutup":"Kunci")+'</button><button class="btn sm" data-bl="'+q.id+'">Kerjakan</button><button class="btn sm bmk'+(ST.bm[q.id]?" on":"")+'" data-bb="'+q.id+'" title="Bookmark">'+(ST.bm[q.id]?"★":"☆")+'</button></div></div>';}).join("")||'<div class="empty">Tidak ada soal yang cocok.</div>';
    if(pages>1) o+='<div class="pager"><button class="btn sm" data-pg="-1" '+(BF.page?"":"disabled")+'>←</button><span class="small">Hal. '+(BF.page+1)+' / '+pages+'</span><button class="btn sm" data-pg="1" '+(BF.page<pages-1?"":"disabled")+'>→</button></div>';
    $("bfOut").innerHTML=o;
    $("bfLearn").onclick=()=>startSession("learn",L,"Belajar · hasil bank soal",{shuf:ST.set.shuf});
    $("bfExam").onclick=()=>startSession("exam",shuffle(L.slice()).slice(0,100),"Ujian · hasil bank soal",{limit:(+ST.set.tpq||0)*Math.min(L.length,100)});
  };
  let tmo=null;
  $("bfQ").oninput=e=>{clearTimeout(tmo);tmo=setTimeout(()=>{BF.q=e.target.value;BF.page=0;upd();},200);};
  [["bfP","ppt"],["bfD","d"],["bfY","ty"],["bfS","st"],["bfT","tag"]].forEach(([id,k])=>$(id).onchange=e=>{BF[k]=e.target.value;BF.page=0;upd();});
  $("app").onclick=e=>{
    const o=e.target.closest("[data-bo]"); if(o){const id=+o.getAttribute("data-bo");BF.open=BF.open===id?null:id;upd();return;}
    const l=e.target.closest("[data-bl]"); if(l){startSession("learn",[QBY[+l.getAttribute("data-bl")]],"Soal #"+l.getAttribute("data-bl"),{shuf:ST.set.shuf});return;}
    const b=e.target.closest("[data-bb]"); if(b){toggleBm(+b.getAttribute("data-bb"));upd();renderNav("bank");return;}
    const pg=e.target.closest("[data-pg]"); if(pg){BF.page+= +pg.getAttribute("data-pg");upd();window.scrollTo(0,0);}
  };
  upd();
}
const sel=(id,label,opts,cur)=>'<div class="field"><label for="'+id+'">'+label+'</label><select id="'+id+'">'+opts.map(([v,l])=>'<option value="'+esc(v)+'"'+(String(cur)===String(v)?" selected":"")+'>'+esc(l)+'</option>').join("")+'</select></div>';

/* wrong answer bank */
function pageWrong(){
  const W=QS.filter(isWrong), G=QS.filter(isWeakOk);
  let h='<div class="page-h"><div><h1>Soal salah (wrong answer bank)</h1><p>Otomatis berisi soal yang jawaban terakhirmu salah. Soal keluar dari daftar ini setelah kamu menjawabnya benar.</p></div></div>';
  h+='<div class="kpis">'+kpi(W.length,"Jawaban terakhir salah")+kpi(W.filter(q=>stat(q.id).lc==="y").length,"Salah padahal yakin")+kpi(G.length,"Benar tapi menebak")+kpi(QS.filter(q=>(stat(q.id)||{}).w>=2).length,"Salah ≥ 2 kali")+'</div>';
  h+='<div class="row mt"><button class="btn pri" id="wRem" '+(W.length+G.length?"":"disabled")+'>Remedial otomatis (maks. 40 soal)</button><button class="btn" id="wAll" '+(W.length?"":"disabled")+'>Ulangi semua soal salah</button><button class="btn" id="wG" '+(G.length?"":"disabled")+'>Ulangi soal tebakan</button></div>';
  if(!W.length&&!G.length){ $("app").innerHTML=h+'<div class="empty mt">Belum ada soal salah. Kerjakan soal di mode belajar atau CBT.</div>'; bindW(); return; }
  const grp=groupBy(W.concat(G.filter(q=>!W.includes(q))),q=>q.ppt);
  [...grp.entries()].sort((a,b)=>PIDX[a[0]]-PIDX[b[0]]).forEach(([pid,l])=>{
    h+='<div class="panel mt"><div class="row"><h2 style="flex:1">'+esc(PBY[pid].title)+' <span class="muted small">('+l.length+')</span></h2><button class="btn sm" data-wp="'+pid+'">Ulangi topik ini</button></div>';
    l.forEach(q=>{const s=stat(q.id);const your=s.la!=null&&q.o[s.la]?q.o[s.la][0]:null;
      h+='<details class="wrong-item"><summary class="qrow" style="margin:0;border:none;cursor:pointer;list-style:none"><span class="st '+(s.last?"ok":"no")+'"></span><span class="tx">'+esc(strip(q.s).slice(0,190))+(strip(q.s).length>190?"…":"")+
         '<div class="m">'+esc(q.topik)+' · salah '+s.w+'× dari '+s.n+(s.lc?' · terakhir <span class="confpill '+s.lc+'">'+CONF[s.lc]+'</span>':'')+(s.last?' · <b>benar tapi menebak</b>':'')+'</div>'+
         (your&&!s.last?'<div class="m">Jawabanmu: <span class="bad-t">'+strip(your)+'</span> · Kunci: <span class="good-t">'+strip(q.o[q.a][0])+'</span></div>':'')+'</span></summary>'+
         '<div style="padding:0 14px 14px"><div class="stem">'+q.s+'</div>'+figure(q)+explain(q,null)+'<button class="btn sm" data-wq="'+q.id+'">Ulangi soal ini</button></div></details>';});
    h+='</div>';
  });
  $("app").innerHTML=h; bindW();
}
function bindW(){
  const W=QS.filter(isWrong), G=QS.filter(isWeakOk);
  $("wRem").onclick=startRemedial;
  $("wAll").onclick=()=>startSession("learn",shuffle(W.slice()),"Ulangi semua soal salah",{shuf:ST.set.shuf});
  $("wG").onclick=()=>startSession("learn",shuffle(G.slice()),"Perkuat soal tebakan",{shuf:ST.set.shuf});
  $("app").onclick=e=>{
    const p=e.target.closest("[data-wp]"); if(p){const id=p.getAttribute("data-wp");startSession("learn",W.concat(G).filter(q=>q.ppt===id),"Ulangi salah · "+PBY[id].title,{shuf:ST.set.shuf});return;}
    const q=e.target.closest("[data-wq]"); if(q){startSession("learn",[QBY[+q.getAttribute("data-wq")]],"Ulangi soal",{shuf:ST.set.shuf});}
  };
}

/* bookmark */
function pageBookmark(){
  const L=Object.keys(ST.bm).map(Number).filter(id=>QBY[id]).sort((a,b)=>ST.bm[b]-ST.bm[a]).map(id=>QBY[id]);
  let h='<div class="page-h"><div><h1>Bookmark</h1><p>Soal yang kamu simpan untuk dipelajari ulang. Simpan dengan tombol ☆ di soal atau tombol <kbd>B</kbd>.</p></div></div>';
  h+='<div class="row"><button class="btn pri" id="bmL" '+(L.length?"":"disabled")+'>Belajar semua bookmark ('+L.length+')</button><button class="btn" id="bmE" '+(L.length?"":"disabled")+'>Ujian dari bookmark</button></div>';
  h+=L.length?'<div class="mt">'+L.map(q=>'<details class="wrong-item"><summary class="qrow" style="margin:0;border:none;cursor:pointer;list-style:none"><span class="st '+(status(q)==="new"?"":status(q))+'"></span><span class="tx">'+esc(strip(q.s).slice(0,190))+'<div class="m">'+esc(PBY[q.ppt].title)+' · '+esc(q.topik)+'</div></span></summary><div style="padding:0 14px 14px"><div class="stem">'+q.s+'</div>'+figure(q)+explain(q,null)+'<div class="row"><button class="btn sm" data-bq="'+q.id+'">Kerjakan</button><button class="btn sm" data-bx="'+q.id+'">Hapus bookmark</button></div></div></details>').join("")+'</div>':'<div class="empty mt">Belum ada bookmark.</div>';
  $("app").innerHTML=h;
  $("bmL").onclick=()=>startSession("learn",L,"Belajar · bookmark",{shuf:ST.set.shuf});
  $("bmE").onclick=()=>startSession("exam",shuffle(L.slice()),"Ujian · bookmark",{limit:(+ST.set.tpq||0)*L.length});
  $("app").onclick=e=>{
    const q=e.target.closest("[data-bq]"); if(q){startSession("learn",[QBY[+q.getAttribute("data-bq")]],"Soal bookmark",{shuf:ST.set.shuf});return;}
    const x=e.target.closest("[data-bx]"); if(x){toggleBm(+x.getAttribute("data-bx"));pageBookmark();renderNav("bookmark");}
  };
}

/* riwayat */
function pageHist(){
  const H=ST.hist.slice().reverse();
  let h='<div class="page-h"><div><h1>Riwayat ujian & sesi</h1><p>Disimpan di browser ini (60 sesi terakhir). Ketuk “Tinjau” untuk membuka kembali jawaban dan pembahasannya.</p></div></div>';
  if(!H.length){$("app").innerHTML=h+'<div class="empty">Belum ada riwayat.</div>';return;}
  h+='<div class="panel"><div class="tbl-wrap"><table class="rt"><tr><th>Tanggal</th><th>Sesi</th><th class="n">Soal</th><th class="n">Benar</th><th class="n">Skor</th><th class="n">Durasi</th><th></th></tr>'+
    H.map(x=>'<tr><td class="n" style="text-align:left">'+esc(x.date)+'</td><td><span class="pill '+(x.mode==="exam"?"brand":"")+'">'+(x.mode==="exam"?"CBT":"Belajar")+'</span> '+esc(x.title)+(x.timeout?' <span class="small bad-t">(waktu habis)</span>':'')+'</td><td class="n">'+x.n+'</td><td class="n">'+x.ok+'</td><td class="n"><b class="'+accTxt(x.pct/100)+'">'+x.pct+'%</b></td><td class="n">'+(x.dur!=null?fmt(x.dur):"–")+'</td><td class="n">'+(x.items?'<button class="btn sm" data-hv="'+x.id+'">Tinjau</button>':'')+' <button class="btn sm ghost" data-hd="'+x.id+'" title="Hapus">✕</button></td></tr>').join("")+'</table></div></div>';
  $("app").innerHTML=h;
  $("app").onclick=e=>{
    const v=e.target.closest("[data-hv]"); if(v){openHist(v.getAttribute("data-hv"));return;}
    const d=e.target.closest("[data-hd]"); if(d){const id=d.getAttribute("data-hd");ask("Hapus riwayat ini?","Statistik per soal tidak ikut terhapus.",()=>{ST.hist=ST.hist.filter(x=>x.id!==id);save();pageHist();renderNav("riwayat");},"Hapus");}
  };
}
function openHist(id){
  const x=ST.hist.find(h=>h.id===id); if(!x||!x.items) return;
  const items=x.items.filter(r=>QBY[r[0]]).map(r=>({id:r[0],ord:String(r[1]).split("").map(Number),ans:r[2],conf:r[3]||null,fl:!!r[4],struck:{}}));
  items.forEach(it=>{const q=QBY[it.id];if(it.ord.length!==q.o.length) it.ord=q.o.map((_,i)=>i);});
  S={mode:x.mode,title:x.title,items,cur:0,done:true,t0:Date.now()-(x.dur||0)*1000,durSec:x.dur||0,timeout:x.timeout,fromHist:true};
  location.hash="hasil"; results();
}

/* analisis */
function pageAnalysis(){
  let h='<div class="page-h"><div><h1>Analisis performa</h1><p>Akurasi dihitung dari jawaban terakhir tiap soal yang pernah dikerjakan.</p></div></div>';
  const bars=(rows,lbl)=>rows.map(r=>'<div class="hbar"><span class="t" title="'+esc(lbl(r))+'">'+lbl(r)+'</span><span class="bar"><i class="'+(r.done?accCls(r.acc):"")+'" style="width:'+(r.done?Math.round(r.acc*100):0)+'%"></i></span><span class="v '+(r.done?accTxt(r.acc):"")+'">'+(r.done?Math.round(r.acc*100)+'%':'–')+'<br><span class="small muted" style="font-weight:500">'+r.done+'/'+r.n+'</span></span></div>').join("");
  const byP=PPTS.map(p=>Object.assign({p},agg(QS.filter(q=>q.ppt===p.id)))).filter(r=>r.n);
  const byB=BAGS.map(b=>Object.assign({b},agg(QS.filter(q=>PBY[q.ppt].bagian===b))));
  const byD=[1,2,3,0].map(d=>Object.assign({d},agg(QS.filter(q=>(q.d||0)===d)))).filter(r=>r.n);
  const byT=Object.keys(TYPE).concat(["-"]).map(t=>Object.assign({t},agg(QS.filter(q=>(q.ty||"-")===t)))).filter(r=>r.n);
  h+='<div class="cols2"><div class="panel"><h2>Per mata kuliah</h2>'+bars(byB,r=>esc(r.b))+'</div><div class="panel"><h2>Per tingkat kesulitan</h2>'+bars(byD,r=>r.d?DIFF[r.d]:"Belum diklasifikasi")+'<h2 style="margin-top:14px">Per jenis kognitif</h2>'+bars(byT,r=>r.t==="-"?"Belum diklasifikasi":TYPE[r.t])+'</div></div>';
  h+='<div class="panel mt"><h2>Per topik (PPT)</h2>'+bars(byP,r=>esc(r.p.title))+'</div>';
  const rows=topicRows().filter(r=>r.done>=3);
  const strong=rows.filter(r=>r.acc>=0.8).sort((a,b)=>b.acc-a.acc||b.done-a.done);
  h+='<div class="cols2"><div class="panel mt"><h2>Sudah dikuasai <span class="small muted">(≥80%, ≥3 soal)</span></h2>'+(strong.length?bars(strong.slice(0,12),r=>esc(r.topik)+'<br><span class="small muted">'+esc(PBY[r.ppt].title)+'</span>'):'<div class="empty">Belum ada.</div>')+'</div>'+
     '<div class="panel mt"><h2>Masih lemah <span class="small muted">(&lt;60%)</span></h2>'+weakList(12)+'</div></div>';
  const often=QS.filter(q=>(stat(q.id)||{}).w>=2).sort((a,b)=>stat(b.id).w-stat(a.id).w).slice(0,15);
  h+='<div class="panel mt"><h2>Soal yang sering salah</h2>'+(often.length?often.map(q=>'<div class="qrow"><span class="st no"></span><div class="tx">'+esc(strip(q.s).slice(0,160))+'<div class="m">'+esc(PBY[q.ppt].title)+' · salah '+stat(q.id).w+'×</div></div><div class="ac"><button class="btn sm" data-aq="'+q.id+'">Ulangi</button></div></div>').join(""):'<div class="empty">Belum ada soal yang salah ≥ 2 kali.</div>')+'</div>';
  const cmT=Object.values(ST.cm).reduce((a,v)=>a+v.ok+v.no,0);
  h+='<div class="panel mt"><h2>Analisis keyakinan (semua jawaban)</h2>'+(cmT?cmTable(ST.cm):'<div class="empty">Belum ada data keyakinan.</div>')+'</div>';
  $("app").innerHTML=h;
  $("app").onclick=e=>{const q=e.target.closest("[data-aq]");if(q)startSession("learn",[QBY[+q.getAttribute("data-aq")]],"Ulangi soal",{shuf:ST.set.shuf});};
}

/* pengaturan */
function pageSettings(){
  let used=0; try{used=(localStorage.getItem(KEY)||"").length;}catch(e){}
  let h='<div class="page-h"><div><h1>Pengaturan</h1></div></div><div class="panel">'+
    '<label class="toggle"><input type="checkbox" id="sConf"'+(ST.set.conf?" checked":"")+'> Tanyakan tingkat keyakinan setelah memilih jawaban</label><div class="small muted" style="margin:2px 0 12px 26px">Di mode belajar, jawaban dinilai setelah kamu memilih Yakin / Cukup yakin / Menebak. Di CBT, keyakinan opsional.</div>'+
    '<label class="toggle"><input type="checkbox" id="sShuf"'+(ST.set.shuf?" checked":"")+'> Acak urutan opsi di mode belajar</label><div class="small muted" style="margin:2px 0 12px 26px">Mode CBT selalu mengacak urutan soal dan opsi.</div>'+
    '<div class="setgrid">'+sel("sTpq","Waktu per soal (default CBT)",[[0,"Tanpa batas"],[60,"60 detik"],[72,"72 detik"],[90,"90 detik"],[120,"2 menit"]],ST.set.tpq)+
    sel("sTheme","Tema",[["","Ikuti sistem"],["light","Terang"],["dark","Gelap"]],ST.set.theme||"")+'</div></div>';
  h+='<div class="panel mt"><h2>Data & penyimpanan</h2><p class="small">Semua progres (statistik soal, riwayat, bookmark, soal salah, keyakinan, sesi berjalan) disimpan di <b>localStorage</b> browser ini — sekitar '+Math.round(used/1024)+' KB terpakai'+(storageOk?"":" · <b class='bad-t'>penyimpanan terakhir gagal</b>")+'.</p>'+
    '<ul class="small muted" style="padding-left:18px"><li>Data tidak hilang saat refresh atau browser ditutup.</li><li>Data <b>hilang</b> bila cache/data situs dihapus, memakai mode penyamaran, atau ganti browser/perangkat — tidak ada sinkronisasi laptop ↔ HP.</li><li>Kuota localStorage ±5 MB per situs; detail riwayat lama dipangkas otomatis bila penuh.</li><li>Sinkronisasi lintas perangkat membutuhkan database + login (mis. Supabase/Firebase tier gratis). Bisa ditambahkan nanti tanpa mengubah bank soal.</li></ul>'+
    '<div class="row"><button class="btn" id="sRstH">Hapus riwayat</button><button class="btn" id="sRstB">Hapus bookmark</button><button class="btn" style="color:var(--bad);border-color:var(--bad)" id="sRstAll">Reset semua progres</button></div></div>';
  h+='<div class="panel mt"><h2>Tentang bank soal</h2><p class="small">'+QS.length+' soal, '+PPTS.length+' PPT. Tingkat kesulitan terisi di '+QS.filter(q=>q.d).length+' soal, jenis kognitif di '+QS.filter(q=>q.ty).length+' soal, pembahasan terstruktur (konsep/kata kunci/analisis) di '+QS.filter(q=>q.ks).length+' soal. Sumber utama: PPT dosen; materi tambahan ditandai pada catatan/referensi.</p></div>';
  $("app").innerHTML=h;
  $("sConf").onchange=e=>{ST.set.conf=e.target.checked;save();};
  $("sShuf").onchange=e=>{ST.set.shuf=e.target.checked;save();};
  $("sTpq").onchange=e=>{ST.set.tpq=+e.target.value;save();};
  $("sTheme").onchange=e=>{ST.set.theme=e.target.value||null;setTheme(ST.set.theme);save();};
  $("sRstH").onclick=()=>ask("Hapus semua riwayat?","Statistik per soal tetap ada.",()=>{ST.hist=[];save();route();},"Hapus");
  $("sRstB").onclick=()=>ask("Hapus semua bookmark?","",()=>{ST.bm={};save();route();},"Hapus");
  $("sRstAll").onclick=()=>ask("Reset semua progres?","Statistik, riwayat, bookmark, tanda ragu, data keyakinan, dan sesi berjalan akan dihapus permanen dari browser ini.",()=>{Object.assign(ST,{stats:{},flags:{},bm:{},hist:[],cm:emptyCm(),active:null});save();route();},"Reset");
}

/* ---------------- router ---------------- */
const PAGES={dashboard:pageDashboard,ujian:()=>pageSetup("ujian"),belajar:()=>pageSetup("belajar"),bank:pageBank,salah:pageWrong,bookmark:pageBookmark,riwayat:pageHist,analisis:pageAnalysis,setelan:pageSettings};
function route(){
  const h=(location.hash||"#dashboard").slice(1);
  if(h==="soal"){ if(S&&!S.done){render();return;} if(ST.active&&resumeActive()) return; location.hash="dashboard"; return; }
  if(h==="hasil"){ if(S&&S.done){results();return;} location.hash="dashboard"; return; }
  // keluar dari ujian aktif lewat navigasi: ujian tetap tersimpan & timer tetap berjalan
  stopTimer();
  if(S&&!S.done){ persist(); S=null; }
  if(S&&S.done) S=null;
  const pg=PAGES[h]?h:"dashboard";
  renderNav(pg); $("app").onclick=null; PAGES[pg](); window.scrollTo(0,0);
}
window.addEventListener("hashchange",route);

/* ---------------- keyboard ---------------- */
document.addEventListener("keydown",e=>{
  if($("lb").classList.contains("show")){ if(e.key==="Escape") $("lbX").click(); return; }
  if($("modal").classList.contains("show")){ if(e.key==="Escape") $("mNo").click(); if(e.key==="Enter") $("mYes").click(); return; }
  if(!S||S.done||location.hash!=="#soal") return;
  if(/INPUT|SELECT|TEXTAREA/.test(e.target.tagName)||e.metaKey||e.ctrlKey||e.altKey) return;
  const k=e.key.toUpperCase(), it=S.items[S.cur], idx=LET.indexOf(k);
  if(k.length===1&&idx>=0&&idx<it.ord.length){choose(it.ord[idx]);e.preventDefault();}
  else if(["1","2","3"].includes(e.key)){const c=Object.keys(CONF)[+e.key-1];if(S.mode==="exam"?it.ans!==null:it.pend!=null)setConf(c);}
  else if(e.key==="ArrowRight") go(1);
  else if(e.key==="ArrowLeft") go(-1);
  else if(k==="F") toggleFlag();
  else if(k==="B") toggleBm();
});

/* ---------------- mulai ---------------- */
if(ST.active&&ST.active.mode==="exam"&&(location.hash==="#soal"||!location.hash)) resumeActive();
else route();
})();
