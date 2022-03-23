#list
prenoms = ["Omar","Mahdi","Rym"]
nombres = [1,8,8,9,2,55]
nombres.sort()
print(nombres)
print(prenoms)
print(prenoms[0])
print(prenoms[-2])
prenoms.append("Sana")
print(prenoms)
prenoms.insert(2,"Foulen")
print(prenoms)
prenoms.remove("Foulen")
print(prenoms)
print(prenoms)
#Les tuples
print("--------------------------------------------------")
numbers = (1,2,9,3,7,6,7)
print(numbers)
print(len(numbers))
print(min(numbers))
print(max(numbers))
autre = tuple(prenoms)
print(autre)
#les fonctions
print("--------------------------------------------------")
def greet():
	print("Asslema ")
	print("Omar")
greet()


