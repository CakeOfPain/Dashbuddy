// Settings menu
var settingsMenu = document.getElementById("settingsMenu");
function toggleSettingsMenu() {
    if (settingsMenu.style.display === "none") {
        settingsMenu.style.display = "block";
    } else {
        settingsMenu.style.display = "none";
    }
}
// Problem: Settings und Library sind beide beim Start offen und werden übereinander ausgegeben: sehr unschön
// Teilweise: Error 304, main.css Kommunikationsproblem mit Browser(Edge)
// Änderung: Anstelle des Öffnens der Library, soll bei Click die URL zur ".../edit" geändert werden (Bearbeitungsmodus für die Widgets)
// Code-Änderung: widgetLibrary.style.display="block" zu window.location.href="edit"
function toggleToEditMode() {
    window.location.href="edit";
}
function toggleToDashboardMode() {
    window.location.href = "/";
}

function setBackground(url) {
    document.body.style.backgroundImage = `url(${url})`;
}