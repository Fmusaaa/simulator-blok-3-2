import json,re,os,sys
D=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,D)
from lig import fix as ligfix
L='abcde'
TOPIK=[('Tiroid',r'benjolan di leher|berdebar|nodul di|tiroid|thyro|tsh|ft4|t3|t4|struma|goiter|graves|hashimoto|ptu|metimazol|levotiroks|iodida|billewicz|wayne'),
('Adrenal & kortikosteroid',r'adrenal|suprarenal|kortisol|cortisol|cushing|addison|aldosteron|kortiko|glukokortik|mineralokortik|prednison|deksametason|hidrokortison|zona|hirsut|deltakort|fluorokort'),
('Diabetes melitus',r'langerhans|sering kencing|banyak kencing|diabet|\bdm\b|insulin|glukosa|hba1c|a1c|metformin|sulfonil|glibenkl|glimepir|inkretin|incretin|dpp-4|glp-1|acarbose|alpha-gl|ketoasid|kad\b|ttgo|prediabet|c peptid|tolbutam|lispro|sglt|dapagli|glinid'),
('Dislipidemia & sindrom metabolik',r'lipid|kolesterol|ldl|hdl|trigliserid|statin|fibrat|sindrom metabolik|sindroma metabolik|obesitas|lingkar pinggang|lipoprotein|adipokin|friedewald|apolipo'),
('Gizi klinik',r'gizi|kkal|kalori|diet|mst|amd|protein berdasarkan|makan siang|purin|minyak|asupan|lemak tidak jenuh|fatty'),
('Onkologi & petanda tumor',r'tirosin kinase|tumor|kanker|neoplas|keganasan|ganas|metasta|cea|psa|ca 1|ca125|kemoterapi|onkogen|telomer|p53|apoptosis|monoklonal|vegf|pd-1|siklus untuk proses|checkpoint|diferensiasi|displasia|teratoma|seminoma|paliatif|palliative|stadium'),
('Gout & asam urat',r'asam urat|gout|tofus|purin'),('Imunologi & inflamasi',r'\bles\b|imun|autoimun|komplemen|opsonin|crp|sitokin|interleukin|ig ?e|imunoglobulin|alergi|anafila|histamin|basofil|sel mast|hipersensitiv|sle|lupus|sjogren|polimiositis|kemokin|neutrofil|monosit|kupffer|fase akut|hiv|eosinofil|leukosit'),
('Hemostasis & hemodinamika',r'hemofil|koagulasi|pembekuan|trombosit|trombin|protrombin|inr|warfarin|aptt|tromboplastin|clotting|bleeding|rumple|perdarahan|petechia|ekimosis|hematoma|trombus|emboli|endotel|fibrinolis|kongesti|edema|syok|hemodinamik|cardiac output|stroke volume|systol|diastol|jantung'),
('Asam basa & elektrolit',r'arteri radialis|allen|asidosis|alkalosis|buffer|ph |\bph\b|gas darah|agd|elektrolit|kalium|natrium|kalsium|hipernatrem'),
('Radiologi',r'foto|x foto|rontgen|radiograf|sinar x|grid|film|ct scan|mri|usg|posisi|opasitas|lesi litik|osteoblast|mediastin|ivp|waters|faktor eksposi|magnifikasi|radiasi'),
('Rehabilitasi medik',r'rehabilitasi|impairment|disabil|handicap|cacat|fisioterap|okupasi|terapis wicara|speech|status fungsional|mobilitas|sp\.?kfr|parallel bar|kursi roda'),
('K3 & kesehatan lingkungan',r'kerja|apd|earplug|bisinosis|weil|water|jamban|latrine|ventilasi|sick building|udara|blum|promotif|preventif|epidemiolog|penyuluhan|phbs|prevalensi|ptm|jumantik|rumah sehat|kecelakaan|bahaya|odf'),
('Genetika',r'sindroma xyy|klinefelter|turner|ehler|genetik')]
def topik(s):
    t=s.lower()
    for name,pat in TOPIK:
        if re.search(pat,t): return name
    return 'Lain-lain'
def clean(t):
    t=re.sub(r'\s*One app for all.*$','',t)
    t=re.sub(r'\s+',' ',t).strip()
    return t
SETS=[('art-uam','Articulatio · UAM 3.2','Articulatio','Soal UAM 3.2 angkatan Articulatio (kunci = stabilo di file angkatan)'),
      ('art-uas','Articulatio · UAS 3.2','Articulatio','Soal UAS 3.2 angkatan Articulatio (kunci = stabilo di file angkatan)'),
      ('cal-uam','Calcaneus · UAM 3.2','Calcaneus','Recall UAM 3.2 angkatan Calcaneus’22 (soal asli + rekonstruksi)'),
      ('cal-uas','Calcaneus · UAS 3.2','Calcaneus','Soal UAS 3.2 angkatan Calcaneus (kunci = cetak tebal di file angkatan)')]
