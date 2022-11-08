import datetime
import psycopg2
# hier verbind ik met postgres.
conn = ("host='localhost' user='postgres' password='Mohamed2004' dbname='zuil1'")
connector = psycopg2.connect(conn)
verwerken = connector.cursor()

#hier open ik het bestand zodat de zinnen gelezen worden.
bestand = open('zuil.csv', 'r')
lees = bestand.readlines()
print(bestand)
bestand.close()

#hier geef ik de datum van de beoordeling aan
beoordeling_datum = datetime.datetime.now()

#hier vraag ik om de gegevens van de moderator
naam_moderator= input('wat is uw naam?')
email_moderator = input('wat is uw email?')

#hier zorg ik ervoor dat de zinnen gesplitst worden
for a in lees:
    splita = a.split(',')
    bericht = splita[0]
    print(bericht)

#hier controleer ik het bericht
    controle = input('goed gekeurd of af gekeurd? ')
    if controle == 'goed gekeurd':
        print('uw bericht is goed gekeurd. uw klacht wordt nu behandeld')
    elif controle == 'af gekeurd':
        print('uw bericht is af gekeurd. voer een nieuw bericht in')
    else:
        print('ongeldig')

#hier zet ik de gegevens over
    overzetting = """INSERT INTO scherm(
	bericht, naam, datum, steden, beoordeling_datum, naam_moderator, email_moderator, controle)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""

    x = [splita[0], splita[1], splita[2], splita[3], beoordeling_datum, naam_moderator, email_moderator, controle]

    verwerken.execute(overzetting,x)
    connector.commit()

#hier wordt csv bestand leeggemaakt
file = open('zuil.csv', 'w')
delete = file.truncate()
file.close()
print('Alles is klaar!')