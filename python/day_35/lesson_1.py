import requests

key = '21a13cadd1fe70dc3a018a334297a83a'
url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'lat': 51.507351,
    'lon': -0.127758,
    'appid': key,
}

# headers = {
#     'User-Agent': 'your_app_name/0.0.1'
# }
# , headers=headers
response = requests.get(url, params=params)

print(response)
#lôci loction khôgn thể nhập vao hệ thông lỗi 401
