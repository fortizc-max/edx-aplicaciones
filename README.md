# Aplicaciones · Electrodiagnóstico y Ultrasonido Neuromuscular

Herramientas web de consulta, complementarias al libro *Electrodiagnóstico y Ultrasonido Neuromuscular*.
Todas son páginas estáticas autocontenidas (un solo archivo HTML, sin JavaScript externo ni dependencias),
pensadas para abrirse desde el celular o el navegador y funcionar sin conexión una vez cargadas.

## Sitio publicado

GitHub Pages: **https://fortizc-max.github.io/edx-aplicaciones/**

## Aplicaciones

| App | Carpeta | Contenido |
|-----|---------|-----------|
| EDx adulto · Valores de referencia | [`valores-adultos/`](valores-adultos/) | Neuroconducción motora, sensitiva y de nervio mixto en adultos (Buschbacher 1999/2003): mediano, cubital, peroneo, tibial, sural, safeno; percentiles por edad/sexo/talla. Datos crudos en `valores-adultos/_datos/` |
| EDx pediátrico · Valores de referencia | [`valores-pediatricos/`](valores-pediatricos/) | Neuroconducciones motoras y sensitivas (Ryan 2019), ondas F por estatura (Puksa 2011), ondas F por edad (Cai 1997), FED (Sharma 2020) |
| CIDP · Clasificador de criterios | [`cidp-criterios/`](cidp-criterios/) | Clasificador guiado de la polineuropatía desmielinizante inflamatoria crónica según la guía EAN/PNS 2021 (Van den Bergh 2021): fenotipo clínico, criterios electrodiagnósticos motores (a–g) y sensitivos, y categorías «CIDP» / «posible CIDP» |
| Músculos · latín y español | [`musculos/`](musculos/) | Buscador de equivalencias de los nombres musculares (Terminologia Anatomica), insensible a acentos |
| FSHD · patrón muscular interactivo | [`fshd-musculos/`](fshd-musculos/) | Esquema corporal interactivo del compromiso muscular en la distrofia facioescapulohumeral (temprano/tardío) |
| EMG sintético · actividad espontánea y unidades motoras | [`emg-sintetico/`](emg-sintetico/) | Simulador de EMG con aguja (trazo + sonido sincronizados): fibrilaciones, ondas positivas, fasciculaciones, descargas miotónicas, repetitivas complejas, mioquimias; unidades normal/polifásica/inestable/neuropática/miopática y reclutamiento normal |
| CMAP · conducción motora del nervio mediano | [`cmap-mediano/`](cmap-mediano/) | Simulador del potencial de acción muscular compuesto (muñeca y codo) con cursores arrastrables; calcula latencias, amplitudes, duración, área, velocidad de conducción y caída de amplitud |
| SNAP · conducción sensitiva del nervio mediano | [`snap-mediano/`](snap-mediano/) | Simulador del potencial de acción nervioso sensitivo con cursores de inicio y pico; calcula latencia de inicio y de pico, amplitud base–pico y pico–pico, y velocidad de conducción sensitiva (un solo punto de estímulo) |
| CSI · índice sensorial combinado de Robinson | [`csi-robinson/`](csi-robinson/) | Índice sensorial combinado para el síndrome del túnel del carpo: tres comparaciones mediano vs no mediano (radial–pulgar, cubital–anular y palmar), diferencias de latencia de pico, CSI total e interpretación (normal ≤ 0,9 ms) |
| Estimulación repetitiva · unión neuromuscular | [`estimulacion-repetitiva/`](estimulacion-repetitiva/) | Simulador del test de estimulación nerviosa repetitiva (RNS) con reproducción animada: tren de CMAP, envolvente y cálculo de decremento/incremento; escenarios normal 3 Hz, decremento (miastenia), decremento progresivo e incremento >100 % a 30 Hz (Lambert-Eaton) |
| EMG de fibra única · jitter y bloqueo | [`fibra-unica/`](fibra-unica/) | Simulador de SFEMG (estimulada y voluntaria, normal/anormal): descargas consecutivas superpuestas en cascada, jitter (MCD) y bloqueo con interpretación |
| MUNE · número de unidades motoras | [`mune/`](mune/) | Simulador de la estimación del número de unidades motoras (incremental y multipunto): escalones cuantales / SMUP individuales, SMUP promedio y MUNE = CMAP máx ÷ SMUP; escenario normal y neurogénico |
| Temperatura y neuroconducción | [`temperatura/`](temperatura/) | Efecto de la temperatura sobre el estudio de conducción: latencia, amplitud, duración y velocidad cambian con la temperatura (frío → más lento, más grande, más ancho); recomendación 32–36 °C |
| Bloqueo de conducción y dispersión temporal | [`bloqueo-dispersion/`](bloqueo-dispersion/) | CMAP distal vs proximal: distingue bloqueo (cae amplitud y área) de dispersión temporal (aumenta duración, área conservada); escenarios e interpretación (desmielinizante vs axonal) |

## Cómo añadir una app nueva

1. Crear una subcarpeta con un nombre corto en minúsculas (p. ej. `radiculopatias/`).
2. Poner dentro un único `index.html` autocontenido.
3. Añadir una fila en la tabla de arriba y una tarjeta en el `index.html` raíz.
4. `git add . && git commit && git push` — Pages se actualiza solo en ~1 min.

## Aviso

Material de apoyo a la interpretación clínica. No sustituye el juicio del especialista
ni los valores de referencia propios de cada laboratorio.
