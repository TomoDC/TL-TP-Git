from lexer_rules import tokens
#from operator import add, mul
#from expressions import BinaryOperation, Number

types=dict()
subtypes=dict()

class SemanticException(Exception) :
	pass

def p_inicial(subexps):
    'ss : s'
    subexps[0] = subexps[1]

def p_inicial3(subexps):
    'ss : s ss'
    subexps[0] = subexps[1] + '\n' + subexps[2] 

def p_s_if(subexps):
    's : if'
    subexps[0] = subexps[1]

def p_s_while(subexps):
    's : w'
    subexps[0] = subexps[1]    

def p_s_do(subexps):
    's : d'
    subexps[0] = subexps[1]

def p_s_for(subexps):
    's : for'
    subexps[0] = subexps[1]
    
def p_s_asig(subexps):
    's : a PUNTOCOMA'
    subexps[0] = subexps[1] + subexps[2] 
    
def p_s_o(subexps):
    's : o PUNTOCOMA'
    subexps[0] = subexps[1] + subexps[2] 

def p_s_r(subexps):
    's : RETURN r PUNTOCOMA'
    subexps[0] = subexps[1] + ' ' + subexps[2] + subexps[3]

def p_s_coment(subexps):
    's : COMENTARIO'
    subexps[0] = subexps[1]

def p_r_v(subexps):
    'r : v'
    subexps[0] = subexps[1]["value"]

def p_r_a(subexps):
    'r : a'
    subexps[0] = subexps[1]

def p_r_o(subexps):
    'r : o'
    subexps[0] = subexps[1]

########################################

def p_if(subexps):
    'if : IF LPAREN v RPAREN bq'
    if subexps[3]["type"]=="bool":
    	subexps[0] = subexps[1] + ' ' + subexps[2] + subexps[3]["value"] + subexps[4] + subexps[5]
    else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_if_else(subexps):
    'if : IF LPAREN v RPAREN bq ELSE bq'
    if subexps[3]["type"]=="bool":
    	subexps[0] = subexps[1] + ' ' + subexps[2] + subexps[3]["value"] + subexps[4] + subexps[5] + '\n' + subexps[6] + subexps[7]
    else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_while(subexps):
	'w : WHILE LPAREN v RPAREN bq'
	if subexps[3]["type"]=="bool":
		subexps[0] = subexps[1] + subexps[2] + subexps[3]["value"] + subexps[4] + '\n\t' + subexps[5]
	else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_do_while(subexps):
	'd : DO bq WHILE LPAREN v RPAREN PUNTOCOMA'
	if subexps[5]["type"]=="bool":
		subexps[0] = subexps[1] + subexps[2] + subexps[3] + ' ' + subexps[4] + subexps[5]["value"] + subexps[6] + subexps[7]
	else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_for1(subexps):
	'for : FOR LPAREN PUNTOCOMA v PUNTOCOMA RPAREN bq'

	if subexps[4]["type"]=="bool":
		subexps[0] = subexps[1] + ' ' + subexps[2] + subexps[3] + ' '  + subexps[4]["value"] + subexps[5] + subexps[6] + '\n\t' + subexps[7]
	else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_for2(subexps):
	'for : FOR LPAREN a PUNTOCOMA v PUNTOCOMA RPAREN bq'
	if subexps[5]["type"]=="bool":
		subexps[0] = subexps[1] + ' ' + subexps[2] + subexps[3] + subexps[4] + ' ' + subexps[5]["value"] + subexps[6] + subexps[7] + '\n\t' + subexps[8]
	else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_for3(subexps):
	'for : FOR LPAREN a PUNTOCOMA v PUNTOCOMA o RPAREN bq'
	if subexps[5]["type"]=="bool":	
		subexps[0] = subexps[1] + ' ' + subexps[2] + subexps[3] + subexps[4] + ' ' + subexps[5]["value"] + subexps[6] + ' ' + subexps[7] + subexps[8] + '\n\t' + subexps[9]
	else:
		raise SemanticException("Expresion no-booleana en la guarda")


def p_b_true(subexps):

    '''f : TRUE
         | FALSE'''

    subexps[0] = dict()
    subexps[0]["value"] = subexps[1]
    subexps[0]["type"] = "bool"

def p_b_not(subexps):
    'v : NOT f'
    subexps[0] = dict()
    subexps[0]["type"] = "bool"
    subexps[0]["value"] = subexps[1] + subexps[2]["value"]
    
