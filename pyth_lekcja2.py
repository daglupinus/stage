# PODSUMOWANIE:

# układ ifów:
# 1) jeden z wielu (np. kanał włączony przez pilot; wybieram tam jeden z wielu)
# 2) wiele z wielu (np. wybieram kilka składnikow z puli możliwych składników)


# PEP8 - opis konwencji przyjętej w programowaniu pythonem 


# WNIOSEK:
# Liczby zmiennoprzecinkowe służą bardziej do szybkich obliczeń, ale niekonicznie dokładnych.
# W przypadku pieniędzy lepiej jest pomyśleć o innym typie danych np. decimal.

# print(0.1 * 0.1 * 0.1 * 0.3) # 0.0003000000000000001

# ***************************

# a = 5 #int(input("Podaj barwe a: "))
# b = 5 #int(input("Podaj barwe b: "))
# c = 5 #int(input("Podaj barwe c: "))

# if a>b and a>c:
#     print("red")
# elif b>a and b>c:
#     print("green")
# elif c>a and c>b:
#     print("blue")
# elif a>c and a==b:
#     print("red & green")
# elif a>b and a==c:
#     print("red & blue")
# elif b>a and b==c:
#     print("green and blue")
# elif a==b and a==c and b==c:
#     print("red & green & blue")
    
# x = 5
# if x > 0:
#     print('bialy')
# elif x == 10:
#     print('czerwony')
#elif x == 5:
 #print('niebieski')
#else:
 print('czarny')
    
    
# a = 5 #int(input("podaj liczbe a: "))
# b = 0 #int(input("podaj liczbe b: "))

# print ("1.dodawanie")
# print ("2.odejmowanie")
# print("3.mnozenie")
# print("4.dzielenie")

# dzialanie = 4 #int(input("wybierz jedna z opcji"))

# if dzialanie == 4 and b == 0:
#     print("nie dziel przez 0")
# elif dzialanie == 1:
#     print(a + b)
# elif dzialanie == 2:
#     print(a - b)
# elif dzialanie == 3:
#     print(a * b)
# elif dzialanie == 4:
#     print(a / b)
    

# def is_triangle(a, b, c):
#     return (a ** 2) + (b ** 2) == (c ** 2) 
    
# a = 5 #int(input("Podaj liczbe 1: "))
# b = 3 #int(input("Podaj liczbe 2: "))
# c = 4 #int(input("Podaj liczbe 3: "))

# if is_triangle(a, b, c) or is_triangle(a, c, b) or is_triangle(c, b, a):
#     print("trojkat jest prostokatny")
# else:
#     print("nie mozna zbudowac TR prostokatnego")


 gracz1 = 'P' #input("gracz1 Wybierz K, N, P: ")
 gracz2 = 'K' #input("gracz2 Wybierz K, N, P: ")

# #    P K  N
# # P [*][*][]
# # K [*][*][*]
# # N [*][*][*]

# if gracz1 == gracz2:
#     print('remis')
# if gracz1 == "K" and gracz2 == "N":
#     print("wygrywa gracz1")
# elif gracz1 == "N" and gracz2 == "P":
#     print("wygrywa gracz1")
# elif gracz1 == "P" and gracz2 == "K":
#     print("wygrywa gracz1")
# elif gracz1 == "N" and gracz2 == "K":
#     print("wygrywa gracz2")
# elif gracz1 == "P" and gracz2 == "N":
#     print("wygrywa gracz2")
# elif gracz1 == "K" and gracz2 == "P":
#     print("wygrywa gracz2")

# x = 
# y =
# z = 

# if x == y and x == z:
#     print('bum')

# if x == y:
#     if x == z:
#         print('bum')

# if x == y or x == z:
#     print('bum')
    
# if x == y:
#     print('bum')
# elif x == z:
#     print('bum')


wartosci = []  # tworze puste liste
wartosci = [17, 20, 13, 9, 0, 1, 2, 4, 5, 0, 90] # tworze liste w kilka wartosciami
wartosci.append(91)
print(wartosci)

print('dlugosc', len(wartosci))  # funkcja len informuje nas ile mamy elemntow w liscie

# pobieranie elementów
# pobranie pierwszej liczy
print(wartosci[0])

# pobranie
print(wartosci[len(wartosci) - 1])
# moze jeszcze prosciej
print(wartosci[-1])


# pobieranie przez zakres ma postac <poczatek; koniec)
print(wartosci[1:3])

# jesli nie podam liczby po : to interesuje mnie wszystkie liczby do konca
print(wartosci[1:])

# jesli nie podam liczby przed : to interesuje mnie wszystkie liczby od poczatki
print(wartosci[:4])

# tutaj nie ma kopiowania - mamy wspodzielnie tej samej listy pod inną zmienną
kopia = wartosci
print(id(kopia)) 
print(id(wartosci))

print('po')

# tutaj natomiast mamy plytkie kopiowanie, ktore prowadzi do utworzenie drugiej listy
kopia = wartosci[:] 
print(id(kopia)) 
print(id(wartosci))


print(wartosci[::2], wartosci[1::2])

print(wartosci[::-1]) # odwraca elementy
odwrocone_wartosci = wartosci[::-1] 

print(wartosci)

# [*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*]  !!!
# przepisuje
# [*][*][*][*][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
# a potem usuwa stara tablica

# LISTY:
# sa dynamiczne i nie trzeba przejmowac sie rozmiarem
