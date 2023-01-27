import random
import datetime

#hier wordt het bericht gevraagd
bericht = input('wat is uw bericht? ')
while len(bericht) >= 140:
    bericht = input('Bericht is te lang, probeer het opnieuw.')
datum = datetime.datetime.now()
#hier wordt de naam gevraagd
naam = input('wat is uw naam? ')
if naam == '':
    naam = 'anoniem'
elif ',' in naam:
    print('uw naam mag geen komma bevatten, probeer het nog een keer')
else:
    print(naam)
steden = ['Arnhem', 'Almere', 'Amersfoort']

#hier wordt een random stad gekozen
waarde = random.choice(steden)
print(waarde)
print('uw bericht wordt gecontroleerd door de moderator.')
#hier open ik de csv en schrijf ik de waarden in
csv = open('zuil.csv', 'a')
csv.write('{},{},{},{}\n'.format(bericht, naam, datum, waarde))
csv.close()







