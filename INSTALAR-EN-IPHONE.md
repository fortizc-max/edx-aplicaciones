# Cómo dejar una app del libro en el iPhone

Guía práctica para tener cualquiera de las aplicaciones (valores de referencia, clasificadores, etc.)
como **ícono tipo app** en el iPhone, funcionando **sin conexión**.

> Resumen rápido (método recomendado):
> **Safari → pegar la URL de la app → Compartir ⬆️ → “Agregar a inicio” → Agregar.**

---

## Método recomendado — ícono en la pantalla de inicio (Safari)

Es el más sencillo y fiable. La app queda como un ícono propio, a pantalla completa, y sigue
funcionando sin internet después de la primera carga.

1. En el iPhone, abre **Safari** (el ícono de la brújula 🧭). *No uses Chrome:* la opción de
   pantalla de inicio solo es fiable en Safari, y en iPhone todos los navegadores usan el mismo
   motor, así que se ve igual.
2. Escribe o pega la **URL de la app**. Las apps están publicadas en:
   - Índice: `https://fortizc-max.github.io/edx-aplicaciones/`
   - Valores adulto: `https://fortizc-max.github.io/edx-aplicaciones/valores-adultos/`
   - Valores pediátrico: `https://fortizc-max.github.io/edx-aplicaciones/valores-pediatricos/`
   - Clasificador CIDP: `https://fortizc-max.github.io/edx-aplicaciones/cidp-criterios/`
3. Espera a que **cargue por completo**.
4. Toca el botón **Compartir** = el **cuadrito con la flecha hacia arriba ⬆️** (barra inferior, al
   centro). *No* el botón **“aA”**.
5. En el menú, **desliza hacia abajo** por la lista de acciones hasta encontrar
   **“Agregar a inicio”** (en otros iPhone aparece como **“Añadir a pantalla de inicio”**).
6. (Opcional) edita el **nombre** corto del ícono, p. ej. *EDx Adulto*.
7. Toca **“Agregar”** (arriba a la derecha).

Listo: el ícono queda en la pantalla de inicio, es **privado de ese teléfono** y funciona offline.

---

## Alternativa — archivo offline por iCloud Drive

Útil si se quiere el archivo HTML guardado en el teléfono (sin depender del enlace).

> ⚠️ **Importante:** al tocar un `.html` desde la app **Archivos**, iOS lo abre en una **vista
> previa (Quick Look)** que **no ejecuta bien el JavaScript interactivo** (búsquedas, botones).
> Por eso “no funciona” si se abre así. Soluciones: usar el **método recomendado** de arriba, o
> abrir el archivo con la app **Documents (Readdle)**, cuyo navegador interno sí ejecuta HTML
> local completo y offline.

Para copiar el archivo a iCloud Drive:

1. **En el Mac**, activa iCloud Drive: Ajustes del Sistema → (tu nombre) → **iCloud** → **Drive** →
   activar **“Sincronizar este Mac”**. Se crea la carpeta
   `~/Library/Mobile Documents/com~apple~CloudDocs/`.
2. Copia el archivo `.html` autocontenido de la app a esa carpeta (los archivos de las apps son de
   un solo archivo HTML con los datos embebidos, así que funcionan offline).
3. **En el iPhone**, activa iCloud Drive: Ajustes → (tu nombre) → **iCloud** → **iCloud Drive** →
   **“Sincronizar este iPhone”**.
4. Abre la app **Archivos → Explorar (abajo) → iCloud Drive** y baja para refrescar.
   - Si **iCloud Drive no aparece** en “Ubicaciones”: en Explorar toca **••• → Editar** y actívalo.
5. Abre el archivo con **Documents (Readdle)** para que funcione interactivo (no con la vista
   previa de Archivos).

---

## Solución de problemas (cosas que nos pasaron)

- **“No veo iCloud Drive en el iPhone”** → hay que activarlo en *Ajustes → (tu nombre) → iCloud →
  iCloud Drive → Sincronizar este iPhone*. Los archivos NO se ven dentro de Ajustes, sino en la app
  **Archivos → Explorar → iCloud Drive**.
- **“No aparece ‘Agregar a inicio’ en el menú Compartir”** → casi siempre está, pero hay que
  **deslizar el menú hacia abajo**; el nombre puede ser “Agregar a inicio” o “Añadir a pantalla de
  inicio”. Asegúrate de estar en **Safari** (si ves “Agregar a lecturas / Lista de lectura”, estás
  en Safari, vas bien). Si de verdad falta, ábrelo con **“Editar acciones…”** al final del menú, o
  revisa que **Tiempo de uso → Restricciones de contenido y privacidad** no la esté ocultando.
- **“La app no funciona al abrir el archivo”** → es la vista previa de Archivos (Quick Look), que no
  corre el JavaScript. Usa el método de Safari o ábrelo con Documents (Readdle).
- **Usar siempre Safari, no Chrome**, para el ícono de pantalla de inicio.

---

## Para publicar una app nueva (recordatorio)

1. Crear subcarpeta en minúsculas con un único `index.html` autocontenido.
2. Añadir la tarjeta en el `index.html` raíz y la fila en `README.md`.
3. `git add . && git commit && git push` — GitHub Pages se actualiza en ~1 min.
4. La URL queda como `https://fortizc-max.github.io/edx-aplicaciones/<carpeta>/`, lista para el QR
   del libro y para “Agregar a inicio”.
