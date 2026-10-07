# -*- coding: utf-8 -*-
"""
Generador de la web de CreatorsManager.
Ejecutar:  python3 build.py
Produce todas las páginas HTML (ES y EN), sitemap.xml y robots.txt.
Para cambiar textos o cifras, edita este archivo y vuelve a ejecutarlo.
"""
import os

DOMINIO = "https://creatorsmanager.es"
RAIZ = os.path.dirname(os.path.abspath(__file__))

# ==================================================================
# ROSTER
# ==================================================================
CREADORES = [
    {
        "slug": "xturbo", "nombre": "xTurbo",
        "subs": "7,4M", "subs_en": "7.4M",
        "tags": "minecraft,espana,latam",
        "chips_es": ["Minecraft", "España y LATAM"],
        "chips_en": ["Minecraft", "Spain and LATAM"],
        "datos_es": [("7,4M", "suscriptores"), ("+40M", "visualizaciones al mes"), ("Minecraft", "nicho principal")],
        "datos_en": [("7.4M", "subscribers"), ("+40M", "monthly views"), ("Minecraft", "main niche")],
        "bio_es": """<p>xTurbo es uno de los canales de Minecraft más grandes del mercado hispanohablante. Retos, récords, manhunts y series de alta energía que conectan con un público joven y muy activo en España y Latinoamérica.</p>
<p>Su ritmo de publicación constante y su estilo directo lo convierten en una apuesta segura para campañas que buscan volumen y repetición de impactos en el público gamer.</p>""",
        "bio_en": """<p>xTurbo runs one of the largest Minecraft channels in the Spanish-speaking market. Challenges, records, manhunts and high-energy series that connect with a young, highly active audience across Spain and Latin America.</p>
<p>His consistent upload schedule and direct style make him a safe bet for campaigns that need volume and repeated impact with gaming audiences.</p>""",
        "encaje_es": "Hosting y servidores de Minecraft, periféricos, videojuegos, apps móviles y marketplaces de juegos.",
        "encaje_en": "Minecraft hosting and servers, peripherals, video games, mobile apps and game marketplaces.",
        "canales": [("xTurbo", "https://www.youtube.com/@xTurbo_", "7,4M", "7.4M")],
        "email": "marketing@xturbo.es",
    },
    {
        "slug": "dagar", "nombre": "Dagar",
        "subs": "6,7M", "subs_en": "6.7M",
        "tags": "minecraft,roblox,familiar,espana,latam",
        "chips_es": ["Minecraft", "Roblox", "Familiar"],
        "chips_en": ["Minecraft", "Roblox", "Family"],
        "datos_es": [("6,7M", "suscriptores"), ("2,4M", "en su canal de Roblox"), ("Smart TV", "fuerte co-visionado familiar")],
        "datos_en": [("6.7M", "subscribers"), ("2.4M", "on his Roblox channel"), ("Smart TV", "strong family co-viewing")],
        "bio_es": """<p>Dagar crea aventuras de Minecraft junto a su amigo Nacho, con quien comparte universo propio y libro publicado. Contenido familiar que se ve en el salón de casa: una parte enorme de su consumo llega desde Smart TV, con padres e hijos delante de la pantalla.</p>
<p>Su canal secundario de Roblox amplía el alcance al otro gran juego del público infantil y juvenil. Mercados principales: México, España y el resto de LATAM.</p>""",
        "bio_en": """<p>Dagar creates Minecraft adventures with his friend Nacho. They share their own universe and a published book. Family content watched in the living room: a huge share of his viewing comes from Smart TV, with parents and kids in front of the screen together.</p>
<p>His secondary Roblox channel extends that reach into the other big game for young audiences. Main markets: Mexico, Spain and the rest of LATAM.</p>""",
        "encaje_es": "Juguetes, bebidas y alimentación, videojuegos, apps y editoriales. Marcas que buscan al público familiar hispano.",
        "encaje_en": "Toys, food and drinks, video games, apps and publishers. Brands targeting Spanish-speaking families.",
        "canales": [
            ("Dagar", "https://www.youtube.com/@dagar-minecraft", "6,7M", "6.7M"),
            ("Dagar Roblox", "https://www.youtube.com/@Dagar-Roblox", "2,4M", "2.4M"),
        ],
        "email": None,
    },
    {
        "slug": "arsel", "nombre": "Arsel",
        "subs": "6,5M", "subs_en": "6.5M",
        "tags": "minecraft,espana,latam",
        "chips_es": ["Minecraft", "España y LATAM"],
        "chips_en": ["Minecraft", "Spain and LATAM"],
        "datos_es": [("6,5M", "suscriptores"), ("Pre-roll", "formato estrella: 60 y 90 segundos"), ("Rodaje in-game", "integraciones dentro de Minecraft")],
        "datos_en": [("6.5M", "subscribers"), ("Pre-roll", "signature format: 60 and 90 seconds"), ("In-game", "integrations shot inside Minecraft")],
        "bio_es": """<p>Arsel es un referente del Minecraft hispanohablante con un estilo elaborado y reconocible. Sus integraciones publicitarias se ruedan dentro del propio juego, con escenarios construidos a medida para cada marca, y por eso no se sienten como anuncios: se sienten como parte del vídeo.</p>
<p>Tiene experiencia contrastada en campañas por fases con guion aprobado por la marca antes de grabar, códigos de descuento propios y seguimiento de resultados.</p>""",
        "bio_en": """<p>Arsel is a reference in Spanish-language Minecraft with a polished, recognisable style. His brand integrations are shot inside the game itself, with sets built specifically for each brand, so they never feel like ads: they feel like part of the video.</p>
<p>He has proven experience running phased campaigns with brand-approved scripts before recording, dedicated discount codes and results tracking.</p>""",
        "encaje_es": "Hosting y servidores, VPN y privacidad, gaming gear y tecnología. Ideal para campañas de varias fases.",
        "encaje_en": "Hosting and servers, VPN and privacy, gaming gear and tech. Ideal for multi-phase campaigns.",
        "canales": [
            ("ARSEL", "https://www.youtube.com/@ARSEEL", "6,5M", "6.5M"),
            ("ArselJuega", "https://www.youtube.com/@ArselJuega", "canal secundario", "secondary channel"),
        ],
        "email": None,
    },
    {
        "slug": "danomc", "nombre": "DanoMC",
        "subs": "3,6M", "subs_en": "3.6M",
        "tags": "minecraft,roblox,familiar,espana,latam",
        "chips_es": ["Minecraft", "Familiar", "Multicanal"],
        "chips_en": ["Minecraft", "Family", "Multi-channel"],
        "datos_es": [("3,6M", "suscriptores"), ("+50M", "visualizaciones al mes"), ("82%", "del consumo en Smart TV"), ("53%", "audiencia femenina")],
        "datos_en": [("3.6M", "subscribers"), ("+50M", "monthly views"), ("82%", "of viewing on Smart TV"), ("53%", "female audience")],
        "bio_es": """<p>DanoMC es contenido familiar de Minecraft y gaming que se ve en el salón: más del 82% de su consumo llega desde Smart TV. Su audiencia rompe el tópico del gaming: 53% femenina, con núcleos fuertes entre los 25 y los 44 años. Padres y madres viendo vídeos con sus hijos.</p>
<p>Opera una red de cinco canales (reacciones, Roblox, gameplays y más), lo que permite montar packs promocionales en varios canales a la vez con una sola negociación.</p>""",
        "bio_en": """<p>DanoMC makes family Minecraft and gaming content watched in the living room: over 82% of his viewing comes from Smart TV. His audience breaks the gaming stereotype: 53% female, with strong segments between 25 and 44 years old. Parents watching videos with their kids.</p>
<p>He runs a network of five channels (reactions, Roblox, gameplays and more), which makes multi-channel promo packs possible with a single negotiation.</p>""",
        "encaje_es": "Juguetes, alimentación, gran consumo, apps y videojuegos. La mejor puerta de entrada al salón familiar hispano.",
        "encaje_en": "Toys, food, consumer goods, apps and video games. The best route into the Spanish-speaking family living room.",
        "canales": [
            ("DanoMC", "https://www.youtube.com/@DanoMC", "3,6M", "3.6M"),
            ("DanoMC Reacciona", "https://www.youtube.com/@DanoMinecraft", "reacciones", "reactions"),
            ("DanoBlox", "https://www.youtube.com/@DanoBloxMC", "Roblox", "Roblox"),
            ("DanoMC Juega", "https://www.youtube.com/@DanoJuega", "gameplays", "gameplays"),
            ("KeciyoMC", "https://www.youtube.com/@KeciyoMC", "canal hermano", "sister channel"),
        ],
        "email": None,
    },
    {
        "slug": "marzy", "nombre": "The MarZy",
        "subs": "3,6M", "subs_en": "3.6M",
        "tags": "minecraft,espana",
        "chips_es": ["Minecraft narrativo", "España"],
        "chips_en": ["Narrative Minecraft", "Spain"],
        "datos_es": [("3,6M", "suscriptores"), ("+695", "vídeos publicados"), ("10-23M", "visualizaciones en su serie estrella")],
        "datos_en": [("3.6M", "subscribers"), ("+695", "published videos"), ("10-23M", "views on his flagship series")],
        "bio_es": """<p>The MarZy hace Minecraft narrativo y cinematográfico: misterio, bases secretas, clanes, infiltraciones y supervivencia. Su serie estrella de supervivencia en bases secretas acumula vídeos de entre 10 y 23 millones de visualizaciones.</p>
<p>Tiene servidor propio (Hydracraft), libros publicados y una de las comunidades más fieles del Minecraft español, activa en Discord y dentro del propio servidor. Para una marca, eso significa audiencia que vuelve vídeo tras vídeo.</p>""",
        "bio_en": """<p>The MarZy makes narrative, cinematic Minecraft: mystery, secret bases, clans, infiltrations and survival. His flagship secret-base survival series has videos reaching between 10 and 23 million views each.</p>
<p>He owns his own server (Hydracraft), has published books and leads one of the most loyal communities in Spanish Minecraft, active on Discord and inside the server itself. For a brand, that means an audience that comes back video after video.</p>""",
        "encaje_es": "Videojuegos, tecnología, editoriales y marcas que buscan integraciones elaboradas con storytelling.",
        "encaje_en": "Video games, tech, publishers and brands looking for elaborate, story-driven integrations.",
        "canales": [
            ("The MarZy", "https://www.youtube.com/@TheMarZy", "3,6M", "3.6M"),
            ("MarzyTV", None, "63K", "63K"),
            ("MarzyBlox", None, "18,5K", "18.5K"),
        ],
        "email": None,
    },
    {
        "slug": "mateo", "nombre": "Mateo Ferruz",
        "subs": "1,1M", "subs_en": "1.1M",
        "tags": "salud,espana,latam",
        "chips_es": ["Salud y fitness", "Divulgación"],
        "chips_en": ["Health and fitness", "Science-based"],
        "datos_es": [("1,1M", "suscriptores en YouTube"), ("22,7M", "visualizaciones en 28 días"), ("78,8%", "de retención media"), ("66%", "de usuarios recurrentes")],
        "datos_en": [("1.1M", "YouTube subscribers"), ("22.7M", "views in 28 days"), ("78.8%", "average watch percentage"), ("66%", "returning viewers")],
        "bio_es": """<p>Mateo Ferruz hace divulgación viral sobre el cuerpo humano, el entrenamiento, la nutrición y el sueño, siempre con base científica. Sus métricas de retención son excepcionales: un 78,8% de porcentaje medio visto y dos de cada tres espectadores que vuelven.</p>
<p>Es probador natural de productos en cámara y el creador del roster fuera del gaming: la prueba de que la agencia también cubre lifestyle y salud. Núcleo de audiencia de 25 a 44 años repartido entre México, Argentina, España, Colombia y Perú, con presencia también en TikTok e Instagram.</p>""",
        "bio_en": """<p>Mateo Ferruz creates viral, science-based content about the human body, training, nutrition and sleep. His retention metrics are exceptional: a 78.8% average watch percentage and two out of three viewers coming back.</p>
<p>He is a natural on-camera product tester and the roster's creator outside gaming: proof that the agency also covers lifestyle and health. Core audience aged 25 to 44 across Mexico, Argentina, Spain, Colombia and Peru, with a presence on TikTok and Instagram too.</p>""",
        "encaje_es": "Salud, deporte, suplementación, apps de hábitos y tecnología de consumo para público adulto.",
        "encaje_en": "Health, sport, supplements, habit apps and consumer tech for adult audiences.",
        "canales": [
            ("Mateo Ferruz", "https://www.youtube.com/@mateo.ferruz", "1,1M", "1.1M"),
            ("TikTok", "https://www.tiktok.com/@mateo.ferruz", "~200K", "~200K"),
            ("Instagram", "https://www.instagram.com/mateo.ferruz", "~110K", "~110K"),
        ],
        "email": None,
    },
    {
        "slug": "magagames", "nombre": "MagaGames",
        "subs": None, "subs_en": None,
        "tags": "minecraft,familiar,espana,latam",
        "chips_es": ["Minecraft", "Familiar", "España, LATAM y EE. UU."],
        "chips_en": ["Minecraft", "Family", "Spain, LATAM and US"],
        "datos_es": [("Familiar", "retos, series y roleplay"), ("3 mercados", "España, LATAM e hispanos en EE. UU.")],
        "datos_en": [("Family", "challenges, series and roleplay"), ("3 markets", "Spain, LATAM and US Hispanics")],
        "bio_es": """<p>MagaGames hace Minecraft family-friendly: retos, series y roleplay pensados para público joven y familias. Su comunidad se reparte entre España, Latinoamérica y la comunidad hispana de Estados Unidos, lo que lo convierte en una vía directa a tres mercados a la vez.</p>
<p>Contenido 100% apto para todas las edades, ideal para marcas de juguetes, alimentación y entretenimiento que necesitan un entorno seguro para su mensaje.</p>""",
        "bio_en": """<p>MagaGames makes family-friendly Minecraft: challenges, series and roleplay designed for young audiences and families. His community spans Spain, Latin America and the Hispanic community in the United States, a direct route into three markets at once.</p>
<p>Content that is 100% all-ages, ideal for toy, food and entertainment brands that need a safe environment for their message.</p>""",
        "encaje_es": "Juguetes, bebidas y alimentación, entretenimiento y apps para público joven y familiar.",
        "encaje_en": "Toys, food and drinks, entertainment and apps for young and family audiences.",
        "canales": [("MagaGames", "https://www.youtube.com/@MagaGamesMc", "canal principal", "main channel")],
        "email": "contacto@magagames.mx",
    },
]

