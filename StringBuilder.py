class StringBuilder:

    # Efficient string concatenation

    def __init__(self):
        self.array = []

    # Append substring to the existing string
    def append(self, word):
        self.array.append(str(word))
        return True

    def delete_substring(self, start, end):
        # TODO
        pass

    # Delete char at index
    def delete_char_at(self, index):

        if index > len(self.array) - 1 or index < 0:
            raise RuntimeError("index must be (0 <= index <= length-1)")

        prev_substring_lenght = 0
        for i in range(len(self.array)):
            substring_lenght = len(self.array[i])
            substring = self.array[i]
            if index <= prev_substring_lenght + substring_lenght:
                char_index = index - idx
                self.array[i] = substring[:char_index] + substring[char_index:]
            prev_substring_lenght += len(substring)

    # Build the string
    def build(self):
        return ''.join(self.array)

    def to_string(self):
        return self.build()
