# -*- coding: utf-8 -*-
import os.path as path
import os
import json

user_base_dict = {'ban': 0,
             'bt': 0,
             'wordly': 0,
			 'admin': 0,
			 'marks_collect': 0,
			 'city': 0
            }
user = {}
def convert(f):
	user = {}
	"""
	f - object for iteration
	"""
	f = f.readlines(0)
	f = f[0].replace("{", "")
	f = f.replace("}", "")
	list = f.split(",")
	for i in list:
		key_val = i.split(":")
		m = key_val[0].strip('\'')
		m = m.replace("\"", "")
		try:
			user[m] = int(key_val[1].strip('"\''))
		except:
			user[m] = key_val[1].strip('"\'')
	return user

def authorize(user_id: str):
	user_id = str(user_id)
	if not path.exists('base/' + user_id + '.txt'):
		with open('base/' + user_id + '.txt', 'w', encoding="utf-8") as f:
			f.write(json.dumps(user_base_dict).replace(" ", ""))
	if not path.exists('base/' + user_id + 'marks.txt'):
		with open('base/' + user_id + 'marks.txt', 'w', encoding="utf-8") as f:
			pass

	with open('base/' + user_id + '.txt', 'r', encoding="utf-8") as f:
		user = convert(f)

	return user

def update(user_id: str, data: dict = None):
	user_id = str(user_id)
	if data is None:
		data = authorize(user_id)
	os.remove('base/' + user_id + '.txt')
	with open('base/' + user_id + '.txt', 'w', encoding="utf-8") as f:
		f.write(json.dumps(data).replace(" ", ""))

def city_create(user_id: str, data: str):
	if not path.exists('base/' + user_id + "city.txt"):
		with open('base/' + user_id + "city.txt", "w", encoding="utf-8") as f:
			f.write(data)

def city(user_id):
	if not path.exists('base/' + user_id + "city.txt"):
		return None
	else:
		valueprom = []
		user_city = {}
		with open('base/' + user_id + "city.txt", "r", encoding="utf-8") as f:
			f = f.readlines(0)
			#valueprom = f.split("\n")
			for i in f:
				key, value = i.split(":")
				user_city[key] = value.replace("\n", "")
		return user_city

def city_change(user_id: str, city: dict = None):
	info_city = str(city)
	info = info_city.replace("{", "")
	info = info.replace("}", "")
	info = info.replace(" ", "")
	info = info.replace(",", "\n")
	info = info.replace('"', "")
	info = info.replace("'", "")
	print(info)
	with open('base/' + user_id + "city.txt", "w", encoding="utf-8") as f:
		f.write(info)
