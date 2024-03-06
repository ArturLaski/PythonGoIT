def cost_delivery(quantity, *args, discount = 0):
    if quantity <= 0:
        raise ValueError(f"Wprowadziles wartosc {quantity} ktora jest < 0")
    total = 5 #Pierwsza przesyłka 5
    total += (quantity - 1) * 2 #Kazda nastepna 2
    total *= (1 - discount) #doliczam rabat
    return total
    
    