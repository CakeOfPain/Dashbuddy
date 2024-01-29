var slider = document.getElementById("background-blur");
var output = document.getElementById("blur");
output.innerHTML = "Background Blur: " + slider.value + "px"; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
    output.innerHTML = "Background Blur: " + this.value + "px";
    document.documentElement.style.setProperty("--blur-strength", this.value + "px");
}

// Set Accent Color
function setAccentColor(color) {
    document.documentElement.style.setProperty("--accent-color", color);
}

function toggleSettingsMenu() {
    var x = document.getElementById("settingsMenu");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function toggleWidgetMenu() {
    var x = document.getElementById("widgetLibrary");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}