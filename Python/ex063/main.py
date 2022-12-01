import random as r
# колличество дней в месяце
def get_dany_numb(month, r = False):
    match month:
        case (1|3|5|7|8|10|12):
            return 31
        case (4|6|9|11):
            return 30
        case 2:
            return 29 if r else 28
    if month > 12:
        return get_dany_numb(month - 12)
    else:
        return 0 

# генератор +- похожих температур
def get_temperature(month,day):
    MAX = 30
    MIN = -10
    RANGE = 2
    STEP = (MAX - MIN)/5

    def aver_in_month(month):
        if month < 6:
            return MIN + STEP*(month-1)
        elif month > 6:
            return MAX - STEP*(month-1-6)
        else:
            return MAX
    month_range_f = aver_in_month(month)
    month_range_s = aver_in_month(month+1)
    
    a = int(month_range_f - (month_range_f - month_range_s)/get_dany_numb(month)*day)
    return r.randint((a-RANGE)*10, (a+RANGE)*10)/10

# заполнение случайными температурами 
temperature_list = [[get_temperature(month,day) for day in range(1, (get_dany_numb(month))+1) ] for month in range(1,13)]

# для хранения максимальной температуры
class max_temperature:
    def __init__(self):
        self.list = []
        self.aver = -120
        self.month = 0
        self.day = 0

    def see(self):
        print('7 дней с максимальной средней температурой: ')
        print('Начинается в {} месяце и на {} дне. Средняя температура в этот период: {}'.format(self.month, self.day, round(self.aver*10)/10))

# временный список для сравнения с максимальной температуры
seven_days_list = []


temp = max_temperature()

# перебор всех температур 
for month, days_list in enumerate(temperature_list):
    for day, temperature in enumerate(days_list):
        seven_days_list.append(temperature)
        if len(seven_days_list) == 7:
            seven_days_list.pop(0)
            aver = sum(seven_days_list)/7
            if aver > temp.aver:
                temp.list = seven_days_list.copy()
                temp.aver = aver
                temp.day = day+1
                temp.month = month+1
        else:
            continue
        
        
        
temp.see()
# print(temperature_list)