def p_b_and_or(subexps):
    '''v : v OR f
    v : v AND f'''
    if (not (subexps[1]["type"]=="bool")): raise SemanticException("Expresion no-booleana")
    subexps[0] = dict()
    subexps[0]["type"] = "bool"
    subexps[0]["value"] = subexps[1]["value"] + ' ' + subexps[2] + ' ' + subexps[3]["value"]
    
def p_b_igualigual(subexps):
    '''v : v IGUALIGUAL f
    v : v DESIGUALDAD f'''
    if (not (subexps[1]["type"]==subexps[3]["type"])): raise SemanticException("Comparacion entre valores de distinto tipo") 
    # Comparar subtipos
    subexps[0] = dict()
    subexps[0]["type"] = "bool"
    subexps[0]["value"] = subexps[1]["value"] + ' ' + subexps[2] + ' ' + subexps[3]["value"]

def p_b_mayor(subexps):
    '''v : v MAYOR f
    v : v MENOR f'''
    subexps[0] = dict()
    subexps[0]["type"] = "bool"
    subexps[0]["value"] = subexps[1]["value"] + ' ' + subexps[2] + ' ' + subexps[3]["value"]

def p_v_parentesis(subexps):
    'f : LPAREN v RPAREN'
    subexps[0]["type"] = subexps[2]["type"]
    subexps[0]["value"] = subexps[1] + subexps[2]["value"] + subexps[3]

def p_f_v(subexps):
    'v : f'
    subexps[0] = subexps[1]

def p_v_binaria(subexps):
    '''v : v MENOS f
    v : v POR f
    v : v DIV f
    v : v POTENCIA f
    v : v PORCENTAJE f'''
    if (subexps[1]["type"] not in ["int", "float"] and subexps[3]["type"] not in ["int", "float"]): 
        raise SemanticException("Incompatible type")
    subexps[0] = dict()
    subexps[0]["type"] = "int" if subexps[1]["type"]=="int" and subexps[3]["type"]=="int" else "float"
    subexps[0]["value"] = subexps[1]["value"] + ' ' + subexps[2] + ' ' + subexps[3]["value"]

def p_v_suma(subexps):
    'v : v SUMA f'
    subexps[0] = dict()
    if (subexps[1]["type"] in ["int", "float"] and subexps[3]["type"] in ["int", "float"]): 
	    subexps[0]["type"] = "int" if subexps[1]["type"]=="int" and subexps[3]["type"]=="int" else "float"
    elif (subexps[1]["type"] in ["CADENA"] and subexps[3]["type"] in ["CADENA"]):
	    subexps[0]["type"] = "CADENA"
    else: raise SemanticException("Incompatible type")
    subexps[0]["value"] = subexps[1]["value"] + ' ' + subexps[2] + ' ' + subexps[3]["value"]

def p_v_pregunta(subexps):
    'v : v INTERROGACION v DOSPUNTOS f'
    if (not (subexps[1]["type"]=="bool" and subexps[3]["type"]==subexps[5]["type"])): raise SemanticException("Error en los types de argumentos")
    subexps[0]["type"] = "bool"
    subexps[0]["value"] = subexps[1]["value"] + subexps[2] + ' ' + subexps[3]["value"] + ' ' + subexps[4] + ' ' + subexps[5]["value"]
     
def p_v_num(subexps):
    'f : NUMBER'
    red = {"value": str(subexps[1]["value"]), "type": subexps[1]["type"]}
    subexps[0] = red

def p_v_var(subexps):
    'f : VARIABLE index'
    subexps[0] = dict()
    subexps[0]["type"] = buscar(types[subexps[1]], subtypes.get(subexps[1]), subexps[2]["value"])
    subexps[0]["value"] = subexps[1] + subexps[2]["value"]

def p_b_colineales(subexps):
    'v : COLINEALES LPAREN v COMA v RPAREN'
    if (not (subexps[3]["type"]=="vector" and subexps[5]["type"]=="vector")): raise SemanticException("Error en los tipos de argumentos")
    if (not (subexps[3]["subtipo"]["type"] in ["int", "float"] and subexps[5]["subtipo"]["type"] in ["int", "float"])): raise SemanticException("Error en los tipos de argumentos")
    subexps[0]["type"] = "bool"
    subexps[0]["value"] = subexps[1] + subexps[2] + subexps[3]["value"] + subexps[4] + ' ' + subexps[5]["value"] + subexps[6]    
    
