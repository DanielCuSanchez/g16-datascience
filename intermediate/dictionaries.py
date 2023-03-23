# Dictionaries: They are similar like objects in JS, the way the data is stored is with keys and values.

countries = {
  1:{
    "name": "Mexico",
    "flag": "🚩",
    "continent": "America"
  },
  2: {
      "name": "Marruecos",
      "flag": "🏴",
      "continent": "Africa"
  },
  3: {
      "name": "Spain",
      "flag": "🎏",
      "continent": "Europe"
  },
  4: {
      "name": "Portugal",
      "flag": "🚩",
      "continent": "Europe"
  }
}

print(type(countries))
print(len(countries))

# Get a specific key
#print(countries.get(3))

for key in countries.keys():
  print(key)

for value in countries.values():
  print(value)

for key, value in countries.items():
  print(key, value)

for key in countries:
  print(countries[key])

#for x in range(len(countries)):
  #print(countries[x])
