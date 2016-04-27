# INFORMACJE:
# ścieżka względna 'plik.txt' lub '../../plik.txt'   (lepsza jeśli mamy pisać program dla kilku komputerów)
# ścieżka bezwzględna to taka pełna np. /home/pk/des/plik.txt  - Pamiętajmy o \\ na windowsie

# Pamiętajmy o tym, żeby jednocześnie nie mieć otwartych wiele plików (np. ponad 60), ponieważ pliki zasób ograniczony.

str -> jest unicode

# TRYBY:
# r - read
# w - write
# a - append
# b..


# document.seek(10) skacze do odpowiedniego miejsca

document = open('/home/pk/des/plik.txt', 'r')
document.read() # pozwala wziąć wszystko na raz, ale niestety należy na rozmiar pliki 

for line in document:
    print(line)   # pamietamy, ze linie maja znak nowego wiersza na koncu strip,  rstrip

# nic nie wyświetli, ponieważ mamy już EOF 
for line in document:
    print(line)
    
# with open('...') as document:
#     content = document.read()

print(content)
    
    
# while document:
#     part = document.read(1024)
    
# https://docs.python.org/2/tutorial/inputoutput.html


lines = [
    '1. ABC 10 punktów',
    '2. FOO 5 punktów',
    '3. BOO 1 punktów'
]

document.write('\n'.join(lines))


# 1) złączyć wszystkie pliki w jedno (tryb tekstowy)
# 2) program do dzielenia dużego pliku na kilka mniejszych
# 3) odwrotnego działanie do programu #2 