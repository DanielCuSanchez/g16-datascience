
class Superhero:
  name = ""
  universe = ""
  image = ""
  powerstats = ""

  def __init__(self, name, universe, image, powerstats):
    self.name = name
    self.universe = universe
    self.image = image
    self.powerstats = powerstats

  def fight(self):
    return print("Superman is fighting! 👊")

  def get_name(self):
    return self.name


superman = Superhero("Superman", "DC Comics", "image.png", "Force")

print(superman.image)
print(superman.name)
print(superman.universe)
print(superman.powerstats)

print(superman.get_name())
