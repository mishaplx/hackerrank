#You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
#For example, alison heck should be capitalised correctly as Alison Heck.
string = input('введите строку: ')
def check(str):
    new_string = str.split()
    x = []
    for i in range(len(new_string)):
        if new_string[i].isalpha() == True:
            x1 = new_string[i].title()
            x.append(x1)
        elif new_string[i].isalpha() == False:
            x.append(new_string[i])

    print(' '.join(x))

check(string)