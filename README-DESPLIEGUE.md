# Web de CreatorsManager · Guía de puesta en marcha

Web estática multipágina (29 páginas, castellano e inglés). No necesita build, ni Node, ni Supabase: se sube tal cual y funciona.

## 1. Subirla a GitHub

1. Entra en github.com y crea un repositorio nuevo: **creatorsmanager-web** (privado o público, da igual).
2. En la página del repo vacío, pulsa **uploading an existing file**.
3. Descomprime el zip en tu ordenador y arrastra TODO el contenido de la carpeta (no la carpeta en sí: los archivos y subcarpetas que hay dentro, para que index.html quede en la raíz del repo).
4. Commit changes.

## 2. Conectarla a Vercel

1. En vercel.com, **Add New > Project** e importa el repo creatorsmanager-web.
2. Framework Preset: **Other**. No toques nada más (ni build command ni output directory: es estática).
3. **Deploy**. En un minuto tienes la web en una URL tipo creatorsmanager-web.vercel.app.
4. A partir de aquí, cada cambio que subas al repo se despliega solo.

## 3. Dominio creatorsmanager.es

1. En el proyecto de Vercel: **Settings > Domains > Add** y escribe creatorsmanager.es (añade también www.creatorsmanager.es).
2. Vercel te dará un registro A (76.76.21.21) y un CNAME para www. Cópialos en el panel DNS de donde tengas comprado el dominio.
3. En 5-30 minutos el dominio queda activo con HTTPS automático.

## 4. Activar los formularios (2 minutos)

Los dos formularios (marcas y creadores) envían con Web3Forms, gratis hasta 250 envíos/mes:

1. Entra en **web3forms.com**, escribe contacto@creatorsmanager.es y pulsa Create Access Key.
2. Te llega la clave a ese correo.
3. Abre **js/site.js** y en la línea 10 sustituye PON_AQUI_TU_ACCESS_KEY por tu clave.
4. Sube el cambio al repo. Hasta que no pongas la clave, el formulario muestra un aviso con el email de contacto en su lugar (la web nunca se queda muda).

Incluyen validación, honeypot anti-spam, mensaje de éxito/error y asunto distinto según sea marca o creador, para que los distingas en la bandeja.

## 5. Pendientes que dependen de ti

- **Cifra de MagaGames**: su tarjeta sale sin número de suscriptores. Cuando la tengas, edita build.py (campo "subs" de magagames), ejecuta `python3 build.py` y sube los HTML. Si no quieres tocar Python, dímelo y te paso los HTML ya regenerados.
- **Cifra de Dagar**: está puesta la de vuestro media kit (6,7M). Las fuentes públicas muestran fotos antiguas del canal con cifras distintas, así que dale un vistazo antes de publicar.
- **Logos de marcas**: ya están montados Supabase, Hostinger, Arduino y hide.me (img/marcas/). Para añadir otra, suma su logo a esa carpeta y una línea en build.py.
- **Testimonios**: hay 3 plantillas con corchetes en la portada. Rellénalos o pásamelos.
- **Datos legales**: en aviso-legal.html y privacidad.html hay dos [COMPLETAR]: tu NIF y tu dirección. Revisa los tres textos legales antes de publicar.
- **Enlaces de canales**: revisa que los handles de YouTube de xTurbo (@xTurbo_) y ArselJuega sean correctos; el resto vienen de tu prompt.
- **Avatares**: si algún día quieres cambiarlos, son los archivos de img/creadores/ (avatar-arsel.jpg, avatar-dagar.jpg, etc.). Mismo nombre, misma carpeta, y listo. Los de MarZy (200px) y Maga (160px) son pequeños: si tienes versiones más grandes, mejor.

## 6. Cómo editar textos en el futuro

Toda la web se genera desde **build.py** (textos, roster, cifras, FAQ, en los dos idiomas). Lo más cómodo: edita ahí y ejecuta `python3 build.py`, que regenera los 29 HTML de golpe. También puedes editar cualquier .html directamente si es un cambio puntual.

## Estructura

- index.html + en/ (portada ES y EN)
- creadores.html + creadores/*.html (roster con filtros y ficha por creador, enlazable para mandar a marcas)
- marcas.html (servicios, formatos, proceso, FAQ)
- soy-creador.html (representación + CTA al formulario)
- agencia.html (historia y fundador)
- contacto.html (formulario doble; llega con el creador preseleccionado desde las fichas)
- aviso-legal / privacidad / cookies + banner de cookies
- sitemap.xml, robots.txt, vercel.json, Open Graph y favicons con el escudo CM
