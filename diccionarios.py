
print('P1:')
lengua_espanola={
  'abeja': 'Insecto que poliniza flores y crea miel.',
  'amarillo': 'Color primario de tonos brillantes',
  'zorro': 'Animal mamifero de climas templados con pelaje'
}

print(lengua_espanola)

print('P2:')
print(lengua_espanola['abeja'])

print('P3:')
lengua_espanola2={
  'zorro': 'Animal mamifero de climas templados con pelaje',
  'abeja': 'Insecto que poliniza flores y crea miel.',
  'amarillo': 'Color primario de tonos brillantes'
}
print(lengua_espanola2['abeja'])

print('P4:')

mapamundi={
  'panama': 1000,
  'chile': 'Cordillera',
  'colombia': 'A',
  'venezuela': [0,1,2,3],
  'brasil': {'rio':200, 'belo':500}
}

print(mapamundi)
mapamundi['argentina']=5000
print(mapamundi)

print('P5:')
print(mapamundi)
del mapamundi['argentina']
print(mapamundi)

print('P6:')
for key in mapamundi.keys():
  print(key)

print('P7:')
for val in mapamundi.values():
  print(val)

print('P8:')
for key in mapamundi.keys():
  if key[0]=='c':
    print(key+' : '+mapamundi[key])

print('P9:')
for key in mapamundi.keys():
  if len(key)==6:
    #print(key)
    print(key+' : '+str(mapamundi[key]))

print('P10:')
for key in mapamundi.keys():
  if key=='brasil':
    for key2 in mapamundi[key].keys():
      print(key2+' : '+str(mapamundi[key][key2]))
