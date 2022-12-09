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


def write_to_file(text, file_name, type = 'w+'):
        file = open(file_name, type, encoding="utf8")
        file.write(text)
        file.close()