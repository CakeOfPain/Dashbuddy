from datetime import date
from datetime import datetime
import calendar
from flask import render_template


def getCalendar():
    currentDate=datetime.now()
    dayOfTheWeek=currentDate.strftime("%A")
    date=currentDate.strftime("%d.%m.%Y")
    daydate=f"{dayOfTheWeek}, der {date}"

    today = calendar.datetime.datetime.now()
    year, month = today.year, today.month

    cal_month = calendar.monthcalendar(year, month)
    wochentage = ["MO", "DI", "MI", "DO", "FR", "SA", "SO"]
    dayOfTheWeek_string=" ".join(wochentage)

    html_calendar="<table style='width:100%'>\n"
    html_calendar +="<tr>"+"".join(f"<th>{tag}</th>" for tag in wochentage)+"</tr>\n"

    for week in cal_month:
        html_calendar +="<tr>" + "".join(f"<td>{tag if tag != 0 else ''}</td>" for tag in week) + "</tr>\n"
    html_calendar+="</table>"

    cal_month_string=html_calendar
    return render_template("calendar/index.html", weeks=cal_month_string, weekdays=dayOfTheWeek_string, dateDay=daydate),200

def createPlugin(plugin):
    plugin.name('calendar')
    plugin.describe('Shows a calendar')
    plugin.content(getCalendar)
