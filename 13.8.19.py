number_of_tickets = int(input("Введите количество билетов:"))
expenses = 0
for i in range(number_of_tickets):
    age = int(input("Введите возраст посетителя:"))
    if age < 18:
        continue
    elif 18 <= age <= 25:
        expenses += 990
    else:
        expenses += 1390

if number_of_tickets > 3:
    print("Сумма к оплате (скидка 10%): ", expenses * 0.9)
else:
    print("Сумма к оплате:", expenses)

