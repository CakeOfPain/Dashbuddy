# API-Specifications

## Widget-API

The Widget-API is being used for saving and retrieving the layout of the dashboard.
The returned List contain the Rows. Each Row is a List of widgets objects (columns).
Each Widget object has the following fields:
- `plugin` The plugin that is going to be showed
- `params` The parameters for the plugin (query params)

Example:
```json
[
    {
        "height": 0.5,
        "widgets": [
            {
                "params": {},
                "plugin": "blank"
            },
            {
                "plugin": "blank"
            },
            {
                "params": {},
                "plugin": "watch"
            },
            {
                "plugin": "blank"
            },
            {
                "params": {},
                "plugin": "blank"
            }
        ]
    },
    {
        "height": 3,
        "widgets": [
            {
                "params": {
                    "show_terminus": "1",
                    "station_id": "8004094",
                    "you_funny": "1"
                },
                "plugin": "timetable"
            },
            {
                "plugin": "blank"
            },
            {
                "params": {},
                "plugin": "blank"
            },
            {
                "params": {},
                "plugin": "blank"
            },
            {
                "params": {},
                "plugin": "calendar"
            }
        ]
    },
    {
        "height": 1,
        "widgets": [
            {
                "params": {
                    "tag": "muffins"
                },
                "plugin": "gif"
            },
            {
                "plugin": "blank"
            },
            {
                "params": {},
                "plugin": "blank"
            }
        ]
    }
]
```
Methods:
- `GET /api/widgets` for retrieving the list of widgets
- `POST /api/widgets` for overriding the list of widgets

## Customization-API

Returns the Settings as object (dictionary), containing the settings as keys.
Can also be used for changing the Settings.

Example:
```json
{
    "Some Setting": 1.0,
    "More Setting": "blubber"
}
```
Methods:
- `GET /api/customization` for retrieving the customization object
- `POST /api/customization` for overriding the customization object