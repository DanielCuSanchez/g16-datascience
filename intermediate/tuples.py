# Tuples are unchangeable and ordered, it accepts duplicated values

myTuple = (2.3, 4.5, 1.2, 6.7, 8.0, 8.0)

print(type(myTuple))
# myTuple[3] = 6.9
print(myTuple)

for x in range(len(myTuple)):
  print(myTuple[x])

print("---------------------------")

for x in myTuple:
  print(x)