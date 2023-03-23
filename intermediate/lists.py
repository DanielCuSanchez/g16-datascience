# Lists: They are indexed, they can have duplicated values and they can be ordered, changeable


fruits = ["🍍", "🍇", "🍉", "🥝", "🥝", "🥝"]

#type() this function returns the class of the object

print(fruits)
print(type(fruits))

print(len(fruits))

for x in range(len(fruits)):
  print(fruits[x])
  fruits[x] = "🥭"
  print(fruits[x])

print(fruits)

