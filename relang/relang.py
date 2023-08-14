class Relang:
    cursor = 0
    def __init__(self, text):
        self.text = text

    def peek(self):
        return self.text[cursor]

    def pop(self):
        output = self.text[cursor]
        cursor += 1
        return output

    def expect(self, char_expected):
        if self.peek() in char_expected:
            return true
        else:
            raise ValueError(f'Got {self.peek()}, but expected one of: {char_expected.join(" ")}')
