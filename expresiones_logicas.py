
# problema 1

# Quiero que escriba una sentencia sencilla en 
# la que, si el valor de una variable es igual a 
# 5, imprima que indica que esta variable es igual 
# a 5. Establezca la variable en 5.

var=5
if var==5:
  print('P1: variable var es igual a 5')

# problema 2

# Quiero que escriba una sentencia sencilla en la
# que si el valor de una variable es igual a 5,
# imprima «Esta variable es igual a 5!». Establezca
# la variable en 5. Quiero que escribas una
# declaración IF ELSE que diga, si una variable es
# igual a 5, imprime "¡Esto es genial!" y de lo
# contrario imprime "¡Esto es malo!" Haz que tu
# variable sea igual a 3.

var=5
if var==5:
  print('P2: Esta variable es igual a 5!')

var=3
if var==5:
  print('P2: ¡Esto es genial!')
else:
  print('P2: ¡Esto es malo!')

# Problema 3

# ¡Venga con su propia lógica de sentencia IF! 
# Esto debe anidarse y utilizar ELIF.

var=-1
if var==5:
  print('P3[T]: ¡Esto es genial!')
  if var>2:
    print('P3[T]: var>2')
  elif var<0:
    print('P3[T]: var<0')
  else:
    print('P3[T]: var<=2 and var>=0')
else:
  print('P3[F]: ¡Esto es malo!')
  if var>10:
    print('P3[F]: var>2')
  elif var<0:
    print('P3[F]: var<0')
  else:
    print('P3[F]: var<=10 and var>=0')
