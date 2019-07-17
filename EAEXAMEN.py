lista = []
n = int(input(print("ingrese el largo de la lista: ")))
while n < 1:
	n = input(print("ingrese el largo de la lista: "))
for i in range(2, n*2, 2):
	numero = i**3
	lista.append(int(numero))
print(lista[0])
print(lista[1:-1])
print(lista[-1])

