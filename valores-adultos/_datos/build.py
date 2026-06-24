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

with open(os.path.join(HERE, "_template.html"), encoding="utf-8") as _f:
    HTML = _f.read()

out = HTML.replace("__DATA__", DATA)
with open(os.path.join(APP, "index.html"), "w", encoding="utf-8") as f:
    f.write(out)
print("  escrito:", os.path.join(APP, "index.html"), f"({len(out)} bytes)")
