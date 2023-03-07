import alphabet

letter_list = alphabet.alphabet_list

def encode(text, shift):
  
  text_list = text.split(" ")
  
  if len(text_list):
    for str in range(0, len(text_list)):
      text_list[str] = list(text_list[str])
      for letter in range(0, len(text_list[str])):
        if text_list[str][letter] in letter_list:
          shiffted_letter = letter_list.index(text_list[str][letter]) + shift
        
          if len(letter_list) - 1 < shiffted_letter:
            
            shiffted_letter = shiffted_letter % len(letter_list)
            shiffted_letter = letter_list[shiffted_letter]
            
          else: 
            shiffted_letter = letter_list[shiffted_letter]
            
          text_list[str][letter] = shiffted_letter
      text_list[str] = ''.join(text_list[str])    
  text_list = ' '.join(text_list)
  print(text_list)

def decode(text, shift):
  text_list = text.split(" ")
  
  if len(text_list):
    for str in range(0, len(text_list)):
      text_list[str] = list(text_list[str])
      for letter in range(0, len(text_list[str])):
        if text_list[str][letter] in letter_list:
          shiffted_letter = letter_list.index(text_list[str][letter]) - shift
          if shiffted_letter < 0:
            
            shiffted_letter = shiffted_letter % len(letter_list)
            shiffted_letter = letter_list[shiffted_letter]
            
          else: 
            shiffted_letter = letter_list[shiffted_letter]
            
          text_list[str][letter] = shiffted_letter
      text_list[str] = ''.join(text_list[str])    
  text_list = ' '.join(text_list)
  print(text_list)
