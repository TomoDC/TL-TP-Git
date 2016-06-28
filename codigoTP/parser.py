import lexer_rules
import parser_rules
import lex
import yacc
lexer = lex.lex(module=lexer_rules)
parser = yacc.yacc(module=parser_rules)
text = "if (true OR false) {a = 100;a = 200; holu = 12;} \n holu = 14;\n print(\"Mundo!\"); poneenter = 12; return v=9; 1 == 2;"
ast = parser.parse(text, lexer)

print ast