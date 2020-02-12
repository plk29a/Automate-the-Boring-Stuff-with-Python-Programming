#funkcja input(), str(), int()

print('Hi, \nwhat is your name?') #Pyta o imie.
Name = input()


Name = Name.title()
if Name: #pusty string ma wartość falsey.
    print('Nice to meet you, ', Name)
else:
    print('Noname is no name :(')

print(Name + ', how old are you') #pyta o wiek
Wiek = input()

#Sprawdzenie czy wiek jest liczbą z przedziału 0-99

print('You born in ' + str(2020 - int(Wiek))) #podaje datę urodzenia



