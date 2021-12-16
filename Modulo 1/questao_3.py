while True:
    p1 = str(input('Mora perto da vítima? [S/N]\n'))
    p2 = str(input('Já trabahlou com a vítima? [S/N]\n'))
    p3 = str(input('Telefonou para a vítima? [S/N]\n'))
    p4 = str(input('Esteve no local do crime [S/N]\n'))
    p5 = str(input('Devia para a Vítima? [S/N]\n'))
    break

pontos = 0

if p1 == 'S':
    pontos += 1
if p2 == 'S':
    pontos += 1
if p3 == 'S':
    pontos +=1
if p4 == 'S':
    pontos += 1
if p5 == 'S':
    pontos +=1
    
print(pontos)
    
    


