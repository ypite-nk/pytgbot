# -*- coding: utf-8 -*-
import os.path as path
import json

class User():
	"""
	Класс Дата-базы, регулирует:
		Профиль (Profile)- pr_
		Control time - ct_
		Статусы (Status) - st_
	"""
	def __init__(self, uid: str):
		self.uid = uid
		self.path = f"base/{self.uid}.txt"

		self.translate_pr_to_dict = {
			"pr_ID":"ID",
			"pr_Nickname":"Никнейм",
			"pr_Name":"Имя",
			"pr_Birthday":"День рождения",
			"pr_Buisness":"Интересы",
			"pr_city":"Город",
			"pr_VIP":"VIP",
			"pr_Rait":"Рейтинг",
			"pr_Beta-acc":"Бета-доступ"
			}

		self.translate_dict_to_pr = {
			"ID":"pr_ID",
			"Никнейм":"pr_Nickname",
			"Имя":"pr_Name",
			"День рождения":"pr_Birthday",
			"Интересы":"pr_Buisness",
			"Город":"pr_city",
			"VIP":"pr_VIP",
			"Рейтинг":"pr_Rait",
			"Бета-доступ":"pr_Beta-acc"
			}

		self.translate_ct_to_dict = {
			"ct_ban":"ban",
			"ct_beta":"beta",
			"ct_admin":"admin"
			}

		self.translate_dict_to_ct = {
			"ban":"ct_ban",
			"beta":"ct_beta",
			"admin":"ct_admin"
			}

		self.translate_st_to_dict = {
			"st_nickname":"nickname",
			"st_name":"name",
			"st_birthday":"birthday",
			"st_buisness":"buisness"
			}

		self.translate_dict_to_st = {
			"nickname":"st_nickname",
			"name":"st_name",
			"birthday":"st_birthday",
			"buisness":"st_buisness"
			}

		self.user_dict = {
			"pr_ID":self.uid,
			"pr_Nickname":"None",
			"pr_Name":"None",
			"pr_Birthday":"None",
			"pr_Buisness":"None",
			"pr_city":"None",
			"pr_VIP":"None",
			"pr_Rait":"None",
			"pr_Beta-acc":"None",
			"ct_ban":"0",
			"ct_beta":"1",
			"ct_admin":"0",
			"st_nickname":"0",
			"st_name":"0",
			"st_birthday":"0",
			"st_buisness":"0"
			}

	def authorize(self) -> None:
		if not path.exists(self.path):
			with open(self.path, "w", encoding="utf-8") as f: f.write(json.dumps(self.user_dict))

	def get_user_profile(self) -> dict:
		if not path.exists(self.path): self.authorize()
		
		self.dict = {}

		with open(self.path, "r", encoding="utf-8") as file:
			file = json.loads("".join(file.readlines(0)))

			for i in file.keys():
				if "pr_" in i:
					self.dict[self.translate_pr_to_dict[i]] = file[i]

			return self.dict

	def get_user_control(self) -> dict:
		if not path.exists(self.path):
			self.authorize()
		if path.exists(self.path):
			self.dict = {}

			with open(self.path, "r", encoding="utf-8") as file:
				file = json.loads("".join(file.readlines(0)))

				for i in file.keys():
					if "ct_" in i:
						self.dict[self.translate_ct_to_dict[i]] = int(file[i])

				return self.dict

	def get_user_status(self) -> dict:
		if not path.exists(self.path):
			self.authorize()
		if path.exists(self.path):
			self.dict = {}

			with open(self.path, "r", encoding="utf-8") as file:
				file = json.loads("".join(file.readlines(0)))

				for i in file.keys():
					if "st_" in i:
						self.dict[self.translate_st_to_dict[i]] = int(file[i])

				return self.dict

	def write_user_profile(self, user_profile_dict: dict) -> None:
		if path.exists(self.path):
			output = {}

			for i in user_profile_dict.keys(): output[self.translate_dict_to_pr[i]] = str(user_profile_dict[i])
			for i in self.get_user_control().keys(): output[self.translate_dict_to_ct[i]] = self.get_user_control()[i]
			for i in self.get_user_status().keys(): output[self.translate_dict_to_st[i]] = self.get_user_status()[i]

			with open(self.path, "w", encoding="utf-8") as file:
				file.write(json.dumps(output))

	def write_user_control(self, user_control_dict: dict) -> None:
		if path.exists(self.path):
			output = {}

			for i in self.get_user_profile().keys(): output[self.translate_dict_to_pr[i]] = self.get_user_profile()[i]
			for i in user_control_dict.keys(): output[self.translate_dict_to_ct[i]] = str(user_control_dict[i])
			for i in self.get_user_status().keys(): output[self.translate_dict_to_st[i]] = self.get_user_status()[i]

			with open(self.path, "w", encoding="utf-8") as file:
				file.write(json.dumps(output))

	def write_user_status(self, user_status_dict: dict) -> None:
		if path.exists(self.path):
			output = {}

			for i in self.get_user_profile().keys(): output[self.translate_dict_to_pr[i]] = self.get_user_profile()[i]
			for i in self.get_user_control().keys(): output[self.translate_dict_to_ct[i]] = self.get_user_control()[i]
			for i in user_status_dict.keys(): output[self.translate_dict_to_st[i]] = str(user_status_dict[i])

			with open(self.path, "w", encoding="utf-8") as file:
				file.write(json.dumps(output))

def users_info() -> list:
	with open('base/users.txt', 'r', encoding="utf-8") as f:
		users = f.readlines(0)
		info = []
		for i in users: info.append(i.replace("\n", ""))
		return info

