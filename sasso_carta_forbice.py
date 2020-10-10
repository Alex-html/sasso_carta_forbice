# sasso carta forbice --> programma per principianti ; open source.
# implementare interfacccia grafica
import random as r
#inizio programma
print("****************************") 
print("** sasso,carta o forbice! **") #stampa di un semplice menù visivo
print("**************************** \n") 
while True : # ciclo che si ripete fino a quando l'utente da in input parole o caratteri diversi da "si"
 
 z=r.randint(1,3) # scelta del computer dellla propria mossa : 1= sasso, 2=carta, 3=forbice
 x=input("Sasso,carta, forbice... \n")# scelta da parte dell'utente 
 if q=="sasso":
    if z==1:
       print("pareggio \n")
    elif z==2:
        print("Hai perso \n")
    elif z==3:
        print("Hai vinto \n")        
 elif q=="carta":    
    if z==1:
       print("Hai vinto \n")
    elif z==2:
        print("Pareggio \n")
    elif z==3:
        print("Hai perso \n")
 elif q=="forbice":   
    if z==1:
       print("Hai perso \n")
    elif z==2:
        print("Hai vinto \n")
    elif z==3:
        print("Pareggio \n")
 else: # questa opzione verifica i casi in cui l'utente digiti qualcosa che non sia sasso,carta o forbice 
    print("Attenzione! Scelta non valida.") 
 risposta=input("Vuoi continuare?  ")  
 risposta.lower() 
 if risposta=="si": 
     continue       # se la risposta è si ,il ciclo si ripeterà
 else:
     exit()    #altrimenti esce dal programma       


                                            # github: Alex-html  