import getpass
import flask

def createContent():
    return flask.render_template('/greetings/index.html', username=getpass.getuser())

def createPlugin(plugin):
    plugin.name('greetings')
    plugin.describe('Greets the user')
    plugin.content(createContent)