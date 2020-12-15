# David Grunheidt Vilela Ordine - 16202253
import sys
import ply.lex as lex
import tokrules

def generateTokensListFromCode(file_path: str) -> list:
    # Read the entire contents of the file
    file = open(file_path, 'r')
    code = file.read()
    file.close()

    # Build the lexer
    lexer = lex.lex(module=tokrules)
    lexer.symbol_table = dict()

    # Give the lexer some input
    lexer.input(code)

    tokens_list = []

    # Tokenize
    for token in lexer:
        tokens_list.append(token)

    return tokens_list

    # print("\nSymbol table:\n")
    # print(lexer.symbol_table)

if __name__ == '__main__':
    # Get the file path
    file_path = sys.argv[1]

    for token in generateTokensListFromCode(file_path):
        print(token)
