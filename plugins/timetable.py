from flask import request, render_template
import requests
import xml.etree.ElementTree as ET

def date2Friendly(timecode):
    timecode = f"{timecode[6]+timecode[7]}:{timecode[8]+timecode[9]} Uhr"
    return timecode

def path2Friendly(trainpath):
    trainpath = trainpath.split("|")
    return trainpath

def getTimetable(eva, date, time):
    infraGoUrl = f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/plan/{eva}/{date}/{time}"

    headers = {
            "DB-Client-Id": dbApiId,
            "DB-Api-Key": dbApiSecret,
            "accept": "application/xml"
        }
    
    response = requests.get(infraGoUrl, headers=headers)
    data = ET.fromstring(response.text)

    timetable = []

    timetable.append(data.get("station"))

    for s in data:
        for t in s:
            train = [
                [
                    [s[0].attrib.get("c"), s[1].attrib.get("l")],
                    s[1].attrib.get("pp"),
                    date2Friendly(s[1].attrib.get("pt"))
                ],
                path2Friendly(s[1].attrib.get("ppth"))
            ]
            timetable.append(train)

    print(timetable)
    return timetable

def createWidget():
    timetable = getTimetable(8000157, 240201, 12)
    return render_template("timetable/index.html", stationName=timetable[0]), 200

def createPlugin(plugin):
    plugin.name("timetable")
    plugin.describe("See arrivals and departures")
    plugin.api("fetch", getTimetable)
    plugin.content(createWidget)