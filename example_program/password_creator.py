import random
import hashlib

def create_password(length):
  capital_letters = ('A',  'B',  'C',  'D',  'E',  'F',  'G',  'H',  'I',  'J',  'K',  'L',  'M', 'N','Ñ','O','P','Q','R','S','T','U','V','X','Y','Z')
  lower_case = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z')
  numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
  symbols = ('*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"', " ")
  combinations = capital_letters + lower_case + numbers + symbols
  password = []
  for i in range(length):
    char = random.choice(combinations)
    password.append(char)
  print("".join(password))
  hash_p = hashlib.md5("".join(password).encode())
  return hash_p.hexdigest()

