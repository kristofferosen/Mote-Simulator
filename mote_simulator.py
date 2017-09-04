import sched, time
import csv
import requests
import json


print('Posting every 30min to http://192.81.221.165:8085/api/plant')
with open('data.json') as data_file:    
    data = json.load(data_file)

i = 0
s = sched.scheduler(time.time, time.sleep)

def do_something(sc,iterator): 

	print("Posting")
    r = requests.post('http://192.81.221.165:8085/api/plant', auth=('user', 'pass'), data=data[iterator])
    iterator = iterator + 1
    if(i==701):
    	i = 0
    r = requests.post('http://192.81.221.165:8085/api/plant', auth=('user', 'pass'), data=data[iterator])
    iterator = iterator + 1
    if(i==701):
    	i = 0
    r = requests.post('http://192.81.221.165:8085/api/plant', auth=('user', 'pass'), data=data[iterator])
    iterator = iterator + 1
    if(i==701):
    	i = 0
    
    s.enter(1800, 1, do_something, (sc,iterator))


s.enter(1800, 1, do_something, (s,i))
s.run()


