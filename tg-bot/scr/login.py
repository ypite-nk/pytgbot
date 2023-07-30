# -*- coding: utf-8 -*-
import os.path as path
import os
import json

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

def replaced(info):
	info = info.replace("{", "").replace("}", "")
	infos = info.split(", ")
	all_info = []
	return_info = ""
	for i in infos:
		ni = i.split(": ")
		for i in ni:
			all_info.append(i.replace("'", "").replace('"', ''))
	for i in range(len(all_info)):
		i += 1
		if i//2 != 0 and i//2 != (i-1)//2:
			return_info += all_info[i-1] + "\n"
		else:
			return_info += all_info[i-1] + ":"

	return return_info

def json_reworking(info: list, uid: str = '0'):
	users = []

	for i in info:
		users.append(i.replace("\n", ""))
	if uid not in users:
		users.append(uid)
	return users

def authorize(user_id: str):
	user_id = str(user_id)

	user_base_dict = {
		'ban': 0,
		'bt': 0,
		'wordly': 0,
		'admin': 0,
		'marks_collect': 0,
		'city': 0
		}

	if not path.exists(f'base/{user_id}.txt'):
		with open(f'base/{user_id}.txt', 'w', encoding="utf-8") as f:
			f.write(json.dumps(user_base_dict).replace(" ", ""))

	if not path.exists(f'base/{user_id}marks.txt'):
		with open(f'base/{user_id}marks.txt', 'w', encoding="utf-8") as f:
			pass

	with open(f'base/{user_id}.txt', 'r', encoding="utf-8") as f:
		user = convert(f)

	with open('base/users.txt', 'r', encoding="utf-8") as f:
		users = f.readlines(0)

	users = json_reworking(users, user_id)
	users = '\n'.join(users)

	with open('base/users.txt', 'w', encoding="utf-8") as f:
		f.write(users)

	if not path.exists(f'base/{user_id}user.txt'):
		with open(f'base/{user_id}user.txt', 'w', encoding='utf-8') as f:
			f.write(f"ID:{user_id}\nНикнейм:Нет\nИмя:Нет\nДень рождения:Нет\nИнтересы:Нет\nVIP:Нет\nРейтинг:Нет\nБета-доступ:Нет\nСтатус:Нет")
		with open(f'base/{user_id}user_status.txt', 'w', encoding='utf-8') as f:
			f.write("nickname:0\nname:0\nbirthday:0\nbuisness:0")

	return user

def update(user_id: str, data: dict = None):
	if data is None:
		data = authorize(str(user_id))
	with open('base/' + str(user_id) + '.txt', 'w', encoding="utf-8") as f:
		f.write(json.dumps(data).replace(" ", ""))

def user(user_id: str):
	with open(f'base/{user_id}user.txt', 'r', encoding='utf-8') as f:
		user = {}
		for i in f.readlines(0):
			key, value = i.split(":")
			user[key] = value.replace("\n", "")
		return user

def user_change(user_id: str, data: dict):
	with open(f"base/{user_id}user.txt", "w", encoding="utf-8") as f: f.write(replaced(str(data)))

def users_info():
	with open('base/users.txt', 'r', encoding="utf-8") as f:
		users = json_reworking(f.readlines(0))
		return users

def user_status(user_id: str):
	with open(f'base/{user_id}user_status.txt', 'r', encoding='utf-8') as f:
		user_status = {}
		for i in f.readlines(0):
			key, value = i.split(":")
			user_status[key] = int(value.replace("\n", ""))
		return user_status

def user_status_change(user_id: str, data: dict):
	with open(f'base/{user_id}user_status.txt', 'w', encoding='utf-8') as f: f.write(replaced(str(data)))

def city_create(user_id: str, info: str, status: str, data: str):
	with open('base/cities/' + user_id + "city.txt", "w", encoding="utf-8") as f: f.write(info)
	with open('base/cities/' + user_id + "city_status.txt", "w", encoding="utf-8") as f: f.write(status)
	with open('base/cities/' + user_id + "city_data.txt", "w", encoding="utf-8") as f: f.write(data)

def authorize_city(user_id: str):
	if not path.exists(f'base/cities/P{user_id}city.txt'): return None
	else:
		with open(f'base/cities/P{user_id}city.txt', "r", encoding="utf-8") as f:
			user_city = {}
			for i in f.readlines(0):
				key, value = i.split(":")
				user_city[key] = value.replace("\n", "")
			return user_city

def city_status(user_id: str):
	if not path.exists(f'base/cities/{user_id}city_status.txt'): return None
	else:
		with open(f'base/cities/{user_id}city_status.txt', "r", encoding="utf-8") as f:
			user_city = {}
			for i in f.readlines(0):
				key, value = i.split(":")
				user_city[key] = int(value.replace("\n", ""))
			return user_city

def city_data(user_id: str):
	if not path.exists(f'base/cities/{user_id}city_data.txt'): return None
	else:
		with open(f'base/cities/{user_id}city_data.txt', 'r', encoding='utf-8') as f:
			city_data = {}
			for i in f.readlines(0):
				key, value = i.split(":")
				city_data[key] = int(value.replace("\n", ""))
			return city_data

def city_change(user_id: str, city: dict):
	with open(f'base/cities/{user_id}city.txt', 'w', encoding='utf-8') as f: f.write(replaced(str(city)))

def city_status_change(user_id: str, status: dict):
	with open(f'base/cities/{user_id}city_status.txt', 'w', encoding='utf-8') as f: f.write(replaced(str(status)))

def city_data_change(user_id: str, data: dict):
	with open(f'base/cities/{user_id}city_data.txt', 'w', encoding='utf-8') as f: f.write(replaced(str(data)))