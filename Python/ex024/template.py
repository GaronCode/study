def open_file(path, p = 'r'):
    try: 
        f = open(path, p)
    except IOError:
        print('Файл '+FILE_NAME+' не существует!')
        return False
    else:
        return f


from G_polynomial import G_polynomial

poly_string_1 = open_file('mch_1.txt').read()
poly_string_2 = open_file('mch_2.txt').read()

p1 = G_polynomial(poly_string_1).see()
p2 = G_polynomial(poly_string_2).see()


p1.sum(p2).see()
