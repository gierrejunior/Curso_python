def separador():
    print('-='*90)
    
times_em_ordem = (
    'Corinthians', 'Palmeiras', 'São Paulo', 'Atlético-MG', 'Botafogo',
    'Santos', 'Fluminense', 'Coritiba', 'América-MG', 'Avaí', 'Internacional',
    'Atletico-PR', 'Bragantino', 'Flamengo', 'Goiás', 'Cuiabá', 'Atlético-GO',
    'Juventude', 'Ceará SC', 'Fortaleza'
)

separador()
print(f"Lista de times do Brasileirão: {times_em_ordem}")
separador()
print(f'Os 5 primeiros são: {times_em_ordem[:5]} ')
separador()
print(f'Os 4 últimos são {times_em_ordem[-4:]}')
separador()
print(f'Times em ordem alfabética: {sorted(times_em_ordem)}')
separador()
print(f'O Fluminense está na {times_em_ordem.index("Fluminense")+1}ª Posição')