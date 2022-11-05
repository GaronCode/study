class G_polynomial:
    poly_list = {}

    def __init__(self, string = ''):
        self.string_to_poly_list(string)

    @classmethod
    def sup_int(self, i):
        if i =='':
            return 1
        return int(i)

    def poly_to_str(self):
        text = ''
        for ex in self.poly_list:
            multi = self.poly_list[ex]
            unit = ''
            if ex == 0:
                unit = str(multi)
            else:
                if ex == 1:
                    t = "x"
                else:
                    t = "x^" + str(ex)
                unit = str(multi) + t
            
            if multi >= 0:
                t = " + "
            else:
                t = " - "
            unit = t + unit
            text += unit
        return text[3:]

    def string_to_poly_list(self, string):
        list = {}
        tmp = string.split()
        z = 1
        for i in tmp:
            z = 1
            if i == "+":
                continue
            elif i == "-":
                z = -1
                continue
            a = i.split('x')
            if len(a) == 1:
                if 0 in list:
                    list[0] += int(a[0])
                else:
                    list[0] = int(a[0])
                continue
            elif len(a) == 2:
                list[self.sup_int(a[1][1:])] = self.sup_int(a[0]) * z
            else:
                print('Ошибка парсинга')
                break
        self.poly_list = list
        return self

    def see(self):
        print(self.poly_to_str())
        return self

    def sum(self, another):
        list = {}
        mch1 = self.poly_list
        mch2 = another.poly_list
        def add(mch):
            for i in mch:
                if i in list:
                    list[i] += mch[i]
                else:
                    list[i] = mch[i]
        add(mch1)
        add(mch2)
        self.poly_list = list
        return self






