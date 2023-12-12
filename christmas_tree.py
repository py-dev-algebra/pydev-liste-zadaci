
# visina stabla 10
tree_height = int(input('Upisite visinu drvca: '))

# tree_height - 1
# tree_height - 2
# tree_height - 3

for i in range(tree_height):
    print(' ' * (tree_height - (i + 1)), '*' * (2 * i - 1), sep='')
# print(' ' * (tree_height - 2), '*' * (2 * index - 1), sep='')
# print(' ' * (tree_height - 3), '*' * (2 * index - 1), sep='')
# print('------*******------')
# print('-----*********-----')
# print('----***********----')
# print('---*************---')
# print('--***************--')
# print('-*****************-')
# print('*******************')

for i in range(2):
    print(' ' * (tree_height - 3), '| |', sep='')