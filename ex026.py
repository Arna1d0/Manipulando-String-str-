frase = str(input('Digite uma frase : ')).strip().upper()
#strip eliminando os espçaos desnecessarios o upper deixando tudo que o usuario digitar em maiusculo
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A posição da primeira letra A é {}.'.format(frase.find('A') + 1))
print('A ultima letra A apareceu na posição {}.'.format(frase.rfind('A') + 1))
