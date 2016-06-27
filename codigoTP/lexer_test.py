import lexer_rules
from ply.lex import lex
text = "if else , a=100;  i++; asd.eqw1d.holi; s = \"asafddf\" multiplicacionEscalar 0.2=123 for while #do dcfs 12!$#%& \n asd=10"
lexer = lex(module=lexer_rules)
lexer.input(text)
token = lexer.token()
while token is not None:
	print token.value
	print token.type
	token = lexer.token()
	
#"a=100;\n for (i=1; i<a; i++) while b = b+10*i;\n r_fq; #sadf fsdaf\n res=b*0.8; alumno.holu"
