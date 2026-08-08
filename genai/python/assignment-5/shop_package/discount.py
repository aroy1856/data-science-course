def apply_discount(price, discount_percentage):
    return price * (1 - discount_percentage / 100)

def flat_discount(price):
    return price - 50