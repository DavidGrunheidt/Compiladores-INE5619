import ply.lex as lex
import tokrules

# Build the lexer
lexer = lex.lex(module=tokrules)

# Test it out
data = '''
if (1 == 2) {
	test = .1223
	test2 = "String doida"
}
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
for tok in lexer:
     print(tok)