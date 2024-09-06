# AP_Template
LaTeX Vorlage für das Anfängerpraktikum ohne Anspruch auf Vollständigkeit oder Perfektion sowie ein paar Tipps für LaTeX Anfänger*innen in der Datei tipps.pdf und eine Beipspiel für einen Plot mit Python. 

### Enthät folgende Dateien und Ordner:
- **main.tex** tex-Datei in der das Dokument definiert wird, packages geladen werden und die einzelnen Abschnitte eingebunden werden.
- **packages.sty** wird von main.tex aufgerufen und enthält häufig verwendetet usepackages
- Im Ordner **sections/** sind Dateien für die einzelnen Abschnitte des Protokolls abgelegt. Damit bleibt main.tex aufgeräumter und die collaboration v.a. über git wird einfacher.
- Ordner **figures/** für Abbildungen. Der Ordner ist als Standard Pfad für Abbildungen gesetzt und damit kann eine datei example.png in diesem ordner mit \includegraphics{example} eingebunden werden statt \includegraphics{figures/example}
- Ordner **labnotes/** für die Scans des Laborhefts
- **tipps.pdf** Tipps für LaTeX Anfänger*innen
- **plot.py** Beispiel für das Erstellen eines Plots mit Python

Solltet ihr Fehler finden oder Verbesserungsvorschläge haben, schreibt mir gerne.
