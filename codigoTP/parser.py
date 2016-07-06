import lexer_rules
import parser_rules
import lex
import yacc
lexer = lex.lex(module=lexer_rules)
parser = yacc.yacc(module=parser_rules)
text = '''for (a = 0; a < 10; a++)
	d = 1;
for (; true; ) {
	# Co
	# men
	# tario
	b = 2;
	c = 3;
}
for (d = b; b != c; a += b)
	# Co
	# men
	# tario
	e = 10;
for (b = false ? c + d : a; a + b + c == d - e - d; ) {
	a = d;
	d = a;
}
for (; a + b + c == d - e - d; b = false ? c + d : a)
	a = d;
d = a;
if (false)
	for (; true; )
		for (; false; ) {
			if (true)
				if (false) {
					f = "donde estoy?";
				} else {
					for (c = b; b > c; b = c)
						a = a;
				}
		}
else
	for (; true; )
		f = "NO";
'''


#a = 1; a++; if (true OR false) {a = 100;a = 200; holu = 12;} \n holu[14] = 14;\n print(\"Mundo!\"); poneenter = 12; return v=9; a = 1 == 2;"
ast = parser.parse(text, lexer)

print ast
