/* CreatorsManager · site.js */

/* ============================================================
   FORMULARIOS → GOOGLE APPS SCRIPT
   Los formularios envían los datos a un web app de Apps Script
   que los vuelca en la hoja de Google de CreatorsManager.
   Pega aquí abajo la URL de despliegue (termina en /exec).
   ============================================================ */
const APPS_SCRIPT_URL = "PON_AQUI_LA_URL_DEL_WEB_APP";

const LANG = document.documentElement.lang === "en" ? "en" : "es";
const TXT = {
  es: {
    enviando: "Enviando...",
    ok: "Recibido. Te contestamos en menos de 24 h laborables.",
    error: "No se ha podido enviar. Escríbenos a contacto@creatorsmanager.es",
    sinClave: "El formulario aún no está activado. Escríbenos a contacto@creatorsmanager.es"
  },
  en: {
    enviando: "Sending...",
    ok: "Got it. We reply within 24 business hours.",
    error: "Something went wrong. Email us at contacto@creatorsmanager.es",
    sinClave: "This form is not active yet. Email us at contacto@creatorsmanager.es"
  }
}[LANG];

/* ---------- Menú móvil ---------- */
const burger = document.querySelector(".nav-burger");
const links = document.querySelector(".nav-links");
if (burger && links) {
  burger.addEventListener("click", () => {
    const abierto = links.classList.toggle("abierto");
    burger.setAttribute("aria-expanded", abierto ? "true" : "false");
  });
}

/* ---------- Entrada orquestada del hero ---------- */
const hero = document.querySelector(".hero");
if (hero) requestAnimationFrame(() => hero.classList.add("listo"));

/* ---------- Revelado sobrio al hacer scroll ---------- */
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const revelables = document.querySelectorAll(".revelar");
if (revelables.length && !reduceMotion && "IntersectionObserver" in window) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add("visto"); io.unobserve(e.target); }
    });
  }, { threshold: 0.15 });
  revelables.forEach((el) => io.observe(el));
} else {
  revelables.forEach((el) => el.classList.add("visto"));
}

/* ---------- Contadores del marcador ---------- */
function animaContador(el) {
  const fin = parseFloat(el.dataset.fin);
  const decimales = el.dataset.fin.includes(".") ? 1 : 0;
  const prefijo = el.dataset.prefijo || "";
  const sufijo = el.dataset.sufijo || "";
  const dur = 1400;
  const t0 = performance.now();
  function tick(t) {
    const p = Math.min((t - t0) / dur, 1);
    const suave = 1 - Math.pow(1 - p, 3);
    el.textContent = prefijo + (fin * suave).toFixed(decimales).replace(".", ",") + sufijo;
    if (p < 1) requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
}
const contadores = document.querySelectorAll("[data-fin]");
if (contadores.length) {
  if (reduceMotion || !("IntersectionObserver" in window)) {
    contadores.forEach((el) => {
      el.textContent = (el.dataset.prefijo || "") + el.dataset.fin.replace(".", ",") + (el.dataset.sufijo || "");
    });
  } else {
    const ioC = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) { animaContador(e.target); ioC.unobserve(e.target); }
      });
    }, { threshold: 0.4 });
    contadores.forEach((el) => ioC.observe(el));
  }
}

/* ---------- Filtros del roster ---------- */
const filtros = document.querySelectorAll(".filtro");
const cartas = document.querySelectorAll(".carta[data-tags]");
filtros.forEach((btn) => {
  btn.addEventListener("click", () => {
    filtros.forEach((b) => b.classList.remove("activo"));
    btn.classList.add("activo");
    const f = btn.dataset.filtro;
    cartas.forEach((c) => {
      const tags = c.dataset.tags.split(",");
      c.style.display = (f === "todos" || tags.includes(f)) ? "" : "none";
    });
  });
});

/* ---------- Pestañas de formulario ---------- */
const tabs = document.querySelectorAll(".form-tab");
tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    tabs.forEach((t) => t.classList.remove("activo"));
    tab.classList.add("activo");
    document.querySelectorAll(".form-panel").forEach((p) => (p.hidden = true));
    const panel = document.getElementById(tab.dataset.panel);
    if (panel) panel.hidden = false;
  });
});

