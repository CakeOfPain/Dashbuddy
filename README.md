# Dashbuddy
Extendable Dashboard written in Python.

## Demo
<iframe width="966" height="471" src="https://www.youtube.com/embed/5hDGjZO-zWU" title="dashbuddy" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Requirements PIP

First install the python package requirements for this project:
```bash
pip install -r requirements.txt
```

## Run the application

Make sure you have installed the requirements first before running this project.
To run the project, execute this command:
```bash
flask --app dashbuddy run
```

## Features
- Widgets: Widgets can be added removed and moved on the dashboard. You can edit them in the edit mode.
- Plugins: Plugins can be created with python scripts you put into the `./plugins` folder of this project.
- Standard Plugins:
  - [gifGiphy.py](./plugins/gifGiphy.py): can be used for showing random gifs on a widget
  - [greetings.py](./plugins/greetings.py): Just greeds the user with the name specified in the system
  - [calendar.py](./plugins/calendar.py): Very basic calendar for you to use on a widget
  - [timetable.py](./plugins/timetable.py): If you travel by train in germany, this plugin shows you the train-timetable of a given line between two locations.
  - [watch.py](./plugins/watch.py): Well, it's a watch, showing you the current time

## Docs
- [API-Specifications](./docs/Specifications.md)

Also take a look at the folder `./docs/progresstree` which has to be opened with obsidian.
Within this folder is the so called `progresstree` of the project, which indicates the progress of the project.
It's similar to a skilltree in video-games.