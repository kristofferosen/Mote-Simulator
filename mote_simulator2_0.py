
import sched, time
import csv
import requests
import json
from random import randint

NUMBER_OF_AREAS = 2
NUMBER_OF_MOTES = 50
AREAS = []
DATA_SETS = []
DATA_FILES = ["data2_1.json","data2_1.json","data2_1.json"]
LIMITS = []
ITERATORS = []
#AREA_NAMES = ["Backyard 1", "Backyard 2", "Green House 1","Green House 2", "Green House 3", "Corn Field 1", "Cornfield 2", "Living Room", "Basement"]
#AREAS_NAMED = []

for i in range(len(DATA_FILES)):
	with open(DATA_FILES[i]) as data_file:
		data = json.load(data_file)    
		DATA_SETS.append(data)
		LIMITS.append(len(data)-2)





for i in range(NUMBER_OF_AREAS):
	print(str(i))
	AREAS.append(randint(0, len(DATA_SETS)))
	ITERATORS.append(2)
	#AREAS_NAMED.append(AREA_NAMES[i])

print(AREAS)

s = sched.scheduler(time.time, time.sleep)



def emitt(): 
	for i in range(NUMBER_OF_AREAS):
		print("Area: " + str(i))
		for j in range(NUMBER_OF_MOTES):
			
			rand = randint(-1, 1)
			reading = DATA_SETS[AREAS[i]][ITERATORS[i]+rand]
			datastring = "{\"area\":\""+str(i)+"\", \"mote\":\""+str(j)+"\", \"soilMoisture\":\"" + reading.get("soilMoisture") + "\", \"soilTemperature\":\"" + reading.get("soilTemperature") + "\", \"numberOfAreas\":\""+str(NUMBER_OF_AREAS)+"\", \"numberOfMotes\":\""+ str(NUMBER_OF_MOTES)+"\"}"
			
			
			dataobject = json.loads(datastring)

			if(j== 10):
				#print("mote: " + str(j) +" Reads: "+ reading.get("soilMoisture"))
				print(dataobject)


			#print(reading)
			r = requests.post('http://192.81.221.165:81/api/datapoint2', auth=('user', 'pass'), data=dataobject)

		ITERATORS[i] = ITERATORS[i] + 1

		if (LIMITS[AREAS[i]] == ITERATORS[i]):
			ITERATORS[i] = 2
	s.enter(10, 1, emitt,())

#emitt()
s.enter(1, 1, emitt,())
s.run()	