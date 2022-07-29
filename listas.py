

lista1=['a','b','c','d']
print('P1: '+str(lista1))

lista2=[1,2,3,4]
print('P2: '+str(lista2))

lista3=['a','b',3,4]
print('P3: '+str(lista3))

print('P4:')
print(lista1[0])
print(lista1[1])
print(lista1[2])
print(lista1[3])

print('P5:')
for i in range(0,4):
  print(lista1[i])

print('P6:')
for i in range(0,len(lista1)):
  print(lista1[i])

print('P7:')
print(lista2)
print(lista2[0])
del lista2[0]
print(lista2)
print(lista2[0])

print('P8:')
print(lista3)
#del lista3
#print(lista3)

print('P9:')
print(lista2)
print(lista2[1])
del lista2[1]
print(lista2)
print(lista2[1])

print('P10:')
print(lista3)
lista3.append('x')
lista3.append('z')
print(lista3)


print('P11:')
lista4=[]
print(lista4)
lista4.append('hola')
print(lista4)

print('P12:')
lista4=[]
print(lista4)
lista4.append('hola')
print(lista4)
del lista4[0]
print(lista4)

