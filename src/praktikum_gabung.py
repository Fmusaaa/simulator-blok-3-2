"""Gabungkan Praktikum Koagulasi ke halaman praktikum-neoplasma/ (satu simulator, dibedakan per praktikum).
Idempoten: soal koagulasi lama di halaman dibuang lalu diganti dari src/praktikum_koagulasi.py.
python3 src/praktikum_gabung.py"""
import json, re, sys
sys.path.insert(0, 'src')
from praktikum_koagulasi import Q as KQ, CATS as KCATS

PAGE = 'praktikum-neoplasma/index.html'
t = open(PAGE).read()

def grab(name):
    m = re.search(r'const %s=(.*?);\n' % name, t, re.S)
    return json.loads(m.group(1))
cats = grab('CATS'); qs = grab('QS')
qs = [q for q in qs if q.get('pk', 'neo') == 'neo']
for q in qs: q['pk'] = 'neo'
cats = {k: dict(v, pk=v.get('pk', 'neo')) for k, v in cats.items() if v.get('pk', 'neo') == 'neo'}
for k, v in KCATS.items(): cats['k_' + k] = dict(v, pk='koag')
for q in KQ:
    q = dict(q); q['c'] = 'k_' + q['c']; q['pk'] = 'koag'; q['num'] = 'K' + str(q['num']); qs.append(q)
assert len(qs) == 32 + len(KQ)

def rep(old, new):
    global t
    if new in t: return                           # sudah diterapkan
    assert t.count(old) == 1, old[:80]
    t = t.replace(old, new)

t = re.sub(r'const CATS=\{.*?\};\n', lambda m: 'const CATS=' + json.dumps(cats, ensure_ascii=False) + ';\n', t, count=1, flags=re.S)
t = re.sub(r'const QS=\[.*?\];\n', lambda m: 'const QS=' + json.dumps(qs, ensure_ascii=False) + ';\n', t, count=1, flags=re.S)

# ---- teks & header ----
rep('<title>Praktikum Neoplasma Modul 3.2</title>', '<title>Praktikum Modul 3.2 – Neoplasma & Koagulasi</title>')
rep('<div class="brand"><h1>Praktikum Neoplasma 3.2</h1><p id="sub">24 gambar, 32 soal</p></div>',
    '<div class="brand"><h1 id="brandH">Praktikum 3.2</h1><p id="sub">Neoplasma & Koagulasi</p></div>'
    '<div class="pkseg" role="group" aria-label="Pilih praktikum"><button data-pk="neo">Neoplasma</button><button data-pk="koag">Koagulasi</button></div>')
rep('placeholder="mis. griseofulvin, Th2, nekrosis"', 'placeholder="mis. displasia, Brecher, Lee and White"')
rep('''        <div>
          <h3>Sumber soal</h3>''', '''        <div>
          <h3>Praktikum</h3>
          <div class="chips" id="prakChips"></div>
        </div>
        <div>
          <h3>Sumber soal</h3>''')
rep('.timer{', '.pkseg{display:flex;border:1px solid var(--line);border-radius:9px;overflow:hidden;flex:none}'
    '.pkseg button{border:0;background:var(--card);padding:7px 11px;font-size:14px;font-weight:600;cursor:pointer;color:var(--muted)}'
    '.pkseg button[aria-pressed="true"]{background:var(--hema);color:var(--on-accent)}'
    '.pkbadge{display:inline-block;font-size:12px;font-weight:700;padding:1px 7px;border-radius:6px;margin-right:6px;background:var(--hema-soft);color:var(--hema)}'
    '.pkbadge.koag{background:var(--eosin-soft);color:var(--eosin)}'
    '@media (max-width:520px){.pkseg button{padding:6px 8px;font-size:13px}.brand p{display:none}}\n.timer{')

# ---- logika ----
rep('const setup={mode:\'latihan\',cats:new Set(Object.keys(CATS)),src:\'all\'};',
    'const PRAK={neo:{n:"Neoplasma",d:"Histopatologi neoplasma"},koag:{n:"Koagulasi",d:"Pemeriksaan koagulasi & POCT"},all:{n:"Gabungan",d:"Neoplasma + Koagulasi"}};\n'
    'const catsOf=pk=>Object.keys(CATS).filter(c=>pk==="all"||CATS[c].pk===pk);\n'
    'let PK=(/koag/i.test(location.hash)?"koag":/neo/i.test(location.hash)?"neo":ls.get("-pk","neo")); if(!PRAK[PK]) PK="neo";\n'
    'const setup={mode:\'latihan\',pk:PK,cats:new Set(catsOf(PK)),src:\'all\'};\n'
    'const idsOf=pk=>QS.map((q,i)=>i).filter(i=>pk==="all"||QS[i].pk===pk);\n'
    'function setPk(pk,start){ setup.pk=pk; setup.cats=new Set(catsOf(pk)); ls.set("-pk",pk); try{history.replaceState(null,"","#"+(pk==="koag"?"koagulasi":pk==="neo"?"neoplasma":"gabungan"))}catch(e){}\n'
    '  if(start){ if(S&&S.mode===\'ujian\'&&!S.submitted&&!confirm("Ujian sedang berjalan. Pindah praktikum dan tinggalkan ujian ini?")) return;\n'
    '    newSession(idsOf(pk),{mode:\'latihan\',shufQ:false,shufOpt:$("shufOpt").checked,secs:60}); }\n'
    '  renderSetup(); }\n'
    'const sessPk=()=>{const s=new Set(S.ids.map(i=>QS[i].pk));return s.size===1?[...s][0]:"all";};\n'
    'const pkBadge=pk=>`<span class="pkbadge ${pk}">${PRAK[pk].n}</span>`;')
