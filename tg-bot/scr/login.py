# -*- coding: utf-8 -*-
import os.path as path
import os
import json

user_base_dict = {'ban': 0,
             'bt': 0,
             'wordly': 0,
			 'admin': 0,
			 'marks_collect': 0
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
		#print(i, i//2)
		if i//2 != 0 and i//2 != (i-1)//2:
			return_info += all_info[i-1] + "\n"
		else:
			return_info += all_info[i-1] + ":"

	return return_info

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

def city_create(user_id: str, info: str, status: str, data: str):
	if not path.exists('base/cities/' + user_id + "city.txt"):
		with open('base/' + user_id + "city.txt", "w", encoding="utf-8") as f:
			f.write(info)
		with open('base/' + user_id + "city_status.txt", "w", encoding="utf-8") as f:
			f.write(status)
		with open('base/' + user_id + "city_data.txt", "w", encoding="utf-8") as f:
			f.write(data)

def authorize_city(user_id: str):
	if not path.exists('base/cities/' + user_id + "city.txt"):
		return None
	else:
		user_city = {}
		with open('base/cities/' + user_id + "city_status.txt", "r", encoding="utf-8") as f:
			f = f.readlines(0)
			for i in f:
				key, value = i.split(":")
				user_city[key] = int(value.replace("\n", ""))
		return user_city

def city_info(user_id: str):
	if not path.exists('base/cities/' + user_id + "city.txt"):
		return None
	else:
		user_city = {}
		with open('base/cities/' + user_id + "city.txt", "r", encoding="utf-8") as f:
			f = f.readlines(0)
			for i in f:
				key, value = i.split(":")
				user_city[key] = value.replace("\n", "")
		return user_city

def city_data(user_id: str):
	if not path.exists('base/cities/' + user_id + 'city_data.txt'):
		return None
	else:
		city_data = {}
		with open('base/cities/' + user_id + 'city_data.txt', 'r', encoding='utf-8') as f:
			f = f.readlines(0)
			for i in f:
				key, value = i.split(":")
				city_data[key] = value.replace("\n", "")
		return city_data

def city_change(user_id: str, city: dict):
	info = replaced(str(city))
	with open('base/cities/' + user_id + "city.txt", "w", encoding="utf-8") as f:
		f.write(info)

def city_status_change(user_id: str, status: dict):
	info = replaced(str(status))
	with open('base/cities/' + user_id + "city_status.txt", "w", encoding="utf-8") as f:
		f.write(info)

def city_data_change(user_id: str, data: dict):
	info = replaced(str(data))
	with open('base/cities/' + user_id + "city_data.txt", "w", encoding="utf-8") as f:
		f.write(info)