from flask import request, render_template
import logging
import requests
import xml.etree.ElementTree as ET

dbApiId = "11ee6296e52f2c41be3956420627b6a3"
dbApiSecret = "5ec59e4b2fdfb645be715940e47c54e0"

logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', level=logging.INFO)
logging.info('DB Timetable Plugin')

def fetchTime(timecode):
    timecode = f"{timecode[6]+timecode[7]}:{timecode[8]+timecode[9]} Uhr"
    return timecode

def fetchPath(train):
    logging.info(train.tag)

    #ich bin dumm, das geht net :()

    return train

def getTimetable(eva, date, time):
    infraGoUrl = f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/plan/{eva}/{date}/{time}"

    headers = {
            "DB-Client-Id": dbApiId,
            "DB-Api-Key": dbApiSecret,
            "accept": "application/xml"
        }
    
    response = requests.get(infraGoUrl, headers=headers)
    logging.info(f'HTTP Response from Timetables V1: {response}')
    data = ET.fromstring(response.text)

    timetable = []

    timetable.append(data.get("station"))

    for service in data:
        train = [
            [
                [service[0].attrib.get("c"), service[1].attrib.get("l")],
                service[1].attrib.get("pp"),
                fetchTime(service[1].attrib.get("pt"))
            ],
            fetchPath(service)
        ]
        timetable.append(train)
    return timetable

def createWidget():
    timetable = getTimetable(8004094, 240205, 17)
    return render_template("timetable/index.html", stationName=timetable[0]), 200

def createPlugin(plugin):
    plugin.name("timetable")
    plugin.describe("See arrivals and departures")
    plugin.api("fetch", getTimetable)
    plugin.content(createWidget)