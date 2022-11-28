class G_directory():
    list = []
    record_keys = [
        {
            'main':'name',
            'text':'Имя'
        },
        {
            'main': 'tel',
            'text': 'Телефон'
        },
        {
            'main': 'adress',
            'text': 'Адрес'
        }
    ]
    texts = {
        'null': 'отсутствует',
        'empty': 'пусто',
        'std_name': 'Справочник'
    }
    name = ''
# запись
# {
#     name: 'ivan'
#     tel: '+6 123 432 4545'
#     adress: 'alfa str. 144'
# }
    def __init__(self, string = ''):
        self.name = string if string else self.texts['std_name']
    def add_record(self, name = '', tel = '', adress = ''):
        self.list.append({
            "name": name,
            "tel": tel,
            "adress": adress
        })
        return self.list[-1] # возвращает эту запись

    def delete_record(self, record):
        self.list.remove(record)
    # где key - по чему искать (name, tel, adress)
    # возвращает запись
    def find_record_by(self, key, val):
        for record in self.list:
            if record[key] == val:
                return record

    def record_to_str(self,record):
        str = ''
        for k in self.record_keys:
            str += '{}: {}  '.format(k['text'], record[k['main']] if record[k['main']] else self.texts['null']) 
        return str

    def records_to_str(self, sep = '\n'):
        str = ''
        i = 1
        for record in self.list:
            str += '{}: {} {}'.format(i, self.record_to_str(record), sep)
            i+=1
        return str

    def export_xml_str(self):
        import re
        str = '<?xml version="1.0" encoding="UTF-8"?>\n<phoneBook name="{}">\n'.format(re.sub('[^A-Za-z0-9]+', '', self.name))
        for record in self.list:
            str += '\t<contact>\n'
            for k in self.record_keys:
                str += '\t\t<{}>{}</{}>\n'.format(k['main'],record[k['main']],k['main']) if record[k['main']] else ''
            str += '\t</contact>\n'
        str +='</phoneBook>'
        return str

    def import_xml_str(self, str):

        def get_params(p_name, str):
            s = p_name+'='
            if s in str:
                startIndex = str.find(s)+len(s)
                quote_symbol = str[startIndex]
                str_for_find = str[startIndex+1:]
                endIndex = str_for_find.find(quote_symbol)
                return str_for_find[:endIndex]
            else:
                return ''

        str_list = str.split('\n')
        for i in str_list:
            if '<phoneBook' in i:
                self.name = get_params('name', i)
                continue
            


        print(str_list)

    def export_xml_file(self, file_name = ''):
        import re
        if file_name == '':
            file_name = self.name
        file_name = re.sub('[^A-Za-z0-9]+', '', file_name) + '.xml'
        self.write_to_file(self.export_xml_str(), file_name)
        return self


    @staticmethod
    def write_to_file(text, file_name):
        file = open(file_name, 'w+', encoding="utf8")
        file.write(text)
        file.close()
        
    @staticmethod
    def read_file(file_name):
        try: 
            f = open(file_name, 'r', encoding="utf8")
        except IOError:
            print('Файл ('+file_name+') не существует!')
            return False
        else:
            s = f.read()
            f.close()
            return f