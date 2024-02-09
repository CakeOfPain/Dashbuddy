var slider = document.getElementById("background-blur");
// var output = document.getElementById("blur");
// output.innerHTML = "Background Blur: " + slider.value + "px"; // Display the default slider value


const widgetContainer = document.getElementById('widget-container');
async function loadWidgets() {
    const response = await fetch("/api/widgets");
    const responseJson =  await response.json();

    widgetContainer.innerHTML = responseJson.map(row => {
        return `<div class="widget-container-row" style="height: ${row.height * 10}em">` + row.widgets.map(column => {
            if(column.plugin === "blank") {
                return '<div></div>';
            }
            const params = Object.keys(column.params).map(key => encodeURI(key) + "=" + encodeURI(column.params[key])).join("&")
            return `<iframe class="widget" src="/plugin/${column.plugin}?${params}"></iframe>`
        }).join("") + "</div>";
    }).join("");
}
loadWidgets();

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function () {
    output.innerHTML = "Background Blur: " + this.value + "px";
    document.documentElement.style.setProperty("--blur-strength", this.value + "px");
}

// Set Accent Color
function setAccentColor(color) {
    document.documentElement.style.setProperty("--accent-color", '#' + color);
}
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
var widgetLibrary = document.getElementById("widgetLibrary");
function toggleWidgetMenu() {
    if (widgetLibrary.style.display === "none") {
        window.location.href="edit";
    } else {
        widgetLibrary.style.display = "none";
    }
}