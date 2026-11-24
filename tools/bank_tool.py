#!/usr/bin/env python3
"""Alat pengelolaan bank soal Simulator Blok 3.2.

  python3 tools/bank_tool.py validate            # cek skema + anti-clue, cetak laporan
  python3 tools/bank_tool.py validate --ppt tir  # hanya satu PPT
  python3 tools/bank_tool.py apply content/tir.txt [...]   # terapkan file revisi ke data/bank.json
  python3 tools/bank_tool.py dump tir            # cetak soal satu PPT (format revisi) untuk diedit

Format file revisi (content/<ppt>.txt), satu blok per soal:

  #123 d=2 ty=application
  ks: konsep yang diuji (1–2 kalimat)
  kw: kata kunci 1; kata kunci 2; kata kunci 3
  an: analisis kasus / cara berpikir menuju jawaban
  A: teks opsi || fakta tentang opsi || alasan benar/salah
  B*: teks opsi kunci || fakta || alasan
  C: = || fakta || alasan          ("=" berarti teks opsi lama dipertahankan)
  ...
  p: clinical pearl (opsional, mengganti pearl lama)
  n+: catatan tambahan slide vs referensi (opsional, ditambahkan)
  ref: referensi (opsional; default otomatis dari PPT + slide)

Aturan:
  * d = 1 mudah, 2 sedang, 3 sulit
  * ty = recall | understanding | application | analysis | integrated
  * Soal ber-tag asli/rekon/slide: teks stem & opsi TIDAK boleh diubah (pakai "=").
"""
import json, re, sys, os, statistics, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANK = os.path.join(ROOT, 'data', 'bank.json')
LOCKED = {'asli', 'rekon', 'slide'}
TYPES = {'recall', 'understanding', 'application', 'analysis', 'integrated'}
ABSOLUTE = re.compile(r'\b(selalu|tidak pernah|pasti|semua|satu-satunya|always|never|only)\b', re.I)
strip = lambda s: re.sub(r'\s+', ' ', re.sub(r'<[a-zA-Z/][^>]*>', ' ', s or '')).strip()


def load():
    return json.load(open(BANK))


def save(b):
    with open(BANK, 'w') as f:
        json.dump(b, f, ensure_ascii=False)


def clue(q):
    """Kembalikan (correct_is_longest, rasio panjang kunci / rata-rata distraktor)."""
    ls = [len(strip(o[0])) for o in q['o']]
    a = q['a']
    others = [l for i, l in enumerate(ls) if i != a] or [1]
    return ls[a] == max(ls) and ls.count(max(ls)) == 1, ls[a] / max(1, statistics.mean(others))


def validate(b, ppt=None, verbose=True):
    qs = [q for q in b['qs'] if not ppt or q['ppt'] == ppt]
    ids = collections.Counter(q['id'] for q in b['qs'])
    errs, warns = [], []
    longest = 0; ratios = []; meta = collections.Counter(); stand = []
    for q in qs:
        tag = q.get('tag') or ''
        if ids[q['id']] > 1: errs.append((q['id'], 'id ganda'))
        if q['ppt'] not in {p['id'] for p in b['ppts']}: errs.append((q['id'], 'ppt tidak dikenal'))
        if not (0 <= q['a'] < len(q['o'])): errs.append((q['id'], 'kunci di luar opsi'))
        if len(q['o']) != 5 and tag not in LOCKED: warns.append((q['id'], f"{len(q['o'])} opsi (standar 5)"))
        texts = [strip(o[0]).lower() for o in q['o']]
        if len(set(texts)) != len(texts): errs.append((q['id'], 'opsi kembar'))
        for i, o in enumerate(q['o']):
            if len(o) < 3: errs.append((q['id'], f'opsi {i} tanpa pembahasan')); continue
            if len(strip(o[1]) + strip(o[2])) < 25: warns.append((q['id'], f'pembahasan opsi {"ABCDE"[i]} terlalu pendek'))
        for k in ('d', 'ty', 'ks', 'kw', 'an'):
            if q.get(k): meta[k] += 1
        if q.get('ty') and q['ty'] not in TYPES: errs.append((q['id'], 'ty tidak valid'))
        if q.get('d') and q['d'] not in (1, 2, 3): errs.append((q['id'], 'd tidak valid'))
        if tag in LOCKED: continue
        isl, r = clue(q); ratios.append(r); longest += isl
        ls = sorted(len(strip(o[0])) for o in q['o'])
        if isl and len(ls) > 1 and len(strip(q['o'][q['a']][0])) >= 1.2 * ls[-2] and len(strip(q['o'][q['a']][0])) - ls[-2] >= 8:
            stand.append(q['id'])
        if r >= 1.5: warns.append((q['id'], f'kunci {r:.1f}× lebih panjang dari distraktor'))
        ab = [bool(ABSOLUTE.search(t)) for t in texts]
        if any(ab) and not ab[q['a']] and sum(ab) == len(ab) - 1:
            warns.append((q['id'], 'semua distraktor memakai kata absolut, kunci tidak'))
    n = len([q for q in qs if (q.get('tag') or '') not in LOCKED])
    rep = {
        'soal': len(qs), 'dinilai_anti_clue': n,
        'kunci_terpanjang_%': round(100 * longest / n, 1) if n else 0,
        'kunci_menonjol_%': round(100 * len(stand) / n, 1) if n else 0,
        'rasio_panjang_rata2': round(statistics.mean(ratios), 2) if ratios else 0,
        'metadata': {k: f'{meta[k]}/{len(qs)}' for k in ('d', 'ty', 'ks', 'kw', 'an')},
        'error': len(errs), 'peringatan': len(warns),
        'posisi_kunci': dict(collections.Counter('ABCDE'[q['a']] for q in qs if q['a'] < 5)),
    }
    rep['kunci_menonjol_id'] = stand[:40]
    if verbose:
        print(json.dumps(rep, ensure_ascii=False, indent=1))
        for e in errs[:50]: print('ERROR', *e)
        w = collections.Counter(x[1].split(' ')[0] for x in warns)
        print('ringkasan peringatan:', dict(w.most_common(8)))
    return rep, errs, warns


