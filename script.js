document.addEventListener("DOMContentLoaded", function() {
const skipLink = document.querySelector(".skip-link");
if (skipLink) {
skipLink.addEventListener("click", function(e) {
e.preventDefault();
const mainContent = document.getElementById("main");
if (mainContent) {
mainContent.setAttribute("tabindex", "-1");
mainContent.focus();
}
});
}
const buttons = document.querySelectorAll("button");
buttons.forEach(function(button) {
button.addEventListener("keydown", function(e) {
if (e.key === "Enter" || e.key === " ") {
e.preventDefault();
button.click();
}
});
});
const inputs = document.querySelectorAll("input");
inputs.forEach(function(input) {
input.setAttribute("aria-describedby", "help-" + input.id);
});
});
