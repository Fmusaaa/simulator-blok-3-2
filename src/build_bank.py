import json,re,random,collections,html
d=json.load(open('src/old_banks.json'))

PPTS=[ # id, judul asli PPT, bagian, dosen
 ("el","Pemeriksaan Elektrolit 2025","Patologi Klinik","dr. Meta Safitri, Sp.PK"),
 ("agd","Pemeriksaan Analisis Gas Darah 2025","Patologi Klinik","dr. Meta Safitri, Sp.PK"),
 ("tm","Pemeriksaan Tumor Marker 2026","Patologi Klinik","dr. Meta Safitri, Sp.PK"),
 ("tir","Pemeriksaan Tiroid 2026","Patologi Klinik","dr. Meta Safitri, Sp.PK"),
 ("koag","Asistensi Praktikum Pemeriksaan Koagulasi","Patologi Klinik","dr. Meta Safitri, Sp.PK"),
 ("ldm","Aspek Laboratorium Diabetes Melitus 2026","Patologi Klinik","dr. Meta Safitri, Sp.PK"),
 ("rinf","Respon Imun Non Infeksi 2026","Patologi Klinik","dr. Meta Safitri, Sp.PK"),
 ("gdm","Tatalaksana Gizi pada DM","Ilmu Gizi",""),
 ("gdl","Aspek Dietik pada Dislipidemi","Ilmu Gizi",""),
 ("gkv","Aspek Dietik pada Penyakit Kardiovaskuler dan Keganasan","Ilmu Gizi",""),
 ("imun","Imunopatologi (Modul 3.2)","Patologi Anatomi","dr. Djamila Zakaria, Sp.PA"),
 ("hemo","Gangguan Hemodinamik","Patologi Anatomi","dr. Djamila Zakaria, Sp.PA"),
 ("ftr","Drugs for Thyroid Disease and Renal Failure","Farmakologi","dr. Ahmad Muhyi"),
 ("ster","Steroid","Farmakologi","dr. Putri Azalia"),
 ("ado","Antidiabetes Oral 2026","Farmakologi","dr. Putri Azalia"),
 ("ktp","Kelainan Tiroid dan Paratiroid","Penyakit Dalam","dr. Diana Novitasari, Sp.PD-KEMD"),
 ("sm","Sindroma Metabolik","Penyakit Dalam","dr. Diana Novitasari, Sp.PD-KEMD"),
 ("cush","Cushing Syndrome","Penyakit Dalam","dr. Diana Novitasari, Sp.PD-KEMD"),
 ("add","Addison's Disease","Penyakit Dalam","dr. Diana Novitasari, Sp.PD-KEMD"),
 ("kfr","Ilmu Kedokteran Fisik dan Rehabilitasi","Rehabilitasi Medik","dr. R. D. Lestari, Sp.KFR"),
 ("lain","Recall UAM 3.2 – topik di luar 20 PPT","Recall UAM 3.2","Neoplasma, onkologi, radiologi, K3, lipid & hemostasis PK"),
]
PID=[p[0] for p in PPTS]
Q=[]
def add(ppt,topik,q,tag="",src=""):
    assert ppt in PID,ppt
    Q.append(dict(ppt=ppt,topik=topik,s=q['s'],o=[list(x) for x in q['o']],a=q['a'],p=q.get('p',''),k=q.get('k',''),t=q.get('t',''),n=q.get('n',''),tag=tag,src=src))

def catname(f,c): return d[f]['cats'].get(c,{}).get('n',c)

