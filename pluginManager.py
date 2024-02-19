import os
import sys
from pathlib import Path
import flask
import traceback
from typing import Any

class Plugin(object):
    def __init__(self):
        self.pluginName: str|None = None
        self.description: str|None = None
        self.apis: set[tuple[str, Any, tuple]] = set()
        self.contentRenderer = lambda: ("Empty", 200)
        self.params = ()

    def name(self, pluginName: str):
        self.pluginName = pluginName
    def describe(self, description: str):
        self.description = description
    def api(self, name: str, callback, params=()):
        self.apis.add((name, callback, params))
    def content(self, callback, params=()):
        self.contentRenderer = callback
        self.params = params

class PluginManager(object):
    def __init__(self, app: flask.Flask):
        self.flaskApp = app
        self.pluginPaths   = {path for path in os.listdir('./plugins') if path.endswith('.py')}
        self.pluginNames   = {Path(pluginPath).stem for pluginPath in self.pluginPaths}
        self.pluginModules = {getattr(__import__(f'plugins.{pluginName}'), pluginName) for pluginName in self.pluginNames}

    def manage(self):
        plugins = set(zip(self.pluginModules, self.pluginPaths))
        validPlugins = {(pluginModule, pluginPath) for pluginModule, pluginPath in plugins if hasattr(pluginModule, "createPlugin")}
        invalidPlugins = plugins - validPlugins
        for _, pluginPath in invalidPlugins:
            print(f'Warning: The file named "{pluginPath}" within the plugin folder is missing the function "createPlugin"',file=sys.stderr)
            print('=> Going to skip this plugin (plugin will not be loaded)', file=sys.stderr)
        createPluginFunctions = [(pluginModule.createPlugin, pluginPath) for pluginModule, pluginPath in validPlugins]

        self.plugins: list[Plugin] = []
        for createPlugin, pluginPath in createPluginFunctions:
            try:
                plugin = Plugin()
                createPlugin(plugin)
                plugin.contentRenderer.__name__ += pluginPath
                self.plugins.append(plugin)
                for name, callback, _ in plugin.apis:
                    callback.__name__ += pluginPath
                    self.flaskApp.get(f'/api/plugin/{plugin.pluginName}/{name}')(callback)
                self.flaskApp.get(f'/plugin/{plugin.pluginName}')(plugin.contentRenderer)
            except Exception:
                print(f'Warning: The file named "{pluginPath}" within the plugin folder has an invalid "createPlugin" function implementation',file=sys.stderr)
                print('=> Going to skip this plugin (plugin will not be loaded)', file=sys.stderr)
                print(f'Exception from plugin "{pluginPath}":', file=sys.stderr)
                traceback.print_exc()
    def listPluginsJson(self):
        return [{
            "name": plugin.pluginName,
            "description": plugin.description,
            "params": plugin.params,
            "apis": [{
                "name": name,
                "params": params
            } for name, _, params in plugin.apis],
        } for plugin in self.plugins]