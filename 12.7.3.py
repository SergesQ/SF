per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
#money = 100000
money = int(input("Введите сумму вклада:"))
deposit_TKB = int(money / 100 * per_cent['ТКБ'])
deposit_СКБ = int(money / 100 * per_cent['СКБ'])
deposit_ВТБ = int(money / 100 * per_cent['ВТБ'])
deposit_СБЕР = int(money / 100 * per_cent['СБЕР'])
deposit = [deposit_TKB, deposit_СКБ, deposit_ВТБ, deposit_СБЕР]
print('deposit =')
print(deposit)
max_bank_deposit = max(deposit)
print('Максимальная сумма, которую вы можете заработать -', (max_bank_deposit))