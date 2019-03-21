"""
A palindrom is a string that is the same forwards and backwards
A palindrom has even letters and possibly an odd letter
A permutation is a rearrangement of letters. Two words with the same character counts
We need to find out if the permuted string has even letters and possibly a single odd letter
"""

def palindrom_permutation(palindrom_string, permuted_string):
    # use an hash table to count how many times each character appear
    hash_table = []
    if len(palindrom_string) != len(permuted_string):
        return False
    for item in permuted_string:
        hash_table[item] += 1
    # iterate through the dictionary and ensure that no more one character has an odd count
    # use a variable if the odd letter already appeared
    odd_letter = 0
    for k,v in hash_table:
        if v % 2 != 0:
            odd_letter += 1
        # immediately return False if there are more then 1 odd letters
        if odd_letter > 1:
            return False
    return True

if __name__ == "__main__":
    palindrom_permutation("character", "cther")
