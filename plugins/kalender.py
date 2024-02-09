from datetime import date
from datetime import datetime
import calendar
from flask import render_template

def getDate():
    aktuellesD=date.today()
    furweekday=str(aktuellesD)
    return furweekday, 200
    
def getWeekDay():
    wochentage=["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag"]
    tag=date.weekday()
    return wochentage[tag], 200

def getCalender():
    kalenderseite=calendar.HTMLCalendar(calendar.MONDAY)
    aus=kalenderseite.formatmonth(datetime.now().date().year,datetime.now().date().month)
    return(aus), 200

def getContent():
    return render_template("calendar/index.html"), 200

def createPlugin(plugin):
    plugin.name('calendar')
    plugin.describe('Zeigt den Kalender')
    plugin.api('get-Date',getDate)
    plugin.api('get-Weekday',getWeekDay)
    plugin.api('get-Calender',getCalender)
    plugin.content(getContent)