FILTROS = [
    ("todos", "Todos", "All"),
    ("minecraft", "Minecraft", "Minecraft"),
    ("roblox", "Roblox", "Roblox"),
    ("familiar", "Familiar", "Family"),
    ("salud", "Salud y fitness", "Health and fitness"),
    ("espana", "España", "Spain"),
    ("latam", "LATAM", "LATAM"),
]

# ==================================================================
# PLANTILLAS COMUNES
# ==================================================================

def head(lang, titulo, desc, ruta_es, ruta_en, es_en=False):
    ruta = ruta_en if es_en else ruta_es
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMINIO}{ruta}">
<link rel="alternate" hreflang="es" href="{DOMINIO}{ruta_es}">
<link rel="alternate" hreflang="en" href="{DOMINIO}{ruta_en}">
<link rel="alternate" hreflang="x-default" href="{DOMINIO}{ruta_es}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="CreatorsManager">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{DOMINIO}/og-creatorsmanager.jpg">
<meta property="og:url" content="{DOMINIO}{ruta}">
<meta property="og:locale" content="{'en_US' if es_en else 'es_ES'}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="32x32" href="/img/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/img/icon-192.png">
<link rel="apple-touch-icon" sizes="180x180" href="/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Archivo:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/site.css">
<script defer src="/js/site.js"></script>
</head>
<body>
"""

NAV_ES = [("Inicio", "/"), ("Creadores", "/creadores"), ("Marcas", "/marcas"), ("Soy creador", "/soy-creador"), ("Agencia", "/agencia")]
NAV_EN = [("Home", "/en/"), ("Creators", "/en/creadores"), ("Brands", "/en/marcas"), ("For creators", "/en/soy-creador"), ("Agency", "/en/agencia")]

def nav(es_en, activo, ruta_alterna):
    items = NAV_EN if es_en else NAV_ES
    contacto = ("/en/contacto", "Contact") if es_en else ("/contacto", "Contacto")
    lang_label = "ES" if es_en else "EN"
    enlaces = "\n".join(
        f'      <a href="{url}"{" class=\"activo\"" if url == activo else ""}>{txt}</a>'
        for txt, url in items
    )
    return f"""<header class="nav">
  <div class="wrap nav-inner">
    <a href="{'/en/' if es_en else '/'}" class="nav-logo">
      <img src="/img/logo-cm.png" alt="CreatorsManager" width="44" height="50">
      <span>Creators<b>Manager</b></span>
    </a>
    <button class="nav-burger" aria-expanded="false" aria-label="{'Open menu' if es_en else 'Abrir menú'}">&#9776;</button>
    <nav class="nav-links">
{enlaces}
      <a href="{contacto[0]}" class="btn nav-cta" style="padding:10px 18px; font-size:.95rem">{contacto[1]}</a>
      <a href="{ruta_alterna}" class="nav-lang" lang="{'es' if es_en else 'en'}" aria-label="{'Versión en español' if es_en else 'English version'}">{lang_label}</a>
    </nav>
  </div>
</header>
"""

def footer(es_en):
    y = "2025-2026"
    creadores_links = "\n".join(
        f'        <li><a href="{"/en" if es_en else ""}/creadores/{c["slug"]}">{c["nombre"]}</a></li>' for c in CREADORES
    )
    if es_en:
        cols = f"""      <div>
        <h4>Agency</h4>
        <ul>
          <li><a href="/en/marcas">For brands</a></li>
          <li><a href="/en/soy-creador">For creators</a></li>
          <li><a href="/en/agencia">About us</a></li>
          <li><a href="/en/contacto">Contact</a></li>
          <li><a href="https://www.linkedin.com/in/julen-aldazabal-punzano-8974281bb/" target="_blank" rel="noopener">LinkedIn</a></li>
        </ul>
      </div>
      <div>
        <h4>Roster</h4>
        <ul>
{creadores_links}
        </ul>
      </div>
      <div>
        <h4>Legal</h4>
        <ul>
          <li><a href="/aviso-legal">Legal notice (ES)</a></li>
          <li><a href="/privacidad">Privacy policy (ES)</a></li>
          <li><a href="/cookies">Cookie policy (ES)</a></li>
        </ul>
      </div>"""
        claim = "Influencer marketing agency for the Spanish-speaking market. YouTube first."
        aviso = "CreatorsManager works with brands worldwide in Spanish and English."
    else:
        cols = f"""      <div>
        <h4>Agencia</h4>
        <ul>
          <li><a href="/marcas">Para marcas</a></li>
          <li><a href="/soy-creador">Para creadores</a></li>
          <li><a href="/agencia">Quiénes somos</a></li>
          <li><a href="/contacto">Contacto</a></li>
          <li><a href="https://www.linkedin.com/in/julen-aldazabal-punzano-8974281bb/" target="_blank" rel="noopener">LinkedIn</a></li>
        </ul>
      </div>
      <div>
        <h4>Roster</h4>
        <ul>
{creadores_links}
        </ul>
      </div>
      <div>
        <h4>Legal</h4>
        <ul>
          <li><a href="/aviso-legal">Aviso legal</a></li>
          <li><a href="/privacidad">Política de privacidad</a></li>
          <li><a href="/cookies">Política de cookies</a></li>
        </ul>
      </div>"""
        claim = "Agencia de influencer marketing para el mercado hispanohablante. YouTube primero."
        aviso = "Trabajamos con marcas de todo el mundo, en castellano y en inglés."
    cookies_txt = (
        "We only use technical cookies and a local preference to remember this choice. No third-party trackers.",
        "Accept", "Essential only"
    ) if es_en else (
        "Solo usamos cookies técnicas y una preferencia local para recordar esta elección. Sin rastreadores de terceros.",
        "Aceptar", "Solo esenciales"
    )
    return f"""<footer>
  <div class="wrap">
    <div class="pie-grid">
      <div class="pie-logo">
        <img src="/img/logo-cm.png" alt="CreatorsManager">
        <p>{claim}</p>
        <p><a href="mailto:contacto@creatorsmanager.es">contacto@creatorsmanager.es</a></p>
      </div>
{cols}
    </div>
    <p class="pie-legal">&copy; {y} CreatorsManager &middot; Julen Aldazabal Punzano &middot; {aviso}</p>
  </div>
