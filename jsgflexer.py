# -+- coding:utf-8 -*-
# license: GPLv3 or later
# author: Arne Köhn <arne@arne-koehn.de>
import re
from ply import lex

tokens = (
    'COMMENT',
    'COLON',
    'BIIMPL',
    'STR',
    'NUMBER',
    'COMMA',
    'SLASH',
    'IMPL',
    'SEMICOLON',
    'EQUALS',
    'PIPE',
    'LESS',
    'GREATER',
    'LBRACKET',
    'RBRACKET',
    'MODIFIER'
    )

t_SEMICOLON = r';'
t_EQUALS  = r'='
t_PIPE    = r'\|'
t_LESS    = r'<'
t_GREATER = r'>'
t_LBRACKET = r'\('
t_RBRACKET = r'\)'

# no return value -> discard
def t_COMMENT(t):
    r'//[^\n]*|/\*[^/]*\*/|\#[^\n]*'
    pass

# A regular expression rule with some action code
def t_NUMBER(t):
    r'-?\d+'
    t.value = int(t.value)    
    return t

def t_STR(t):
    r"'(?:[^\\']|\\.)*'|[\w§]+"
    t.value = t.value.strip("'")
    # Only single and double quotes need to be unescaped
    t.value = t.value.replace(r'\"',r'"')
    t.value = t.value.replace(r"\'",r"'")
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    if t.value[0] not in ('[', ']', '+', '*'):
        print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex(reflags=re.UNICODE)
