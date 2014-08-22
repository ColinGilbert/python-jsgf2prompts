#! /usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (C) 2010  Arne Köhn <arne@arne-koehn.de>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ply import yacc

from jsgflexer import tokens, lexer

    
class ParseException(Exception):
    def __init__(self,p):
        self.line = p.lineno
        self.token = p.value

class ItemName(str):
    pass

def p_Grammar(p):
    'Grammar : STR STR SEMICOLON Model'
    p[0] = p[4]

def p_Model(p):
    'Model : Model Rule'
    p[1][p[2][0]]=p[2][1]
    p[0] = p[1]

def p_Rules(p):
    'Model : Rule'
    p[0] = {p[1][0]:p[1][1]}

def p_Rule(p):
    'Rule :  LESS STR GREATER EQUALS RuleList SEMICOLON'
    p[0] = (p[2], p[5])

def p_Rule_Public(p):
    'Rule : STR LESS STR GREATER EQUALS RuleList SEMICOLON'
    p[0] = (p[3], p[6])

def p_Alternative(p):
    'RuleList : RuleList PIPE ItemList'
    p[1].append(p[3])
    p[0] = p[1]

def p_SingleRuleList(p):
    'RuleList : ItemList'
    p[0] = [p[1]]

def p_Word(p):
    'Item : STR'
    p[0] = [p[1]]

def p_Wlist(p):
    'Item : LBRACKET ItemList RBRACKET'
    p[0] = p[2]

def p_Itemname(p):
    'Item : LESS STR GREATER'
    p[0] = [ItemName(p[2])]

def p_ItemList(p):
    'ItemList : ItemList Item'
    p[1].extend(p[2])
    p[0] = p[1]

def p_SingleItemList(p):
    'ItemList : Item'
    p[0] = p[1]


    

#def p_rulename(p):
#    pass

# Error rule for syntax errors
def p_error(p):
    raise ParseException(p)

# Build the parser
parser = yacc.yacc()



def get_sentences(model,start):
    res = [] # list of sentences
    for alternative in model[start]:
        p = [] # possible sentences for one alternative
        for w in alternative:
            if isinstance(w,ItemName):
                subsentences = get_sentences(model,w)
                if len(p)>0:
                    newp = []
                    for l in p:
                        for s in subsentences:
                            newp.append(l+s)
                    p = newp
                else:
                    p = subsentences
            else:
                if len(p)>0:
                    for l in p:
                        l.append(w)
                else:
                    p.append([w])
        res.extend(p)
    return res

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3: # we got some file to check
        f = sys.argv[1]
        startrule = sys.argv[2]
        try:
            s = open(f).read()
        except EOFError:
            exit("File not found "+ f)
        try:
            outfile = open('prompts', 'w')
            result = parser.parse(s)
            for r in get_sentences(result,startrule):
                outfile.write('<sil> ')
                outfile.write(" ".join(r))
                outfile.write(' </sil>\n')
        except ParseException,e:
            sys.stderr.write(
                "Error at line %i, wrong token %s\n"%
                (e.line, e.token))
            print "UNPARSABLE: ",f
            parser.restart()
    else:
        print '''
pass a file and a start rule as command line arguments and this
program will print all possible sentences.
'''
