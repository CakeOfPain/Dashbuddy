from flask import request, render_template
import logging
import requests
import xml.etree.ElementTree as ET


logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', level=logging.INFO)
logging.info('DB Timetable Plugin')

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
    logging.info(timetable)
    return timetable

def createWidget():
    timetable = getTimetable(8004094, 240208, 17)
    return render_template("timetable/index.html", stationName=timetable[0]), 200

def createPlugin(plugin):
    plugin.name("timetable")
    plugin.describe("See arrivals and departures")
    plugin.api("fetch", getTimetable)
    plugin.content(createWidget)