BASE_MINUTES = 60
BASE_SMS = 30
BASE_INTERNET_MB = 1024
BASE_PRICE = 24.99
EXTRA_MINUTE_PRICE = 0.89
EXTRA_SMS_PRICE = 0.59
EXTRA_MB_PRICE = 0.79
TAX_RATE = 0.02

used_minutes = int(input("Введите количество израсходованных минут: "))
used_sms = int(input("Введите количество израсходованных SMS: "))
used_internet_mb = int(input("Введите количество израсходованного интернет-трафика (МБ): "))
extra_minutes = max(0, used_minutes - BASE_MINUTES)
extra_sms = max(0, used_sms - BASE_SMS)
extra_internet = max(0, used_internet_mb - BASE_INTERNET_MB)
extra_minutes_cost = extra_minutes * EXTRA_MINUTE_PRICE
extra_sms_cost = extra_sms * EXTRA_SMS_PRICE
extra_internet_cost = extra_internet * EXTRA_MB_PRICE
subtotal = BASE_PRICE + extra_minutes_cost + extra_sms_cost + extra_internet_cost
tax = subtotal * TAX_RATE
total = subtotal + tax
print("\n" + "="*50)
print(f"Базовая стоимость тарифа: {BASE_PRICE:.2f} руб.")

if extra_minutes > 0:
    print(f"Дополнительные минуты ({extra_minutes} мин.): {extra_minutes_cost:.2f} руб.")

if extra_sms > 0:
    print(f"Дополнительные SMS ({extra_sms} шт.): {extra_sms_cost:.2f} руб.")

if extra_internet > 0:
    print(f"Дополнительный интернет ({extra_internet} МБ): {extra_internet_cost:.2f} руб.")

print(f"Сумма до налога: {subtotal:.2f} руб.")
print(f"Налог (2%): {tax:.2f} руб.")
print(f"Итоговая сумма к оплате: {total:.2f} руб.")
print("="*50)