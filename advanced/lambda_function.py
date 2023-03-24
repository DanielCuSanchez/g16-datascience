# Lambda: Is a reserved word for using to create shorter versions of functions.


def sum(n1, n2):
  return n1 + n2

# sum = (n1, n2) =>  n1+n2
sum_lambda = lambda n1,n2 : n1 + n2

print(sum(2, 10))
print(sum_lambda(2, 10))

# Ejemplo 1
def molde_principal( modelo ):
  #  equivalent in JS `${variable_1} lo que sea ${variable_2}`
  return lambda version : f'El modelo base es {modelo} y la version es {version}. '

mazda3 = molde_principal("Mazda 3")
mazda2 = molde_principal("Mazda 2")

print(mazda2('hatchback 🚗'))
print(mazda2('sedan'))

print(mazda3('hatchback 🚙'))
print(mazda3('sedan ST'))
print(mazda3('sedan EX'))
print(mazda3('sedan LX'))


# Ejemplo 2

def tabla(numero):
  return lambda x :  f' {numero} x {x} = {x * numero}'

tabla_2 = tabla(2)
tabla_3 = tabla(3)
tabla_4 = tabla(4)

for x in range(1, 11):
  print(tabla_2(x))
  print(tabla_3(x))
  print(tabla_4(x))