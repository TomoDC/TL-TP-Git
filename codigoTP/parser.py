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
'''text = a = 10;
b = [a];
c = [1, 2, 3];
print(a);
print("Hola");
print(c);
print((1 > 2 ? "Mun" + "do" : "a todos") + "!");
d = length(b);

print(length(c) + 5);

e = length(capitalizar("MAYUSCULAS"));
print(capitalizar("m" + "M"));

print(capitalizar(colineales(b, c) ? "B" : "C"));
multiplicacionEscalar(b, a);
print(length([1, length(multiplicacionEscalar(b, a, colineales(c, c))), length(capitalizar("2"))]));'''
'''length("IDLE");
capitalizar("-");
colineales(b, c);
'''


#a = 1; a++; if (true OR false) {a = 100;a = 200; holu = 12;} \n holu[14] = 14;\n print(\"Mundo!\"); poneenter = 12; return v=9; a = 1 == 2;"
ast = parser.parse(text, lexer)

fileout.write(ast)
fileout.write('\n')
