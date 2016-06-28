import lexer_rules
import parser_rules
from ply.lex import lex
from ply.yacc import yacc
lexer = lex(module=lexer_rules)
parser = yacc(module=parser_rules)
text = "if (true OR false) {a = 100;a = 200; holu = 12;} \n holu = 14;\n print(\"Mundo!\"); poneenter = 12;"
ast = parser.parse(text, lexer)

print ast
