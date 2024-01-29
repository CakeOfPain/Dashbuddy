# API-Specifications

## Widget-API

The Widget-API is being used for saving and retrieving the layout of the dashboard.
The returned List contain the Rows. Each Row is a List of widgets objects (columns).
Each Widget object got the fields:
- `plugin` The plugin that is going to be showed
- `params` The parameters for the plugin (query params)

Example:
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