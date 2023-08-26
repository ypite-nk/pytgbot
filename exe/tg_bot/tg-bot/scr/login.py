# -*- coding: utf-8 -*-
import os.path as path
import json, pytz
import datetime

def users_profile_info() -> list:
	with open('base/users_profile.txt', 'r', encoding="utf-8") as f:
		users = f.readlines(0)
		info = []
		for i in users: info.append(i.replace("\n", ""))
		return info

def users_city_info() -> list:
	with open('base/users_city.txt', 'r', encoding="utf-8") as f:
		users = f.readlines(0)
		info = []
		for i in users: info.append(i.replace("\n", ""))
		return info
	
def cost_rubles() -> dict:
	with open("base/costs_r.txt", "r", encoding="utf-8") as file:
		return json.loads("".join(file.readlines(0)))
	
def cost_youshk() -> dict:
	with open("base/costs_y.txt", "r", encoding="utf-8") as file:
		return json.loads("".join(file.readlines(0)))

def budget_get() -> dict:
	if not path.exists("base/bank/budget.txt"):
		with open("base/bank/budget.txt", "r", encoding="utf-8") as file:
			return json.loads("".join(file.readlines(0)))

def budget_write(type_write: str = None, value: any = None) -> None:
	with open("base/bank/budget.txt", "r", encoding="utf-8") as file:
		file = json.loads("".join(file.readlines(0)))
			
		if type_write is None:
			clear_dict = {
				"spend": 0,
				"get": 0
				}
			with open("base/bank/budget.txt", "w", encoding="utf-8") as f: f.write(json.dumps(clear_dict))

		else:
			
			for key in file.keys():
				if key == type_write: file[key] = int(file[key]) + int(value)
		
			with open("base/bank/budget.txt", "w", encoding="utf-8") as budget: budget.write(json.dumps(file))

def actions_update(type_update: str) -> None:
	new_key = type_update + datetime.datetime.now(pytz.timezone('Asia/Irkutsk')).date() # 2023-08-15
		
	keys, values = [], []
	inflation = 4
	
	with open("base/bank/actions.txt", "r", encoding="utf-8") as file: actions = json.loads("".join(file.readlines(0)))

	for key in actions.keys(): keys.append(key)
	for value in actions.values(): values.append(value)
	
	for name, cost in keys, values:
		budget = budget_get()
		budget_write()
		
		# set cost for action
		cost = cost*( (1+inflation) / 100 ) * ( int(budget['get']) - int(budget['spend']) / 100 )
		#
		# re-write function
		with open(f"base/bank/{name}_Memory.txt", "r", encoding="utf-8") as file:
			memory = json.loads("".join(file.readlines(0)))
			memory[new_key] = cost
			
		with open(f"base/bank/{name}_Memory.txt", "w", encoding="utf-8") as file:
			file.write(json.dumps(memory))