BLOCK = re.compile(r'^#(\d+)(.*)$')


def parse(path):
    out = []; cur = None
    for raw in open(path, encoding='utf-8'):
        line = raw.rstrip('\n')
        if not line.strip() or line.startswith('//'): continue
        m = BLOCK.match(line)
        if m:
            cur = {'id': int(m.group(1)), 'opts': []}
            for kv in m.group(2).split():
                k, _, v = kv.partition('=')
                cur[k] = v
            out.append(cur); continue
        if cur is None: raise SystemExit(f'{path}: baris di luar blok: {line[:60]}')
        m = re.match(r'^([A-E])(\*?):\s*(.*)$', line)
        if m:
            parts = [x.strip() for x in m.group(3).split('||')]
            if len(parts) != 3: raise SystemExit(f'{path} #{cur["id"]} opsi {m.group(1)} harus 3 bagian: {line[:80]}')
            cur['opts'].append((m.group(1), m.group(2) == '*', parts)); continue
        m = re.match(r'^(ks|kw|an|p|n\+|ref|s):\s*(.*)$', line)
        if m: cur[m.group(1)] = m.group(2).strip(); continue
        # baris lanjutan untuk field terakhir
        raise SystemExit(f'{path} #{cur["id"]}: baris tidak dikenali: {line[:80]}')
    return out


def apply(b, blocks, src):
    by = {q['id']: q for q in b['qs']}
    n = 0
    for bl in blocks:
        q = by.get(bl['id'])
        if not q: raise SystemExit(f'{src}: soal #{bl["id"]} tidak ada')
        locked = (q.get('tag') or '') in LOCKED
        if bl['opts']:
            letters = [o[0] for o in bl['opts']]
            if letters != list('ABCDE'[:len(letters)]): raise SystemExit(f'#{q["id"]}: urutan opsi harus A,B,C,…')
            if locked and len(bl['opts']) != len(q['o']): raise SystemExit(f'#{q["id"]}: soal {q["tag"]} tidak boleh tambah/kurangi opsi')
            keys = [i for i, o in enumerate(bl['opts']) if o[1]]
            if len(keys) != 1: raise SystemExit(f'#{q["id"]}: harus tepat satu kunci (*)')
            if locked and keys[0] != q['a']: raise SystemExit(f'#{q["id"]}: kunci soal {q["tag"]} tidak boleh berubah')
            new = []
            for i, (L, isk, (t, fakta, alasan)) in enumerate(bl['opts']):
                if t == '=':
                    if i >= len(q['o']): raise SystemExit(f'#{q["id"]}: opsi {L} "=" tapi opsi lama tidak ada')
                    t = q['o'][i][0]
                elif locked and strip(t) != strip(q['o'][i][0]):
                    raise SystemExit(f'#{q["id"]}: teks opsi soal {q["tag"]} tidak boleh diubah (pakai "=")')
                new.append([t, fakta, alasan])
            if not locked and keys[0] != q['a']:
                # kunci boleh dipindah posisinya hanya jika teks kuncinya sama
                pass
            q['o'] = new; q['a'] = keys[0]
        if 'd' in bl: q['d'] = int(bl['d'])
        if 'ty' in bl: q['ty'] = bl['ty']
        for k in ('ks', 'an', 'ref'):
            if bl.get(k): q[k] = bl[k]
        if bl.get('kw'): q['kw'] = [x.strip() for x in bl['kw'].split(';') if x.strip()]
        if bl.get('p'): q['p'] = bl['p']
        if bl.get('s'):
            if locked: raise SystemExit(f'#{q["id"]}: stem soal {q["tag"]} tidak boleh diubah')
            q['s'] = bl['s']
        if bl.get('n+'): q['n'] = (q.get('n') + ' ' if q.get('n') else '') + bl['n+']
        q['rev'] = 2
        n += 1
    return n


def dump(b, ppt):
    for q in b['qs']:
        if q['ppt'] != ppt: continue
        isl, r = clue(q)
        print(f"#{q['id']} tag={q.get('tag') or '-'} topik={q['topik']!r} clue={'Y' if isl else '-'}{r:.1f}")
        print('S:', strip(q['s']))
        for i, o in enumerate(q['o']):
            print(f"{'ABCDE'[i]}{'*' if i == q['a'] else ''}: {strip(o[0])} || {strip(o[1])} || {strip(o[2])}")
        for k in ('p', 'k', 't', 'n'):
            if q.get(k): print(f'{k}: {strip(q[k])}')
        print()


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit()
    b = load()
    if a[0] == 'validate':
        ppt = a[a.index('--ppt') + 1] if '--ppt' in a else None
        rep, errs, warns = validate(b, ppt)
        if '--list' in a:
            for w in warns: print('WARN', *w)
        sys.exit(1 if errs else 0)
    if a[0] == 'apply':
        tot = 0
        for p in a[1:]:
            tot += apply(b, parse(p), p)
        rep, errs, _ = validate(b, verbose=False)
        if errs:
            for e in errs[:20]: print('ERROR', *e)
            raise SystemExit('tidak disimpan: ada error')
        save(b); print('diterapkan', tot, 'soal')
    if a[0] == 'dump':
        dump(b, a[1])
