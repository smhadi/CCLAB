class LL1Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.current_token = None

    def next_token(self):
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
            self.index += 1
        else:
            self.current_token = None

    def match(self, expected_token):
        if self.current_token and self.current_token[0] == expected_token:
            self.next_token()
        else:
            raise ValueError(f"Syntax error: expected {expected_token}, found {self.current_token[0]}")

    def factor(self):
        token_type, token_value = self.current_token
        if token_type == 'Var:' or token_type == 'Number:':
            value = float(token_value) if token_type == 'Number:' else 0
            self.next_token()
            return value
        elif token_type == 'Left Paren:':
            self.match('Left Paren:')
            result = self.expression()
            self.match('Right Paren:')
            return result
        else:
            raise ValueError(f"Syntax error: unexpected token {token_type}")

    def term(self):
        result = self.factor()
        while self.current_token and self.current_token[0] in ['Operator:', '*','/']:
            op = self.current_token
            self.next_token()
            right = self.factor()
            if op[1] == '*':
                result *= right
            elif op[1] == '/':
                result /= right
        return result

    def expression(self):
        result = self.term()
        while self.current_token and self.current_token[0] in ['Operator:', '+', '-']:
            op = self.current_token
            self.next_token()
            right = self.term()
            if op[1] == '+':
                result += right
            elif op[1] == '-':
                result -= right
        return result

    def parse(self):
        self.next_token()
        return self.expression()

# Example usage:
input_string = "c = 3 + 5"

try:
    scanner = Scanner(input_string)
    parser = LL1Parser(scanner.tokens)
    result = parser.parse()
    print(result)
except ValueError as e:
    print("Error:", e)
