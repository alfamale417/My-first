document.addEventListener("DOMContentLoaded", () => {
  const yearEl = document.getElementById("year");
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  const form = document.getElementById("contactForm");
  const note = document.getElementById("formNote");

  if (form && note) {
    form.addEventListener("submit", (event) => {
      event.preventDefault();

      const formData = new FormData(form);
      const name = (formData.get("name") || "there").toString().trim();
      const email = (formData.get("email") || "").toString().trim();

      if (!email) {
        note.textContent = "Please enter a valid email address.";
        note.style.color = "#fbbf24";
        return;
      }

      note.textContent = `Thanks, ${name}! Your request has been recorded. Connect with your audience and start monetizing.`;
      note.style.color = "#34d399";
      form.reset();
    });
  }
});
