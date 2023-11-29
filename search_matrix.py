def search_matrix(matrix, target):
    for i in matrix:
        left = 0
        right = len(i) - 1
        while left < right:
            mid = (left + right) // 2
            if i[mid] == target:
                return True
            elif i[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    return False


print(search_matrix([[1, 3, 5, 7, 9], [10, 11, 16, 20, 25], [23, 30, 34, 60, 45]], 20))
print(search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