class City():
	"""
	Класс Дата-базы, регулирует:
		Профиль (Profile)- pr_
		Статусы изменений (Status) - st_
		Управление (data) - dt_
	"""
	def __init__(self, uid: str):
		self.uid = uid
		self.path = f"base/cities/{uid}.txt"

		self.city_dict = {
			"pr_cityname":"None",
			"pr_country":"None",
			"pr_subject":"None",
			"pr_create_data":"2023",
			"pr_size":"1",
			"pr_people":"0",
			"pr_mayor":"None",
			"pr_sign":"None",
			"pr_gymn":"None",
			"pr_history":"None",
			"st_cityname":"0",
			"st_sign":"0",
			"st_gymn":"0",
			"st_history":"0",
			"st_mayor":"0",
			"dt_budget":"70000",
			"dt_energyhave":"0",
			"dt_waterhave":"0",
			"dt_profit":"50000",
			"dt_expense":"0",
			"dt_energyexpense":"0",
			"dt_waterexpense":"0"
			}

		self.translate_pr_to_dict = {
			"pr_cityname":"Имя",
			"pr_country":"Страна",
			"pr_subject":"Субъект",
			"pr_create_data":"Дата создания",
			"pr_size":"Размер",
			"pr_people":"Население",
			"pr_mayor":"Мэр",
			"pr_sign":"Герб",
			"pr_gymn":"Гимн",
			"pr_history":"История"
			}

		self.translate_dict_to_pr = {
			"Имя":"pr_cityname",
			"Страна":"pr_country",
			"Субъект":"pr_subject",
			"Дата создания":"pr_create_data",
			"Размер":"pr_size",
			"Население":"pr_people",
			"Мэр":"pr_mayor",
			"Герб":"pr_sign",
			"Гимн":"pr_gymn",
			"История":"pr_history"
			}

		self.translate_st_to_dict = {
			"st_cityname":"cityname",
			"st_sign":"sign",
			"st_gymn":"gymn",
			"st_history":"history",
			"st_mayor":"mayor"
			}

		self.translate_dict_to_st = {
			"cityname":"st_cityname",
			"sign":"st_sign",
			"gymn":"st_gymn",
			"history":"st_history",
			"mayor":"st_mayor"
			}

		self.translate_dt_to_dict = {
			"dt_budget":"Бюджет",
			"dt_energyhave":"Электроэнергия",
			"dt_waterhave":"Водоснабжение",
			"dt_profit":"Доход",
			"dt_expense":"Расходы",
			"dt_energyexpense":"Электропотребление",
			"dt_waterexpense":"Водопотребление"
			}

		self.translate_dict_to_dt = {
			"Бюджет":"dt_budget",
			"Электроэнергия":"dt_energyhave",
			"Водоснабжение":"dt_waterhave",
			"Доход":"dt_profit",
			"Расходы":"dt_expense",
			"Электропотребление":"dt_energyexpense",
			"Водопотребление":"dt_waterexpense"
			}

	def authorize(self) -> bool:
		if not path.exists(self.path):
			with open(self.path, "w", encoding="utf-8") as f: f.write(json.dumps(self.city_dict))
			return False
		return True

	def get_city_info(self) -> dict:
		if not path.exists(self.path): return None

		output = {}

		with open(self.path, "r", encoding="utf-8") as file:
			file = json.loads("".join(file.readlines(0)))

			for i in file.keys():
				if "pr_" in i:
					output[self.translate_pr_to_dict[i]] = file[i]

			return output

	def get_city_status(self) -> dict:
		if not path.exists(self.path): return None

		output = {}

		with open(self.path, "r", encoding="utf-8") as file:
			file = json.loads("".join(file.readlines(0)))

			for i in file.keys():
				if "st_" in i:
					output[self.translate_st_to_dict[i]] = int(file[i])

			return output

	def get_city_data(self) -> dict:
		if not path.exists(self.path): return None

		output = {}

		with open(self.path, "r", encoding="utf-8") as file:
			file = json.loads("".join(file.readlines(0)))

			for i in file.keys():
				if "dt_" in i:
					output[self.translate_dt_to_dict[i]] = int(file[i])

			return output

	def write_city_profile(self, city_profile_dict: dict) -> None:
		if path.exists(self.path):
			output = {}

			for i in city_profile_dict.keys(): output[self.translate_dict_to_pr[i]] = str(city_profile_dict[i])
			for i in self.get_city_status().keys(): output[self.translate_dict_to_st[i]] = self.get_city_status()[i]
			for i in self.get_city_data().keys(): output[self.translate_dict_to_dt[i]] = self.get_city_data()[i]

			with open(self.path, "w", encoding="utf-8") as file:
				file.write(json.dumps(output))

	def write_city_status(self, city_status_dict: dict) -> None:
		if path.exists(self.path):
			output = {}

			for i in self.get_city_info().keys(): output[self.translate_dict_to_pr[i]] = self.get_city_info()[i]
			for i in city_status_dict.keys(): output[self.translate_dict_to_st[i]] = str(city_status_dict[i])
			for i in self.get_city_data().keys(): output[self.translate_dict_to_dt[i]] = self.get_city_data()[i]

			with open(self.path, "w", encoding="utf-8") as file:
				file.write(json.dumps(output))

	def write_city_data(self, city_data_dict: dict) -> None:
		if path.exists(self.path):
			output = {}

			for i in self.get_city_info().keys(): output[self.translate_dict_to_pr[i]] = self.get_city_info()[i]
			for i in self.get_city_status().keys(): output[self.translate_dict_to_st[i]] = self.get_city_status()[i]
			for i in city_data_dict.keys(): output[self.translate_dict_to_dt[i]] = str(city_data_dict[i])

			with open(self.path, "w", encoding="utf-8") as file:
				file.write(json.dumps(output))