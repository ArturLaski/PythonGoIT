DEFAULT_DISCOUNT = 0.05

def get_discount_price_customer(price, customer):
    discount = customer.get("discount", DEFAULT_DISCOUNT)
    discounted_price = price * (1 - discount)
    return discounted_price
