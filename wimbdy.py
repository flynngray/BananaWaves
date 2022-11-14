import requests
import csv
import pandas as pd


def wimbdy(latitude, longitude):
	LAT = str(latitude)
	LONG = str(longitude)
	combo = LAT + "," + LONG


	url = "https://visual-crossing-weather.p.rapidapi.com/forecast"

	querystring = {"aggregateHours":"24","location":combo,"contentType":"csv","unitGroup":"us","shortColumnNames":"1"}

	headers = {
		"X-RapidAPI-Key": "6520434f99mshb47aa5f323c8a54p16f385jsn176f39a1c3c6",
		"X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com"
	}


	response = requests.request("GET", url, headers=headers, params=querystring)

	# print(response)
	# print(type(response))
	# print(response.apparent_encoding)


	decoded_content = response.content.decode('utf-8')

	cr = csv.reader(decoded_content.splitlines(), delimiter=',')
	# my_list = list(cr)
	# for row in my_list:
	#     print(row)


	df = pd.DataFrame(cr)

	# print(df.to_string()) 

	# print(df[1])
	# print(df[6])
	# print(df[10])

	# print()
	# print("direction: " + df[6][1])
	# print("speed: " + df[10][1])

	direct = df[6][1]
	speed = df[10][1]


	return [direct, speed]
	# df = pd.read_csv(cr)
	# saved_column = df.column_name #you can also use df['column_name']

a = [40, 100]