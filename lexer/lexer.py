# David Grunheidt Vilela Ordine - 16202253

import sys
import ply.lex as lex
import tokrules

# Get the file path
file_path = sys.argv[1]

# Read the entire contents of the file
file = open(file_path, 'r')
code = file.read()
file.close()

# Build the lexer
lexer = lex.lex(module=tokrules)
lexer.symbol_table = dict()

# Give the lexer some input
lexer.input(code)

# Tokenize
for tok in lexer:
     print(tok)

print("\nSymbol table:\n")
print(lexer.symbol_table)