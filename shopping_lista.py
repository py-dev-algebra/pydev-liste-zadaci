'''kreirajte aplikaciju koja korisniku omogucava:

- zatim korisnika pita koliko je platio svaki od artikala s popisa 
        te u popis uz svaki zapis dodaje i njegovu cijenu. 
	    ako neka stavka nije kupljena onda neka upise nulu
- nakon toga ponovno ispisuje popis za kupovinu, ali ovaj puta s cijenama 
        i na kraju koliko je ukupno potroseno novaca na kupovinu
'''


shopping_list = []

shopping_list_size = int(input('Koliko zapisa zelite unitei u listu? '))
print()

for i in range(shopping_list_size):
    grocery = input('Upisite naziv namirnice: ')
    shopping_list.append(grocery)

print('\nPopis za kupovinu:')
# index = 0 -> preporuka enumerate(naziv_liste)
for index, grocery in enumerate(shopping_list):
    print(f'{index + 1}. {grocery}')
    # index += 1

print(80 * "*", '\n', '\n')

# ['Chia', 'Spinat', 'Baklava']

# ['Chia', 4.99, 'Spinat', 2.59, 'Baklava', 8.79]

# [['Chia', 4.99], ['Spinat', 2.59], ['Baklava', 8.79]]

shopping_list_with_prices = []

for index, grocery in enumerate(shopping_list):
    grocery_price = float(input(f'Upisite cijenu za {grocery}: '))
    
#     temp_list = []
#     temp_list.append(grocery)
#     temp_list.append(grocery_price)
#     shopping_list_with_prices.append(temp_list)
    shopping_list_with_prices.append([grocery, grocery_price])

# [['Chia', 4.99], ['Spinat', 2.59], ['Baklava', 8.79]]
for grocery_with_price in shopping_list_with_prices:
    for grocery in grocery_with_price:
        print(grocery)

