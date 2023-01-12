import requests

def wether(city):
    API_key = '4321a3d417b53045aa1b6617c529c910'
    response_wether = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric&lang=ru")
    global_inf = response_wether.json()
    temp = global_inf['main']['temp']
    return temp