

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