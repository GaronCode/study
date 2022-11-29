def print_matrix(m):
    s = '\n'
    line_number = 0
    for y in m:
        s += "{}) ".format(line_number)
        line_number+=1
        for i in y:
            s +=" "*(5-len(str(i)))+ str(i)
        s +="\n"
    print(s)