#!/usr/bin/env python3
"""Ensambla los JSON de Buschbacher en un index.html autocontenido.
Valida que cada fila tenga el mismo número de celdas que columnas."""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
APP  = os.path.dirname(HERE)

def load(name, default_group):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        data = json.load(f)
    for st in data:
        st.setdefault("group", default_group)
    return data

studies = []
studies += load("motor.json",   "motor")
studies += load("sensory.json", "sensitivo")
studies += load("extras.json",  None)  # ya traen group
studies += load("especiales.json", "especial")  # cola larga: nervios poco frecuentes (Manual 2015)
studies += load("especiales2.json", "especial")  # 2.ª tanda de nervios poco frecuentes
studies += load("especiales3.json", "especial")  # 3.ª tanda: MII, craneales, raíces, pudendo

# --- validación de forma ---
problems = 0
for st in studies:
    for m in st["measures"]:
        ncol = len(m["columns"])
        for i, row in enumerate(m["rows"]):
            if len(row) != ncol:
                problems += 1
                print(f"  ⚠ {st['study_key']} / {m['name']} / fila {i}: "
                      f"{len(row)} celdas vs {ncol} columnas", file=sys.stderr)
if problems:
    print(f"VALIDACIÓN: {problems} desajustes de forma", file=sys.stderr)
else:
    print("VALIDACIÓN: todas las filas cuadran con sus columnas ✓")

# --- orden por grupo ---
order = {"motor": 0, "sensitivo": 1, "mixto": 2, "especial": 3}
seq   = {"mediano-motor":0,"cubital-motor":1,"peroneo-motor":2,"tibial-motor":3,
         "mediano-sensitivo":0,"cubital-sensitivo":1,"sural-sensitivo":2,
         "safeno-sensitivo":3,"sural-vs-safeno":4,
         "mediano-mixto":0,"cubital-mixto":1,"diferencia-mediano-cubital":2}
studies.sort(key=lambda s: (order.get(s["group"],9), seq.get(s["study_key"],9)))

n_meas = sum(len(s["measures"]) for s in studies)
print(f"  {len(studies)} estudios, {n_meas} tablas de medidas")

DATA = json.dumps(studies, ensure_ascii=False)

