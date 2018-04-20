def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

print "sum_all of [4, 3, 6] is 13:", sum_all([4, 3, 6]) == 13
print "sum_all of [1, 2, 3, 4] is 10:", sum_all([1, 2, 3, 4]) == 10
