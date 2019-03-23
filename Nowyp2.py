tekst= 'Anna, pawel, Tomek'
tab=tekst.split(',')
print(tekst)
print(tab)
imie=tab[0]
print(imie)
print(type(tab))

imieDuze=imie.upper()
print(imieDuze)
imieMale = imie.lower()
print(imieMale)

#sprawdzanie zawartosci
zawartosc=imie.isalpha()
print(zawartosc)
print(type(zawartosc))

imie = ''
zawartosc=imie.isalpha()
print(zawartosc)
print(type(zawartosc))

imie = 'Julia'
print('\nDane uzytkownika: \nMasz na imie:')

text1= 'Jan\n'
text2= 'Nowak'
print(text1 + text2)

text1= text1.rstrip()
print(text1+text2)
print(text1 + ' ' + text2)

#wyswietlanie lancuchow znakow

#wszystkie wersje Pythona

text= '%s, Java i %s'%('PHP', 'Python')
print(text1)

#nowsze wersje pythona 2.6

text='{0}, Java i {1}'.format("PHP","python")
print(text)

#help(text.replace)
new=text.replace('PHP', 'C#')
print(new)

#wpisywanie danych
rok='2019'
miesiac='marzec'
dzien='23'

print('Data:', end=' ')
print(dzien,miesiac,rok)

print('Data:', end=' ')
print(dzien,miesiac,rok sep='-')




