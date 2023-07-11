# -*- coding: utf-8 -*-
import os.path as path
import os
import json

user_base_dict = {'ban': 0,
             'bt': 0,
             'wordly': 0,
			 'admin': 0
            }
user = {}
def convert(f):
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
		user[m] = int(key_val[1].strip('"\''))
	return user

def authorize(user_id: str):
	global user
	user_id = str(user_id)
	if not path.exists('base/' + user_id + '.txt'):
		with open('base/' + user_id + '.txt', 'w') as f:
			f.write(json.dumps(user_base_dict).replace(" ", ""))
	if not path.exists('base/' + user_id + 'marks.txt'):
		with open('base/' + user_id + 'marks.txt', 'w') as f:
			pass

	with open('base/' + user_id + '.txt', 'r') as f:
		return convert(f)

def update(user_id: str, data: dict = None):
	user_id = str(user_id)
	if data is None:
		data = authorize(user_id)
	os.remove('base/' + user_id + '.txt')
	with open('base/' + user_id + '.txt', 'w') as f:
		f.write(json.dumps(data).replace(" ", ""))