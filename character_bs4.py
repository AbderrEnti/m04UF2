#!/usr/bin/python3

from bs4 import BeautifulSoup

file = open('characters.facx','r')
soup = BeautifulSoup(file, 'xml')
characters = soup.find_all("character")
file.close()
file_weapons = open('weapons.faw','r')
soup_weapons = BeautifulSoup(file_weapons, 'xml')
weapons = soup_weapons.find_all("weapon")
file_weapons.close()
file_character_weapons = open('characters_weapons.facwx', 'r')
soup_character_weapons = BeautifulSoup(file_character_weapons, 'xml')
character_weapons = soup_character_weapons.find_all("character_weapon")
file_character_weapons.close()
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

opcion = input("\n¿Qué deseas hacer? (1. Matar, 2. Mostrar items del personaje escogido, 3. Mostrar daño del personaje): ")
if opcion == '1':
	characters = [char for char in characters if hasattr(char, 'get') and char.get('id') != id]
	with open('characters.facx', 'w') as file:
		file.write(soup.prettify())
	print("El personaje ha sido eliminado.")
elif opcion == '2':
		file = open('characters_items.facix', 'r')
		soup = BeautifulSoup(file, 'xml')
		file.close()
		characters_items = soup.find_all('character_item')
		items_ids = []
		for character_item in characters_items:	
			if character_item.find("character")["id"] == id:
				id_item = character_item.find("name")["id"]
				items_ids.append(id_item)
		if len(items_ids) <= 0:
			print("El personaje no tiene item")
			exit()
		file = open('characters_items.facix', 'r')
		soup = BeautifulSoup(file, 'xml')
		file.close()
		items = soup.find_all('item', {'id':True})
		print("\tItems:")
		for item in items:
			if item['id'] in  items_ids:
				print(item.find("item").text)
elif opcion =='3':
	damage_total = 0
	for character_weapon in character_weapons:
		if character_weapon.find("character")['id'] == id:
			weapon_id = character_weapon.find("weapon")['id']
			for weapon in weapons:
				if weapon['id'] == weapon_id:
					damage_total += int(weapon.find("damage").text)
	print(f"\tDaño total del personaje: {damage_total}")