</footer>
<div class="cookies" role="dialog" aria-label="Cookies">
  <p>{cookies_txt[0]} <a href="/cookies">{'Cookie policy' if es_en else 'Más información'}</a>.</p>
  <div class="cookies-botones">
    <button class="btn" data-cookies="todas">{cookies_txt[1]}</button>
    <button class="btn btn-hueso" data-cookies="esenciales">{cookies_txt[2]}</button>
  </div>
</div>
</body>
</html>
"""

def escribe(ruta, contenido):
    destino = os.path.join(RAIZ, ruta.lstrip("/"))
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        f.write(contenido)
    print("ok", ruta)

def carta(c, es_en):
    chips = c["chips_en"] if es_en else c["chips_es"]
    etiquetas = "".join(f'<span class="etiqueta">{ch}</span>' for ch in chips)
    pref = "/en" if es_en else ""
    if es_en:
        subs_html = (f'<span class="carta-subs">{c["subs_en"]}<small>subscribers on YouTube</small></span>'
                     if c["subs_en"] else '<span class="carta-subs">100%<small>family friendly</small></span>')
        boton = "View profile"
    else:
        subs_html = (f'<span class="carta-subs">{c["subs"]}<small>suscriptores en YouTube</small></span>'
                     if c["subs"] else '<span class="carta-subs">100%<small>family friendly</small></span>')
        boton = "Ver ficha"
    return f"""      <a class="carta revelar" data-tags="{c['tags']}" href="{pref}/creadores/{c['slug']}">
        <div class="carta-cabecera"><img src="/img/creadores/avatar-{c['slug']}.jpg" alt="{c['nombre']}" loading="lazy" width="132" height="132"></div>
        <div class="carta-cuerpo">
          <h3>{c['nombre']}</h3>
          {subs_html}
          <div class="carta-etiquetas">{etiquetas}</div>
          <div class="carta-pie"><span class="btn">{boton}</span></div>
        </div>
      </a>"""

def grid_roster(es_en):
    return f"""    <div class="roster-grid">
{chr(10).join(carta(c, es_en) for c in CREADORES)}
    </div>"""

def filtros_html(es_en):
    botones = "\n".join(
        f'      <button class="filtro{" activo" if clave == "todos" else ""}" data-filtro="{clave}">{en if es_en else es}</button>'
        for clave, es, en in FILTROS
    )
    return f'    <div class="filtros">\n{botones}\n    </div>'

MARCADOR_ES = """  <div class="wrap">
    <div class="marcador">
      <div class="marcador-item"><span class="num" data-fin="40" data-prefijo="+">+40</span><span class="des">campañas gestionadas</span></div>
      <div class="marcador-item"><span class="num" data-fin="25" data-prefijo="+" data-sufijo="M">+25M</span><span class="des">suscriptores en el roster</span></div>
      <div class="marcador-item"><span class="num" data-fin="7">7</span><span class="des">creadores representados</span></div>
      <div class="marcador-item"><span class="num" data-fin="7" data-prefijo="+">+7</span><span class="des">años de experiencia en el sector</span></div>
    </div>
  </div>"""

MARCADOR_EN = """  <div class="wrap">
    <div class="marcador">
      <div class="marcador-item"><span class="num" data-fin="40" data-prefijo="+">+40</span><span class="des">campaigns managed</span></div>
      <div class="marcador-item"><span class="num" data-fin="25" data-prefijo="+" data-sufijo="M">+25M</span><span class="des">subscribers across the roster</span></div>
      <div class="marcador-item"><span class="num" data-fin="7">7</span><span class="des">creators represented</span></div>
      <div class="marcador-item"><span class="num" data-fin="7" data-prefijo="+">+7</span><span class="des">years of industry experience</span></div>
    </div>
  </div>"""

def plantel_hero():
    pos = [
        ("xturbo",   "top:0; left:6%;",    "148px", "0s"),
        ("dagar",    "top:4%; right:2%;",  "132px", ".8s"),
        ("arsel",    "top:38%; left:0;",   "116px", "1.6s"),
        ("danomc",   "top:44%; right:14%;","124px", ".4s"),
        ("marzy",    "bottom:0; left:28%;","108px", "1.2s"),
        ("mateo",    "bottom:2%; right:0;","104px", "2s"),
    ]
    fichas = "\n".join(
        f'        <div class="ficha-flotante" style="{estilo} --t:{t}; --d:{d}"><img src="/img/creadores/avatar-{slug}.jpg" alt="" width="132" height="132"><span>{next(c["nombre"] for c in CREADORES if c["slug"] == slug)}</span></div>'
        for slug, estilo, t, d in pos
    )
    return f'      <div class="plantel" data-entrada style="--orden:3" aria-hidden="true">\n{fichas}\n      </div>'

def franja_cta(es_en):
    if es_en:
        return """<section class="franja-cta">
  <div class="wrap">
    <h2>Your next campaign starts with one email</h2>
    <a class="btn btn-tinta btn-grande" href="/en/contacto">Tell us about it</a>
  </div>
</section>
"""
    return """<section class="franja-cta">
  <div class="wrap">
    <h2>Tu próxima campaña empieza con un email</h2>
    <a class="btn btn-tinta btn-grande" href="/contacto">Cuéntanosla</a>
  </div>
</section>
"""

# ==================================================================
# PÁGINAS
# ==================================================================

def pagina_inicio(es_en):
    if not es_en:
        html = head("es", "CreatorsManager · Influencer marketing con los grandes creadores hispanohablantes de YouTube",
                    "Agencia de influencer marketing. Representamos a 7 creadores con más de 25 millones de suscriptores y gestionamos tu campaña de principio a fin.",
                    "/", "/en/")
        html += nav(False, "/", "/en/")
        html += f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1 data-entrada style="--orden:0">Los creadores que mueven al público <span class="ambar">hispanohablante</span></h1>
      <p class="lead" data-entrada style="--orden:1">Agencia de influencer marketing especializada en YouTube. Representamos en exclusiva a 7 creadores con más de 25 millones de suscriptores y gestionamos cada campaña de principio a fin.</p>
      <div class="hero-acciones" data-entrada style="--orden:2">
        <a class="btn btn-grande" href="/marcas">Soy una marca</a>
        <a class="btn btn-hueso btn-grande" href="/soy-creador">Soy creador</a>
      </div>
      <p class="hero-nota" data-entrada style="--orden:4">Trabajamos a diario con marcas de Europa, Estados Unidos y Asia, en castellano y en inglés.</p>
    </div>
{plantel_hero()}
  </div>
</section>
<section>
{MARCADOR_ES}
</section>
<section class="seccion" id="roster">
  <div class="wrap">
    <h2 class="revelar">El roster</h2>
    <p class="lead revelar">Siete creadores, una regla: solo proponemos colaboraciones que tienen sentido para su audiencia. Por eso funcionan.</p>
{grid_roster(False)}
    <p class="centrado" style="margin-top:34px"><a class="btn btn-naranja" href="/creadores">Ver el roster completo</a></p>
  </div>
</section>
<section class="seccion seccion-crema">
  <div class="wrap">
    <h2 class="revelar">Qué hacemos</h2>
    <div class="dos-columnas">
      <div class="panel revelar">
        <h3>Para marcas</h3>
        <ul>
          <li>Seleccionamos al creador ideal según tu público, mercado y producto</li>
          <li>Diseñamos la campaña: integraciones, vídeos dedicados, packs y formatos cortos</li>
          <li>Negociación, contrato y un único interlocutor durante toda la campaña</li>
          <li>Guion aprobado por la marca antes de grabar y reporting final con métricas reales</li>
        </ul>
        <p style="margin:18px 0 0"><a class="btn" href="/marcas">Servicios para marcas</a></p>
      </div>
      <div class="panel panel-ambar revelar">
        <h3>Para creadores</h3>
        <ul>
          <li>Representación comercial exclusiva y gestión de tu bandeja de marcas</li>
          <li>Prospección activa de marcas, además de las que llegan solas</li>
          <li>Negociación de tarifas, siempre priorizando el fee fijo</li>
          <li>Filtro de estafas y estrategia de crecimiento a largo plazo</li>
        </ul>
        <p style="margin:18px 0 0"><a class="btn btn-hueso" href="/soy-creador">Quiero representación</a></p>
      </div>
    </div>
  </div>
</section>
<section class="seccion">
  <div class="wrap">
    <h2 class="revelar">Marcas que confían en nosotros</h2>
    <p class="lead revelar">Más de 40 campañas con marcas de hosting, gaming, tecnología, apps y gran consumo de Europa, América y Asia.</p>
    <div class="cinta-marcas">
      <div class="marca-logo revelar"><img src="/img/marcas/supabase.png" alt="Supabase" loading="lazy"><span>Supabase</span></div>
      <div class="marca-logo revelar"><img src="/img/marcas/hostinger.png" alt="Hostinger" loading="lazy"><span>Hostinger</span></div>
      <div class="marca-logo revelar"><img src="/img/marcas/arduino.png" alt="Arduino" loading="lazy"><span>Arduino</span></div>
      <div class="marca-logo revelar"><img src="/img/marcas/hideme.png" alt="hide.me" loading="lazy"><span>hide.me</span></div>
    </div>
  </div>
</section>
{franja_cta(False)}
"""
        html += footer(False)
        escribe("/index.html", html)
    else:
        html = head("en", "CreatorsManager · Influencer marketing with the top Spanish-speaking YouTube creators",
                    "Influencer marketing agency. We exclusively represent 7 creators with over 25 million subscribers and manage your campaign end to end.",
                    "/", "/en/", True)
        html += nav(True, "/en/", "/")
        html += f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1 data-entrada style="--orden:0">The creators who move the <span class="ambar">Spanish-speaking</span> audience</h1>
      <p class="lead" data-entrada style="--orden:1">An influencer marketing agency built around YouTube. We exclusively represent 7 creators with over 25 million subscribers and manage every campaign end to end.</p>
      <div class="hero-acciones" data-entrada style="--orden:2">
        <a class="btn btn-grande" href="/en/marcas">I'm a brand</a>
        <a class="btn btn-hueso btn-grande" href="/en/soy-creador">I'm a creator</a>
      </div>
      <p class="hero-nota" data-entrada style="--orden:4">We work daily with brands across Europe, the US and Asia, in Spanish and English.</p>
    </div>
{plantel_hero()}
  </div>
</section>
<section>
{MARCADOR_EN}
</section>
<section class="seccion" id="roster">
  <div class="wrap">
    <h2 class="revelar">The roster</h2>
    <p class="lead revelar">Seven creators, one rule: we only pitch collaborations that make sense for their audience. That is why they work.</p>
{grid_roster(True)}
    <p class="centrado" style="margin-top:34px"><a class="btn btn-naranja" href="/en/creadores">See the full roster</a></p>
  </div>
