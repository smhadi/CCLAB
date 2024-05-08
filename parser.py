import re

class Scanner:
    def __init__(self, input_string):
        self.input_string = input_string
        self.patterns = [
            (r'\+', 'Operator: '), (r'-', 'Operator: '), (r'\*', 'Operator: '), 
            (r'/', 'Operator: '), (r'\^', 'Operator: '), (r'=', 'Assignment: '),
            (r';', 'Delimiter: '), (r'User\s+In:', 'User In:'), (r'Print:', 'Print:'),
            (r'[a-zA-Z_][a-zA-Z0-9_]*', 'Var:'), (r'\d+(\.\d*)?', 'Number:'),
            (r'\(', 'Left Paren: '), (r'\)', 'Right Paren: ')
        ]
        self.tokens = self.tokenize()

    def tokenize(self):
        tokens = []
        input_string = self.input_string.strip()
        
        while input_string:
            match = None
            for pattern, token_type in self.patterns:
                regex_match = re.match(pattern, input_string)
                if regex_match:
                    match = (token_type, regex_match.group(0))
                    input_string = input_string[regex_match.end():].strip()
                    break
            if not match:
                raise ValueError(f"Invalid token at: '{input_string}'")
            tokens.append(match)
        
        return tokens

class LL1Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.current_token = None
        self.variables = {}

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
        if token_type == 'Var:':
            value = self.variables.get(token_value)
            if value is None:
                raise ValueError(f"Variable '{token_value}' is not defined")
            self.next_token()
            return value
        elif token_type == 'Number:':
            value = float(token_value)
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

    def assign_variable(self, var_name, value):
        self.variables[var_name] = value

    def get_variable(self, var_name):
        return self.variables.get(var_name)

# Example usage:
input_string = "x = 3 + 5"

try:
    scanner = Scanner(input_string)
    parser = LL1Parser(scanner.tokens)
    parser.match('Var:')  # Ensure first token is a variable
    var_name = scanner.tokens[0][1]  # Extract variable name
    parser.match('Assignment:')  # Ensure second token is an assignment
    result = parser.parse()  # Parse expression
    parser.assign_variable(var_name, result)  # Assign result to variable
    var_value = parser.get_variable(var_name)  # Retrieve variable value
    print(f"Value of variable '{var_name}': {var_value}")
except ValueError as e:
    print("Error:", e)
