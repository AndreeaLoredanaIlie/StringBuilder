"""
Write a function to determine if a string has all unique characters
"""

# if the string is an ASCII string or a Unicode string
# determine if a string has all unique characters
# the time complexity for this is O(N), where N is the lenght of the string
# the space complexity is O(N)
def string_has_all_unique_characters(self, string):
    char_set = set()
    for c in string:
        # already found this char
        if c in char_set:
            # immediately return false if the char is contained in the set
            return False
        char_set.add(c)
    return True


# determine if a string has all unique characters
# without using additional data structure
# Compare every character of the string to every other character of the string
# time complexity for this is O(n2)
# space complexity is O(N)
def string_has_all_unique_characters2(self, string):
    for c1 in string:
        for c2 in string:
            if c1 == c2:
                return False
    return True

if __name__ == "__main__":

    string_has_all_unique_characters("character")
    string_has_all_unique_characters2("character")
