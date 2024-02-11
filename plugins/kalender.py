from datetime import date
from datetime import datetime
import calendar
from flask import render_template
    
def getCalender():
    aktuellesD=datetime.now()
    wochentag=aktuellesD.strftime("%A")
    datum=aktuellesD.strftime("%d.%m.%Y")
    tagdatum=f"{wochentag}, der {datum}"

    heute=datetime.now()
    jahr=heute.year
    monat=heute.month
    tag=heute.day

    kal_monat=calendar.monthcalendar(jahr,monat)
    for woche in kal_monat:
        for i, t in enumerate(woche):
            if t== tag:
                woche[i]=str(t).lstrip("0")
    wochentage=["MO","DI","MI","DO","FR","SA","SO"]
    wochentage_string=" ".join(wochentage)

    aktueller_wochentag=calendar.weekday(jahr,monat,tag)
    markierter_tag=wochentage[aktueller_wochentag]+"*"

    kal_monat_string="\n".join(" ".join(markierter_tag if t==tag else str(t) for t in woche) for woche in kal_monat)

    return render_template("calendar/index.html", weekDays=wochentage_string, weeks=kal_monat_string, dateDay=tagdatum),200

def createPlugin(plugin):
    plugin.name('calendar')
    plugin.describe('Zeigt den Kalender')
    plugin.api('get-Calender',getCalender)
    plugin.content(getCalender)
