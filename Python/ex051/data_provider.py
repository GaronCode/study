from random import randint

def get_temperature(sensor):
    return randint(-20, 0) if sensor else randint(0, 20)

def get_pressure(sensor):
    if sensor:
        return randint(720, 750) 
    return randint(750, 770)

def get_wind_speed(sensor):
    return randint(0, 30) if sensor else randint(30, 50)

def data_collection():
    return (get_pressure(1),get_temperature(1),get_wind_speed(1))