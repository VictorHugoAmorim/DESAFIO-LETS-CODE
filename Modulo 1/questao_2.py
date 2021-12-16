idade = int(input('Digite sua idade:\n'))
sal = float(input('Digite seu salário:\n'))
sexo = str(input('Informe seu sexo [M/F ou Outro]: \n'))

if idade >=0 and idade <= 150:
    pass
else:
    print('Favor digitar um nº entre 0 e 150')

if sal > 0:
    pass
else:
    print('Favor digitar um nº maior que 0')

if sexo in 'MF' or sexo == 'Outro':
    pass
else:
    print('Favor digitar apenas "M", "F" ou "Outro"')


            