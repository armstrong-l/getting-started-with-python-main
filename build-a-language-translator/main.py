translations = {
  "hello":"hola",
  "thank you":"gracias",
  "sorry":"lo siento",
  "good morning":"buenos dias",
  "good evening":"buenas noches",
  "goodbye":"chau",
  "see you later":"hasta luego",
  "name":"nombre",
  "cat":"gato",
  "dog":"perro"
}

done = False

print('Type "done" at any time to exit')

while not done:
  word = input("Please enter an English word to translate: ")
  word = word.lower()
  if word == "done":
    done = True
  elif word in translations:
    print(word + " is " + translations[word])
  else:
    print("Sorry, this word is not in the dictionary")