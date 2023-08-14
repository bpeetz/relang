class Relang:
    def __init__(self, text):
        self.ALL_POSSIBLE_DIGITS = list(map(str, [i for i in range(0, 10)]))
        self.ALL_POSSIBLE_OPERATORS = ["-", "+", "/", "*", "^"]
        self.text = text
        self.cursor = 0
        self.parsed_text = self.parse(text)

    def parse(self):


    def _peek(self):
        if len(self.text) > 0 and self.cursor < len(self.text):
            return self.text[self.cursor]
        else:
            return None

    def _pop(self):
        output = self.text[self.cursor]
        self.cursor += 1
        return output

    def _expect(self, char_expected):
        if self._peek() in char_expected:
            return True
        else:
            raise ValueError(
                f'Got {self._peek()}, but expected one of: {", ".join(char__expected)}'
            )

    def _remove_whitespace(self):
        while self._peek() == " ":
            self._pop()

    # Parse functions
    def _parse_whole_number(self):
        self._remove_whitespace()
        output = 0
        while self._peek() in self.ALL_POSSIBLE_DIGITS:
            output *= 10
            output += int(self._pop())
        return str(output)

    def _parse_operator(self):
        self._remove_whitespace()
        if self._expect(self.ALL_POSSIBLE_OPERATORS):
            return self._pop()

    def _parse_term(self):
        output = ""
        while self._peek() is not None:
            output += self._parse_whole_number()
            if self._peek() is not None:
                output += self._parse_operator()
        return output
