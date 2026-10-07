import requests
import json

while True:
    try:
        city=input("what city you want to look up today / type stop to quit : ").strip().lower()
        state=input("what state: ").strip().lower
        if city=="stop":
            break
        
    except ValueError:
        print("please enter a correct city")
        continue
        
    Api_key="d7c7ae49e9bcf5ec5c1bb8c1faaa599b"
    URl=f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},&appid={Api_key}&units=imperial"

    response=requests.get(URl).json()
    country=response['sys']['country']

    weather = response['weather'][0]['description']
    temp=response['main']['temp']
    feels_like=response['main']['feels_like']
    
    if temp<32:
        print(f"the temperature is {temp} degrees and its a freezing day, Dress warm ")
    elif temp <50:
        print(f"The temperature is {temp} degrees and its a cold day")
    elif temp <65:
        print(f"The temperature is {temp} degrees and its chilly")
    elif temp < 75:
        print(f"The tempreature is {temp} degrees and its cool")
    else :
        print(f"The temperature is {temp} degrees and its hot ")
    # print(weather)
    # print(temp)
    # print(feels_like)


   