pontos = 0

p1 = str(input('Mora perto da vítima? [S/N]\n'))
while p1.upper() not in 'SN':
    print('Favor digite apenas S ou N')
    p1 = str(input('Mora perto da vítima? [S/N]\n'))
if p1.upper() == 'S':
    pontos += 1

p2 = str(input('Já trabalhou com a vítima? [S/N]\n'))
while p2.upper() not in 'SN':
    print('Favor digite apenas S ou N')
    p2 = str(input('Já trabalhou com a vítima? [S/N]\n'))
if p2.upper() == 'S':
    pontos += 1

p3 = str(input('Telefonou para a vítima? [S/N]\n'))
while p3.upper() not in 'SN':
    print('Favor digite apenas S ou N')
    p3 = str(input('Telefonou para a vítima? [S/N]\n'))
if p3.upper() == 'S':
    pontos += 1

p4 = str(input('Esteve no local do crime [S/N]\n'))
while p4.upper() not in 'SN':
    print('Favor digite apenas S ou N')
    p4 = str(input('Esteve no local do crime  [S/N]\n'))
if p4.upper() == 'S':
    pontos += 1   

p5 = str(input('Devia para a Vítima? [S/N]\n'))
while p3.upper() not in 'SN':
    print('Favor digite apenas S ou N')
    p5 = str(input('Devia para a Vítima? [S/N]\n'))
if p5.upper() == 'S':
    pontos += 1

if pontos == 5:
    print('#'*10,' ASSASSINO ','#'*10)
elif pontos == 4 or pontos == 3:
    print('#'*10,' CÚMPLICE ','#'*10)
elif pontos == 2:
    print('#'*10,' NECESSÁRIO OUTRA INVESTIGAÇÃO ','#'*10)
else:
    print('#'*10,' LIBERADO ','#'*10)
    
print(f'Nº de pontuação: {pontos}')
    
    


