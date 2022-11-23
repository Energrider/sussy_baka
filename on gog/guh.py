new_file = open('loop.txt', 'w', encoding='utf-8')

content = input('Ko vēlies ierakstīt failā? ')
amount = int(('Cik reizes vēlies ierakstīt failā? '))

for i in range (amount):
    new_file .write(content + '\n')

new_file.close()

print('Rakstīšana pabeigta!')