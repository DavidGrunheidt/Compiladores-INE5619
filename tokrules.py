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

t_INTCONST = r'[0-9]+'
t_FLOATCONST = r'[0-9]+.[0-9]+'
t_STRINGCONST = r'\"([^\\\"]|\\.)*\"'
t_NULLCONST = r'null'

identifiers = ['IDFUNC', 'ID']

tokens = list(reserved.values()) + operators + specials + constants + identifiers


# Check for id's including reserved words. If it's a reserved word, change it's token type to some of the reserved ones.
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')

    if t.type == 'ID':
        if t.value.startswith('func'):
            t.type = 'IDFUNC'
        t.lexer.symbol_table[t.value] = {"linha": t.lineno, "coluna": t.lexpos, "type": t.type}

    # Check for reserved words
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Includes the prefix "ignore_" in the token declaration to force a token to be ignored. For example:
t_ignore_COMMENT = r'//.*'

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character " + str(t.value[0]) + " at line " + str(t.lineno) + " and column " + str(t.lexpos))
    t.lexer.skip(1)