</section>
<section class="seccion seccion-crema">
  <div class="wrap">
    <h2 class="revelar">What we do</h2>
    <div class="dos-columnas">
      <div class="panel revelar">
        <h3>For brands</h3>
        <ul>
          <li>We match you with the right creator for your audience, market and product</li>
          <li>We design the campaign: integrations, dedicated videos, packs and short formats</li>
          <li>Negotiation, contract and a single point of contact for the whole campaign</li>
          <li>Brand-approved scripts before recording and final reporting with real metrics</li>
        </ul>
        <p style="margin:18px 0 0"><a class="btn" href="/en/marcas">Services for brands</a></p>
      </div>
      <div class="panel panel-ambar revelar">
        <h3>For creators</h3>
        <ul>
          <li>Exclusive commercial representation and full inbox management</li>
          <li>Active brand prospecting on top of the deals that come to you</li>
          <li>Rate negotiation, always prioritising fixed fees</li>
          <li>Scam filtering and a long-term growth strategy</li>
        </ul>
        <p style="margin:18px 0 0"><a class="btn btn-hueso" href="/en/soy-creador">I want representation</a></p>
      </div>
    </div>
  </div>
</section>
<section class="seccion">
  <div class="wrap">
    <h2 class="revelar">Brands that trust us</h2>
    <p class="lead revelar">Over 40 campaigns with hosting, gaming, tech, app and consumer brands across Europe, the Americas and Asia.</p>
    <div class="cinta-marcas">
      <div class="marca-logo revelar"><img src="/img/marcas/supabase.png" alt="Supabase" loading="lazy"><span>Supabase</span></div>
      <div class="marca-logo revelar"><img src="/img/marcas/hostinger.png" alt="Hostinger" loading="lazy"><span>Hostinger</span></div>
      <div class="marca-logo revelar"><img src="/img/marcas/arduino.png" alt="Arduino" loading="lazy"><span>Arduino</span></div>
      <div class="marca-logo revelar"><img src="/img/marcas/hideme.png" alt="hide.me" loading="lazy"><span>hide.me</span></div>
    </div>
  </div>
</section>
{franja_cta(True)}
"""
        html += footer(True)
        escribe("/en/index.html", html)

def pagina_roster(es_en):
    if not es_en:
        html = head("es", "El roster · Creadores representados por CreatorsManager",
                    "Minecraft, Roblox, contenido familiar y salud. Conoce a los 7 creadores hispanohablantes que representamos en exclusiva.",
                    "/creadores", "/en/creadores")
        html += nav(False, "/creadores", "/en/creadores")
        html += f"""<section class="seccion seccion-tinta" style="padding-bottom:60px">
  <div class="wrap">
    <h1>El roster</h1>
    <p class="lead">Cada creador del roster está aquí por su comunidad, no solo por su cifra. Filtra por nicho o mercado y abre su ficha para ver datos, canales y formatos.</p>
  </div>
</section>
<section class="seccion" style="padding-top:44px">
  <div class="wrap">
{filtros_html(False)}
{grid_roster(False)}
    <p style="margin-top:34px; color:var(--gris-texto); font-size:.95rem">Las tarifas no se publican en la web: se facilitan siempre en privado, según formato, fechas y alcance de cada campaña. <a href="/contacto">Pídenos una propuesta</a>.</p>
  </div>
</section>
{franja_cta(False)}
"""
        html += footer(False)
        escribe("/creadores.html", html)
    else:
        html = head("en", "The roster · Creators represented by CreatorsManager",
                    "Minecraft, Roblox, family content and health. Meet the 7 Spanish-speaking creators we exclusively represent.",
                    "/creadores", "/en/creadores", True)
        html += nav(True, "/en/creadores", "/creadores")
        html += f"""<section class="seccion seccion-tinta" style="padding-bottom:60px">
  <div class="wrap">
    <h1>The roster</h1>
    <p class="lead">Every creator on this roster is here for their community, not just their numbers. Filter by niche or market and open a profile for data, channels and formats.</p>
  </div>
</section>
<section class="seccion" style="padding-top:44px">
  <div class="wrap">
{filtros_html(True)}
{grid_roster(True)}
    <p style="margin-top:34px; color:var(--gris-texto); font-size:.95rem">Rates are never published on the site: we share them privately, based on format, dates and the scope of each campaign. <a href="/en/contacto">Request a proposal</a>.</p>
  </div>
</section>
{franja_cta(True)}
"""
        html += footer(True)
        escribe("/en/creadores.html", html)

def pagina_creador(c, es_en):
    pref = "/en" if es_en else ""
    ruta_es = f"/creadores/{c['slug']}"
    ruta_en = f"/en/creadores/{c['slug']}"
    chips = c["chips_en"] if es_en else c["chips_es"]
    datos = c["datos_en"] if es_en else c["datos_es"]
    bio = c["bio_en"] if es_en else c["bio_es"]
    encaje = c["encaje_en"] if es_en else c["encaje_es"]
    etiquetas = "".join(f'<span class="etiqueta" style="background:var(--papel)">{ch}</span>' for ch in chips)
    datos_html = "\n".join(f'        <div class="dato"><b>{b}</b><span>{s}</span></div>' for b, s in datos)
    canales_items = []
    for nombre, url, nota_es, nota_en in c["canales"]:
        nota = nota_en if es_en else nota_es
        if url:
            canales_items.append(f'      <li><a href="{url}" target="_blank" rel="noopener"><span>{nombre}</span><span class="canal-sub">{nota} &#8599;</span></a></li>')
        else:
            canales_items.append(f'      <li><span class="canal-fijo"><span>{nombre}</span><span class="canal-sub">{nota}</span></span></li>')
    canales_html = "\n".join(canales_items)
    if es_en:
        titulo = f"{c['nombre']} · Represented by CreatorsManager"
        desc = f"{c['nombre']}: data, channels and collaboration formats. Work with {c['nombre']} through CreatorsManager."
        t_canales, t_encaje, t_cta, t_volver = "Channels", "A great fit for", f"Work with {c['nombre']}", "Back to the roster"
        t_email = "Direct contact"
        cta_sub = "Tell us about your campaign and we will send a tailored proposal, with no published rates and no commitment."
    else:
        titulo = f"{c['nombre']} · Representado por CreatorsManager"
        desc = f"{c['nombre']}: datos, canales y formatos de colaboración. Trabaja con {c['nombre']} a través de CreatorsManager."
        t_canales, t_encaje, t_cta, t_volver = "Canales", "Encaja especialmente con", f"Quiero trabajar con {c['nombre']}", "Volver al roster"
        t_email = "Contacto directo"
        cta_sub = "Cuéntanos tu campaña y te mandamos una propuesta a medida, sin tarifas públicas y sin compromiso."
    email_html = f'<p style="margin-top:14px; font-size:.95rem">{t_email}: <a href="mailto:{c["email"]}">{c["email"]}</a></p>' if c["email"] else ""
    html = head("en" if es_en else "es", titulo, desc, ruta_es, ruta_en, es_en)
    html += nav(es_en, f"{pref}/creadores", ruta_en if not es_en else ruta_es)
    html += f"""<section class="ficha-hero">
  <div class="wrap ficha-hero-grid">
    <img src="/img/creadores/avatar-{c['slug']}.jpg" alt="{c['nombre']}" width="210" height="210">
    <div>
      <h1>{c['nombre']}</h1>
      <div class="carta-etiquetas" style="justify-content:flex-start">{etiquetas}</div>
      <div class="ficha-datos">
{datos_html}
      </div>
      <a class="btn btn-grande" href="{pref}/contacto?creador={c['slug']}">{t_cta}</a>
    </div>
  </div>
</section>
<section class="seccion">
  <div class="wrap">
    <div class="dos-columnas">
      <div>
{bio}
        <div class="panel panel-crema" style="margin-top:26px; box-shadow:var(--sombra-mini)">
          <h3>{t_encaje}</h3>
          <p style="margin:0">{encaje}</p>
        </div>
      </div>
      <div>
        <h3>{t_canales}</h3>
        <ul class="lista-canales">
{canales_html}
        </ul>
        {email_html}
      </div>
    </div>
  </div>
</section>
<section class="franja-cta">
  <div class="wrap">
    <div>
      <h2>{t_cta}</h2>
      <p style="margin:10px 0 0; max-width:48ch">{cta_sub}</p>
    </div>
    <a class="btn btn-tinta btn-grande" href="{pref}/contacto?creador={c['slug']}">{'Request a proposal' if es_en else 'Pedir propuesta'}</a>
  </div>
</section>
<section class="seccion" style="padding:40px 0">
  <div class="wrap"><a class="btn btn-hueso" href="{pref}/creadores">&larr; {t_volver}</a></div>
