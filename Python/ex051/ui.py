import data_provider as prov
import logger as log


def temperature_view(sensor):
    a = prov.get_temperature(sensor)
    log.temperature_logger(a)
    return a

def wind_speed_view(sensor):
    a = prov.get_wind_speed(sensor)
    log.wind_speed_logger(a)
    return a

def pressure_view(sensor):
    a = prov.get_pressure(sensor)
    log.pressure_logger(a)
    return a




def see(data):
    print(data)

def get_value(text = 'value = '):
    return int(input(text))