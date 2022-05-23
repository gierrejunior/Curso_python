# extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenovo', 'Vinte')
# n = int(input('Digite um número entre 0 e 20:'))
# while n >20 :
#     n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
# print(f'Você digitou o número {extenso[n]}')


#------------------------ RESOLUÇÃO DO PROFESSOR -----------------------------------------------------  

# from xml.etree.ElementInclude import include


# cont = (
#     'Zero', 'Um', 'Dois', 'Três', 'Quatro',
#     'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
#     'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
#     'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito',
#     'Dezenovo', 'Vinte'
#     )
# while True:
#     num = int(input('Digite um número entre 0 e 20: '))
#     if 0 <= num <= 20:
#         break
#     print('Tente novamente. ', end='') # o end ='' , serve para não pular de linha e assim no terminal ficar, Tente novamente. Digite um número entre 0 e 20
# print(f'Você digitou o número {cont[num]}')


#---------------------------------------------- DESAFIO -------------------------------------------------
sair = 0
while True:
    cont = (
    'Zero', 'Um', 'Dois', 'Três', 'Quatro',
    'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
    'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
    'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito',
    'Dezenovo', 'Vinte'
    )
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='') # o end ='' , serve para não pular de linha e assim no terminal ficar, Tente novamente. Digite um número entre 0 e 20
    print(f'Você digitou o número {cont[num]}')
    while True:
        sair_str = str(input('Você deseja continuar? [Y/N]: ').upper())
        if sair_str in "YN":
            if sair_str in 'Y':
                break
            else:
                sair = 1
                break            
        else:
            print('Opção inválida. ', end ='')
            
    if sair == 1:
        break
print('----------------------------Programa Finalizado-------------------------------')