from flask import request, render_template
from markupsafe import Markup

import datetime
import logging
import requests
import xml.etree.ElementTree as ET

dbApiId = "11ee6296e52f2c41be3956420627b6a3"
dbApiSecret = "5ec59e4b2fdfb645be715940e47c54e0"

logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', level=logging.INFO)
logging.info('DB Timetable Plugin')

def fetchLine(train):
    if train[1].attrib.get("l") is None:
        return train[0].attrib.get("n")
    else:
        return train[1].attrib.get("l")

def fetchTime(timecode):
    timecode = f"{timecode[6]+timecode[7]}:{timecode[8]+timecode[9]} Uhr"
    return timecode

def fetchPath(train):
    # Base Variables
    arrival = train.find("ar")
    departure = train.find("dp")
    path = []

    # Check, if Train (1) starts here, (2) ends here or (3) has a stop here.
    if arrival is None and departure is not None:
        #logging.info("Zug starter hier und fährt weiter")
        path.append("1")

        # Get Terminus
        pathAfter = departure.attrib.get("ppth")
        pathAfter = pathAfter.split("|")
        path.append(pathAfter[len(pathAfter)-1])

    elif arrival is not None and departure is None:
        #logging.info("Zug endet hier")
        path.append("2")

        # Get first Station
        pathBefore = arrival.attrib.get("ppth")
        pathBefore = pathBefore.split("|")
        path.append(pathBefore[0])

    elif arrival is not None and departure is not None:
        #logging.info("Zug hat planmäßigen Halt hier")
        path.append("3")

        # Get first Station
        pathBefore = arrival.attrib.get("ppth")
        pathBefore = pathBefore.split("|")
        path.append(pathBefore[0])

        # Get Terminus
        pathAfter = departure.attrib.get("ppth")
        pathAfter = pathAfter.split("|")
        path.append(pathAfter[len(pathAfter)-1])

    # Logging for Debug
    #logging.info(path)

    # Return the Linepath
    return path

def getTimetable(eva, date, time):
    infraGoUrl = f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/plan/{eva}/{date}/{time}"

    headers = {
            "DB-Client-Id": dbApiId,
            "DB-Api-Key": dbApiSecret,
            "accept": "application/xml"
        }
    
    response = requests.get(infraGoUrl, headers=headers)
    logging.debug(f'HTTP Response from Timetables V1: {response}')
    data = ET.fromstring(response.text)

    timetable = []

    timetable.append(data.get("station"))

    for service in data:
        train = [
            [
                [service[0].attrib.get("c"), fetchLine(service)],
                service[1].attrib.get("pp"),
                fetchTime(service[1].attrib.get("pt"))
            ],
            fetchPath(service)
        ]
        timetable.append(train)
    logging.debug(timetable)
    return timetable

def createWidget():
    stationId = request.args.get("station_id")
    showTerminatingTrains = bool(request.args.get("show_terminus") == "1")
    now = datetime.datetime.now()

    # Hält die nächsten 8000 Jahre xD Bis dahin hat jemand anderes bestimmt ne bessere Lösung gefunden
    dateNow = f'{str(now.year)[2]+str(now.year)[3]}{"{:02d}".format(now.month)}{"{:02d}".format(now.day)}'
    timeNow = "{:02d}".format(now.hour)
    timetable = getTimetable(stationId, dateNow, timeNow)
    trains = ""

    for i in range(len(timetable)):
        if i == 0:
            logging.debug(f'Timetable Index 0 -> Station Name {timetable[0]}')
        else:
            trainType = timetable[i][1][0]
            if trainType == "1":
                logging.debug(f'Timetable Index {i} -> Traintype {trainType}')
                trains += f'<div class="train"><h4>{timetable[i][0][0][0]} {timetable[i][0][0][1]} - {timetable[i][1][1]}</h4><p>Abfahrt {timetable[i][0][2]} Gleis {timetable[i][0][1]}</p></div>'
            elif trainType == "2" and showTerminatingTrains:
                logging.debug(f'Timetable Index {i} -> Traintype {trainType}')
                trains += f'<div class="train"><h4>{timetable[i][0][0][0]} {timetable[i][0][0][1]} - {timetable[0]}</h4><p>Ankunft {timetable[i][0][2]}, Zug endet hier!</p></div>'
            elif trainType == "3":
                logging.debug(f'Timetable Index {i} -> Traintype {trainType}')
                trains += f'<div class="train"><h4>{timetable[i][0][0][0]} {timetable[i][0][0][1]} - {timetable[i][1][2]}</h4><p>Abfahrt {timetable[i][0][2]} Gleis {timetable[i][0][1]}</p></div>'
    
    data = Markup(f'{trains}')

    # Für das Meme :D
    if bool(request.args.get("you_funny") == "1"):
        meme = "/static/meme.gif"
    else:
        meme = ""

    return render_template("timetable/index.html", stationName=timetable[0], timetableData = data, meme = meme), 200

def createPlugin(plugin):
    plugin.name("timetable")
    plugin.describe("See arrivals and departures")
    plugin.api("fetch", getTimetable)
    plugin.content(createWidget, params=('station_id', 'show_terminus', 'you_funny',))