</section>
"""
    html += footer(es_en)
    escribe(f"{pref}/creadores/{c['slug']}.html", html)

def pagina_marcas(es_en):
    pref = "/en" if es_en else ""
    if not es_en:
        formatos = [
            ("Pre-roll 60\"", "Integración de un minuto al inicio del vídeo. El formato más eficiente para dar a conocer tu marca al público del creador."),
            ("Pre-roll 90\"", "Minuto y medio para explicar producto, demo y oferta. Ideal cuando el mensaje necesita más contexto."),
            ("Vídeo dedicado", "Un vídeo completo construido alrededor de tu marca, rodado al estilo natural del creador."),
            ("Pack de 3 vídeos", "Campaña por fases: conocimiento de marca, conexión con la audiencia y conversión. Cada vídeo cumple un papel."),
            ("Pack multicanal", "Un mismo mensaje en varios canales del roster a la vez, con una sola negociación y un solo interlocutor."),
            ("Shorts, TikTok y Reels", "Formatos cortos para amplificar la campaña principal o probar mensaje con menos inversión."),
        ]
        proceso = [
            ("Briefing", "Nos cuentas objetivos, producto, mercado y presupuesto. Si escribes en inglés, respondemos en inglés."),
            ("Propuesta", "Seleccionamos creadores y formatos y te enviamos una propuesta a medida con alcance estimado."),
            ("Acuerdo", "Negociamos condiciones y firmamos contrato. Pago directo, sin plataformas intermediarias opacas."),
            ("Producción", "Pasamos el briefing al creador y te enviamos el guion para que lo apruebes antes de grabar."),
            ("Publicación", "Lanzamiento coordinado en las fechas acordadas, con códigos de descuento o enlaces si la campaña los lleva."),
            ("Reporting", "Te entregamos las métricas reales del vídeo y una valoración para plantear las siguientes campañas."),
        ]
        faq = [
            ("¿Cuánto tarda una campaña de principio a fin?", "Depende del calendario del creador, pero lo habitual son de 3 a 6 semanas desde el acuerdo hasta la publicación. Si tienes una fecha de lanzamiento cerrada, dínoslo en el briefing y organizamos el calendario alrededor de ella."),
            ("¿Cómo elegís al creador para mi marca?", "Por encaje real con tu público objetivo, tu mercado y tu producto, no por cifra bruta de suscriptores. Si tu producto no encaja con la audiencia de un creador, te lo decimos y te proponemos alternativas."),
            ("¿Trabajáis con afiliación o solo con fee fijo?", "Priorizamos el fee fijo o modelos híbridos de fijo más comisión. Los códigos de descuento y los enlaces de afiliado funcionan muy bien como complemento de la campaña, no como único modelo de pago."),
            ("¿Qué categorías no aceptáis?", "Cada creador tiene categorías vetadas que respetamos siempre: apuestas, casinos, cripto, alcohol, tabaco, vapeo y contenido para adultos, entre otras. La mayoría del roster es contenido familiar y eso se protege."),
            ("¿Qué mercados cubrís?", "España y toda Latinoamérica, con especial fuerza en México, Argentina, Colombia, Chile y Perú, además de la comunidad hispana de Estados Unidos. Trabajamos con marcas de cualquier país, en castellano o en inglés."),
            ("¿Publicáis tarifas?", "No. Cada campaña se presupuesta según creador, formato, fechas y derechos de uso. Escríbenos con tu briefing y te enviamos la propuesta con precios en privado."),
        ]
        html = head("es", "Para marcas · Campañas de influencer marketing en YouTube · CreatorsManager",
                    "Integraciones, vídeos dedicados y packs multicanal con los grandes creadores hispanohablantes de YouTube. Gestión completa de la campaña.",
                    "/marcas", "/en/marcas")
        html += nav(False, "/marcas", "/en/marcas")
        formatos_html = "\n".join(f'      <div class="formato revelar"><span class="pico">{t}</span><p>{d}</p></div>' for t, d in formatos)
        proceso_html = "\n".join(f'      <li class="paso revelar"><span class="paso-num">{i+1}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(proceso))
        faq_html = "\n".join(f'      <details class="revelar"><summary>{p}</summary><p>{r}</p></details>' for p, r in faq)
        html += f"""<section class="seccion seccion-tinta" style="padding-bottom:60px">
  <div class="wrap">
    <h1>Tu marca, dentro del vídeo</h1>
    <p class="lead">No vendemos menciones: diseñamos integraciones que se adaptan al estilo natural de cada creador. Tú tienes un único interlocutor, apruebas el guion antes de grabar y recibes las métricas reales al final.</p>
    <div class="hero-acciones" style="margin-top:28px">
      <a class="btn btn-grande" href="/contacto">Pedir propuesta</a>
      <a class="btn btn-hueso btn-grande" href="/creadores">Ver el roster</a>
    </div>
  </div>
</section>
<section class="seccion">
  <div class="wrap">
    <h2 class="revelar">Qué hacemos por tu marca</h2>
    <div class="dos-columnas">
      <div class="panel revelar">
        <h3>Gestión completa</h3>
        <ul>
          <li>Selección del creador ideal según público objetivo, mercado y producto</li>
          <li>Diseño de campaña: integraciones, vídeos dedicados, packs multivídeo y multicanal</li>
          <li>Negociación, contratos y coordinación de briefings, guiones y entregas</li>
          <li>Reporting final con métricas reales del vídeo</li>
        </ul>
      </div>
      <div class="panel panel-crema revelar">
        <h3>Complementos que convierten</h3>
        <ul>
          <li>Códigos de descuento propios por creador</li>
          <li>Enlaces de afiliado como refuerzo de la campaña</li>
          <li>Sorteos con la comunidad del creador</li>
          <li>Opciones de paid usage y whitelisting del contenido</li>
        </ul>
      </div>
    </div>
  </div>
</section>
<section class="seccion seccion-crema">
  <div class="wrap">
    <h2 class="revelar">Formatos de colaboración</h2>
    <div class="formatos-grid">
{formatos_html}
    </div>
  </div>
</section>
<section class="seccion">
  <div class="wrap">
    <h2 class="revelar">Cómo trabajamos</h2>
    <p class="lead revelar">Seis pasos, un interlocutor y cero sorpresas.</p>
    <ol class="proceso">
{proceso_html}
    </ol>
  </div>
</section>
<section class="seccion seccion-crema">
  <div class="wrap">
    <h2 class="revelar">Sectores con los que trabajamos</h2>
    <p class="lead revelar">Hosting y servidores de Minecraft, VPN y privacidad, periféricos y gaming gear, sillas gaming, videojuegos y apps móviles, marketplaces de juegos, herramientas de IA y software para creadores, tecnología de consumo, editoriales, y salud y deporte.</p>
  </div>
</section>
<section class="seccion">
  <div class="wrap">
    <h2 class="revelar">Preguntas frecuentes</h2>
    <div class="faq">
{faq_html}
    </div>
  </div>
</section>
{franja_cta(False)}
"""
        html += footer(False)
        escribe("/marcas.html", html)
    else:
        formatos = [
            ("Pre-roll 60\"", "A one-minute integration at the start of the video. The most efficient format to introduce your brand to the creator's audience."),
            ("Pre-roll 90\"", "Ninety seconds to explain product, demo and offer. Ideal when the message needs more context."),
            ("Dedicated video", "A full video built around your brand, shot in the creator's natural style."),
            ("3-video pack", "A phased campaign: awareness, connection and conversion. Each video plays its part."),
            ("Multi-channel pack", "One message across several roster channels at once, with a single negotiation and a single point of contact."),
            ("Shorts, TikTok and Reels", "Short formats to amplify the main campaign or test messaging with a smaller budget."),
        ]
        proceso = [
            ("Briefing", "Tell us your goals, product, market and budget. Write in English and we reply in English."),
            ("Proposal", "We select creators and formats and send a tailored proposal with estimated reach."),
            ("Agreement", "We negotiate terms and sign the contract. Direct payment, no opaque middle platforms."),
            ("Production", "We brief the creator and send you the script for approval before anything is recorded."),
            ("Launch", "Coordinated publication on the agreed dates, with discount codes or links if the campaign includes them."),
            ("Reporting", "You get the video's real metrics and our read on how to approach the next campaigns."),
        ]
        faq = [
            ("How long does a campaign take end to end?", "It depends on the creator's calendar, but 3 to 6 weeks from agreement to publication is typical. If you have a fixed launch date, tell us in the briefing and we build the calendar around it."),
            ("How do you choose the creator for my brand?", "By real fit with your target audience, market and product, not by raw subscriber count. If your product does not fit a creator's audience, we say so and suggest alternatives."),
            ("Do you work on affiliate deals or fixed fees only?", "We prioritise fixed fees or hybrid models of fixed fee plus commission. Discount codes and affiliate links work very well as a complement to the campaign, not as the only payment model."),
            ("Which categories do you not accept?", "Each creator has vetoed categories we always respect: gambling, casinos, crypto, alcohol, tobacco, vaping and adult content, among others. Most of the roster is family content and we protect that."),
            ("Which markets do you cover?", "Spain and all of Latin America, with particular strength in Mexico, Argentina, Colombia, Chile and Peru, plus the Hispanic community in the US. We work with brands from any country, in Spanish or English."),
            ("Do you publish rates?", "No. Every campaign is priced by creator, format, dates and usage rights. Send us your briefing and we will share the proposal with pricing privately."),
        ]
        html = head("en", "For brands · YouTube influencer marketing campaigns · CreatorsManager",
                    "Integrations, dedicated videos and multi-channel packs with the top Spanish-speaking YouTube creators. Full campaign management.",
                    "/marcas", "/en/marcas", True)
        html += nav(True, "/en/marcas", "/marcas")
        formatos_html = "\n".join(f'      <div class="formato revelar"><span class="pico">{t}</span><p>{d}</p></div>' for t, d in formatos)
        proceso_html = "\n".join(f'      <li class="paso revelar"><span class="paso-num">{i+1}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(proceso))
        faq_html = "\n".join(f'      <details class="revelar"><summary>{p}</summary><p>{r}</p></details>' for p, r in faq)
        html += f"""<section class="seccion seccion-tinta" style="padding-bottom:60px">
  <div class="wrap">
    <h1>Your brand, inside the video</h1>
    <p class="lead">We do not sell mentions: we design integrations that adapt to each creator's natural style. You get one point of contact, you approve the script before recording and you receive real metrics at the end.</p>
    <div class="hero-acciones" style="margin-top:28px">
      <a class="btn btn-grande" href="/en/contacto">Request a proposal</a>
      <a class="btn btn-hueso btn-grande" href="/en/creadores">See the roster</a>
    </div>
  </div>
</section>
<section class="seccion">
  <div class="wrap">
    <h2 class="revelar">What we do for your brand</h2>
    <div class="dos-columnas">
      <div class="panel revelar">
        <h3>Full management</h3>
        <ul>
          <li>Creator selection based on your target audience, market and product</li>
          <li>Campaign design: integrations, dedicated videos, multi-video and multi-channel packs</li>
          <li>Negotiation, contracts and coordination of briefings, scripts and deliveries</li>
          <li>Final reporting with the video's real metrics</li>
        </ul>
      </div>
      <div class="panel panel-crema revelar">
        <h3>Extras that convert</h3>
        <ul>
          <li>Dedicated discount codes per creator</li>
          <li>Affiliate links to reinforce the campaign</li>
          <li>Giveaways with the creator's community</li>
          <li>Paid usage and whitelisting options for the content</li>
        </ul>
      </div>
    </div>
  </div>
</section>
<section class="seccion seccion-crema">
  <div class="wrap">
    <h2 class="revelar">Collaboration formats</h2>
    <div class="formatos-grid">
{formatos_html}
    </div>
  </div>
</section>
<section class="seccion">
  <div class="wrap">
    <h2 class="revelar">How we work</h2>
    <p class="lead revelar">Six steps, one point of contact, zero surprises.</p>
    <ol class="proceso">
{proceso_html}
    </ol>
  </div>
