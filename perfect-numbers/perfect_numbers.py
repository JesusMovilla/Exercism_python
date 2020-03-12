def classify(number):
    if number < 1:
        raise ValueError(ValueError)
    x = sum((n for n in range(1, number) if not number % n))
    if number == x:
        return "perfect"
    if number < x:
        return "abundant"
    if number == 1 or number > x:
        return "deficient"
