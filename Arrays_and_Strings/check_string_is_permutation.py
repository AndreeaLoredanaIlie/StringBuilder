"""
Given two strings, write a function to decide if a string is a permutation of the other
"""

# what is a permutation? two words with the same character counts
# A permutation is a rearrangement of letters.
# ask about case sensitive and if the whitespace is significant
# check of they have the same length
# one solution is to sort the strings and then to compare them
# time complexity is O(1)
# space complexity is O()
def check_string_is_permutation(self, string1, string2):
    sorted_string1 = sort(string1)
    sorted_string2 = sort(string2)
    return string1 == string2

if __name__ == "__main__":

    check_string_is_permutation("character", "cther")
