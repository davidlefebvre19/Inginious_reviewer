import sqlite3



def list_of_tuples_id_tasks_with_succes_number_sorted():
	conn = sqlite3.connect('schema.sqlite')
	cursor = conn.cursor()

	succes_frequency = {}

	for row in cursor.execute("SELECT DISTINCT task FROM submissions"):
		succes_frequency[row[0]] = None
	for row in cursor.execute("SELECT task, result FROM submissions WHERE result LIKE '%succes%'"):
		if succes_frequency[row[0]] == None:
			succes_frequency[row[0]] = 1
		else :
			succes_frequency[row[0]] += 1
	conn.close()
	sorted_succes_frequency = sorted(succes_frequency.items(), key = lambda kv:(kv[1], kv[0]))
	return sorted_succes_frequency

conn = sqlite3.connect('schema.sqlite')
cursor = conn.cursor()
data = {}
test_list = []
# for i in range(1,13):  #creation dict avec ses keys via une boucle de la forme data = {01 : 0 , 02 : 0, ... , 12 : 0}
# 	if i < 10:
# 		key = ('0' + str(i))
# 		data[key] = 0
# 	else:
# 		data[str(i)] = 0

id_numbers = 0
for row in cursor.execute("SELECT submitted_on from submissions "):
	splitted = str(row[0]).split('-')
	time = str(splitted[0]) + str(splitted[1])
	# test_list.append(time)
	if time not in data:
		data[time] = 0
	else:
		data[time] += 1
	id_numbers += 1
	# time = (str(row[0])).split('-')
	# data[time[1]] += 1
sorted_list = []
for elem in sorted(data.items()):
	sorted_list.append([elem[0] , elem[1]])
# [['201902', 16846], ['201903', 26748], ['201904', 960], ['201905', 9245], ['201906', 12626], ['201907', 646], ['201908', 3051], ['201909', 19133], 
# ['201910', 89774], ['201911', 60061], ['201912', 79278], ['202001', 100369], ['202002', 563]]
# converting time to month
converter = {
	'202001' : '2020 - Janvier',
	'202002' : '2020 - Fevrier',
	'202003' : '2020 - Mars',
	'202004' : '2020 - Avril',
	'202005' : '2020 - Mai',
	'202006' : '2020 - Juin',
	'202007' : '2020 - Juillet',
	'202008' : '2020 - Aout',
	'202009' : '2020 - Septembre',
	'202010' : '2020 - Octobre',
	'202011' : '2020 - Novembre',
	'202012' : '2020 - Decembre',
	'201901' : '2019 - Janvier',
	'201902' : '2019 - Fevrier',
	'201903' : '2019 - Mars',
	'201904' : '2019 - Avril',
	'201905' : '2019 - Mai',
	'201906' : '2019 - Juin',
	'201907' : '2019 - Juillet',
	'201908' : '2019 - Aout',
	'201909' : '2019 - Septembre',
	'201910' : '2019 - Octobre',
	'201911' : '2019 - Novembre',
	'201912' : '2019 - Decembre'
}


print('total: ' + str(id_numbers))
for elem in sorted_list:
	elem[0] = converter[elem[0]]
print(sorted_list)
print(len(sorted_list))
	# print(elem[0][-2:])

# conn = sqlite3.connect('schema.sqlite')
# cursor = conn.cursor()