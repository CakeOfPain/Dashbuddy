const widgetContainer = document.getElementById('widget-container');
async function loadWidgets() {
    const responseWidget = await fetch("/api/widgets");
    const responseWidgetJson = await responseWidget.json();

    const responsePlugins = await fetch("/api/plugins");
    const responsePluginsJson = await responsePlugins.json();

    widgetContainer.innerHTML = responseWidgetJson.map((row, y) => {
        return `<div class="widget-container-row" style="height: ${row.height * 10}em">` + row.widgets.map((column, x) => {
            const options =
                (responseWidgetJson.length > 1 || row.length > 1 ? `<option value="delete">Delete Widget</option>` : "") +
                `<option value="new-row">Append New Row</option>` +
                `<option value="new-column">Split Widget</option>` +
                `<option value="increase-height">Increase Row Height</option>` +
                `<option value="decrease-height">Decrease Row Height</option>` +
                `<option value="blank" ${column.plugin === "blank" ? "selected" : ""}>blank widget</option>` +
                responsePluginsJson.map(plugin => `<option value="${plugin.name}" ${plugin.name === column.plugin ? "selected" : ""}> ${plugin.name} - ${plugin.description}</option>`).join("");

            const pluginDescription = responsePluginsJson.filter(x => x.name === column.plugin)?.[0];

            const parameters = (pluginDescription?.params ?? []).map(param => {
                return `<div>${param}:<input onchange="editParam(${y}, ${x}, '${param}')" id="param${y}x${x}-${param}" value="${column.params?.[param] ?? ""}"></div>`;
            }).join("")

            return `<div class="widget">` +
                `<select id="widget${y}x${x}" onchange="alterWidget(${y}, ${x})">>${options}</select>` +
                parameters +
                `</div>`
        }).join("") + "</div>";
    }).join("");
}

async function alterWidget(y, x) {
    const widgetElement = document.getElementById(`widget${y}x${x}`);
    const selected = widgetElement.value;

    const widgets = await fetch("/api/widgets");
    const widgetsJson = await widgets.json();

    if (selected === "delete") {
        widgetsJson[y].widgets.splice(x, 1);
        if (widgetsJson[y].widgets.length < 1) {
            widgetsJson.splice(y, 1);
        }
    } else if (selected === "new-column") {
        widgetsJson[y].widgets.splice(x, 0, { plugin: "blank" });
    } else if (selected === "new-row") {
        widgetsJson.splice(y + 1, 0, { height: 1, widgets: [{ plugin: "blank" }] });
    } else if (selected === "increase-height") {
        widgetsJson[y].height *= 2;
    } else if (selected === "decrease-height") {
        widgetsJson[y].height *= 0.5;
    } else {
        widgetsJson[y].widgets[x].plugin = selected;
        widgetsJson[y].widgets[x].params = {};
    }

    await fetch("/api/widgets", { method: "POST", body: JSON.stringify(widgetsJson) })
    await loadWidgets();
}

async function editParam(y, x, param) {
    const paramInput = document.getElementById(`param${y}x${x}-${param}`);

    const widgets = await fetch("/api/widgets");
    const widgetsJson = await widgets.json();

    widgetsJson[y].widgets[x].params[param] = paramInput.value;

    await fetch("/api/widgets", { method: "POST", body: JSON.stringify(widgetsJson) })
    await loadWidgets();
}

loadWidgets();