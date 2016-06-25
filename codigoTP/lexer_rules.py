tokens = ['PUNTOCOMA', 'HASHTAG', 'LLAVEABIERTA', 'LLAVECERRADA', 'IF', 'ELSE', 'LPAREN', 'RPAREN', 'FOR', 'WHILE', 'DO', 'MULTIPLICACIONESCALAR', 'CAPITALIZAR', 'COLINEALES', 'PRINT', 'LENGTH', 'IGUAL', 'SUMA', 'MENOS', 'POR', 'DIV', 'POTENCIA', 'PORCENTAJE', 'DESIGUALDAD', 'MAYOR', 'MENOR', 'AND', 'OR', 'NOT', 'TRUE', 'FALSE', 'INTERROGACION', 'DOSPUNTOS', 'VARIABLE', 'INT', 'FLOAT', 'CORCHETEA', 'CORCHETEC', 'COMA', 'COMILLA', 'REGISTRO', 'BEGIN', 'END', 'RETURN']

t_PUNTOCOMA = r"\;"
t_LLAVEABIERTA = r"\{"
t_LLAVECERRADA = r"\}"
t_IF = r"if"
t_ELSE = r"else"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_FOR = r"for"
t_WHILE = r"while"
t_DO = r"do"
t_MULTIPLICACIONESCALAR = r"multiplicacionEscalar"
t_CAPITALIZAR = r"capitalizar"
t_COLINEALES = r"colineales"
t_PRINT = r"print"
t_LENGTH = r"length"
t_IGUAL = r"="
t_SUMA = r"\+"
t_MENOS = r"\-"
t_POR = r"\*"
t_DIV = r"\/"
t_POTENCIA = r"\^"
t_PORCENTAJE = r"\%"
t_DESIGUALDAD = r"\!="
t_MAYOR = r"\>"
t_MENOR = r"\<"
t_AND = r"AND"
t_OR = r"OR"
t_NOT = r"NOT"
t_INTERROGACION = r"\?"
t_DOSPUNTOS = r"\:"
t_CORCHETEA = r"\{"
t_CORCHETEC = r"\}"
t_COMA = r","
t_COMILLA = r"\""
t_BEGIN = r"begin"
t_END = r"end"
t_RETURN = r"return"
t_TRUE = r"true"
#Tal vez hay q ponerle el tipo
t_FALSE = r"false"
#Tal vez hay q ponerle el tipo


def t_INT(token):
	r"[0-9][0-9]*"
	token.value = int(token.value)
	return token
	
def t_VARIABLE(token):
	r"[a-zA-Z][\_a-zA-Z0-9]*"
	token.value = str(token.value)
	return token

#def t_CADENA(token):
#def t_CAMPO(token):

def t_REGISTRO(token):
	r"[a-zA-Z]+\.[a-zA-Z]+"
	return token

def t_FLOAT(token):
	r"[0-9][0-9]*\.[0-9]+"
	token.value = float(token.value)
	return token

def t_NEWLINE(token):
    r"\n+"
    token.lexer.lineno += len(token.value)

t_ignore = " \t"

def t_HASHTAG(token):
	r"\#"
	return token
	
def t_error(token):
    message = "Token desconocido:"
    message += "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise Exception(message)