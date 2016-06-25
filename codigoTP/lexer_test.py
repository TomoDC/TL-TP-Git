import lexer_rules
from ply.lex import lex
text = "if (a=100) (asd + 80)"
lexer = lex(module=lexer_rules)
lexer.input(text)
token = lexer.token()
while token is not None:
	print token.value
	token = lexer.token()
