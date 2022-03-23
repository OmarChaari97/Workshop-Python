#Les chaines
workshop = "Botnets and Iot Security"
print(workshop.upper())
print(workshop.lower())
print(workshop)

#Existance d'une sous chaine dans une chaine
print(workshop.find('and'))
#and ---> & 
print(workshop.replace('and','&'))
print(workshop)

a = 'bonjour'
prenom = 'omar'
mes = '{},{}, dans botnets'.format(a,prenom)
print(mes)