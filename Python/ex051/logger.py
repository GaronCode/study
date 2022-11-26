from datetime import datetime

def logger(data, name):
    time = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as f:
        s = '{};{};{}\n'.format(time,name,data)
        f.write(s)
        return s

def temperature_logger(d):
    logger(d, 'temperature')

def pressure_logger(d):
    logger(d, 'pressure')

def wind_speed_logger(d):
    logger(d, 'wind speed')