def p_v_mEvvb(subexps):
    'v : MULTIPLICACIONESCALAR LPAREN v COMA v COMA v RPAREN'
    if (not (subexps[3]["type"]=="vector")): raise SemanticException("Error en los tipos de argumentos")
    if (not (subexps[3]["subtipo"]["type"] in ["int", "float"])): raise SemanticException("Error en los tipos de argumentos")
    if (not (subexps[5]["type"] in ["int", "float"]=="numero" and subexps[7]["type"]=="bool")): raise SemanticException("Error en los tipos de argumentos")
    subexps[0]["type"] = "int"
    subexps[0]["value"] = subexps[1] + subexps[2] + subexps[3] + subexps[4] + subexps[5] + subexps[6] + subexps[7] + subexps[8]
        
def p_v_mEvv(subexps):
    'v : MULTIPLICACIONESCALAR LPAREN v COMA v RPAREN'
    if (not (subexps[3]["type"]=="vector")): raise SemanticException("Error en los tipos de argumentos")
    if (not (subexps[3]["subtipo"]["type"] in ["int", "float"])): raise SemanticException("Error en los tipos de argumentos")
    if (not (subexps[5]["type"] in ["int", "float"])): raise SemanticException("Error en los tipos de argumentos")
    subexps[0]["type"] = "float"
    subexps[0]["value"] = subexps[1] + subexps[2] + subexps[3] + subexps[4] + subexps[5] + subexps[6]

def p_v_cap(subexps):
    'v : CAPITALIZAR LPAREN v RPAREN'
    if (subexps[3]["type"] not in ["CADENA"]): raise SemanticException("Incompatible type")
    subexps[0]["type"] = "CADENA"
    subexps[0]["value"] = subexps[1] + subexps[2] + subexps[3]["value"] + subexps[4]

def p_v_length(subexps):
    'v : LENGTH LPAREN v RPAREN'
    if subexps[3]["type"] not in ["CADENA", "vector"]: raise SemanticException("Incompatible type")
    subexps[0] = dict()
    subexps[0]["type"] = "int"
    subexps[0]["value"] = subexps[1] + subexps[2] + subexps[3]["value"] + subexps[4]

def p_f_cadena(subexps):
    'f : CADENA'
    subexps[0] = subexps[1]

def p_v_explicita(subexps):
    'expl : CORCHETEA lista CORCHETEC'
    subexps[0] = dict()
    subexps[0]["type"] = "vector"
    subexps[0]["subtype"] = {"type": subexps[2]["type"], "subtype": subexps[2].get("subtype")}
    subexps[0]["value"] = subexps[1] + subexps[2]["value"] + subexps[3]

def p_v_explicita_2(subexps):
    'expl : LLAVEABIERTA listareg LLAVECERRADA'
    subexps[0] = dict()
    subexps[0]["type"] = "registro"
    subexps[0]["subtype"] = {"type": subexps[2]["type"], "subtype": subexps[2].get("subtype")}
    subexps[0]["value"] = subexps[1] + subexps[2]["value"] + subexps[3]

def p_v_lista(subexps):
    'lista : lista COMA v'
    if (subexps[1]["type"] != subexps[3]["type"]): raise SemanticException("Vectors can only have one type")
    subexps[0] = dict()
    subexps[0]["type"] = subexps[1]["type"]
    subexps[0]["value"] = subexps[1]["value"] + subexps[2] + ' ' + subexps[3]["value"]

def p_v_lista2(subexps):
    'lista : v'
    subexps[0] = subexps[1]

def p_v_listareg(subexps):
    'listareg : listareg COMA VARIABLE DOSPUNTOS v'
    subexps[0] = dict()
    subexps[0]["type"] = "registro"
    subexps[0]["subtype"] = dict()
    subexps[0]["subtype"][subexps[3]] = {"type": subexps[5]["type"], "subtype": subexps[5].get("subtype")} ### mejorar
    subexps[0]["value"] = subexps[1]["value"] + subexps[2] + ' ' + subexps[3] + subexps[4] + subexps[5]["value"]

def p_v_listareg2(subexps):
    'listareg : VARIABLE DOSPUNTOS v'
    subexps[0] = dict()
    subexps[0]["type"] = "registro"
    subexps[0]["subtype"] = {subexps[1]: {"type": subexps[3]["type"], "subtype": subexps[3].get("subtype")}} ### mejorar
    subexps[0]["value"] = subexps[1] + subexps[2] + subexps[3]["value"]

def p_v_v2explicita(subexps):
    'f : expl index'
    subexps[0] = dict()
    subexps[0]["type"] = buscar(subexps[1]["type"], subexps[1]["subtype"], subexps[2]["value"])
    subexps[0]["value"] = subexps[1]["value"] + subexps[2]["value"]

def p_a_var(subexps):
    'a : VARIABLE index IGUAL v' # mejorar
    types[subexps[1]] = subexps[4]["type"]
    subexps[0] = subexps[1] + subexps[2]["value"] + ' ' + subexps[3] + ' ' + subexps[4]["value"]

