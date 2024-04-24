# Python-Package geist_module einbinden und einen Aliasnamen vergeben
import geist_module as g
from random import choice

# Instanziieren eines Objektes der Klasse Geist
screamer = g.Geist("Screamer", 5)
screamer.spuken()
print(screamer)

# Instanziieren eines Objektes der Klasse Schleimgeist
slimey = g.Schleimgeist("Slimey", 8)
slimey.spuken()
print(slimey)

# Instanziieren eines Objektes der Klasse Kannibalengeist
bloodied_squire = g.Kannibalengeist("Bloodies Squire", 3)
bloodied_squire.spuken()
print(bloodied_squire)

# Instanziieren eines Objektes der Klasse Kannibalengeist
fat_maniac = g.Kannibalengeist("Fat Maniac", 3)

# Liste aller Geister erstellen
geister = [bloodied_squire, screamer, slimey, g.Schleimgeist("Nightmare", 4), fat_maniac]

print()
for geist in geister:
    print(geist)

# Instanziieren Geisterjunge Caspar
geisterjunge = g.Geisterjunge("Caspar", 10)
print(geisterjunge)

# Instanziieren Geisterjäger
geisterjaeger = [g.Geisterjaeger("Peter"),
                 g.Geisterjaeger("Ray"),
                 g.Geisterjaeger("Egon")]

print("Spielbeginn")
for jaeger in geisterjaeger:
    print(jaeger)

# # Test für "sichtbar machen"
# geisterjunge.sichtbar_machen(geister[4])
# for geist in geister:
#     print(geist)
# # Test für "Geist fangen"
# geisterjaeger[0].geist_fangen(geister[0])
# for jaeger in geisterjaeger:
#     print(jaeger)

# Spielrunden
for spielrunde in range(0, 10):
    zufall_geist = choice(geister)
    geisterjunge.sichtbar_machen(zufall_geist)

    zufall_jaeger = choice(geisterjaeger)

    zufall_jaeger.geist_fangen(choice(geister))
    if zufall_geist.gefangen:
        geister.remove(zufall_geist)
    else:
        zufall_geist.sichtbar = False


# Spielstand
for jaeger in geisterjaeger:
    print(jaeger)
for geist in geister:
    print(geist)
