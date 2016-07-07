import lexer_rules
import parser_rules
import lex
import yacc
import sys

filein = sys.argv[1]
fileout = sys.argv[2]

if filein == "": text = raw_input()
else : 
	text = ""
	filein = open(filein, 'r')
	for line in filein:
		text += line

if fileout == "": fileout = sys.stdout
else: fileout = file.open(fileout, 'w')
	
lexer = lex.lex(module=lexer_rules)
parser = yacc.yacc(module=parser_rules)

ast = parser.parse(text, lexer)

fileout.write(ast)
fileout.write('\n')
