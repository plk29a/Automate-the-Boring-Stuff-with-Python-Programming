 #funkcja input(), str(), int()

print('Hi, \nwhat is your nickname?') #Pyta o imie.
Name = input()


Name = Name.title()
if Name: #pusty string ma wartość falsey.
    print('Nice to meet you, ', Name)
else:
    print('Noname is no name :(')



while True:
    print(Name + ', how old are you?') #pyta o wiek
    Wiek = input() #podajesz wiek

    try:
        int(Wiek)
        if int(Wiek) <= 99 and int(Wiek) > 0: #sprawdza czy jest to liczba od 0 do 99 i przerywa pętle
            break
        else:
            print('Are you sure?') #podaje komunikat jeśli jest poza przedziałem
    except ValueError:    
        print('it is not a number.') 
#Sprawdzenie czy wiek jest liczbą z przedziału 0-99

print('You born in ' + str(2020 - int(Wiek))) #podaje datę urodzenia



