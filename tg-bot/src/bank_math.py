# -*- coding: utf-8 -*-
import datetime
import os

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def get_graphic(name: str, time_dict: dict, action: bool = None):
    days = mdates.DayLocator()
    timeFmt = mdates.DateFormatter('%m-%d')
    
    time_list_keys, time_list_values = [], []
    
    for key in time_dict.keys(): time_list_keys.append(key)
    for value in time_dict.values(): time_list_values.append(value)
    
    if action:
        date_list = []
        value_list = []
        
        for i in range(len(time_list_keys)):
            if 'fast$' in time_list_keys[i]:
                date_list.append(time_list_keys[i])
                value_list.append(time_list_values[i])
                
        number = -1
        date_list = [date_list[-7].replace("fast$", ""),
                     date_list[-6].replace("fast$", ""),
                     date_list[-5].replace("fast$", ""),
                     date_list[-4].replace("fast$", ""),
                     date_list[-3].replace("fast$", ""),
                     date_list[-2].replace("fast$", ""),
                     date_list[-1].replace("fast$", "")
                     ]
        value_list = [int(value_list[-7]),
                      int(value_list[-6]),
                      int(value_list[-5]),
                      int(value_list[-4]),
                      int(value_list[-3]),
                      int(value_list[-2]),
                      int(value_list[-1])
                      ]
            
        events = []
        for date in date_list:
            y, m, d = date.split("-")
            events.append(datetime.date(int(y), int(m), int(d)))
            
        fig, ax = plt.subplots()
        plt.grid(True)
        plt.plot(events, value_list)
        ax.xaxis.set_major_locator(days)
        ax.xaxis.set_major_formatter(timeFmt)
        ax.xaxis.set_minor_locator(days)
        
        path = f'{name}fast.png'
        if os.path.exists(path):
            os.remove(path)
        plt.savefig(path)
        
        return path
        
    else:
        start_date, end_date = time_list_keys[-10], time_list_keys[-2]
        start_cost, end_cost = time_list_values[-10], time_list_values[-2]
        start_date = start_date.replace("slow$", "")
        end_date = end_date.replace("slow$", "")
            
        y1, m1, d1 = start_date.split("-")
        y2, m2, d2 = end_date.split("-")
            
        events = [datetime.date(int(y1), int(m1), int(d1)),
                  datetime.date(int(y2), int(m2), int(d2))]
        readings = [int(start_cost), int(end_cost)]
        
        fig, ax = plt.subplots()
        plt.grid(True)
        plt.plot(events, readings)
        ax.xaxis.set_major_locator(days)
        ax.xaxis.set_major_formatter(timeFmt)
        ax.xaxis.set_minor_locator(days)
        
        path = f'{name}slow.png'
        if os.path.exists(path):
            os.remove(path)
        plt.savefig(path)
        
        return path
        
def show_graph(uid: str, name: str) -> str:
    from login import Bank
    from login import get_memory
    
    profile = Bank(uid).get_user_bank()
    
    if profile[name] == 'True': return get_graphic(name, get_memory(name), True)
    else: return get_graphic(name, get_memory(name))