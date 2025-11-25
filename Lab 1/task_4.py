amount = int(input("Введите сумму в рублях: "))
original_amount = amount

# Список номиналов от большего к меньшему
denominations = [100, 50, 10, 5, 2, 1]
names = ["Купюр по 100 рублей", "Купюр по 50 рублей", "Купюр по 10 рублей",
         "Купюр по 5 рублей", "Монет по 2 рубля", "Монет по 1 рублю"]

results = []
for denom in denominations:
    count = amount // denom
    amount %= denom
    results.append(count)

print(f"Сумма: {original_amount} рублей")
for name, count in zip(names, results):
    print(f"{name}: {count}")