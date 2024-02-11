from datetime import date
from datetime import datetime
import calendar
from flask import render_template


# Problem mit dem Plugin: Der Kalender wird immer auf die Komplete Breite gestreckt!
def getCalender():
    aktuellesD=datetime.now()
    wochentag=aktuellesD.strftime("%A")
    datum=aktuellesD.strftime("%d.%m.%Y")
    tagdatum=f"{wochentag}, der {datum}"

    heute = calendar.datetime.datetime.now()
    jahr, monat = heute.year, heute.month

    kal_monat = calendar.monthcalendar(jahr, monat)
    wochentage = ["MO", "DI", "MI", "DO", "FR", "SA", "SO"]
    wochentage_string=" ".join(wochentage)

    html_kalendar="<table>\n"
    html_kalendar +="<tr>"+"".join(f"<th>{tag}</th>" for tag in wochentage)+"</tr>\n"

    for woche in kal_monat:
        html_kalendar +="<tr>" + "".join(f"<td>{tag if tag != 0 else ''}</td>" for tag in woche) + "</tr>\n"
    html_kalendar+="</table>"

    kal_monat_string=html_kalendar
    return render_template("calendar/index.html", weeks=kal_monat_string, weekdays=wochentage_string, dateDay=tagdatum),200

def createPlugin(plugin):
    plugin.name('calendar')
    plugin.describe('Zeigt den Kalender')
    plugin.api('get-Calender',getCalender)
    plugin.content(getCalender)
