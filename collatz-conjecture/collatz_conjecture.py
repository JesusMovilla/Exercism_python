def steps(number):
    step = 0
    if number == 1:
        return step
    if number > 0:
        while number != 1:
            if (number % 2) == 0:
                number = (number / 2)
            else:
                number = ((3 * number) + 1)
            step += 1
        return step
    else:
        raise ValueError(ValueError)
