def search_matrix(matrix, target):
    if not len(matrix):
        return False

    if len(matrix) == 1:
        a = search_target(matrix[0], target)
        return a

    left_matrix = 0
    right_matrix = len(matrix) - 1
    new_mid = 0
    search = None
    while left_matrix < right_matrix:
        mid_matrix = round((left_matrix + right_matrix) / 2 + 0.1)
        if matrix[left_matrix][-1] >= target:
            new_mid = mid_matrix - 1
            search = search_target(matrix[new_mid], target)
            left_matrix += 2
        elif matrix[right_matrix][0] <= target:
            new_mid = mid_matrix + 1
            search = search_target(matrix[new_mid], target)
            right_matrix -= 2
        else:
            search = search_target(matrix[mid_matrix], target)
            right_matrix -= 2
        return search
    return False


def search_target(l_matrix, target):
    left = 0
    right = len(l_matrix) - 1
    while left < right:
        mid = round((left + right) / 2 + 0.1)
        if l_matrix[mid] == target:
            return True
        elif l_matrix[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if l_matrix[0] == target:
        return True
    elif l_matrix[-1] == target:
        return True
    else:
        return False


print(search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(search_matrix([[1]], 1))
print(search_matrix([[1]], 2))
print(search_matrix([[1, 2]], 2))
