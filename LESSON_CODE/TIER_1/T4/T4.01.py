def amount_payment(payment):
    # zmienna dla dodatnich płatności
    total_positive_payments = 0

    # przeglądanie tablicy payment zasilonej jako parametr
    for value in payment:
        # jeżeli dodatnia wartość to zasil zmienną dodatnich płatności
        if value > 0:
            total_positive_payments += value

    return total_positive_payments

# przykładowe dane
payment_list = [100, -50, 200, -30, -20, 50]
result = amount_payment(payment_list)
print(f"Total positive payment amount: {result}")