# 1. Reverse Vowels
# 
# Given a string `s`, reverse only all the vowels in the string and return it.
# 
# The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.
# 
# **Example 1**:
# 
# ```
# Input: s= "hello"
# Output: "holle"
# ```
# 
# **Example 2**:
# 
# ```
# Input: s= "AEIOU"
# Output: "UOIEA"
# ```
# 
# **Example 3**:
# 
# ```
# Input: s= "DesignGUrus"
# Output: "DusUgnGires"
# ```

# def change_vowels(word):
#     data = ['a', 'e', 'i', 'o', 'u']
#     new_word = list(map(lambda x: x, word))
#     left = 0
#     right = len(word) - 1
#     while left < right:
#         if word[left].lower() in data and word[right].lower() in data:
#             new_word.insert(left, new_word.pop(right))
#             new_word.insert(right, new_word.pop(left + 1))
#             left += 1
#             right -= 1
#         elif not (word[left] in data):
#             left += 1
#         else:
#             right -= 1
#
#     return "".join(new_word)


def change_vowels(word):
    data = ['a', 'e', 'i', 'o', 'u']
    left_word = ''
    right_word = ''
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left].lower() in data and word[right].lower() in data:
            left_word += word[right]
            right_word += word[left]
            left += 1
            right -= 1
        elif not (word[left] in data):
            left_word += word[left]
            left += 1
        else:
            right_word += word[right]
            right -= 1
    if len(left_word + right_word) != len(word):
        left_word += word[left]
    new_word = left_word + right_word[::-1]
    return new_word


print(change_vowels("hello"))
print(change_vowels("AEIOU"))
print(change_vowels("DesignGUrus"))
