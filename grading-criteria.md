<!-- https://github.com/skills/communicate-using-markdown -->

# Grading Criteria Programmieren T3INF1004
In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

## FACHKOMPETENZ (40 Punkte)

# Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10) 

## - Algorithmenbeschreibung

## - Datentypen

- [bool](https://github.com/CakeOfPain/Dashbuddy/blob/df92ce0aa2cbae4b21508d448df3fbe73af835c9/plugins/timetable.py#L129)
- [str](https://github.com/CakeOfPain/Dashbuddy/blob/df92ce0aa2cbae4b21508d448df3fbe73af835c9/plugins/kalender.py#L19)
- [set](https://github.com/CakeOfPain/Dashbuddy/blob/df92ce0aa2cbae4b21508d448df3fbe73af835c9/pluginManager.py#L12C21-L12C59)
- [closure](https://github.com/CakeOfPain/Dashbuddy/blob/df92ce0aa2cbae4b21508d448df3fbe73af835c9/pluginManager.py#L13)
- [list](https://github.com/CakeOfPain/Dashbuddy/blob/df92ce0aa2cbae4b21508d448df3fbe73af835c9/pluginManager.py#L42)
- [dict](https://github.com/CakeOfPain/Dashbuddy/blob/df92ce0aa2cbae4b21508d448df3fbe73af835c9/pluginManager.py#L59)
- [int](https://github.com/CakeOfPain/Dashbuddy/blob/df92ce0aa2cbae4b21508d448df3fbe73af835c9/dashbuddy.py#L36)
- [tuple](https://github.com/CakeOfPain/Dashbuddy/blob/df92ce0aa2cbae4b21508d448df3fbe73af835c9/plugins/gifGiphy.py#L30C32-L30C47)


## - E/A-Operationen und Dateiverarbeitung

Widgets:

- Eingabe über die Edit-Funktion des Plugin:
  - [html inputs](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/static/scripts/editWidgets.js#L23)
  - [html select](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/static/scripts/editWidgets.js#L27)
- Weiterverarbeitung durch APIs:
  - [Aufruf der API für Widgets zum speichern](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/static/scripts/editWidgets.js#L66)
  - [Verarbeitung des API Aufrufs](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/dashbuddy.py#L39)
  - [Aufruf der API für Widgets zum lesen](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/static/scripts/renderWidgets.js#L5)

DB-Plugin:
- Verarbeitung einer Anfrage zu einer Timetable der DB:
  - [Eingabe der Station-ID über Parameter](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/plugins/timetable.py#L101)
  - [Verarbeitung des Requests](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/plugins/timetable.py#L70)
  - [Darstellung als HTML](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/plugins/timetable.py#L134C10-L134C117)

Konsole:
- [print](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/pluginManager.py#L38)

Dateien:
- [Datei Eingabe](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/dashbuddy.py#L51)
- [Datei Ausgabe](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/dashbuddy.py#L40)

## - Operatoren

- [String Concatenation](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/plugins/kalender.py#L25)
- [Vergleichsoperator](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/plugins/timetable.py#L129)
- [InkrementierenMitOperator](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/pluginManager.py#L47)
- [Zuweisungsoperator](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/pluginManager.py#L23)
- [MinusOperator](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/pluginManager.py#L36)
- [MemberAccessOperator](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/plugins/timetable.py#L81)
- [Typ-Spezifizier-Operator](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/pluginManager.py#L10)
- Und noch viele mehr!

## - Kontrollstrukturen
- [for-Schleife](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/plugins/timetable.py#L111)
- [if-else-Abfrage](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/plugins/timetable.py#L112)
- [if-else-if-Abfrage](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/plugins/timetable.py#L116)
- [with](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/dashbuddy.py#L40)
- [for-comprehension](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/pluginManager.py#L35)
- [try-except](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/pluginManager.py#L44)

## - Funktionen
- [Funktion](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/dashbuddy.py#L34)
- [Lambda](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/pluginManager.py#L13)
- [Methode](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/pluginManager.py#L33)

## - Stringverarbeitung

- [String Interpolation/Formatting](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/pluginManager.py#L54)
- [String Concatenation](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/plugins/kalender.py#L25)
- [Split](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/plugins/timetable.py#L38C21-L38C30)

## - Strukturierte Datentypen

- [Plugin](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/pluginManager.py#L8)
- [Plugin-Manager](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/pluginManager.py#L26)

# Sie können die Syntax und Semantik von Python (10)
<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->
- [PluginManager](https://github.com/CakeOfPain/Dashbuddy/blob/main/pluginManager.py)
Auf den PluginManager sind wir besonders stolz, da dieser Code es ermöglicht, verschiedenen Funktionen als seperate Plugins zu implementieren und sie dynamisch mit einer Flask-Anwendung zu laden. Dadurch wird eine flexible Achitektur ermöglicht, um die Funktionalität von Dashbuddy zu erweitern.
Zunächst wird hierbei dei Python-Class [Plugin](https://github.com/CakeOfPain/Dashbuddy/blob/main/pluginManager.py#L8) definiert. Diese besteht aus mehreren Funktionen. Diese Klasse definiert die Struktur eines Plugins. Darin ist somit festgelegt, dass jedes Plugin einen [Namen](https://github.com/CakeOfPain/Dashbuddy/blob/main/pluginManager.py#L16), eine [Beschreibung](https://github.com/CakeOfPain/Dashbuddy/blob/main/pluginManager.py#L18), mehrere [APIs](https://github.com/CakeOfPain/Dashbuddy/blob/main/pluginManager.py#L20) und eine Funktion namens [content](https://github.com/CakeOfPain/Dashbuddy/blob/main/pluginManager.py#L22) zum Rendern des Inhalts besitzt.
Darauf folgt die Python-Klasse [PluginManager](https://github.com/CakeOfPain/Dashbuddy/blob/main/pluginManager.py#L26). Diese Klasse verfolgt den Zweck alle Plugins zu verwalten. Dafür werden alle Dateien aus dem Verzeichnis [./plugins](https://github.com/CakeOfPain/Dashbuddy/tree/main/plugins). Dann werden die Plugins überprüft, ob sie die Funktion [createPlugin](https://github.com/CakeOfPain/Dashbuddy/blob/main/pluginManager.py#L35) enthalten. Falls eine Datei diese Funktion nicht enthält, wird sie übersprungen und eine [Warnung](https://github.com/CakeOfPain/Dashbuddy/blob/main/pluginManager.py#L38) ausgegeben. Für alle Dateien, die diese Funktion enthalten wird ein Plugin-Objekt erstellt und die Funktion [createPlugin](https://github.com/CakeOfPain/Dashbuddy/blob/main/pluginManager.py#L46) aufgerufen, um das Plugin zu initialisieren.

# Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)
<!-- Anhand von commits zeigen, wie jeder im Projekt einen Beitrag geleistet hat -->
Commits von [`@CakeOfPain`](https://github.com/CakeOfPain) (Leo Englert):

- https://github.com/CakeOfPain/Dashbuddy/commit/7df47ea92eee09223438f70e2af4547226b60fa7
- https://github.com/CakeOfPain/Dashbuddy/commit/fcab67801bb582917fbecd19fc8b8a7ba28bde43
- https://github.com/CakeOfPain/Dashbuddy/commit/22a17b8d5d197973178d14dfb9b801f5212e8b32

Commits von [`Sebastian`](https://github.com/riedl-sebastian) (Sebastian Riedl):

- https://github.com/CakeOfPain/Dashbuddy/commit/c96fe6a166defb4b33b603d2e287aa39a020f7f0
- https://github.com/CakeOfPain/Dashbuddy/commit/5934ce496ac81c12199ed77d71867f6b55d6413e
- https://github.com/CakeOfPain/Dashbuddy/commit/8f3e6235a61e02dd4e73dca9b4ca0d9c7733ab64

Commits von [`@Evolinox`](https://github.com/Evolinox) (Pascal Jedicke):

- https://github.com/CakeOfPain/Dashbuddy/commit/e1db4e321751e45feb101a48b0169ebf01e7ca41
- https://github.com/CakeOfPain/Dashbuddy/commit/178bb7fb7fcf90498bd7af642bfdbb032b81da0a
- https://github.com/CakeOfPain/Dashbuddy/commit/b6cb93d62b731da8802be29716c886582c996128

# Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)
<!-- Eine Stelle aus dem Projekt wählen auf die sie besonders stolz sind und begründen -->
[Stelle aus dem Code (Set & Tuple)](https://github.com/CakeOfPain/Dashbuddy/blob/8d1947e7bdfd4a8c96b6badaf37059bf05f39634/pluginManager.py#L12)
Durch das Set, werden doppelte API-Routen von Plugins automatisch herausgefiltert.

## METHODENKOMPETENZ (10 Punkte)

# Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)
<!-- Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein) -->

- [Visual Studio Code](https://code.visualstudio.com/)
  - ![vscode](./docs/vscode.png)
- [Github](https://github.com/CakeOfPain/Dashbuddy)
  - ![github](/./docs/github.png)
- [Obsidian](https://obsidian.md/)
  - ![obsidian](./docs/Obsidian.png)


## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studierenden können ihre Software erläutern und begründen. (5)
<!-- Jeder in der Gruppe: You have helped someone else and taught something to a fellow student (get a support message from one person) -->
Wir haben uns nach den Vorlesungen in der Bibliothek getroffen und Pair-Programming betrieben, weshalb keine Aufzeichnungen vorhanden sind.

# Sie können existierenden Code analysieren und beurteilen. (5)
<!-- Pro Gruppe:You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project in the critique, use these evaluation criteria to critique the other project. Make sure they get a top grade after making the suggested changes -->
[Peer Review](./peer-review.md) für das Projekt [OpenGL-Tetris](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project/).

# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
<!-- Which technology did you learn outside of the teacher given input -->
- [FlaskWebframework](https://github.com/CakeOfPain/Dashbuddy/blob/main/Wetterausgabe%20Test.py#L10)
- [JavaScript](https://github.com/CakeOfPain/Dashbuddy/blob/main/static/scripts/renderWidgets.js)
- [CSS](https://github.com/CakeOfPain/Dashbuddy/blob/main/static/css/main.css)
- [HTML](https://github.com/CakeOfPain/Dashbuddy/blob/main/templates/timetable/index.html)
- [PythonClass](https://github.com/CakeOfPain/Dashbuddy/blob/main/pluginManager.py#L8)
<!-- Did you or your group get help from someone in the classroom (get a support message here from the person who helped you) -->
Unsere Gruppe stand in einem produktiven Gedankenaustausch mit dem Team von [OpenGLTetris](https://github.com/rpfaeffle/DHBW-Programming-1-Final-Project). Die Kommunikation hat hauptsächlich im schulischen Umfeld face-to-face stattgefunden, weshalb es hierfür keine Textnachrichten gibt.


## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

# Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30) - Alle ein Punkt wo er stolz ist
<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->

<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->
- [KalendarWidget](https://github.com/CakeOfPain/Dashbuddy/blob/main/plugins/kalender.py)
Ein Problem, welches bei der Entwicklung des Kalendar-Plugins in Python aufgetreten ist, dass HTML die Zeilenbrüche im Pythonquelltext nicht erkennt. Dadurch kann ein schöner Kalendar in Python geschrieben nicht einfach in die HTML-Datei integriert werden. Um den Kalender richtig ausgeben zu lassen (die Tage oben, darunter die richtigen Daten), muss der Kalendar in HTML-Code im Pythondokument ungeschrieben werden. Nach diesem umschreiben, muss der gesamte HTML-Kalender, der nun noch aus mehreren Strings besteht, zu einem String zusammengefasst werden. Damit dieser String in der HTML-Datei interpretiert und nicht einfach ausgegeben wird, muss noch ein zusätzlicher Befehl hinzugefügt werden.


