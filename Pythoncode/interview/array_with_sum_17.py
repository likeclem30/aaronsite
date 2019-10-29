def check_sums(array,s):
    possible_sum =set()
    for item in array:
        if item in possible_sum:
            return True
        possible_sum.add(s-item)
    return False

    print(check_sums([10,4,5,7],17),"\n")
    print(check_sums([10,5,5,6],17))