simple={ # file: {cat: (ppt, topik or None=use cat name)}
 'elektrolit-agd-teks':{'el':('el',None),'agd':('agd',None)},
 'tumor-marker':{'konsep':('tm',None),'spesifik':('tm',None),'lab':('tm',None)},
 'tiroid-koagulasi':{'tiroid':('tir',None),'koag':('koag',None)},
 'gizi-klinik':{'dm':('gdm','Bank soal materi'),'dl':('gdl','Bank soal materi'),'kv':('gkv','Bank soal materi')},
 'model-uam-3-2-gizi':{'dm':('gdm','Soal kasus model UAM'),'dl':('gdl','Soal kasus model UAM'),'kv':('gkv','Soal kasus model UAM')},
 'imunopatologi':{c:('imun',None) for c in ['dasar','hiper','sle','imunodef']},
 'obat-tiroid-ginjal':{c:('ftr',None) for c in ['dasar','hipo','hiper','para','ginjal']},
 'steroid-antidiabetes':{'steroid':('ster','Kortikosteroid'),'ado':('ado','Antidiabetes oral'),'insulin':('ado','Insulin')},
 'kelainan-tiroid-paratiroid':{c:('ktp',None) for c in ['tt','hipo','para']},
 'sindroma-metabolik-cushing-addison':{'sm':('sm','Sindroma metabolik, obesitas & hipertensi'),'lip':('sm','Dislipidemia'),'cush':('cush','Sindrom Cushing'),'add':('add','Penyakit Addison')},
}
for f,m in simple.items():
    for q in d[f]['qs']:
        ppt,top=m[q['c']]
        add(ppt,top or catname(f,q['c']),q,src=f)

# Recall UAM 3.2 (SOAL ASLI) - pemetaan per nomor ke PPT
uam={1:'ldm',2:'sm',3:'sm',4:'sm',5:'ldm',6:'ldm',7:'ldm',8:'ktp',9:'ftr',10:'cush',11:'ldm',
 12:'gdm',13:'gdm',14:'gdm',15:'gdm',16:'gdm',17:'gdm',18:'gkv',19:'gkv',20:'sm',21:'sm',22:'lain',23:'lain',
 24:'lain',25:'hemo',26:'hemo',27:'hemo',28:'agd',29:'agd',30:'agd',31:'agd',38:'tm',39:'tm',40:'tm',
 47:'imun',48:'imun',49:'hemo',50:'hemo',51:'hemo',52:'hemo',53:'hemo',54:'ado',55:'ado',56:'ado',57:'ado',58:'ado'}
for q in d['uam-3-2']['qs']:
    ppt=uam.get(q['num'],'lain')
    add(ppt,'Recall UAM 3.2' if ppt!='lain' else catname('uam-3-2',q['c']),q,tag='asli',src='uam-3-2')
model={1:'ldm',2:'ldm',3:'ldm',4:'ktp',5:'cush',6:'ado',7:'ado',8:'ado',16:'tm',17:'tm',18:'hemo',19:'hemo',20:'hemo',21:'hemo',24:'agd',26:'ldm',27:'gdm',28:'gdm'}
for q in d['model-soal-uam-3-2']['qs']:
    ppt=model.get(q['num'],'lain')
    add(ppt,'Prediksi model UAM' if ppt!='lain' else catname('model-soal-uam-3-2',q['c']),q,tag='prediksi',src='model-soal-uam-3-2')

# Soal baru
N=[]
exec(open('src/new1.py').read()); exec(open('src/new2.py').read())
for x in N:
    add(x['c'],x['sub'],dict(s=x['s'],o=x['o'],a=0,p=x['p'],k=x['k'],t=x['t'],n=x['n']),tag='baru',src='baru')


# dedupe by normalized stem
def norm(s): return re.sub(r'\W+','',re.sub('<[^>]+>','',s).lower())[:160]
seen={};out=[];dup=0
for q in Q:
    k=norm(q['s'])+norm(q['o'][q['a']][0])
    if k in seen: dup+=1; continue
    seen[k]=1; out.append(q)
for i,q in enumerate(out,1): q['id']=i
# validasi
for q in out:
    assert len(q['o'])>=2 and 0<=q['a']<len(q['o']), q['id']
    for o in q['o']: assert len(o)==3 and all(isinstance(x,str) and x.strip() for x in o), (q['id'],o)
cnt=collections.Counter(q['ppt'] for q in out)
print('total',len(out),'dup',dup)
for p in PPTS: print(f"{p[0]:5} {cnt[p[0]]:4}  {p[1]}")
print(collections.Counter(q['tag'] for q in out))
json.dump(dict(ppts=[dict(id=a,title=b,bagian=c,dosen=e) for a,b,c,e in PPTS],qs=out),open('data/bank.json','w'),ensure_ascii=False)