########################################

def p_a_var1(subexps):
    'index : index CORCHETEA v CORCHETEC'

    print subexps[3]

    subexps[0] = dict()
    subexps[0]["type"] = "vector"
    subexps[0]["subtype"] = {"type" : subexps[1]["type"], "subtype" : subexps[1].get("subtype")}
    if (subexps[3]["type"] not in ["int", "float"]): raise SemanticException("Vector index not a number")
    subexps[0]["value"] = subexps[1]["value"] + subexps[2] + subexps[3]["value"] + subexps[4]

def p_a_var2(subexps):
    'index : index PUNTO VARIABLE'
    subexps[0] = dict()
    subexps[0]["type"] = "registro"
    subexps[0]["subtype"] = {subexps[3]: {"type": subexps[1]["type"]}}
    subexps[0]["value"] = subexps[1]["value"] + subexps[2] + subexps[3]

def p_a_var3(subexps):
    'index : '
    subexps[0] = dict()
    subexps[0]["type"] = {"type" : "empty"}
    subexps[0]["value"] = ""

def p_o_masigual(subexps):
    '''o : VARIABLE index MASIGUAL v
    o : VARIABLE index MENOSIGUAL v
    o : VARIABLE index PORIGUAL v
    o : VARIABLE index DIVIGUAL v'''
	
    if (types[subexps[1]] == "vector" or types[subexps[1]] == "registro"):
	    asigtype = buscar(types[subexps[1]], subtypes[subexps[1]], subexps[2]["value"])
    else: asigtype = types[subexps[1]]
    if (asigtype not in ["int", "float"] or subexps[4]["type"] not in ["int", "float"]): raise SemanticException("Valor no numerico")

    subexps[0] = subexps[1] + ' ' + subexps[2]["value"] + subexps[3] + ' ' + subexps[4]["value"]
    
def p_o_masmas(subexps):
    '''o : VARIABLE index MASMAS
    o : VARIABLE index MENOSMENOS'''

    if (types[subexps[1]] == "vector" or types[subexps[1]] == "registro"):
	    asigtype = buscar(types[subexps[1]], subtypes[subexps[1]], subexps[2]["value"])
    else: asigtype = types[subexps[1]]
    if (asigtype not in ["int", "float"]): raise SemanticException("Valor no numerico")
    subexps[0] = subexps[1] + subexps[2]["value"] + subexps[3]

def p_o_masmasv(subexps):
    '''o : MASMAS VARIABLE index
    o : MENOSMENOS VARIABLE index'''
    if (types[subexps[2]] == "vector" or types[subexps[2]] == "registro"):
	    asigtype = buscar(types[subexps[2]], subtypes[subexps[2]], subexps[3]["value"])
    else: asigtype = types[subexps[1]]
    if (asigtype not in ["int", "float"]): raise SemanticException("Valor no numerico")
    subexps[0] = subexps[1] + subexps[2] + subexps[3]["value"]

def p_o_print(subexps):
    'o : PRINT LPAREN v RPAREN'
    subexps[0] = subexps[1] + subexps[2] + subexps[3]["value"] + subexps[4]

def p_bq1(subexps):
	'bq : s'
	subexps[0] = subexps[1]
	
def p_bq2(subexps):
	'bq : LLAVEABIERTA ss LLAVECERRADA'
	subexps[0] = subexps[1] + '\n\t' + "\n\t".join(subexps[2].split("\n")) + '\n' + subexps[3]

def p_error(token):
    message = "[Syntax error]"
    if token is not None:
        message += "\ntype:" + token.type
        message += "\nvalue:" + str(token.value)
        message += "\nline:" + str(token.lineno)
        message += "\nposition:" + str(token.lexpos)
    raise Exception(message)


{"type": "vector", "subtype": {"type": "vector", "subtype": {"type":"int"}}}
{"type": "registro", "subtype": {"campo": {"type": "registro", "subtype": {"campo2": {"type": "int"}}}}}

def buscar(tipo, subtype, search):
	if (search == ""): 
		return tipo;
	if search[0] == "[": 
		if (tipo != "vector"): print "Error"
		end = search.find("]")
		return buscar(subtype["type"], subtype.get("subtype"), search[end + 1:])
	if (tipo != "registro"): print "Error"
	split = search[1:].find(".") + 1
	if split == 0: split = len(search) + 1
	if (subtype.get(search[1:split]) == None): print "Error"
	else: return buscar(subtype[search[1:split]]["type"], subtype[search[1:split]].get("subtype"), search[split:])

