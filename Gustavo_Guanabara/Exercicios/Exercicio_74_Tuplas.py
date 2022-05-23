# import random
# num = (random.sample(range(10), k=5))
# maior = num[0]
# menor = num[0]
# for x in num:
#     if x > maior:
#         maior = x
#     if  x < menor:
#         menor = x
    
    
# print(f'Os valores sorteados foram: {num}')
# print(f'O maior valor sorteado foi {maior}')
# print(f'O menor valor sorteado foi {menor}')


#------------------------ RESOLUÇÃO DO PROFESSOR -----------------------------------------------------  

from random import randint

numeros = (
    randint(1,10),randint(1,10),randint(1,10),
    randint(1,10),randint(1,10)   
)
print('Os valores sorteados foram: ',end='')
for n in numeros:
    print(f'{n}', end = '')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
