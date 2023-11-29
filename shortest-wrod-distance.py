#
# 2. Shortest Word Distance
#
# Given an array of strings `words` and two different strings that already exist in the array `word1` and `word2`,
# return  the shortest distance between these two words in the list.
#
# **Example 1**:
#
# ```
# Input: words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], word1 = "fox", word2 = "dog"
# Output: 5
# Explanation: The distance between "fox" and "dog" is 5 words.
# ```
#
# **Example 2**:
#
# ```
# Input: words = ["a", "c", "d", "b", "a"], word1 = "a", word2 = "b"
# Output: 1
# Explanation: The shortest distance between "a" and "b" is 1 word
# ```
def get_between_distance(word_list, word1, word2):
    search_words = [word1, word2]
    width = len(word_list)
    left = 0
    right = len(word_list) - 1
    while left < right:
        if word_list[left] in search_words and word_list[right] in search_words:
            width = right - left

        if not (word_list[left] in [word1, word2]) or word_list[right] in [word1, word2]:
            left += 1
        else:
            right -= 1
    return width


print(get_between_distance(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 'fox', 'dog'))
print(get_between_distance(["a", "c", "d", "b", "a"], 'a', 'b'))
