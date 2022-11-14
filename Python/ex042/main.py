def random_list(r = 15):
    from random import randint
    return [randint(1,9) for i in range(r)]

def list_contains_another_list(f_list, s_list):
    len_f = len(f_list)
    len_s = len(s_list)
    for i in range(len_f - len_s + 1):
        if s_list == l[i:i+len_s]:
            return True
    return False

print('список: ',l := random_list())
N = input('входящее число N: ')
l2 = [int(i) for i in list(str(N))]







print('входит' if list_contains_another_list(l,l2) else 'не входит')