</section>
<section class="seccion seccion-crema">
  <div class="wrap">
    <h2 class="revelar">Industries we usually work with</h2>
    <p class="lead revelar">Minecraft hosting and servers, VPN and privacy, peripherals and gaming gear, gaming chairs, video games and mobile apps, game marketplaces, AI tools and creator software, consumer tech, publishers, and health and sport.</p>
  </div>
</section>
<section class="seccion">
  <div class="wrap">
    <h2 class="revelar">Frequently asked questions</h2>
    <div class="faq">
{faq_html}
    </div>
  </div>
</section>
{franja_cta(True)}
"""
        html += footer(True)
        escribe("/en/marcas.html", html)

def pagina_soycreador(es_en):
    if not es_en:
        html = head("es", "Para creadores · Representación exclusiva · CreatorsManager",
                    "Representación comercial para creadores hispanohablantes de YouTube: prospección activa de marcas, negociación, filtro de estafas y estrategia a largo plazo.",
                    "/soy-creador", "/en/soy-creador")
        html += nav(False, "/soy-creador", "/en/soy-creador")
        html += f"""<section class="seccion seccion-tinta" style="padding-bottom:60px">
  <div class="wrap">
    <h1>Tú creas. Nosotros negociamos.</h1>
    <p class="lead">Representación comercial exclusiva para creadores hispanohablantes de YouTube. Nos encargamos de las marcas para que tú te encargues del contenido.</p>
    <div class="hero-acciones" style="margin-top:28px">
      <a class="btn btn-grande" href="/contacto?tipo=creador">Quiero representación</a>
    </div>
  </div>
</section>
<section class="seccion">
  <div class="wrap">
    <h2 class="revelar">Qué hacemos por ti</h2>
    <div class="dos-columnas">
      <div class="panel revelar">
        <h3>Tu bandeja, gestionada</h3>
        <ul>
          <li>Gestionamos todas las propuestas de marcas que te llegan</li>
          <li>Filtramos estafas y ofertas de baja calidad antes de que te roben tiempo</li>
          <li>Negociamos tarifas y condiciones priorizando siempre el fee fijo</li>
          <li>Revisamos contratos y protegemos los derechos de tu contenido</li>
        </ul>
      </div>
      <div class="panel panel-ambar revelar">
        <h3>Y salimos a buscar más</h3>
        <ul>
          <li>Prospección activa: contactamos marcas que encajan con tu audiencia</li>
          <li>Solo propuestas con sentido: tus categorías vetadas se respetan siempre</li>
          <li>Buscamos marcas que repitan, no campañas de una sola vez</li>
          <li>Estrategia de crecimiento y posicionamiento a largo plazo</li>
        </ul>
      </div>
    </div>
  </div>
</section>
<section class="seccion seccion-crema">
  <div class="wrap">
    <h2 class="revelar">Nuestra filosofía</h2>
    <div class="formatos-grid">
      <div class="formato revelar"><span class="pico">Encaje real</span><p>Solo te proponemos colaboraciones que tienen sentido para tu audiencia. Si una marca no encaja, se descarta, por bien que pague.</p></div>
      <div class="formato revelar"><span class="pico">Contenido auténtico</span><p>Las integraciones se adaptan a tu estilo natural. No grabas anuncios forzados: por eso tus patrocinios funcionan y las marcas vuelven.</p></div>
      <div class="formato revelar"><span class="pico">Transparencia</span><p>Contratos claros, pago directo y cuentas claras. Sabes en todo momento qué se ha negociado y en qué condiciones.</p></div>
      <div class="formato revelar"><span class="pico">Largo plazo</span><p>Cuidamos tu marca personal. Una mala colaboración hoy te cierra puertas mañana, y eso no nos lo permitimos.</p></div>
    </div>
  </div>
</section>
<section class="franja-cta">
  <div class="wrap">
    <h2>¿Hablamos de tu canal?</h2>
    <a class="btn btn-tinta btn-grande" href="/contacto?tipo=creador">Enviar mi canal</a>
  </div>
</section>
"""
        html += footer(False)
        escribe("/soy-creador.html", html)
    else:
        html = head("en", "For creators · Exclusive representation · CreatorsManager",
                    "Commercial representation for Spanish-speaking YouTube creators: active brand prospecting, negotiation, scam filtering and long-term strategy.",
                    "/soy-creador", "/en/soy-creador", True)
        html += nav(True, "/en/soy-creador", "/soy-creador")
        html += f"""<section class="seccion seccion-tinta" style="padding-bottom:60px">
  <div class="wrap">
    <h1>You create. We negotiate.</h1>
    <p class="lead">Exclusive commercial representation for Spanish-speaking YouTube creators. We handle the brands so you can handle the content.</p>
    <div class="hero-acciones" style="margin-top:28px">
      <a class="btn btn-grande" href="/en/contacto?tipo=creador">I want representation</a>
    </div>
  </div>
</section>
<section class="seccion">
  <div class="wrap">
    <h2 class="revelar">What we do for you</h2>
    <div class="dos-columnas">
      <div class="panel revelar">
        <h3>Your inbox, managed</h3>
        <ul>
          <li>We manage every brand proposal that reaches you</li>
          <li>We filter scams and low-quality offers before they waste your time</li>
          <li>We negotiate rates and terms, always prioritising fixed fees</li>
          <li>We review contracts and protect the rights to your content</li>
        </ul>
      </div>
      <div class="panel panel-ambar revelar">
        <h3>And we go find more</h3>
        <ul>
          <li>Active prospecting: we reach out to brands that fit your audience</li>
          <li>Only proposals that make sense: your vetoed categories are always respected</li>
          <li>We look for brands that come back, not one-off campaigns</li>
          <li>Long-term growth and positioning strategy</li>
        </ul>
      </div>
    </div>
  </div>
</section>
<section class="seccion seccion-crema">
  <div class="wrap">
    <h2 class="revelar">How we think</h2>
    <div class="formatos-grid">
      <div class="formato revelar"><span class="pico">Real fit</span><p>We only pitch collaborations that make sense for your audience. If a brand does not fit, it is out, however well it pays.</p></div>
      <div class="formato revelar"><span class="pico">Authentic content</span><p>Integrations adapt to your natural style. You never record forced ads: that is why your sponsorships work and brands come back.</p></div>
      <div class="formato revelar"><span class="pico">Transparency</span><p>Clear contracts, direct payment, clear accounting. You always know what was negotiated and on what terms.</p></div>
      <div class="formato revelar"><span class="pico">Long term</span><p>We look after your personal brand. One bad collaboration today closes doors tomorrow, and we do not allow that.</p></div>
    </div>
  </div>
</section>
<section class="franja-cta">
  <div class="wrap">
    <h2>Shall we talk about your channel?</h2>
    <a class="btn btn-tinta btn-grande" href="/en/contacto?tipo=creador">Submit my channel</a>
  </div>
</section>
"""
        html += footer(True)
        escribe("/en/soy-creador.html", html)

def pagina_agencia(es_en):
    if not es_en:
        html = head("es", "Quiénes somos · CreatorsManager, agencia de influencer marketing fundada en 2025",
                    "CreatorsManager, fundada en 2025 por Julen Aldazabal, conecta marcas con los grandes creadores hispanohablantes de YouTube.",
                    "/agencia", "/en/agencia")
        html += nav(False, "/agencia", "/en/agencia")
        html += f"""<section class="seccion seccion-tinta" style="padding-bottom:60px">
  <div class="wrap">
    <h1>Gente del sector, no intermediarios</h1>
    <p class="lead">CreatorsManager se fundó en 2025, con siete años de oficio detrás: su fundador lleva desde 2019 conectando marcas con creadores hispanohablantes de YouTube, campaña a campaña.</p>
  </div>
</section>
<section class="seccion">
  <div class="wrap">
    <div class="dos-columnas">
      <div>
        <h2 class="revelar">La historia</h2>
        <p class="revelar">CreatorsManager se fundó en 2025, pero el oficio viene de antes: Julen lleva desde 2019 gestionando las marcas de creadores de Minecraft. La fórmula siempre ha sido simple: conocer YouTube a fondo, decir que no a lo que no encaja y tratar bien a las dos partes del acuerdo.</p>
        <p class="revelar">Al formalizarse la agencia, esa fórmula no ha cambiado. Ha cambiado la escala: hoy representamos en exclusiva a 7 creadores que suman más de 25 millones de suscriptores, hemos gestionado más de 40 campañas publicitarias y trabajamos a diario con marcas y agencias de Europa, Estados Unidos y Asia, en castellano y en inglés.</p>
        <p class="revelar">Operamos desde Euskadi, España, con la vista puesta en todo el mercado hispanohablante: España, México, Argentina, Colombia, Chile, Perú y la comunidad hispana de Estados Unidos.</p>
      </div>
      <div class="panel panel-crema revelar" style="align-self:start">
        <h3>Julen Aldazabal Punzano</h3>
        <p>Founder e Influencer Marketing Manager. Lleva desde 2019 negociando campañas entre marcas y creadores, y sigue siendo el interlocutor directo de cada cuenta: cuando escribes a CreatorsManager, hablas con quien decide.</p>
        <a class="btn" href="https://www.linkedin.com/in/julen-aldazabal-punzano-8974281bb/" target="_blank" rel="noopener">LinkedIn de Julen</a>
      </div>
    </div>
  </div>
</section>
<section class="seccion seccion-crema">
  <div class="wrap">
    <h2 class="revelar">En qué creemos</h2>
    <div class="formatos-grid">
      <div class="formato revelar"><span class="pico">Encaje real</span><p>Solo proponemos colaboraciones con sentido para la audiencia del creador. Las categorías vetadas de cada creador se respetan siempre.</p></div>
      <div class="formato revelar"><span class="pico">Contenido auténtico</span><p>Las integraciones se adaptan al estilo natural de cada creador, no al revés. Por eso funcionan.</p></div>
      <div class="formato revelar"><span class="pico">Transparencia</span><p>Contratos claros y pago directo, sin plataformas intermediarias opacas.</p></div>
      <div class="formato revelar"><span class="pico">Largo plazo</span><p>Buscamos marcas que repitan y creadores que crezcan. Las campañas de usar y tirar no construyen nada.</p></div>
      <div class="formato revelar"><span class="pico">Un interlocutor</span><p>La marca habla con una sola persona durante toda la campaña, del briefing al reporting.</p></div>
    </div>
  </div>
