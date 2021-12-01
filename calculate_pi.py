def calculate_pi(n_terms):
    pi_result = 0
    nominator = 4
    denominator = 1
    operand = 1

    for _ in range(n_terms):
        pi_result += operand * (nominator/denominator)
        denominator += 2
        operand = operand * -1

    return pi_result

print(calculate_pi(1000000))