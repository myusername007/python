def format_name(first,last,middle = None):
    if middle == None:
        print("Привіт, ", last, first)
    else:
        print("Привіт, ", last, first, middle)

fname = input("Введіть ім'я: ")
lname = input("Введіть прізвище: ")
mname = input("По-батькові: ")
format_name(fname,lname,mname)

fname = input("Введіть ім'я: ")
lname = input("Введіть прізвище: ")
mname = input("По-батькові: ")
format_name(fname,lname,mname)
