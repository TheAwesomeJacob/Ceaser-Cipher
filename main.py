import coder_fun

shiffted_letter = ""
cont = True

while cont:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction == "encode":
    coder_fun.encode(text, shift)
  elif direction == "decode":
    coder_fun.decode(text, shift)
  else:
    print("Wrong value!") 

  want_cont = input("Do you want again? Type 'yes' or 'no':\n")
  if want_cont == "no":
    cont = False
    print("Goodbye!")