rep('S={v:QS.length,mode:o.mode,', 'S={v:QS.length,pk:setup.pk,mode:o.mode,')
rep('<span class="cat"><span class="dot" style="background:${cat.c}"></span>${cat.n}</span>',
    '<span class="cat">${pkBadge(q.pk)}<span class="dot" style="background:${cat.c}"></span>${cat.n}</span>')
rep("HIST.unshift({d:Date.now(),m:S.mode,n,ok,", "HIST.unshift({d:Date.now(),pk:sessPk(),m:S.mode,n,ok,")
rep("<span>${t} · ${x.m==='ujian'?'Ujian':'Latihan'} · ${x.n} soal</span>",
    "<span>${t} · ${PRAK[x.pk||'neo'].n} · ${x.m==='ujian'?'Ujian':'Latihan'} · ${x.n} soal</span>")
rep("$(\"sub\").textContent=(S.mode==='ujian'?'Mode ujian':'Mode latihan')+`, ${n} soal`;",
    "{const sp=sessPk(); $(\"brandH\").textContent='Praktikum '+(sp==='all'?'3.2':PRAK[sp].n);"
    " document.querySelectorAll('.pkseg button').forEach(b=>b.setAttribute('aria-pressed',b.dataset.pk===sp));"
    " $(\"sub\").textContent=(S.mode==='ujian'?'Mode ujian':'Mode latihan')+`, ${n} soal`;}")
# penguasaan keseluruhan: hanya praktikum yang sedang dipilih
rep("const m={}; let done=0; QS.forEach((q,i)=>{m[q.c]=",
    "const m={}; let done=0, tot=0; const mp=sessPk(); QS.forEach((q,i)=>{if(mp!=='all'&&q.pk!==mp) return; tot++; m[q.c]=")
rep("$(\"masteryTxt\").textContent=`${done} dari ${QS.length} soal pernah dikerjakan.",
    "$(\"masteryTxt\").textContent=`${PRAK[mp].n}: ${done} dari ${tot} soal pernah dikerjakan.")
# setup
rep("const q=QS[i]; if(!setup.cats.has(q.c)) return false;",
    "const q=QS[i]; if(setup.pk!=='all'&&q.pk!==setup.pk) return false; if(!setup.cats.has(q.c)) return false;")
rep("const weak=QS.filter((q,i)=>ST[i]&&ST[i].l===0).length, fresh=QS.filter((q,i)=>!ST[i]).length, noted=QS.filter(q=>NOTES[q.num]).length;\n  const SRC=[['all','Semua soal',QS.length],",
    "const inPk=q=>setup.pk==='all'||q.pk===setup.pk, PQ=QS.filter(inPk);\n"
    "  const weak=QS.filter((q,i)=>inPk(q)&&ST[i]&&ST[i].l===0).length, fresh=QS.filter((q,i)=>inPk(q)&&!ST[i]).length, noted=PQ.filter(q=>NOTES[q.num]).length;\n"
    "  $(\"prakChips\").innerHTML=['neo','koag','all'].map(p=>`<button class=\"chip\" data-p=\"${p}\" aria-pressed=\"${setup.pk===p}\">${PRAK[p].n} <span class=\"n\">${idsOf(p).length}</span></button>`).join(\"\");\n"
    "  $(\"prakChips\").querySelectorAll(\".chip\").forEach(b=>b.onclick=()=>setPk(b.dataset.p,false));\n"
    "  const SRC=[['all','Semua soal',PQ.length],")
rep("$(\"catChips\").innerHTML=Object.keys(CATS).map(c=>",
    "$(\"catChips\").innerHTML=catsOf(setup.pk).map(c=>")
rep("${CATS[c].n} <span class=\"n\">${n}</span></button>`}).join(\"\");",
    "${setup.pk==='all'?PRAK[CATS[c].pk].n+' · ':''}${CATS[c].n} <span class=\"n\">${n}</span></button>`}).join(\"\");")
rep("$(\"shufOpt\").checked=DEF_SHUFOPT;\nrenderSetup();",
    "$(\"shufOpt\").checked=DEF_SHUFOPT;\n"
    "document.querySelectorAll('.pkseg button').forEach(b=>b.onclick=()=>setPk(b.dataset.pk,true));\n"
    "renderSetup();")
rep("if(S&&S.v===QS.length&&Array.isArray(S.ids)&&S.ids.length){ S.enter=Date.now(); render(); }\nelse newSession(QS.map((q,i)=>i),",
    "const hashPk=/koag|neo|gabung/i.test(location.hash);\n"
    "if(S&&S.v===QS.length&&Array.isArray(S.ids)&&S.ids.length&&!(hashPk&&(S.pk||'neo')!==setup.pk)){ S.enter=Date.now(); render(); }\n"
    "else newSession(idsOf(setup.pk),")

open(PAGE, 'w').write(t)
redirect = '''<!DOCTYPE html><html lang="id"><head><meta charset="utf-8"><title>Praktikum Koagulasi Modul 3.2</title>
<meta http-equiv="refresh" content="0; url=../praktikum-neoplasma/index.html#koagulasi">
<script>location.replace("../praktikum-neoplasma/index.html#koagulasi")</script></head>
<body><p>Praktikum Koagulasi sudah digabung ke <a href="../praktikum-neoplasma/index.html#koagulasi">simulator praktikum</a>.</p></body></html>
'''
open('praktikum-koagulasi/index.html', 'w').write(redirect)
print('soal:', len(qs), '| neo', sum(q['pk'] == 'neo' for q in qs), '| koag', sum(q['pk'] == 'koag' for q in qs))
