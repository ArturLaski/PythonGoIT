def cost_delivery(quantity, *_, discount=0):
    """The function returns the amount for the delivery of the order.
    
    The first parameter is the number of items in the order.
    The discount parameter discount, which is passed only as a key parameter, has a default value of 0."""
    
    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result
