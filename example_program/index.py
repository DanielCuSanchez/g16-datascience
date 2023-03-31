from password_creator import create_password
# Example program
def main():
  print("Program is running 🏃")
  length = int(input("Ingresa la longitud: "))
  password = create_password(length)
  print(password)


if __name__ == "__main__":
  main()