HTML = r"""<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>EDx adulto · Valores de referencia (Buschbacher)</title>
<style>
:root{--bg:#0e1726;--card:#16233a;--line:#2a3a59;--txt:#e8eef7;--muted:#9fb2cc;--accent:#3aa0ff;--warn:#ffb74d;--mot:#3aa0ff;--sen:#5ec5a0;--mix:#c79bff}
*{box-sizing:border-box}body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;background:var(--bg);color:var(--txt);line-height:1.45;padding:0 0 60px}
header{background:linear-gradient(180deg,#0b3d5c,#0e2842);padding:16px 16px 13px;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:5}
header h1{margin:0;font-size:18px}header p{margin:4px 0 0;font-size:11.5px;color:var(--muted)}
.wrap{padding:14px;max-width:920px;margin:0 auto}
#q{width:100%;padding:10px 12px;font-size:14px;background:var(--card);border:1px solid var(--line);border-radius:10px;color:var(--txt);margin:12px 0 4px}
#q::placeholder{color:var(--muted)}
.grp{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:22px 0 8px;font-weight:700}
details.study{background:var(--card);border:1px solid var(--line);border-radius:12px;margin-bottom:10px;padding:0 13px;border-left:3px solid var(--line)}
details.g-motor{border-left-color:var(--mot)}details.g-sensitivo{border-left-color:var(--sen)}details.g-mixto{border-left-color:var(--mix)}
summary{padding:13px 0;font-weight:700;font-size:13.5px;cursor:pointer;list-style:none}
summary::-webkit-details-marker{display:none}summary::after{content:"＋";float:right;color:var(--muted)}
details[open]>summary::after{content:"－"}
.tech{font-size:11.5px;color:var(--muted);font-style:italic;border-bottom:1px solid var(--line);padding:0 0 10px;margin-bottom:6px}
dl.mont{display:grid;grid-template-columns:auto 1fr;gap:3px 12px;margin:10px 0 8px;padding-bottom:8px;border-bottom:1px solid var(--line);font-size:11.5px}
dl.mont dt{color:var(--accent);font-weight:600;white-space:nowrap}
dl.mont dd{margin:0;color:var(--txt)}
.ref{font-size:10.5px;color:var(--muted);margin:2px 0 10px}
.meas{margin:12px 0}
.meas h3{font-size:12.5px;color:var(--accent);margin:0 0 6px}
.tw{overflow-x:auto;-webkit-overflow-scrolling:touch;padding-bottom:10px}
table{width:100%;border-collapse:collapse;font-size:12px;min-width:320px}
th,td{padding:6px 7px;text-align:center;border-bottom:1px solid var(--line);white-space:nowrap}
th{color:var(--muted);font-size:10px;text-transform:uppercase;font-weight:700;position:sticky;top:0}
td:first-child,th:first-child{text-align:left;font-weight:600}
tbody tr:hover{background:#1d2d49}
.cut{display:inline-block;font-size:10px;color:var(--muted);margin-left:6px}
.note{font-size:11px;color:var(--warn);margin-top:6px}
footer{max-width:920px;margin:26px auto 0;padding:0 16px}
details.crit{background:#1d2d49;border:1px solid var(--line);border-radius:12px;padding:0 13px}
details.crit summary{color:var(--warn)}
details.crit .body{padding:0 0 13px;font-size:11.5px;color:var(--muted)}
details.crit .body li{margin-bottom:6px}
.hidden{display:none}
.empty{color:var(--muted);font-size:12px;padding:14px 0;font-style:italic}
</style></head><body>
<header>
<h1>Electrodiagnóstico del adulto</h1>
<p>Valores de referencia de neuroconducción · Buschbacher 1999/2003 y Manual 2015 · percentiles por edad, sexo y talla</p>
</header>
<div class="wrap">
<input id="q" type="search" placeholder="Buscar nervio o parámetro (p. ej. peroneo, latencia, sural)…" autocomplete="off">
<div id="app"></div>
<footer>
<details class="crit"><summary>⚠️ Nota metodológica y de uso</summary>
<div class="body"><ul>
<li><b>Fuente.</b> Buschbacher RM, <i>Update on Nerve Conduction Studies</i> (Am J Phys Med Rehabil 1999;78(6 Supl)) y el estudio sural/safeno (2003). Es una de las mayores bases normativas en adultos.</li>
<li><b>Definición del rango normal.</b> Buschbacher recomienda usar los <b>percentiles observados</b> (p3/p5 como límite inferior de amplitud y velocidad; p95/p97 como límite superior de latencia y duración) en lugar de media±2&nbsp;DE, porque varias medidas no siguen una distribución normal.</li>
<li><b>Técnica dependiente.</b> Los valores dependen de la técnica (distancias, sitios de estímulo/registro, temperatura ≥32&nbsp;°C). Contrástelos con los valores de referencia del propio laboratorio.</li>
<li><b>Subgrupos.</b> Cuando una medida varía con la edad, el sexo o la talla, Buschbacher publica subgrupos separados; respételos.</li>
<li><b>Limitaciones de transcripción.</b> Las tablas se transcribieron de los artículos originales (la mayoría en formato imagen). La tabla de <i>duración</i> del cubital sensitivo no se pudo recuperar del PDF. Verifique cualquier valor crítico contra la fuente antes de tomar decisiones clínicas.</li>
</ul></div></details>
<p style="font-size:10.5px;color:var(--muted);margin-top:14px;font-style:italic">Material de apoyo a la interpretación. No sustituye el juicio del especialista ni los valores de referencia propios del laboratorio.</p>
</footer>
</div>
<script>
const STUDIES = __DATA__;
const GRP = {motor:"Estudios motores", sensitivo:"Estudios sensitivos", mixto:"Estudios de nervio mixto y diferencias", especial:"Nervios poco frecuentes (Manual de Buschbacher 2015)"};
const app = document.getElementById("app");

function table(m){
  let h = '<div class="meas" data-txt="'+ (m.name).toLowerCase() +'"><h3>'+m.name+'</h3><div class="tw"><table><thead><tr>';
  m.columns.forEach(c=> h += '<th>'+c+'</th>');
  h += '</tr></thead><tbody>';
  m.rows.forEach(r=>{ h+='<tr>'; r.forEach(c=> h+='<td>'+c+'</td>'); h+='</tr>'; });
  h += '</tbody></table></div></div>';
  return h;
}
function render(list){
  let html=""; let lastG=null;
  list.forEach(st=>{
    if(st.group!==lastG){ html += '<div class="grp">'+(GRP[st.group]||st.group)+'</div>'; lastG=st.group; }
    html += '<details class="study g-'+st.group+'" data-txt="'+(st.study_label+' '+st.measures.map(m=>m.name).join(' ')).toLowerCase()+'">';
    html += '<summary>'+st.study_label+'</summary>';
    if(st.montaje){ html += '<dl class="mont">'; for(const k in st.montaje){ html += '<dt>'+k+'</dt><dd>'+st.montaje[k]+'</dd>'; } html += '</dl>'; }
    if(st.technique_notes) html += '<div class="tech">'+st.technique_notes+'</div>';
    st.measures.forEach(m=> html += table(m));
    html += '<div class="ref">'+st.reference+'</div>';
    html += '</details>';
  });
  app.innerHTML = html || '<div class="empty">Sin resultados.</div>';
}
render(STUDIES);

const q = document.getElementById("q");
const norm = s => s.normalize("NFD").replace(/[\u0300-\u036f]/g,"").toLowerCase();
q.addEventListener("input", ()=>{
  const t = norm(q.value.trim());
  if(!t){ render(STUDIES); return; }
  // filtra estudios cuyo label o alguna medida coincida; abre los que coinciden
  const filtered = STUDIES.map(st=>{
    const montTxt = st.montaje ? Object.values(st.montaje).join(" ") : "";
    const inStudy = norm(st.study_label+" "+montTxt).includes(t);
    const meas = st.measures.filter(m=> norm(m.name).includes(t));
    if(inStudy) return st;
    if(meas.length) return Object.assign({}, st, {measures:meas});
    return null;
  }).filter(Boolean);
  render(filtered);
  document.querySelectorAll("details.study").forEach(d=> d.open=true);
});
</script>
</body></html>"""

out = HTML.replace("__DATA__", DATA)
with open(os.path.join(APP, "index.html"), "w", encoding="utf-8") as f:
    f.write(out)
print("  escrito:", os.path.join(APP, "index.html"), f"({len(out)} bytes)")