qs=[];nid=[0]
def add(setid,no,tag,stem,opts,key,ref,expl,p,n,lbl):
    v=L.index(key); r=None
    if isinstance(ref,list): r=v if key in ref else (L.index(ref[0]) if ref else None)
    elif ref: r=L.index(ref)
    nid[0]+=1
    o=[[opts[i],expl[i] if i<len(expl) else '',''] for i in range(len(opts))]
    qs.append({'id':nid[0],'ppt':setid,'topik':topik(stem+' '+' '.join(opts)),'s':stem,'o':o,'a':v,'v':v,'r':r,'p':p,'k':'','t':'','n':n or '','tag':tag,'lbl':lbl,'no':str(no),'ord':int(re.match(r'\d+',str(no)).group()) if re.match(r'\d+',str(no)) else 0})
def load_pdfset(setid,qjson,kfile,lbl,lig=False):
    Q={str(x['n']):x for x in json.load(open(os.path.join(D,qjson)))}
    def A(no,key,expl,p='',n='',ref=None,fix=None,tag='asli'):
        fix=fix or {}
        src=Q.get(str(no))
        stem=fix.get('s') or (src['stem'] if src else '')
        opts=fix.get('opts') or [o['t'] for o in src['opts']]
        if lig: stem=ligfix(stem); opts=[ligfix(x) for x in opts]
        stem=clean(stem); opts=[clean(x) for x in opts]
        if 'o4' in fix: opts[3]=fix['o4']
        rr=ref if ref is not None else (src.get('ref') if src else None)
        add(setid,no,tag,stem,opts,key,rr,expl,p,n,lbl)
    exec(open(os.path.join(D,kfile)).read(),{'A':A})
# fix khusus AU
AUFIX={27:{'s':'Berapa kebutuhan energi berdasarkan AMD seorang pasien 50 tahun, BB 60, TB 160?','opts':['1.654 kkal','1.645 kkal','1.564 kkal','1.546 kkal','1.456 kkal']},28:{'opts':['Lipolisis','Lipogenesis','Glukoneogenesis','Glikolisis','Dekarboksilasi oksidatif']}}
def load_au():
    Q={x['n']:x for x in json.load(open(os.path.join(D,'AU.q.json')))}
    def A(no,key,expl,p='',n='',fix=None,ref=None,tag='asli'):
        f=AUFIX.get(no,{})
        add_from(Q,no,key,expl,p,n,f,'art-uam','SOAL ASLI · UAM Articulatio',ref)
    exec(open(os.path.join(D,'k_AU.py')).read(),{'A':A})
def add_from(Q,no,key,expl,p,n,f,setid,lbl,ref=None):
    src=Q[no]
    stem=clean(f.get('s',src['stem'])); opts=[clean(x) for x in f.get('opts',[o['t'] for o in src['opts']])]
    add(setid,no,'asli',stem,opts,key,ref if ref is not None else src.get('ref'),expl,p,n,lbl)
load_au()
load_pdfset('art-uas','AS.q.json','k_AS.py','SOAL ASLI · UAS Articulatio')
def load_cu():
    def Q(no,tag,stem,opts,key,ref,expl,p='',n=''):
        add('cal-uam',no,tag,stem,opts,key,ref or None,expl,p,n,'SOAL ASLI · recall UAM Calcaneus' if tag=='asli' else 'SOAL DIREKONSTRUKSI · recall UAM Calcaneus')
    exec(open(os.path.join(D,'k_CU.py')).read(),{'Q':Q})
load_cu()
load_pdfset('cal-uas','CS.q.json','k_CS.py','SOAL ASLI · UAS Calcaneus',lig=True)
for q in qs:
    if q['tag']=='rekon' and q['ppt']=='cal-uas': q['lbl']='SOAL DIREKONSTRUKSI · UAS Calcaneus'
ppts=[{'id':s[0],'title':s[1],'bagian':'Angkatan '+s[2],'dosen':s[3]} for s in SETS]
json.dump({'ppts':ppts,'qs':qs},open(os.path.join(D,'..','..','data','angkatan.json'),'w'),ensure_ascii=False,indent=0)
from collections import Counter
print(len(qs),Counter(q['ppt'] for q in qs),'koreksi',sum(1 for q in qs if q['r'] is not None and q['r']!=q['v']),'tanpa ref',sum(1 for q in qs if q['r'] is None))
print(Counter(q['topik'] for q in qs))
