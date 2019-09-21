def sum_of_divisible_by_n(low, high, n):
    result = 0
    for x in range(low, high+1):
        if x % n == 0:
            result += x
    return result

print(sum_of_divisible_by_n(0,200,3))