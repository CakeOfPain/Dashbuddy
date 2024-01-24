# Plugin Framework created by Pascal

import uuid

# Widget Objekt
class Widget:
    def __init__(self, name, desc, preset, exec):
        self.name = name
        self.id = uuid.uuid4()
        self.desc = desc
        self.preset = preset
        self.exec = exec

    def __str__(self) -> str:
        return f"{self.name}({self.id})"

# Methode, um ein neues Widget zu registrieren
def register(widget):
    print(f"Plugin Framework: Registered {widget}")

# Methode, um ein Widget zu entfernen
def remove(uuid):
    print(f"Plugin Framework: Removed {uuid}")

# Methode, um die Position eines Widgets zu updaten
def updatePosition(uuid, posX, posY):
    print(f"Plugin Framework: Updated {uuid}'s position to X:{posX}, Y:{posY}")

# Methode, um Widgets zu platzieren
def place():
    amount = 2
    print(f"Plugin Framework: Loaded {amount} Widgets")