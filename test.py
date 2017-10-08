import datetime
from rfeed import *
# year, month, date, hh, mm, ss
item1 = Item(
        title = "Kirigami y Marble Maps en Google Summer of Code 2017",
        link = "http://www.kdeblog.com/kirigami-y-marble-maps-en-google-summer-of-code.html",
        description = "Para los que no le sepan, Kirigami es una herramienta que tiene como objetivo "
          "facilitar la vida a los programadores haciendo que sus aplicaciones sean perfectamente usables "
          "en un amplio rango de dispositivos, desde moviles a ordenadores de escritorio. En otras palabras "
          ", el desarrollador solo debe hacer su programa una vez, siendo Kirigami el que se encargara de "
          "ajustar sus opciones graficas y de control para cada tipo de dispositivo.",
    guid = Guid("http://www.kdeblog.com/kirigami-y-marble-maps-en-google-summer-of-code.html"),
        pubDate = datetime.datetime(2017, 10, 07, 0, 0))

feed = Feed(
        title = "Noticias Destacadas",
        link = "http://proyectosbeta.net/noticias_rss/noticias.xml",
        description = "noticias destacadas",
        language = "es-PY",
        lastBuildDate = datetime.datetime.now(),
        items = [item1])

print feed.rss()