/* Preselección de creador vía ?creador= / ?creator= y apertura de la pestaña de marcas */
const params = new URLSearchParams(location.search);
const pre = params.get("creador") || params.get("creator");
if (pre) {
  const casilla = document.querySelector('input[name="creadores[]"][value="' + pre + '"]');
  if (casilla) casilla.checked = true;
  const tabMarca = document.querySelector('.form-tab[data-panel="panel-marca"]');
  if (tabMarca) tabMarca.click();
}
if (params.get("tipo") === "creador" || params.get("type") === "creator") {
  const tabCreador = document.querySelector('.form-tab[data-panel="panel-creador"]');
  if (tabCreador) tabCreador.click();
}

/* ---------- Envío a Google Apps Script ---------- */
const CARGA_PAGINA = Date.now();
document.querySelectorAll("form.form-w3").forEach((form) => {
  form.addEventListener("submit", async (ev) => {
    ev.preventDefault();
    const estado = form.querySelector(".form-estado");
    const botin = form.querySelector('button[type="submit"]');
    estado.className = "form-estado";
    /* Anti-spam: honeypot (solo un bot marcaría la casilla oculta) */
    if (form.querySelector('input[name="botcheck"]').checked) return;
    /* Anti-spam: nadie rellena el formulario en menos de 3 segundos */
    if (Date.now() - CARGA_PAGINA < 3000) return;
    if (!form.reportValidity()) return; /* validación nativa: campos obligatorios y formato email/url */
    if (APPS_SCRIPT_URL.startsWith("PON_AQUI")) {
      estado.textContent = TXT.sinClave;
      estado.classList.add("error");
      return;
    }
    const original = botin.textContent;
    botin.textContent = TXT.enviando;
    botin.disabled = true;
    const datos = new FormData(form);
    datos.append("pagina", location.pathname);
    datos.append("idioma", LANG);
    try {
      /* Apps Script no envía cabeceras CORS: no-cors deja pasar el POST
         (llega y se registra) aunque no podamos leer la respuesta. */
      await fetch(APPS_SCRIPT_URL, { method: "POST", mode: "no-cors", body: datos });
      estado.textContent = TXT.ok;
      estado.classList.add("ok");
      form.reset();
    } catch (e) {
      estado.textContent = TXT.error;
      estado.classList.add("error");
    }
    botin.textContent = original;
    botin.disabled = false;
  });
});

/* ---------- Banner de cookies ---------- */
const banner = document.querySelector(".cookies");
if (banner) {
  let eleccion = null;
  try { eleccion = localStorage.getItem("cm-cookies"); } catch (e) {}
  if (!eleccion) banner.classList.add("visible");
  banner.querySelectorAll("[data-cookies]").forEach((btn) => {
    btn.addEventListener("click", () => {
      try { localStorage.setItem("cm-cookies", btn.dataset.cookies); } catch (e) {}
      banner.classList.remove("visible");
    });
  });
}

/* ---------- Revelados escalonados (hermanos .revelar) ---------- */
if (!reduceMotion) {
  document.querySelectorAll(".revelar").forEach((el) => {
    const hermanos = Array.from(el.parentElement.children).filter((h) => h.classList.contains("revelar"));
    const i = hermanos.indexOf(el);
    if (i > 0) el.style.transitionDelay = Math.min(i * 70, 350) + "ms";
  });
}

/* ---------- Parallax suave del plantel del hero ---------- */
const plantel = document.querySelector(".plantel");
if (hero && plantel && !reduceMotion) {
  let pendiente = false;
  const aplica = () => {
    plantel.style.setProperty("--par", (window.scrollY * -0.08).toFixed(1) + "px");
    pendiente = false;
  };
  window.addEventListener("scroll", () => {
    if (!pendiente) { pendiente = true; requestAnimationFrame(aplica); }
  }, { passive: true });
}
