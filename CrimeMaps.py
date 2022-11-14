import requests

<<<<<<< HEAD
url = "https://instagram47.p.rapidapi.com/user_following"
=======
<<<<<<< HEAD
r = requests.get('https://api.usa.gov/crime/fbi/sapi/api/data/supplemental/not-specified/states/CA/OFFENSE/2000/2022?API_KEY=NA9DrPF8yhGVtuH88SdGPhU2jn5pG59TulaZVxjR').json()

print(dir(r))
print(r)
=======
r = requests.get('https://api.usa.gov/crime/fbi/sapi/api/data/supplemental/not-specified/states/CA/OFFENSE/2000/2022?API_KEY=NA9DrPF8yhGVtuH88SdGPhU2jn5pG59TulaZVxjR')
>>>>>>> refs/remotes/origin/main

querystring = {"userid":"1718924098"}

<<<<<<< HEAD
headers = {
	"X-RapidAPI-Key": "f99e001d27mshdbff5f6c6372b98p13cecfjsn6d862349dfc0",
	"X-RapidAPI-Host": "instagram47.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
=======
#change
#change 2
#change 3
>>>>>>> ba9ce6f20056b107d1973a61e373a521dc8eff52
>>>>>>> refs/remotes/origin/main
