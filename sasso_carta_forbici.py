# sasso carta forbici --> programma per principianti ; open source.
# implementare interfacccia grafica
import random as r
#inizio programma
print("****************************") 
print("** sasso,carta o forbici! **") #stampa di un semplice menù visivo
print("**************************** \n") 
list=["sasso","carta","forbici"]
while True :# il ciclo si ripete fino a quando l'utente non scrive "no" alla domanda:"Vuoi continuare?"
#da notare che per uscire dal programma l'utente deve giocare almeno una volta 
 
 z=r.choice(list) # scelta del computer dellla propria mossa : "sasso"= sasso, "carta"=carta, "forbici"=forbice
 x=input("Sasso,carta, forbici... \n")# scelta da parte dell'utente 
 print("\n")# riga vuota
 print("Scelta dell'utente: "+x+"\n")
 print("Scelta del computer: "+z+"\n")

 if x=="sasso":
    if z=="sasso":
       print("Pareggio \n")
    elif z=="carta":
        print("Hai perso \n")
    elif z=="forbici":
        print("Hai vinto \n")        
 elif x=="carta":    
    if z=="sasso":
       print("Hai vinto \n")
    elif z=="carta":
        print("Pareggio \n")
    elif z=="forbici":
        print("Hai perso \n")
 elif x=="forbice":   
    if z=="sasso":
       print("Hai perso \n")
    elif z=="carta":
        print("Hai vinto \n")
    elif z=="forbici":
        print("Pareggio \n")
 else: # questa opzione verifica i casi in cui l'utente digiti qualcosa che non sia sasso,carta o forbice 
    print("Attenzione! Scelta non valida.") 
 while True:   
  risposta=input("Vuoi continuare?  ")  
  risposta.lower() 
  if risposta=="si": 
     continue       # se la risposta è si ,il ciclo si ripeterà
  elif risposta=="no":
     exit()    #altrimenti esce dal programma 
  else:
     print("La risposta può essere solo 'si' o 'no'. Riprova. ") # in questo caso sono accettate solo due tipi di risposte            


                                            # github: Alex-html  