def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price * (1 - discount)

    apply_discount()
    return price

# przykład użycia:
original_price = 100
discounted_price = discount_price(original_price, 0.2)  # 20% rabatu
print(f"Original Price: {original_price}, Discounted Price: {discounted_price}")
