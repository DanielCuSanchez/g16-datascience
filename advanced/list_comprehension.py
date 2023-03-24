# Lists comprehensions: They are a shorter version of a list declaration, it is used to filter, modify and remove data.

cars_list = ["Mazda 3", "Sentra", "Corolla", "Fusion", "Civic", "Civic", "Civic"]

new_list = [ car for car in cars_list if car == "Civic" ]

print(cars_list)
print(new_list)

squares = [i * i for i in range(10)]
pares = [i for i in range(0,100,2)]

print(squares)
print(pares)