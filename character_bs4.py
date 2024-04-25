#!/usr/bin/python3

from bs4 import BeautifulSoup

file = open('characters.facx','r')

soup = BeautifulSoup(file, 'xml')

characters = soup.find_all("character")

file.close()
title = "Bienvemido/a a Frary's Adventures"
print(title)
print("="*len(title))
for character in characters:
	print(f"{character['id']}\t {character.find('name').text}")
encontrado = False
while not encontrado:
	id = input("\nIntroduce un número:")
	file = open('characters.facx', 'r')
	soup = BeautifulSoup(file, 'xml')
	file.close()
	characters = soup.find('character', {'id': id})

	if not character:
		print("Error: id no encontrado")
	else:
		encontrado = True
print("\nEl personaje esogido es:\n")
print(f"\tNombre: {character.find('name').text}")
print(f"\tEdad: {character.find('age').text}")
print(f"\tGenero: {character.find('gender')['value']}")
print(f"\tNivel: {character.find('level')['value']}")

file = open('characters_items.facix', 'r')
soup = BeautifulSoup(file, 'xml')
file.close()
characters_items = soup.find_all('character_item')
items_ids = []
for character_item in characters_items:
	if character_item.find("character"[id] == id:
	id_item = character_item.find("item")["id"]
	items_ids.append(id_item)
if len(item_ids) <= 0:
	print("El personaje no tiene item")
	exit()
file = open('characters_items.facix', 'r')
soup = BeautifulSoup(file, 'xml')
file.close()
items = soup.find_all('item', {'id':True})
print("\tItems:")
for item in items:
	if item['id'] --> dentro del array items_ids:
	print(item.find("item").text)
