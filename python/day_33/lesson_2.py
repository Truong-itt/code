import  requests
from datetime import datetime

my_lat = 51.500149
my_long = -0.126240
#xây dựng paramêtrrr cho dữ liệu
parameter = {
    "lat":my_lat,
    "lng":my_long,
    "formatted":0,
}
response = requests.get("https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400",params=parameter)
response.raise_for_status()
data = response.json()
# print(data)
print(data['results']['sunrise'])
print(data['results']['sunset'])
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
# #thực hiện lây sra dữ liệu cụ thể
# bien = datetime.now()
# print(bien.hour)