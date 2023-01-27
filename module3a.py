import random
import tkinter
import tkinter as Tk
import requests
import psycopg2
from functools import partial


conn = psycopg2.connect( host="localhost", database="zuil1", port=5432, user="postgres", password="Mohamed2004")
verwerken = conn.cursor()


verwerken.execute("""select Bericht,steden FROM scherm where controle =  'goed gekeurd' order by
                            datum ASC
                      LIMIT 5;
                      """)

weergave = verwerken.fetchall()


a = []
b = []

for c in weergave:
    a.append(c[0] + '\n\n')

for d in weergave:
    b.append(d[1] + '\n')

bericht = ''
for m in a:
    bericht += m

stad = ''
for n in b:
    stad += n

api = "fe517c3f47951f4a367311252c2f96f3"
steden = ['Almere', 'Arnhem','Amersfoort']
city_name = random.choice(steden)
website = "https://api.openweathermap.org/data/2.5/weather?"
volledig = website + 'appid=' + api + '&q=' + city_name + '&units=metric' + '&lang=nl'
aanvraag = requests.get(volledig)
mb = aanvraag.json()


weer = mb['weather'][0]['description']
tempratuur = mb['main']['temp']
vochtigheid = mb['main']['humidity']
gevoels_temp = mb['main']['feels_like']
min_temp = mb['main']['temp_min']
max_temp = mb['main']['temp_max']
wind = mb['wind']['speed']


root = Tk.Tk()
root.title('ns scherm')
root.geometry('1200x600')
root.configure(background='yellow')
#hier maak ik het welkomstbericht
Label = Tk.Label(root, text= 'Welkom bij het Nationaal Spoorwegen!.', font=('Arial', 18), background='yellow', foreground='blue')
Label.pack(padx=20,pady=20)
#hier geef ik het weer aan
weera = Tk.Label(root, text=weer, background='yellow',font=('Arial', 10))
weera.place(x=0,y=0)

#hier geef ik de tempratuur aan
tempratuura = Tk.Label(root, text=(str)(tempratuur)+ ' graden', background='yellow',font=('Arial', 10))
tempratuura.place(x=0,y=20)

#hier geef ik de vochtigheid aan
vochtigheida = Tk.Label(root, text=(str)(vochtigheid)+ ' vochtigheid', background='yellow',font=('Arial', 10))
vochtigheida.place(x=0,y=40)

#hier geef ik gevoelstempratuur aan
gevoels_tempa = Tk.Label(root, text=(str)(gevoels_temp)+ ' gevoelstempratuur', background='yellow',font=('Arial', 10))
gevoels_tempa.place(x=0,y=60)

#hier geef ik minimale tempratuur aan
min_tempa = Tk.Label(root, text=(str)(min_temp)+ ' minimale tempratuur', background='yellow',font=('Arial', 10))
min_tempa.place(x=0,y=80)

#hier geef ik maximale tempratuur aan
max_tempa = Tk.Label(root, text=(str)(max_temp)+ ' maximale tempratuur', background='yellow',font=('Arial', 10))
max_tempa.place(x=0,y=100)

#hier geef ik windsnelheid aan
winda = Tk.Label(root,text=(str)(wind)+ ' windsnelheid', background='yellow',font=('Arial', 10))
winda.place(x=0,y=120)

weergave_bericht =  Tk.Label(root, text= bericht, font=('Arial', 20), background='yellow',)
weergave_bericht.place(x=50, y=220)

weergave_stad = Tk.Label(root, text= stad, font=('Arial', 20), background='yellow')
weergave_stad.place(x=950, y=220)

weergave_titel = Tk.Label(root, text= 'Bericht',font=('Arial', 20), background='yellow', foreground='blue')
weergave_titel.place(x=220, y=160)

weergave_steden = Tk.Label(root, text= 'Stad',font=('Arial', 20), background='yellow', foreground='blue')
weergave_steden.place(x=990, y=160)

root.mainloop()

