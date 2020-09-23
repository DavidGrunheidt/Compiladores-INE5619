# module: tokrules.py
# This module just contains the lexing rules

# Reserved words and it`s token names
reserved = {
	'def': 'DEF',
	'new': 'NEW',
	'break': 'BREAK',
	'for': 'FOR',
	'if': 'IF',
	'else': 'ELSE',
	'int': 'INT',
	'float': 'FLOAT',
	'string': 'STRING',
	'print': 'PRINT',
	'read': 'READ',
	'return': 'RETURN'
}

# Operators
operators = ['ASSIGN', 'GT', 'LT', 'EQ', 'LE', 'GE', 'NEQ', 'PLUS', 'MINUS', 'STAR', 'SLASH', 'REM']

t_ASSIGN = r'='
t_GT = r'>'
t_LT = r'<'
t_EQ = r'=='
t_LE = r'<='
t_GE = r'>='
t_NEQ = r'!='
t_PLUS = r'\+'
t_MINUS = r'-'
t_STAR = r'\*'
t_SLASH = r'/'
t_REM = r'%'

# Special Symbols
specials = ['LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET', 'SEMICOLON', 'COMMA', 'DOT']

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'
t_COMMA = r','
t_DOT = r'\.'

constants = ['INTCONST', 'FLOATCONST', 'STRINGCONST', 'NULLCONST']

t_INTCONST = r'[0-9][0-9]*'
t_FLOATCONST = r'[0-9][0-9]*.[0-9][0-9]*'
t_STRINGCONST = r'\"[ a-zA-Z_0-9]*\"'
t_NULLCONST = r'null'

identifiers = ['ID']

tokens = list(reserved.values()) + operators + specials + constants + identifiers

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID') # Check for reserved words
    return t

# Define a rule so we can track line numbers
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

# Ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)