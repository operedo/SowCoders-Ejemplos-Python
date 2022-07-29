# P1

for i in 'string':
  print('P1: '+i)

# P2
palabra=''
print('P2: '+palabra)
for i in 'string':
  palabra=palabra+i
print('P2: '+palabra)

# P3

for i in range(5):
  print('P3: '+str(i))

# P4
counter=1
for i in range(5):
  for j in range(5):
    print('P4: '+str(counter)+' '+str(i+j))
    counter=counter+1

# P5
palabra='string'
counter=0
print('P5: '+str(len(palabra)))
print('P5: '+palabra[0])
print('P5: '+palabra[1])
print('P5: '+palabra[2])
print('P5: '+palabra[3])
print('P5: '+palabra[4])
print('P5: '+palabra[5])
while counter<len(palabra):
  print('P5: '+palabra[counter])
  counter=counter+1

# P6

count = 0 
while (count < 9): 
   print('P6: The count is:', count)
   count = count + 1 

print("P6: Good bye!")

# P7

x = 10
while x>5:
  print("P7: Hello World!",x)
  x-=1
  #x=x-1

# P8

x = 10
while x>5:
  print("P8: Hello World!",x)
  x-=3
  #x=x-3

# P9

x = 1
while x<5:
  print("P9: Hello World!",x)
  x+=4
  #x=x+4
