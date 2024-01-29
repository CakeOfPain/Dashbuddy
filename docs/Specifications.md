# API-Specifications

## Widget-API

The Widget-API is being used for saving and retrieving the layout of the dashboard.
The returned List contain are the Rows. Each Row has a List of widgets (columns) that are evenly spaced.
Each Widget got the fields:
- `plugin` The plugin that is going to be showed
- `params` The parameters for the plugin (query params)

```json
[
    [
        {
            "plugin": "plugin-xyz-name",
            "params": ["Some parameter of plugin"]
        }
    ],
    [
        {
            "plugin": "plugin2-xyz-name",
            "params": []
        },
        {
            "plugin": "plugin3-xyz-name",
            "params": []
        }
    ]
]
```
Methods:
- `GET /api/widgets` for retrieving the list of widgets
- `POST /api/widgets` for overriding the list of widgets

## Customization-API

Returns the Settings as object (dictionary), containing the settings as keys.

```json
{
    "Some Setting": 1.0,
    "More Setting": "blubber"
}
```
Methods:
- `GET /api/customization` for retrieving the customization object
- `POST /api/customization` for overriding the customization object