class User():
	def __init__(self, uid: str):
		self.uid = uid
		self.path = f"base/{self.uid}.txt"
		self.user_path = f"base/users_profile.txt"

		self.translate_pr_to_dict = {
			"pr_ID":"ID",
			"pr_Nickname":"Никнейм",
			"pr_Name":"Имя",
			"pr_Birthday":"День рождения",
			"pr_Buisness":"Интересы",
			"pr_city":"Город",
			"pr_VIP":"VIP",
			"pr_Rait":"Рейтинг",
			"pr_money":"Юшки",
			"pr_Beta-acc":"Бета-доступ",
			"pr_Lifes":"Попытки"
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
			"Юшки":"pr_money",
			"Бета-доступ":"pr_Beta-acc",
			"Попытки":"pr_Lifes"
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
			"st_buisness":"buisness",
			"st_wordly":"wordly"
			}

		self.translate_dict_to_st = {
			"nickname":"st_nickname",
			"name":"st_name",
			"birthday":"st_birthday",
			"buisness":"st_buisness",
			"wordly":"st_wordly"
			}

		self.translate_ch_to_dict = {
			"ch_nickname":"nickname",
			"ch_name":"name",
			"ch_birthday":"birthday",
			"ch_buisness":"buisness"
			}

		self.translate_dict_to_ch = {
			"nickname":"ch_nickname",
			"name":"ch_name",
			"birthday":"ch_birthday",
			"buisness":"ch_buisness"
			}

		self.user_dict = {
			"pr_ID":self.uid,
			"pr_Nickname":"None",
			"pr_Name":"None",
			"pr_Birthday":"None",
			"pr_Buisness":"None",
			"pr_city":"None",
			"pr_VIP":"None",
			"pr_Rait":0,
			"pr_money":0,
			"pr_Beta-acc":"None",
			"pr_Lifes":1,
			"ct_ban":0,
			"ct_beta":1,
			"ct_admin":0,
			"st_nickname":0,
			"st_name":0,
			"st_birthday":0,
			"st_buisness":0,
			"st_wordly":0,
			"ch_nickname":0,
			"ch_name":0,
			"ch_birthday":0,
			"ch_buisness":0
			}

	def authorize(self) -> None:
		if not path.exists(self.path):
			with open(self.path, "w", encoding="utf-8") as f: f.write(json.dumps(self.user_dict))

			users_uid = users_profile_info()
			users_uid_str = ""
			for i in users_uid:
				users_uid_str += f"{str(i)}\n"

			if self.uid not in users_uid:
				users_uid_str += self.uid

			with open(self.user_path, "w", encoding="utf-8") as f: f.write(users_uid_str)

	def get_user_profile(self) -> dict:
		if not path.exists(self.path): return None
		
		self.dict = {}

		with open(self.path, "r", encoding="utf-8") as file:
			file = json.loads("".join(file.readlines(0)))

			for i in file.keys():
				if "pr_" in i:
					self.dict[self.translate_pr_to_dict[i]] = file[i]

			return self.dict

	def get_user_control(self) -> dict:
		if not path.exists(self.path): return None

		if path.exists(self.path):
			self.dict = {}

			with open(self.path, "r", encoding="utf-8") as file:
				file = json.loads("".join(file.readlines(0)))

				for i in file.keys():
					if "ct_" in i:
						self.dict[self.translate_ct_to_dict[i]] = file[i]

				return self.dict

	def get_user_status(self) -> dict:
		if not path.exists(self.path): return None

		if path.exists(self.path):
			self.dict = {}

			with open(self.path, "r", encoding="utf-8") as file:
				file = json.loads("".join(file.readlines(0)))

				for i in file.keys():
					if "st_" in i:
						self.dict[self.translate_st_to_dict[i]] = file[i]

				return self.dict

	def get_user_change(self) -> dict:
		if not path.exists(self.path): return None

		if path.exists(self.path):
			self.dict = {}

			with open(self.path, "r", encoding="utf-8") as file:
				file = json.loads("".join(file.readlines(0)))

				for i in file.keys():
					if "ch_" in i:
						self.dict[self.translate_ch_to_dict[i]] = file[i]

				return self.dict

	def write_user_profile(self, user_profile_dict: dict) -> None:
		if path.exists(self.path):
			output = {}

			for i in user_profile_dict.keys(): output[self.translate_dict_to_pr[i]] = user_profile_dict[i]
			for i in self.get_user_control().keys(): output[self.translate_dict_to_ct[i]] = self.get_user_control()[i]
			for i in self.get_user_status().keys(): output[self.translate_dict_to_st[i]] = self.get_user_status()[i]
			for i in self.get_user_change().keys(): output[self.translate_dict_to_ch[i]] = self.get_user_change()[i]

			with open(self.path, "w", encoding="utf-8") as file:
				file.write(json.dumps(output))

	def write_user_control(self, user_control_dict: dict) -> None:
		if path.exists(self.path):
			output = {}

			for i in self.get_user_profile().keys(): output[self.translate_dict_to_pr[i]] = self.get_user_profile()[i]
			for i in user_control_dict.keys(): output[self.translate_dict_to_ct[i]] = user_control_dict[i]
			for i in self.get_user_status().keys(): output[self.translate_dict_to_st[i]] = self.get_user_status()[i]
			for i in self.get_user_change().keys(): output[self.translate_dict_to_ch[i]] = self.get_user_change()[i]

			with open(self.path, "w", encoding="utf-8") as file:
				file.write(json.dumps(output))

	def write_user_status(self, user_status_dict: dict) -> None:
		if path.exists(self.path):
			output = {}

			for i in self.get_user_profile().keys(): output[self.translate_dict_to_pr[i]] = self.get_user_profile()[i]
			for i in self.get_user_control().keys(): output[self.translate_dict_to_ct[i]] = self.get_user_control()[i]
			for i in user_status_dict.keys(): output[self.translate_dict_to_st[i]] = user_status_dict[i]
			for i in self.get_user_change().keys(): output[self.translate_dict_to_ch[i]] = self.get_user_change()[i]

			with open(self.path, "w", encoding="utf-8") as file:
				file.write(json.dumps(output))

	def write_user_change(self, user_change_dict) -> None:
		if path.exists(self.path):
			output = {}

			for i in self.get_user_profile().keys(): output[self.translate_dict_to_pr[i]] = self.get_user_profile()[i]
			for i in self.get_user_control().keys(): output[self.translate_dict_to_ct[i]] = self.get_user_control()[i]
			for i in self.get_user_status().keys(): output[self.translate_dict_to_st[i]] = self.get_user_status()[i]
			for i in user_change_dict.keys(): output[self.translate_dict_to_ch[i]] = user_change_dict[i]

			with open(self.path, "w", encoding="utf-8") as file:
				file.write(json.dumps(output))

