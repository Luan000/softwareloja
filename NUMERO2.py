produtos = {'CAMISAS E TECTEL': 11, 'LISTRADAS, POLOS E CAMISAS DE TIME ': 30, 'ELASTANO': 20, 'CAMISAS DA TOMMY': 18,
            'CAMISAS VARIDAS': 25, 'BONÉS E CHINELOS': 15, 'MEIAS': 11, 'CORTA VENTO': 65, 'ÓCULOS NORMAL': 50,
            'CALÇAS JEANS': 28, 'CUECAS': 25, 'ÓCULOS DE DESCANÇO': 35, 'GATILHOS': 6, 'TÊNIS NIKE 4 MOLA': 75,
            'TÊNIS OAKLEY FLEK': 85, 'TÊNIS OAKLEY MODOC': 90, 'TÊNIS FILA': 35}
print('==================================')
print('       PROGRAMA DA LOJA ')
print('==================================')
tot = int(input('VALOR TOTAL DE VENDAS HOJE: '))
acm = s = quantt = lucrot = lucrop = quantp = 0
for c, v in produtos.items():
    s += 1
    q = int(input(f'Quantas \033[33m{c}\033[m você vendeu: '))
    conta = q * v
    acm += conta
    if s >= 14 and q >= 1:
        lucrot += q * 5
        quantt += q
    if s <= 13 and q >= 1:
        quantp += q
        lucrop += q * 0.50
print('==================== FUNCIONÁRIOS ====================')
print(f'TOTAL DE TÊNIS VENDIDOS: {quantt} LUCRO: R${lucrot:.2f}')
print(f"TOTAL DE OUTROS PRODUTOS VENDIDOS: {quantp} LUCRO R${lucrop:.2f}")
print(f'DIÁRIA: R$20.00')
if tot >= 500:
    print(f'COMISSÃP DE META R$5.00')
    print(f'TOTAL PARA CADA: R${lucrot+lucrop+20+5:.2f}')
    s = lucrot+lucrop+20+5
    print(f'PARA DOIS {2*s}')
    tot = tot - 2 * s
else:
    print(f'TOTAL PARA CADA: R${lucrot+lucrop+20:.2f}')
    s = lucrot+lucrop+20
    print(f'PARA DOIS {2 * s}')
    tot = tot - 2 * s
print('======================================================')
print(f'lucro: {tot-acm}')