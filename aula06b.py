#n = float(input('Digite um valor '))
#print(n)
#n2 = input('Digite algo ')
#print('É alfanumérico?: ', n2.isalpha())



print('===== desafio 03 =====')

# Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('Digite um numero '))
n2 = int(input('Digite outro numero '))
s = n1 + n2
print('A soma entre {0} e {1} será {2}'.format(n1, n2, s))

print('===== desafio 04 =====')

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo ')
print('O tipo primitivo deste valor é: ', type(a))
print('É almum?: ', a.isalnum())
print('É alfanumerico?: ', a.isalpha())
print('É decimal?: ', a.isdecimal())
print('É só maiuscula?: ', a.islower())
print('É numérico?: ', a.isnumeric())
print('É um titulo?: ', a.istitle())