class City():
	def __init__(self, uid: str):
		self.uid = uid
		self.path = f"base/cities/{uid}.txt"
		self.user_path = f"base/users_city.txt"

		self.city_dict = {
			"pr_cityname":"None",
			"pr_country":"None",
			"pr_subject":"None",
			"pr_create_data":2023,
			"pr_size":1,
			"pr_people":0,
			"pr_mayor":"None",
			"pr_sign":"None",
			"pr_flag":"None",
			"pr_gymn":"None",
			"pr_history":"None",
			"st_cityname":0,
			"st_sign":0,
			"st_flag":0,
			"st_gymn":0,
			"st_history":0,
			"st_mayor":0,
			"dt_budget":70000,
			"dt_energyhave":0,
			"dt_waterhave":0,
			"dt_profit":50000,
			"dt_expense":0,
			"dt_energyexpense":0,
			"dt_waterexpense":0,
			"ch_cityname":0,
			"ch_sign":0,
			"ch_flag":0,
			"ch_gymn":0,
			"ch_history":0,
			"ch_mayor":0
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
			"pr_flag":"Флаг",
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
			"Флаг":"pr_flag",
			"Гимн":"pr_gymn",
			"История":"pr_history"
			}

		self.translate_st_to_dict = {
			"st_cityname":"cityname",
			"st_sign":"sign",
			"st_flag":"flag",
			"st_gymn":"gymn",
			"st_history":"history",
			"st_mayor":"mayor"
			}

		self.translate_dict_to_st = {
			"cityname":"st_cityname",
			"sign":"st_sign",
			"flag":"st_flag",
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

		self.translate_ch_to_dict = {
			"ch_cityname":"cityname",
			"ch_sign":"sign",
			"ch_flag":"flag",
			"ch_gymn":"gymn",
			"ch_history":"history",
			"ch_mayor":"mayor"
			}

		self.translate_dict_to_ch = {
			"cityname":"ch_cityname",
			"sign":"ch_sign",
			"flag":"ch_flag",
			"gymn":"ch_gymn",
			"history":"ch_history",
			"mayor":"ch_mayor"
			}

	def authorize(self) -> bool:
		if not path.exists(self.path):
			with open(self.path, "w", encoding="utf-8") as f: f.write(json.dumps(self.city_dict))

			users_uid = users_city_info()
			users_uid_str = ""
			for i in users_uid:
				users_uid_str += f"{str(i)}\n"

			if self.uid not in users_uid:
				users_uid_str += self.uid

			with open(self.user_path, "w", encoding="utf-8") as f: f.write(users_uid_str)

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
					output[self.translate_st_to_dict[i]] = file[i]

			return output

	def get_city_data(self) -> dict:
		if not path.exists(self.path): return None

		output = {}

		with open(self.path, "r", encoding="utf-8") as file:
			file = json.loads("".join(file.readlines(0)))

			for i in file.keys():
				if "dt_" in i:
					output[self.translate_dt_to_dict[i]] = file[i]

			return output

	def get_city_change(self) -> dict:
		if not path.exists(self.path): return None

		output = {}

		with open(self.path, "r", encoding="utf-8") as file:
			file = json.loads("".join(file.readlines(0)))

			for i in file.keys():
				if "ch_" in i:
					output[self.translate_ch_to_dict[i]] = file[i]

			return output

	def write_city_profile(self, city_profile_dict: dict) -> None:
		if path.exists(self.path):
			output = {}

			for i in city_profile_dict.keys(): output[self.translate_dict_to_pr[i]] = city_profile_dict[i]
			for i in self.get_city_status().keys(): output[self.translate_dict_to_st[i]] = self.get_city_status()[i]
			for i in self.get_city_data().keys(): output[self.translate_dict_to_dt[i]] = self.get_city_data()[i]
			for i in self.get_city_change().keys(): output[self.translate_dict_to_ch[i]] = self.get_city_change()[i]

			with open(self.path, "w", encoding="utf-8") as file:
				file.write(json.dumps(output))

	def write_city_status(self, city_status_dict: dict) -> None:
		if path.exists(self.path):
			output = {}

			for i in self.get_city_info().keys(): output[self.translate_dict_to_pr[i]] = self.get_city_info()[i]
			for i in city_status_dict.keys(): output[self.translate_dict_to_st[i]] = city_status_dict[i]
			for i in self.get_city_data().keys(): output[self.translate_dict_to_dt[i]] = self.get_city_data()[i]
			for i in self.get_city_change().keys(): output[self.translate_dict_to_ch[i]] = self.get_city_change()[i]

			with open(self.path, "w", encoding="utf-8") as file:
				file.write(json.dumps(output))

	def write_city_data(self, city_data_dict: dict) -> None:
		if path.exists(self.path):
			output = {}

			for i in self.get_city_info().keys(): output[self.translate_dict_to_pr[i]] = self.get_city_info()[i]
			for i in self.get_city_status().keys(): output[self.translate_dict_to_st[i]] = self.get_city_status()[i]
			for i in city_data_dict.keys(): output[self.translate_dict_to_dt[i]] = city_data_dict[i]
			for i in self.get_city_change().keys(): output[self.translate_dict_to_ch[i]] = self.get_city_change()[i]

			with open(self.path, "w", encoding="utf-8") as file:
				file.write(json.dumps(output))

	def write_city_change(self, city_change_dict: dict) -> None:
		if path.exists(self.path):
			output = {}

			for i in self.get_city_info().keys(): output[self.translate_dict_to_pr[i]] = self.get_city_info()[i]
			for i in self.get_city_status().keys(): output[self.translate_dict_to_st[i]] = self.get_city_status()[i]
			for i in self.get_city_data().keys(): output[self.translate_dict_to_dt[i]] = self.get_city_data()[i]
			for i in city_change_dict.keys(): output[self.translate_dict_to_ch[i]] = city_change_dict[i]

			with open(self.path, "w", encoding="utf-8") as file:
				file.write(json.dumps(output))
				
class Bank():
	def __init__(self, user_identificator: str):
		self.uid = user_identificator
		self.path = f'base/bank/{self.uid}.txt'
		
		self.profile = User(self.uid).get_user_profile()

		self.bank = {
			"Подписка":"Без подписки",
			"test":0,
			"test_lvl":0,
			"Balance":self.profile['Юшки'],
			"JxSpeed":"False",
			"MacroMotor":"False"
			}
		
	def authorize(self) -> None:
		if not path.exists(self.path):
			with open(self.path, "w", encoding="utf-8") as file: file.write(json.dumps(self.bank))
			
		else: return None
				
	def get_user_bank(self) -> dict:
		if path.exists(self.path):
			with open(self.path, "r", encoding="utf-8") as file: return json.loads("".join(file.readlines(0)))
			
		else: return None
		
	def write_user_bank(self, new_bank_info: dict) -> None:
		if path.exists(self.path):
			with open(self.path, "w", encoding="utf-8") as file: file.write(json.dumps(new_bank_info))
			
		else: return None
		
class Quest():
	def __init__(self, user_identificator: str):
		self._uid = user_identificator
		self.path = f'menu/more/fun/quests/{self._uid}.txt'
		
		self.profile = User(self._uid).get_user_profile()
		
		self.quest_profile = {
			"ID" : self._uid,
			"Первый квест" : "Не пройден",
			"Второй квест" : "Не пройден"
			}
		
	def authorize(self) -> None:
		if not path.exists(self.path):
			with open(self.path, "w", encoding="utf-8") as file: file.write(json.dumps(self.quest_profile))
			
		else: return None
		
	def get_user_quest(self) -> dict:
		if path.exists(self.path):
			with open(self.path, "r", encoding="utf-8") as file: return json.loads("".join(file.readlines(0)))
			
		else: return None
		
	def write_user_quest(self, new_quest_info: dict) -> None:
		if path.exists(self.path):
			with open(self.path, "w", encoding="utf-8") as file: file.write(json.dumps(new_quest_info))
			
		else: return None