</section>
{franja_cta(False)}
"""
        html += footer(False)
        escribe("/agencia.html", html)
    else:
        html = head("en", "About us · CreatorsManager, influencer marketing agency founded in 2025",
                    "CreatorsManager, founded in 2025 by Julen Aldazabal, connects brands with the top Spanish-speaking YouTube creators.",
                    "/agencia", "/en/agencia", True)
        html += nav(True, "/en/agencia", "/agencia")
        html += f"""<section class="seccion seccion-tinta" style="padding-bottom:60px">
  <div class="wrap">
    <h1>Industry people, not middlemen</h1>
    <p class="lead">CreatorsManager was founded in 2025, with seven years of craft behind it: its founder has been connecting brands with Spanish-speaking YouTube creators since 2019, campaign by campaign.</p>
  </div>
</section>
<section class="seccion">
  <div class="wrap">
    <div class="dos-columnas">
      <div>
        <h2 class="revelar">The story</h2>
        <p class="revelar">CreatorsManager was founded in 2025, but the craft goes back further: Julen has been managing brand deals for Minecraft creators since 2019. The formula has always been simple: know YouTube inside out, say no to what does not fit, and treat both sides of the deal well.</p>
        <p class="revelar">Formalising the agency changed none of that formula. The scale has changed: today we exclusively represent 7 creators with over 25 million combined subscribers, we have managed more than 40 advertising campaigns, and we work daily with brands and agencies across Europe, the US and Asia, in Spanish and English.</p>
        <p class="revelar">We operate from the Basque Country, Spain, focused on the entire Spanish-speaking market: Spain, Mexico, Argentina, Colombia, Chile, Peru and the Hispanic community in the United States.</p>
      </div>
      <div class="panel panel-crema revelar" style="align-self:start">
        <h3>Julen Aldazabal Punzano</h3>
        <p>Founder and Influencer Marketing Manager. He has been negotiating campaigns between brands and creators since 2019 and remains the direct contact for every account: when you write to CreatorsManager, you talk to the person who decides.</p>
        <a class="btn" href="https://www.linkedin.com/in/julen-aldazabal-punzano-8974281bb/" target="_blank" rel="noopener">Julen on LinkedIn</a>
      </div>
    </div>
  </div>
</section>
<section class="seccion seccion-crema">
  <div class="wrap">
    <h2 class="revelar">What we believe in</h2>
    <div class="formatos-grid">
      <div class="formato revelar"><span class="pico">Real fit</span><p>We only pitch collaborations that make sense for the creator's audience. Each creator's vetoed categories are always respected.</p></div>
      <div class="formato revelar"><span class="pico">Authentic content</span><p>Integrations adapt to each creator's natural style, not the other way round. That is why they work.</p></div>
      <div class="formato revelar"><span class="pico">Transparency</span><p>Clear contracts and direct payment, no opaque middle platforms.</p></div>
      <div class="formato revelar"><span class="pico">Long term</span><p>We look for brands that come back and creators that grow. Throwaway campaigns build nothing.</p></div>
      <div class="formato revelar"><span class="pico">One contact</span><p>The brand talks to one person through the whole campaign, from briefing to reporting.</p></div>
    </div>
  </div>
</section>
{franja_cta(True)}
"""
        html += footer(True)
        escribe("/en/agencia.html", html)

def pagina_contacto(es_en):
    checks = "\n".join(
        f'            <label><input type="checkbox" name="creadores[]" value="{c["slug"]}"> {c["nombre"]}</label>'
        for c in CREADORES
    )
    if not es_en:
        html = head("es", "Contacto · CreatorsManager",
                    "Cuéntanos tu campaña o preséntanos tu canal. Respondemos en menos de 24 horas laborables, en castellano o en inglés.",
                    "/contacto", "/en/contacto")
        html += nav(False, "/contacto", "/en/contacto")
        html += f"""<section class="seccion seccion-tinta" style="padding-bottom:60px">
  <div class="wrap">
    <h1>Hablemos</h1>
    <p class="lead">Respondemos en menos de 24 horas laborables, en castellano o en inglés. Si lo prefieres, escríbenos directamente a <a href="mailto:contacto@creatorsmanager.es" style="color:var(--ambar)">contacto@creatorsmanager.es</a>.</p>
  </div>
</section>
<section class="seccion" style="padding-top:50px">
  <div class="wrap">
    <div class="form-tabs">
      <button class="form-tab activo" data-panel="panel-marca">Soy una marca</button>
      <button class="form-tab" data-panel="panel-creador">Soy creador</button>
    </div>
    <div class="form-panel" id="panel-marca">
      <form class="form-w3" novalidate>
        <input type="hidden" name="subject" value="Web · Nueva solicitud de MARCA">
        <input type="hidden" name="from_name" value="Web CreatorsManager">
        <input type="checkbox" name="botcheck" class="hpot" tabindex="-1" autocomplete="off">
        <div class="campos">
          <div><label for="m-nombre">Nombre y apellidos</label><input id="m-nombre" name="nombre" required autocomplete="name"></div>
          <div><label for="m-empresa">Empresa</label><input id="m-empresa" name="empresa" required autocomplete="organization"></div>
          <div><label for="m-email">Email</label><input id="m-email" type="email" name="email" required autocomplete="email"></div>
          <div><label for="m-web">Web de la empresa</label><input id="m-web" type="url" name="web" placeholder="https://" autocomplete="url"></div>
          <div><label for="m-pais">País</label><input id="m-pais" name="pais" autocomplete="country-name"></div>
          <div>
            <label for="m-formato">Formato que te interesa</label>
            <select id="m-formato" name="formato">
              <option>Aún no lo sé</option>
              <option>Pre-roll 60"</option>
              <option>Pre-roll 90"</option>
              <option>Vídeo dedicado</option>
              <option>Pack de 3 vídeos</option>
              <option>Pack multicanal</option>
              <option>Shorts / TikTok / Reels</option>
            </select>
          </div>
          <div class="campo-ancho">
            <fieldset>
              <legend>Creadores que te interesan</legend>
              <div class="check-grid">
{checks}
              </div>
            </fieldset>
          </div>
          <div>
            <label for="m-presupuesto">Presupuesto aproximado</label>
            <select id="m-presupuesto" name="presupuesto">
              <option>Prefiero hablarlo</option>
              <option>Menos de 3.000 &euro;</option>
              <option>3.000 - 10.000 &euro;</option>
              <option>10.000 - 25.000 &euro;</option>
              <option>Más de 25.000 &euro;</option>
            </select>
          </div>
          <div><label for="m-fechas">Fechas de campaña previstas</label><input id="m-fechas" name="fechas" placeholder="Ej.: segunda quincena de noviembre"></div>
          <div class="campo-ancho"><label for="m-mensaje">Cuéntanos la campaña</label><textarea id="m-mensaje" name="mensaje" required placeholder="Producto, objetivo, mercado y todo lo que nos ayude a prepararte la propuesta"></textarea></div>
          <div class="campo-ancho">
            <label class="consentimiento"><input type="checkbox" required> He leído y acepto la <a href="/privacidad">política de privacidad</a>.</label>
          </div>
        </div>
        <p style="margin:22px 0 0"><button type="submit" class="btn btn-grande">Pedir propuesta</button></p>
        <p class="form-estado" role="status"></p>
      </form>
    </div>
    <div class="form-panel" id="panel-creador" hidden>
      <form class="form-w3" novalidate>
        <input type="hidden" name="subject" value="Web · Nueva solicitud de CREADOR">
        <input type="hidden" name="from_name" value="Web CreatorsManager">
        <input type="checkbox" name="botcheck" class="hpot" tabindex="-1" autocomplete="off">
        <div class="campos">
          <div><label for="c-nombre">Nombre</label><input id="c-nombre" name="nombre" required autocomplete="name"></div>
          <div><label for="c-email">Email</label><input id="c-email" type="email" name="email" required autocomplete="email"></div>
          <div><label for="c-canal">Canal de YouTube</label><input id="c-canal" type="url" name="canal" required placeholder="https://www.youtube.com/@tucanal"></div>
          <div><label for="c-subs">Suscriptores</label><input id="c-subs" name="suscriptores" placeholder="Ej.: 350.000"></div>
          <div><label for="c-nicho">Nicho</label><input id="c-nicho" name="nicho" placeholder="Ej.: Minecraft, Roblox, fitness..."></div>
          <div><label for="c-redes">Otras redes</label><input id="c-redes" name="otras_redes" placeholder="TikTok, Instagram, Twitch..."></div>
          <div class="campo-ancho"><label for="c-mensaje">Cuéntanos sobre tu canal</label><textarea id="c-mensaje" name="mensaje" required placeholder="Tu contenido, tu audiencia y qué buscas en una agencia"></textarea></div>
          <div class="campo-ancho">
            <label class="consentimiento"><input type="checkbox" required> He leído y acepto la <a href="/privacidad">política de privacidad</a>.</label>
          </div>
        </div>
        <p style="margin:22px 0 0"><button type="submit" class="btn btn-grande">Enviar mi canal</button></p>
        <p class="form-estado" role="status"></p>
      </form>
    </div>
  </div>
</section>
"""
        html += footer(False)
        escribe("/contacto.html", html)
    else:
        html = head("en", "Contact · CreatorsManager",
                    "Tell us about your campaign or introduce your channel. We reply within 24 business hours, in Spanish or English.",
                    "/contacto", "/en/contacto", True)
        html += nav(True, "/en/contacto", "/contacto")
        html += f"""<section class="seccion seccion-tinta" style="padding-bottom:60px">
  <div class="wrap">
    <h1>Let's talk</h1>
    <p class="lead">We reply within 24 business hours, in Spanish or English. You can also email us directly at <a href="mailto:contacto@creatorsmanager.es" style="color:var(--ambar)">contacto@creatorsmanager.es</a>.</p>
  </div>
