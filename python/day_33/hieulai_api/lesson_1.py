import requests
bien = requests.get('http://api.open-notify.org/iss-now.json')
#doc du lieu thong qua json
data = bien.json()
# print(data)
#tao buo truy cap he thong
data_iss_position = data['iss_position']['latitude']
data_longitude = data['iss_position']['longitude']
print(data_iss_position,data_longitude)

#api na