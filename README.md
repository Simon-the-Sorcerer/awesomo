# A.W.E.S.O.M-O 4000

Discord-Bot für unseren Server

## Installation für systemd

1. Pfade in `systemd/awesomo.service` anpassen
2. `awesomo.service` nach `$HOME/.config/systemd/user` kopieren
3. Service aktivieren:
    ```bash
    $ systemctl --user daemon-reload
    $ systemctl --user enable awesomo.service
    $ systemctl --user start awesomo.service
    $ sudo loginctl enable-linger $USER
    ```

## Features

### meddl

Funktion: Grußform, häufig angewendet in Mittelfranken  
Command: `$meddl`

### info

Funktion: Informationen über den Bot  
Command: `$info`

### hello

Funktion: A.W.E.S.O.M-O stellt sich vor
Command: `$hello`

### next

Funktion: Customer Support
Command: `$next`

### shrug

Funktion: ¯\\_(ツ)_/¯
Command: `$shrug`

### help

Funktion: Übersicht über verfügbare Befehle  
Command: `$help`

### date

#### date create

Funktion: Erstellt einen neuen Termin
Command: `$date create DATUM UHRZEIT BESCHREIBUNG`  
Beispiel: `$date create 2020-02-02 20:20 Rudi aus Buddeln grüßen`

### poll

#### poll create

Funktion: Erstellt eine neue Abstimmung
Command: `$poll create "TITEL" Optionen`
Beispiel: `$poll create "Neues Radlfideo?" Ja Nein "zu kalt"`
