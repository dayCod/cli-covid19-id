import requests
import datetime

today = datetime.datetime.now()
d = datetime.timedelta(days=2)
last_two_days = today - d
formated_date = last_two_days.strftime("%Y-%m-%d")

# KAWALCORONA.COM COVID API BY TEGUH APRIANTO
indonesia_api = requests.get("https://api.kawalcorona.com/indonesia/")

# Government covid-19 api Indonesia Only
update = requests.get("https://data.covid19.go.id/public/api/update.json")
testing_and_vaccination = requests.get("https://data.covid19.go.id/public/api/pemeriksaan-vaksinasi.json")
province = requests.get("https://data.covid19.go.id/public/api/prov.json")
kecamatan = requests.get("https://data.covid19.go.id/public/api/kecamatan_rawan.json")
hospital = requests.get("https://data.covid19.go.id/public/api/rs.json")
province_daily_data = requests.get("https://data.covid19.go.id/public/api/prov_time.json")
city_risk_score = requests.get("https://data.covid19.go.id/public/api/skor.json")
