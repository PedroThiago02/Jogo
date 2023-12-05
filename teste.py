nome=str(input('Digite seu nome: '))
print('Seja bem vindo {} :)'.format(nome))
print('{}, aqui você vai descobrir se seus números são ímpares ou pares! Vamos nessa?'.format(nome))
numero=int(input('Qual número você quer descobrir se é ímpar ou par? '))
if (numero%2==0):
    print('{} é um número par'.format(numero))
else:
    print('{} é um número ímpar'.format(numero))