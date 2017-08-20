# -*- coding: utf-8 -*-

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]

user_answer = input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')

def show_random_quote(my_list):
  	# get a random number
    item = my_list[0] # get a quote from a list
    print(item) # show the quote in the interpreter
    return "program is over" # return value


if user_answer == "B":
	pass
elif user_answer == "C":
	print("C pas la bonne réponse ! Et G pas d’humour, je C...")
else:
# - show another quote
	pass


print(show_random_quote(quotes))