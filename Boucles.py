#Boucle Si
temperature = 5
if temperature > 22:
	print("Chaud")
elif (temperature> 15) and (temperature <=22):
	print("Adéquat")
else:
	print("froid")
# K  (hauteur /0.45) | L (hauteur *0.45) 
hauteur = input("Donnez votre hauteur : ")
choix = input("Donnez votre choix : ")	
if choix.upper() == "K":
	print(float(hauteur) / 0.45)
elif choix.upper() == "L":
	print(float(hauteur) * 0.45)
else:
	print("Choix inconnu")
#boucle for
for i in range(5):
	print("bonjour")
#boucle while
i = 1 
while(i <= 5):
	print("Asslema")
	i = i+1

