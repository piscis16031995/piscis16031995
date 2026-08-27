const yearEl = document.getElementById("anio");
if (yearEl) {
  yearEl.textContent = String(new Date().getFullYear());
}

const startBtn = document.getElementById("empezar");
const message = document.getElementById("mensaje");

startBtn?.addEventListener("click", () => {
  if (!message) return;
  message.textContent = "¡Entorno funcionando! Listo para aprender diseño web.";
});
