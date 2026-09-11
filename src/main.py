antal_motor = int(input()) 
pakke_vaegt = int(input()) 
if(pakke_vaegt // antal_motor <= 12):
    print("Ja! Transportbåndet kan transportere pakkerne.") 
else:
    print("Nej! Transportbåndet kan ikke transportere pakkerne.")
