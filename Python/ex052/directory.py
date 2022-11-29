class G_directory():
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
        'std_name': 'Справочник',
        'done': 'Готово!',
        'dict_name': 'Название справочника',
        'empty_file_name': 'Имя файла не задано',
    }
# запись
# {
#     name: 'ivan'
#     tel: '+6 123 432 4545'
#     adress: 'alfa str. 144'
# }
    def __init__(self, string = ''):
        self.name = string if string else self.texts['std_name']
        self.list = []

    # добавляет запись и возвращает её
    def add_record(self, name = '', tel = '', adress = ''):
        self.list.append({
            "name": name,
            "tel": tel,
            "adress": adress
        })
        return self.list[-1] # возвращает эту запись

    def delete_record(self, record):
        self.list.remove(record)
        return self
    # где key - по чему искать (name, tel, adress)
    # возвращает запись
    def find_record_by(self, key, val):
        a = False
        for record in self.list:
            if record[key] == val:
                return record
        return a

    def record_to_str(self,record):
        str = ''
        for k in self.record_keys:
            str += '   {}: {},'.format(k['text'], record[k['main']])  if record[k['main']] else '' 
        return str[:-1]

    def records_to_str(self):
        str = ''
        i = 1
        for record in self.list:
            str += '\n{}) {} '.format(i, self.record_to_str(record))
            i+=1
        return str

    def see(self):
        print('___________________________________________________')
        print('{}: {}'.format(self.texts['dict_name'], self.name))
        s = self.records_to_str()
        s = self.texts['empty'] if s == '' else s
        print(s)
        return self

    def export_xml_str(self):
        import re
        str = '<?xml version="1.0" encoding="UTF-8"?>\n<phoneBook name="{}">\n'.format(re.sub('[^A-Za-z0-9]+', '', self.name))
        for record in self.list:
            str += '\t<contact'
            for k in self.record_keys:
                str += ' {}="{}"'.format(k['main'],record[k['main']]) if record[k['main']] else ''
            str += '></contact>\n'
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
            if '<contact' in i:
                record = self.add_record()
                for k in self.record_keys:
                    record[k['main']] = get_params(k['main'], i)

        print(self.texts['done'])
        return self

    def export_xml_file(self, file_name = ''):
        import re
        if file_name == '':
            file_name = self.name
        file_name = re.sub('[^A-Za-z0-9]+', '', file_name) + '.xml'
        self.write_to_file(self.export_xml_str(), file_name)
        return self

    def import_xml_file(self, file_name = ''):
        if file_name == '':
            print(self.texts['empty_file_name'])
            return False

        if not(f := self.read_file(file_name)): 
            return False
        
        return self.import_xml_str(f)





    def export_html_str(self):
        import re
        str = """
<html lang="ru">
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
        <h1>{}</h1>
        <ol>""".format(re.sub('[^A-Za-z0-9]+', '', self.name))


        for record in self.list:
            str += '\n            <li>'
            str += self.record_to_str(record)
            str += '></li>'
        str += """
        </ol>
    </body>
</html>
        """
        return str

    def export_html_file(self, file_name = ''):
        import re
        if file_name == '':
            file_name = self.name
        file_name = re.sub('[^A-Za-z0-9]+', '', file_name) + '.html'
        self.write_to_file(self.export_html_str(), file_name)
        return self

    def import_xml_file(self, file_name = ''):
        if file_name == '':
            print(self.texts['empty_file_name'])
            return False

        if not(f := self.read_file(file_name)): 
            return False
        
        return self.import_xml_str(f)









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
            return s