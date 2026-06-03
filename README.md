# Aplicaciones · Electrodiagnóstico y Ultrasonido Neuromuscular

Herramientas web de consulta, complementarias al libro *Electrodiagnóstico y Ultrasonido Neuromuscular*.
Todas son páginas estáticas autocontenidas (un solo archivo HTML, sin JavaScript externo ni dependencias),
pensadas para abrirse desde el celular o el navegador y funcionar sin conexión una vez cargadas.

## Sitio publicado

GitHub Pages: **https://fortizc-max.github.io/edx-aplicaciones/**

## Aplicaciones

| App | Carpeta | Contenido |
|-----|---------|-----------|
| EDx pediátrico · Valores de referencia | [`valores-pediatricos/`](valores-pediatricos/) | Neuroconducciones motoras y sensitivas (Ryan 2019), ondas F por estatura (Puksa 2011), ondas F por edad (Cai 1997), FED (Sharma 2020) |

## Cómo añadir una app nueva

1. Crear una subcarpeta con un nombre corto en minúsculas (p. ej. `radiculopatias/`).
2. Poner dentro un único `index.html` autocontenido.
3. Añadir una fila en la tabla de arriba y una tarjeta en el `index.html` raíz.
4. `git add . && git commit && git push` — Pages se actualiza solo en ~1 min.

## Aviso

Material de apoyo a la interpretación clínica. No sustituye el juicio del especialista
ni los valores de referencia propios de cada laboratorio.
