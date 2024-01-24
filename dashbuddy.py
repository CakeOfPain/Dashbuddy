from flask import Flask, render_template
import plugins.framework as Widget
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    Widget.load()
    widgetView = '<div><h1>widgetView</h1></div>'
    return render_template('widget.html', title="Kalender", desc="Vorlesungen", view=widgetView, utc_dt=datetime.datetime.utcnow())