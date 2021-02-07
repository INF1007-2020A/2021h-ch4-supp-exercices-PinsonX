#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):
	if len(string) % 2 == 0:
		return True


def get_num_char(string, char):
	nb_occurences = 0
	for i in range(len(string)):
		if string[i] == char:
			nb_occurences += 1
	return nb_occurences



def get_first_part_of_name(name):
	premier_nom = ""
	for i in range(len(name)):
		if name[i] == "-" and not 65 <= ord(name[0]) <= 90:
			premier_nom = chr(ord(name[0]) - 32) + name[1:i]
			break
		elif name[i] == "-" :
			premier_nom = name[:i]
			break
	return premier_nom




def get_random_sentence(animals, adjectives, fruits):
	print("Aujourd'hui, j'ai vu un %s s'emparer d'un panier %s plein de %s" % (animals[random.randrange(0, 3)], adjectives[random.randrange(0, 3)], fruits[random.randrange(0, 3)]))


if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
