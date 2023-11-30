def guess(num, pick):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    elif num == pick:
        return 0


def guess_number(n, pick):
    all_num = [i for i in range(1, n + 1)]
    left = 0
    right = len(all_num) - 1
    if len(all_num) == 1:
        return n
    if all_num[0] == pick:
        return pick
    elif all_num[-1] == pick:
        return pick

    while left < right:
        mid = (left + right) // 2
        api = guess(all_num[mid], pick)
        if api == -1:
            right = mid + api
        elif api == 1:
            left = mid + api
        else:
            return all_num[mid]


# print(guess_number(10, 6))
# print(guess_number(1, 1))
# print(guess_number(2, 1))
print(guess_number(4, 1))
