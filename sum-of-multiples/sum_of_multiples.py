def sum_of_multiples(limit, multiples):
    sum_list = []
    for a in multiples:
        [sum_list.append(b) for b in range(1, limit) if a != 0 and b % a == 0]

    return sum(set(sum_list))
