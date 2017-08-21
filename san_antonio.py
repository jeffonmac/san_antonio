# -*- coding: latin-1 -*-
import random

quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
          "On doit pouvoir choisir entre s'écouter parler et se faire entendre."]

characters = ["alvin et les Chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté", "Kirikou"]

# get a quote from a list fonction
def get_random_item(object_list):
    rand_numb = random.randint(0, len(object_list) - 1)
    item = object_list[rand_numb]  # get a quote from a list
    return item  

# capitalize fonction
def capitaliz(word):
    return word.capitalize()

# Format a sentence fonction
def message(character, quote):
    return "{} a dit : {}".format(capitaliz(character), capitaliz(quote))

# The sentence at the launch of the program
user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")

# Loop to generate sentences
while user_answer != "B":
    print(message(get_random_item(characters), get_random_item(quotes)))
    user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")