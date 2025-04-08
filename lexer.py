from token_class import Token

class LexicalAnalyzer:
    def __init__(self, filename):
        # Read the source code from the file
        with open(filename, 'r') as f:
            self.source_code = f.read()
        
        # Tokenize the input
        self.tokens = self._tokenize_input(self.source_code)

        # Initialize current token index and symbol table
        self.current = 0
        self.symbol_table = []

    def _tokenize_input(self, text):
        # Split the input text into tokens
        return text.split()
    
    def show_symbol_table(self):
        # Display the symbol table
        print("Symbol Table:")
        for i, ident in enumerate(self.symbol_table):
            print(f"{i}: {ident}")

    def lex(self):
        # Check if all tokens have been processed
        if self.current >= len(self.tokens):
            return None
        
        # Get the current lexeme and move to the next token
        lexeme = self.tokens[self.current]
        self.current += 1

        # Check for IDENTIFIER
        if (lexeme[0].isalpha() or lexeme[0] == "_") and all(c.isalnum() or c == "_" for c in lexeme):
            if lexeme not in self.symbol_table:
                self.symbol_table.append(lexeme)
            return Token("ID", self.symbol_table.index(lexeme))

        # Check for INTEGER
        if lexeme.startswith("-"):
            num_part = lexeme[1:]
        else:
            num_part = lexeme

        if num_part.isdigit():
            return Token("INTEGER", int(lexeme))

        # Check for FLOAT
        if lexeme.startswith("-"):
            float_part = lexeme[1:]
        else:
            float_part = lexeme

        if "." in float_part:
            parts = float_part.split(".")
            if len(parts) == 2 and all(p.isdigit() for p in parts):
                return Token("FLOAT", float(lexeme))

        # Check for Operators
        if lexeme == "&&":
            return Token("LOGICAL_AND", None)
        if lexeme == "&":
            return Token("BITWISE_AND", None)
        if lexeme == "||":
            return Token("LOGICAL_OR", None)
        if lexeme == "|":
            return Token("BITWISE_OR", None)
        
        if lexeme =="#":
            return Token("nigga", None)

        # If none match, it's an error
        return Token("ERROR", lexeme)



