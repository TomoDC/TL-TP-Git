import lexer_rules
import parser_rules
import lex
import yacc
lexer = lex.lex(module=lexer_rules)
parser = yacc.yacc(module=parser_rules)
text = '''siete = false;
hola = [1, 2, 3][2];
f = false;
x = "y";
y = "x";
campo = [{campo:"1"}, {campo:"2"}, {campo:"3"}][1];
campo = {e:2, eda:["a"][2 + 4], A:8.5};
a = {nombre:"Jose", edad:length("hola")};
b = 10;
j = "";
g = 6;
c = 1.1;
dos = 2 > 2;
print({ca:["1", "2", "4"][5]}.ca);
algo = true;
no = false;
amarillo = [true, true][2];
if ([false][{m:2}.m] == (b > 10))
	while (5 > 10)
		for (; true; ) {
			#AA#AA
			if (f) {
				print("x" + x);
			} else {
				do
					print("y" + y);
				while (1 == 1);
				aa = true AND false;
				bb = NOT aa;
			}
			#print({dos:[1, 2, 3][2 * 3]}.dos + {e:"a", j:j, r:5.5}.r);
		}
if (algo)
	if (no)
		print(2);
	else
		while (amarillo)
			do
				z = [a.edad + length("doce" + capitalizar("2")) / 2, 1.0 + (siete ? ((aa OR bb AND (2 != length("")) ? 1 : 2)) : g * 12 % 3), NOT aa ? b / -5 : c];
			while (dos);
'''


#a = 1; a++; if (true OR false) {a = 100;a = 200; holu = 12;} \n holu[14] = 14;\n print(\"Mundo!\"); poneenter = 12; return v=9; a = 1 == 2;"
ast = parser.parse(text, lexer)

print ast
