#Open file with readlines
with open("example.csv","r") as file:
  contenido = file.readlines()
header = contenido[0]
rows = contenido[1:]
print(header)
#print(rows)
for row in rows:
  print(row)