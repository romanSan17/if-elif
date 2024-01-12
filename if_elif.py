from random import *
nimi=input("Mis on sinu nimi?").capitalize()
print ("Tere,",nimi)
if nimi=="Juku":
    print("Lahme kinno")
    age=int(input("Kui vana sa oled?"))
    if age<0 or age>100:
    pilet="valed vanus"
    elif 0<age<6:
    pilet="free ticket"
    elif 6<=age<14:
    pilet="lapse pilet"
    elif 14<=age<65:
    pilet="täispilet"
    elif age<=100:
    pilet="sooduspilet"
    print(pilet) #Ilus ja õige vastus! "Vale vanus" või "On vaja osta..."

else:
    print("Ma ootan Jukut")









#protsent=randint(-100,500) #0-100 0-60(2) 61-75(3) 76-89(4) 90-100(5)
#print(protsent,"% on testi tulemus")
#if protsent<0 or protsent>100:
#    tulemus="valed andmed"
#elif 0<protsent<60:
#    tulemus="hinne 2"
#elif 60<=protsent<75:
#    tulemus="hinne 3"
#elif 75<=protsent<90:
#    tulemus="hinne 4"
#else:   #=elif 90<=protsent<100:
#    tulemus="hinne 5"
#print (tulemus)



#arv=randint(0,100)  #juhuslik täisarv vahemikust 0...100
#if arv%2==0:
#    print(arv,"on paaris arv")
#else:
#    print(arv,"on paaritu arv")
#print()



#print("Tund on alanud")
#hilinemine=input("Kas õpilane on hilinenud?") #"JAH"-a.upper(), "jah"-a.lower, Yah, yAH
#if hilinemine.upper()=="JAH":
#    print("Õpilane ootab 30 min")
#print("Õpilane astub klassi")

