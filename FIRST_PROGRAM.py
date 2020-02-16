# funkcja input(), str(), int()

name = input('Hi, \nwhat is your nickname?\n')
name = name.title()

if name:  # value of empty string is False
    print('Nice to meet you,', name)
else:
    print('Noname is no name:(')

while True:
    age = input('{}, how old are you?\n'.format(name))

    try:
        int(age)
        if 0 < int(age) <= 99:
            break
        else:
            print('\nAre you sure?')
    except ValueError:    
        print('It is not a number.')


print('You are born in ' + str(2020 - int(age)))
input('<press enter to exit>')
>>>>>>> 62bed099c59bba4f58cd4a46e331fe061e52495b
