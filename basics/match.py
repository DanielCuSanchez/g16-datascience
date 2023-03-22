# switch in python it's equivalent is match
fruit = "🍇"

match fruit:
  case("🍎"):
    print("This is an apple")
  case("🍍"):
    print("This is a pineapple")
  case _:
    print("Default 😆")


