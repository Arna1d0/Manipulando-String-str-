n = str(input('Digite seu nome completo : ')).strip()
nome = n.split()
# split separa por espaços o nome ou frase
print('Muito prazer te conhecer !')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}.'.format(nome[len(nome)-1]))