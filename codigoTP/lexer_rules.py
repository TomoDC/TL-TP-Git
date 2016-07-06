tokens = ['PUNTOCOMA', 'COMENTARIO', 'LLAVEABIERTA', 'LLAVECERRADA', 'IF', 'ELSE', 'LPAREN', 'RPAREN', 'FOR', 'WHILE', 'DO', 'MULTIPLICACIONESCALAR', 'CAPITALIZAR', 'COLINEALES', 'PRINT', 'LENGTH', 'IGUAL', 'SUMA', 'MENOS', 'POR', 'DIV', 'POTENCIA', 'PORCENTAJE', 'DESIGUALDAD', 'MAYOR', 'MENOR', 'AND', 'OR', 'NOT', 'TRUE', 'FALSE', 'INTERROGACION', 'DOSPUNTOS', 'VARIABLE', 'NUMBER', 'CORCHETEA', 'CADENA', 'CORCHETEC', 'COMA', 'PUNTO', 'RETURN', 'NEWLINE', 'MASMAS', 'MENOSMENOS', 'MASIGUAL', 'MENOSIGUAL', 'PORIGUAL', 'DIVIGUAL', 'IGUALIGUAL']

reserved = {
    "for" : "FOR",
	"FOR" : "FOR",
    "while" : "WHILE",
	"WHILE" : "WHILE",
    "do" : "DO",
	"DO" : "DO",
    "if" : "IF",
    "IF" : "IF",
    "else" : "ELSE",
	"ELSE" : "ELSE",
    "multiplicacionEscalar" : "MULTIPLICACIONESCALAR",
    "capitalizar" : "CAPITALIZAR",
    "colineales" : "COLINEALES",
    "print" : "PRINT",
    "length" : "LENGTH",
    "AND" : "AND",
	"OR" : "OR",
	"and" : "AND",
	"or" : "OR",
	"NOT" : "NOT",
	"not" : "NOT",	
	"BEGIN" : "BEGIN",
	"END" : "END",	
	"begin" : "BEGIN",
	"end" : "END",
	"return" : "RETURN",
	"true" : "TRUE",
	"false" : "FALSE",
	"RETURN" : "RETURN",
	"TRUE" : "TRUE",
	"FALSE" : "FALSE"
}
#Tal vez hay q ponerle el tipo a true y false.

t_PUNTO = r"\."
t_PUNTOCOMA = r"\;"
t_LLAVEABIERTA = r"\{"
t_LLAVECERRADA = r"\}"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_IGUALIGUAL = r"=="
t_IGUAL = r"="
t_MASMAS = r"\+\+"
t_MENOSMENOS = r"--"
t_MASIGUAL = r"\+="
t_SUMA = r"\+"
t_MENOSIGUAL = r"-="
t_MENOS = r"\-"
t_PORIGUAL = r"\*="
t_POR = r"\*"
t_DIV = r"\/"
t_DIVIGUAL = r"\/="
t_POTENCIA = r"\^"
t_PORCENTAJE = r"\%"
t_DESIGUALDAD = r"\!="
t_MAYOR = r"\>"
t_MENOR = r"\<"
t_INTERROGACION = r"\?"
t_DOSPUNTOS = r"\:"
t_CORCHETEA = r"\["
t_CORCHETEC = r"\]"
t_COMA = r","

def t_NUMBER(token):
    r"[0-9]+(\.[0-9]+)?"
    if token.value.find(".") >= 0:
        number_type = "float"
        number_value = float(token.value)
    else:
        number_type = "int"
        number_value = int(token.value)
    token.value =  {"value": number_value, "type": number_type}
    return token

#Asumimos que no hoy campos de un registro que a su vez sean registros 
#def t_REGISTRO(token):
#	r"[a-zA-Z]+(\.[a-zA-Z0-9]+)+"
#	return token

def t_VARIABLE(token):
	r"[a-zA-Z][\_a-zA-Z0-9]*"
	if token.value in reserved:
		token.type = reserved[ token.value ]
	return token

def t_CADENA(token):
	r'("[^"]*")'
	token.value = {"value": token.value, "type": token.type}
	return token

def t_NEWLINE(token):
    r"\n+"
    token.lexer.lineno += len(token.value)

t_ignore_WHITESPACES = r"[ \t]+"
t_ignore = " \t"

def t_COMENTARIO(token):
	r"\#[^\n]*"
	return token
#los comentarios acepta solo letras y num.

def t_error(token):
    message = "Token desconocido:"
    message += "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise Exception(message)
