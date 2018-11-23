# "Restful User-Service"
Test
## Aufgabenstellung
Die detaillierte [Aufgabenstellung](TASK.md) beschreibt die notwendigen Schritte zur Realisierung.

## Implementierung
Für die Implementierung des Servers wurde Flask verwendet.
Auf die Applikation kann nun mittels 
```
curl http://localhost:5000
```
zugegriffen werden.

Mögliche befehle
```
curl http://localhost:5000/user

curl http://localhost:5000/user/<username>

curl http://localhost:5000/user/<username> -X DELETE -v

curl http://localhost:5000/user/<username> -d "name=updateName, update@mail.at, <image path.datatype> -X PUT -v

curl http://localhost:5000/user -d "name=newUser, newUser@mail.at, <image path.datatype> -X POST -v

```

Damit alles Persistiert werden kann, wurde ein user.json File erstell.\
Um CRUD Befehle ausführen zu können wurde das jreader.py File erstellt.

Damit user auch ein Profilbild haben können, wurde eine encoder geschrieben, welcher ein Bild in base64
encoded.

Für die Dokumentierung wurde Sphinx verwendet.

## Quellen
[Python](https://docs.python.org/3/)

[Flask](http://flask.pocoo.org/docs/1.0/quickstart/)

[Flask-Restful](https://flask-restful.readthedocs.io/en/latest/quickstart.html)

[Sphinx](http://www.sphinx-doc.org/en/master/)