</section>
<section class="seccion" style="padding-top:50px">
  <div class="wrap">
    <div class="form-tabs">
      <button class="form-tab activo" data-panel="panel-marca">I'm a brand</button>
      <button class="form-tab" data-panel="panel-creador">I'm a creator</button>
    </div>
    <div class="form-panel" id="panel-marca">
      <form class="form-w3" novalidate>
        <input type="hidden" name="subject" value="Web · New BRAND request (EN)">
        <input type="hidden" name="from_name" value="CreatorsManager Website">
        <input type="checkbox" name="botcheck" class="hpot" tabindex="-1" autocomplete="off">
        <div class="campos">
          <div><label for="m-nombre">Full name</label><input id="m-nombre" name="nombre" required autocomplete="name"></div>
          <div><label for="m-empresa">Company</label><input id="m-empresa" name="empresa" required autocomplete="organization"></div>
          <div><label for="m-email">Email</label><input id="m-email" type="email" name="email" required autocomplete="email"></div>
          <div><label for="m-web">Company website</label><input id="m-web" type="url" name="web" placeholder="https://" autocomplete="url"></div>
          <div><label for="m-pais">Country</label><input id="m-pais" name="pais" autocomplete="country-name"></div>
          <div>
            <label for="m-formato">Format you are interested in</label>
            <select id="m-formato" name="formato">
              <option>Not sure yet</option>
              <option>Pre-roll 60"</option>
              <option>Pre-roll 90"</option>
              <option>Dedicated video</option>
              <option>3-video pack</option>
              <option>Multi-channel pack</option>
              <option>Shorts / TikTok / Reels</option>
            </select>
          </div>
          <div class="campo-ancho">
            <fieldset>
              <legend>Creators you are interested in</legend>
              <div class="check-grid">
{checks}
              </div>
            </fieldset>
          </div>
          <div>
            <label for="m-presupuesto">Approximate budget</label>
            <select id="m-presupuesto" name="presupuesto">
              <option>I'd rather discuss it</option>
              <option>Under &euro;3,000</option>
              <option>&euro;3,000 - &euro;10,000</option>
              <option>&euro;10,000 - &euro;25,000</option>
              <option>Over &euro;25,000</option>
            </select>
          </div>
          <div><label for="m-fechas">Planned campaign dates</label><input id="m-fechas" name="fechas" placeholder="E.g.: second half of November"></div>
          <div class="campo-ancho"><label for="m-mensaje">Tell us about the campaign</label><textarea id="m-mensaje" name="mensaje" required placeholder="Product, goal, market and anything that helps us prepare your proposal"></textarea></div>
          <div class="campo-ancho">
            <label class="consentimiento"><input type="checkbox" required> I have read and accept the <a href="/privacidad">privacy policy</a> (Spanish).</label>
          </div>
        </div>
        <p style="margin:22px 0 0"><button type="submit" class="btn btn-grande">Request a proposal</button></p>
        <p class="form-estado" role="status"></p>
      </form>
    </div>
    <div class="form-panel" id="panel-creador" hidden>
      <form class="form-w3" novalidate>
        <input type="hidden" name="subject" value="Web · New CREATOR request (EN)">
        <input type="hidden" name="from_name" value="CreatorsManager Website">
        <input type="checkbox" name="botcheck" class="hpot" tabindex="-1" autocomplete="off">
        <div class="campos">
          <div><label for="c-nombre">Name</label><input id="c-nombre" name="nombre" required autocomplete="name"></div>
          <div><label for="c-email">Email</label><input id="c-email" type="email" name="email" required autocomplete="email"></div>
          <div><label for="c-canal">YouTube channel</label><input id="c-canal" type="url" name="canal" required placeholder="https://www.youtube.com/@yourchannel"></div>
          <div><label for="c-subs">Subscribers</label><input id="c-subs" name="suscriptores" placeholder="E.g.: 350,000"></div>
          <div><label for="c-nicho">Niche</label><input id="c-nicho" name="nicho" placeholder="E.g.: Minecraft, Roblox, fitness..."></div>
          <div><label for="c-redes">Other platforms</label><input id="c-redes" name="otras_redes" placeholder="TikTok, Instagram, Twitch..."></div>
          <div class="campo-ancho"><label for="c-mensaje">Tell us about your channel</label><textarea id="c-mensaje" name="mensaje" required placeholder="Your content, your audience and what you expect from an agency"></textarea></div>
          <div class="campo-ancho">
            <label class="consentimiento"><input type="checkbox" required> I have read and accept the <a href="/privacidad">privacy policy</a> (Spanish).</label>
          </div>
        </div>
        <p style="margin:22px 0 0"><button type="submit" class="btn btn-grande">Submit my channel</button></p>
        <p class="form-estado" role="status"></p>
      </form>
    </div>
  </div>
</section>
"""
        html += footer(True)
        escribe("/en/contacto.html", html)

# ------------------------- Legales (ES) -------------------------

def pagina_legal(archivo, titulo, cuerpo):
    html = head("es", f"{titulo} · CreatorsManager", f"{titulo} de creatorsmanager.es.", f"/{archivo}", f"/{archivo}")
    html += nav(False, "", "/en/")
    html += f'<main class="legal">\n<h1>{titulo}</h1>\n{cuerpo}\n</main>\n'
    html += footer(False)
    escribe(f"/{archivo}.html", html)

LEGAL_AVISO = """
<p>Última revisión: octubre de 2026.</p>
<h2>Titular del sitio</h2>
<p>En cumplimiento de la Ley 34/2002, de Servicios de la Sociedad de la Información y de Comercio Electrónico (LSSI-CE), se informa de que el titular de este sitio web es:</p>
<ul>
<li>Titular: Julen Aldazabal Punzano (CreatorsManager)</li>
<li>NIF: 46373756Y</li>
<li>Domicilio: Calle Askatasun 3, 48200 Durango (Bizkaia), España</li>
<li>Email de contacto: contacto@creatorsmanager.es</li>
</ul>
<h2>Objeto</h2>
<p>Este sitio web tiene por objeto dar a conocer los servicios de representación de creadores de contenido y de gestión de campañas de influencer marketing prestados por CreatorsManager, así como facilitar el contacto entre el titular, las marcas interesadas y los creadores.</p>
<h2>Condiciones de uso</h2>
<p>El acceso a este sitio web es gratuito y atribuye la condición de usuario, que implica la aceptación de estas condiciones. El usuario se compromete a hacer un uso adecuado de los contenidos y a no emplearlos para actividades ilícitas o contrarias a la buena fe.</p>
<h2>Propiedad intelectual</h2>
<p>Los contenidos propios de este sitio (textos, diseño y logotipo de CreatorsManager) son titularidad de su propietario. Los nombres, avatares y marcas de los creadores representados y de terceros pertenecen a sus respectivos titulares y se muestran con fines informativos de la relación de representación.</p>
<h2>Responsabilidad</h2>
<p>El titular no se hace responsable del mal uso que se realice de los contenidos de este sitio ni de los contenidos de los sitios externos enlazados, incluidos los canales de YouTube y redes sociales de los creadores.</p>
<h2>Legislación aplicable</h2>
<p>La relación entre el titular y el usuario se regirá por la normativa española vigente. Cualquier controversia se someterá a los juzgados y tribunales que correspondan conforme a derecho.</p>
"""

LEGAL_PRIVACIDAD = """
<p>Última revisión: octubre de 2026.</p>
<h2>Responsable del tratamiento</h2>
<p>Julen Aldazabal Punzano (CreatorsManager), NIF 46373756Y, con domicilio en Calle Askatasun 3, 48200 Durango (Bizkaia), España, y email de contacto contacto@creatorsmanager.es.</p>
<h2>Qué datos tratamos y con qué finalidad</h2>
<p>A través de los formularios de este sitio web recogemos únicamente los datos que el usuario facilita (nombre, email, empresa, canal y el contenido de su mensaje) con la finalidad de atender su solicitud: preparar propuestas de campaña para marcas o valorar solicitudes de representación de creadores, y mantener la comunicación posterior relacionada con esa solicitud.</p>
<h2>Legitimación</h2>
<p>La base legal del tratamiento es el consentimiento del interesado, prestado al marcar la casilla de aceptación y enviar el formulario (art. 6.1.a RGPD), y la aplicación de medidas precontractuales a petición del interesado (art. 6.1.b RGPD).</p>
<h2>Destinatarios</h2>
<p>Los datos de los formularios se envían a nuestro buzón de correo a través del proveedor Web3Forms, que actúa como encargado del tratamiento para el envío del mensaje. No se ceden datos a terceros salvo obligación legal. Si una solicitud de marca se refiere a un creador concreto, los datos de contacto necesarios podrán compartirse con ese creador para valorar la colaboración.</p>
<h2>Conservación</h2>
<p>Los datos se conservarán mientras dure la relación derivada de la solicitud y, después, durante los plazos necesarios para atender posibles responsabilidades legales.</p>
<h2>Derechos</h2>
<p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo a contacto@creatorsmanager.es. También puedes reclamar ante la Agencia Española de Protección de Datos (aepd.es).</p>
"""

LEGAL_COOKIES = """
<p>Última revisión: octubre de 2026.</p>
<h2>Qué cookies usa este sitio</h2>
<p>Este sitio web utiliza únicamente almacenamiento técnico del navegador para recordar tu elección en el aviso de cookies (clave local "cm-cookies"). No instalamos cookies de análisis, publicidad ni seguimiento de terceros.</p>
<h2>Cookies de terceros</h2>
<p>Las tipografías se cargan desde Google Fonts, que puede registrar la dirección IP necesaria para servir los archivos. Los enlaces a YouTube, TikTok, Instagram y LinkedIn abren en sus respectivos sitios, con sus propias políticas de cookies.</p>
<h2>Cómo gestionar las cookies</h2>
<p>Puedes borrar el almacenamiento local y las cookies desde la configuración de tu navegador en cualquier momento. Si en el futuro incorporamos herramientas de analítica, esta política se actualizará y se pedirá consentimiento previo.</p>
"""

# ------------------------- sitemap / robots -------------------------

def sitemap():
    rutas = ["/", "/creadores", "/marcas", "/soy-creador", "/agencia", "/contacto",
             "/aviso-legal", "/privacidad", "/cookies",
             "/en/", "/en/creadores", "/en/marcas", "/en/soy-creador", "/en/agencia", "/en/contacto"]
    rutas += [f"/creadores/{c['slug']}" for c in CREADORES]
    rutas += [f"/en/creadores/{c['slug']}" for c in CREADORES]
    urls = "\n".join(f"  <url><loc>{DOMINIO}{r}</loc></url>" for r in rutas)
    escribe("/sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    escribe("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMINIO}/sitemap.xml\n")

# ==================================================================
if __name__ == "__main__":
    for es_en in (False, True):
        pagina_inicio(es_en)
        pagina_roster(es_en)
        for c in CREADORES:
            pagina_creador(c, es_en)
        pagina_marcas(es_en)
        pagina_soycreador(es_en)
        pagina_agencia(es_en)
        pagina_contacto(es_en)
    pagina_legal("aviso-legal", "Aviso legal", LEGAL_AVISO)
    pagina_legal("privacidad", "Política de privacidad", LEGAL_PRIVACIDAD)
    pagina_legal("cookies", "Política de cookies", LEGAL_COOKIES)
    sitemap()
    print("\nWeb generada.")
