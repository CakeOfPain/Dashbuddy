# Peer Review [OpenGL-Tetris](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/)

In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.

## FACHKOMPETENZ (40 Punkte)

### Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)

#### Datentypen

Wir haben diese verschiedenen Datentypen gefunden:
- [`bool`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/core/application.py#L28)
- [`bytes`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/constants.py#L48)
- [`deque`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/core/application.py#L68)
- [`dict`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/constants.py)
- [`enum`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/constants.py)
- [`float`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/components/shape.py#L6-L10)
- [`int`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/core/application.py#L26)
- [`list`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/core/application.py#L26)
- [`NoneType`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/main.py#L53)
- [`set`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/constants.py#L31)
- [`str`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/core/application.py#L26)
- [`tuple`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/components/shape.py#L6-L10)

#### E/A-Operationen und Dateiverarbeitung

Nicht die typischen I/O Operationen, aber eigene Art der I/O

- [Input über GLUT](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/core/input.py)
- [Ausgabe über screen via FreeType](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/core/font.py)

#### Operatoren

Hier ein paar Beispiele für verwendete Operatoren:

- https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/core/openGLUtils.py#L6
- https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/main.py#L28

#### Kontrollstrukturen

- [`if`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/core/application.py#L61-L76)
- [`Conditional Expressions`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/core/application.py#L76)

#### Funktionen

Das gesamte Program besteht quasi aus Klassen, welche Funktionen enthalten. Deshalb wird als Referenz hier nur [`src/main.py`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/main.py) angegeben. Funktionen sind jedoch in jeder Datei mit Ausnahme von `src/constants.py` vorhanden.

#### Stringverarbeitung

Stringverarbeitung wird, da es sich hierbei um ein Spiel handelt nicht wirklich behandelt. Jedoch ist sie in der [`Text`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/components/text.py#L13)komponente anzutreffen, auch wenn es sich hierbei nur um ein primitives `split`ting eines strings handelt.

#### Strukturierte Datentypen

Im Laufe des Programs werden mehrfach `lists`, `tuples` und `dicts` und sogar eine `deque` verwendet:

- [`deque`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/core/application.py#L68)
- [`list`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/main.py#L19-L20)
- [`tuple`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/components/shape.py#L6-L9)
- [`dict`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/constants.py#L11-L29)

### Sie können die Syntax und Semantik von Python (10)

### Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)

Die folgenden Beispiele enthalten nicht alle Commits und einige sind auch zusammen entstanden, wurden jedoch nur einem zugeordent, da `co-authored-by` bis dahin noch unbekannt war.

Commits von [`@rpfaeffle`](https://github.com/rpfaeffle):

- https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/commit/fcb63abaa670d84eb7f95b3d7e830e5b07c25071
- https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/commit/c611e733d7e6ca1cc50d5b4a6e4a97fbeba831d7
- https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/commit/6686ffe97b6147422187e3d375c082ce5b546a96

Commits von [`@tim-02-k`](https://github.com/tim-02-k):

- https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/commit/1b20fb76eb92a9746a3ad65e0f2f20f6fcc657b2
- https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/commit/b601566b9bd39c4605a6f68a91e3eaf6a4b6ed8d
- https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/commit/3372b4c019b7ea86c44ef584ee2198f54925ad87

### Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)

Besonders stolz sind wir auf folgenden [Code](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/core/application.py#L60-L76):

Dieser ist Grundlegend für die Rendering-Engine, welche sich hinter dem gesamten Projekt verbirgt. Die Verwendung von `deque` erlaubt eine **O(1)** Zeitkomplexität bei `pop` und `append` verglichen mit `list`, welche eine Zeitkomplexität von O(n) hat.

Verwenung von [`dict` zusammen mit `tuple`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/core/input.py):

Key listener werden in einem `dict` mit `tuple` von `key` und `modifier` gespeichert, um callbacks eindeutig zu identifizieren.

Andere Anwendungen von Datenstrukturen, siehe [Datentypen](#datentypen)

## METHODENKOMPETENZ (10 Punkte)

### Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)

Beispielhafte Screenshots von genutzten Tools (@rpfaeffle):

<img src="assets/images/git-terminal-rpfaeffle.png" alt="Image showing usage of git and the terminal" height="250px" />
<img src="assets/images/vscode-rpfaeffle.png" alt="Image showing usage of vscode and github copilot" height="250px">

Screenshots zur Nutzung eines Code Editors (@tim-02-k):
<img src="assets/images/PyCharm-tim-02-k.png" alt="Image showing usage of PyCharm by JetBrains" height="250px">

## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

### Die Studierenden können ihre Software erläutern und begründen. (5)

Wir haben Pair-Programming betrieben (dadurch keine Aufzeichnungen vorhanden).

### Sie können existierenden Code analysieren und beurteilen. (5)

### Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)

Technologies used outside of the teacher given input:

- FreeType
- OpenGL
- GLUT
- Python Classes

Wir standen im regen Austausch mit der [Dashbuddy](https://github.com/CakeOfPAin/dashbuddy) Gruppe. Aufzeichnungen sind hier leider auch nicht vorhanden, da diese Gespräche persönlich stattfanden.

## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

### Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)

Stolz sind wir eigentlich auf den gesamten Code 😊🥹. Die folgenden Beispiele zeigen jedoch einige Stellen, auf die wir besonders Stolz sind, bzw. welche uns einiges an Hirnschmalz gekostet haben.

Stolz sind wir auf folgenden [Code](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/core/application.py#L60-L76):

Dieser ist Grundlegend für die Rendering-Engine, welche sich hinter dem gesamten Projekt verbirgt. Die Verwendung von `deque` erlaubt eine **O(1)** Zeitkomplexität bei `pop` und `append` verglichen mit `list`, welche eine Zeitkomplexität von O(n) hat. Dies ermöglicht eine relativ konstante Frame-Rate von ungefähr 60 FPS (es wären bestimmt auch mehr möglich, unsere Displays / Monitore schaffen jedoch nur 60 FPS). Hier gab es zu Beginn jedoch auch Probleme, da das Rendering teilweise nicht konstant war.
Durch Debugging konnten wir jedoch den Fehler für die inkonsistente und niedrige Frame-Rate finden. Jeder Frame wurde nicht nur einmal, sonder gleich zweimal gerendert, was dazu führte, dass anstelle von 1 mal pro Frame alle `render` Methoden 2 mal pro Frame aufgrufen wurden (liegt wohl irgendwie an `GLUT` und `glutDisplayFunc`). Die Lösung war dann einen [check](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/core/application.py#L61) für jeden Frame einzufügen, ob die UI schon gerendert wurde.
https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/commit/fcb63abaa670d84eb7f95b3d7e830e5b07c25071

Ein weiteres Stück Code, auf welches wir Stolz sind ist das [`Text-Rendering`](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/blob/main/src/core/font.py) mit Free-Type, die Geschichte des Enstehens ist besser nachzuvollziehen in (https://github.com/rpfaeffle/python-opengl), da es eine ganze Menge Arbeit war, bis es so funktioniert hat, wie es soll. Der Code dahinter mag nicht der komplexeste Algorithmus sein, jedoch steckt einiges an OpenGL Code dahinter, welcher nicht unbedingt leicht zu erschließen ist.
Das Hauptproblem lag hierbei darin, wie OpenGL den Bitmap Buffer von einigen `char` interpretiert hat, was dazu führte, dass einige Zeichen nicht richtig angezeigt wurden. Es hat auch mehrere Ansätze benötigt, bis das Text-Rendering überhaupt funktioniert hat.