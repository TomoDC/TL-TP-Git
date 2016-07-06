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

def p_inicial2(subexps):
    'ss : s NEWLINE ss'
    subexps[0] = subexps[1] + subexps[2] + subexps[3] 

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
    	subexps[0] = subexps[1] + ' ' + subexps[2] + subexps[3] + subexps[4] + subexps[5]
     else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_if_else(subexps):
    'if : IF LPAREN v RPAREN bq ELSE bq'
	if subexps[3]["type"]=="bool":
    	subexps[0] = subexps[1] + ' ' + subexps[2] + subexps[3] + subexps[4] + subexps[5] + '\n' + subexps[6] + subexps[7]
	else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_while(subexps):
	'w : WHILE LPAREN v RPAREN bq'
	if subexps[3]["type"]=="bool":
		subexps[0] = subexps[1] + subexps[2] + subexps[3] + subexps[4] + '\n\t' + subexps[5]
	else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_do_while(subexps):
	'd : DO bq WHILE LPAREN v RPAREN PUNTOCOMA'
	if subexps[5]["type"]=="bool":
		subexps[0] = subexps[1] + subexps[2] + subexps[3] + ' ' + subexps[4] + subexps[5] + subexps[6] + subexps[7]
	else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_for1(subexps):
	'for : FOR LPAREN v RPAREN bq'
	if subexps[3]["type"]=="bool":
		subexps[0] = subexps[1] + ' ' + subexps[2] + subexps[3] + subexps[4] + '\n\t' + subexps[5]
	else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_for2(subexps):
	'for : FOR LPAREN a PUNTOCOMA v RPAREN bq'
	if subexps[5]["type"]]=="bool":
		subexps[0] = subexps[1] + ' ' + subexps[2] + subexps[3] + subexps[4] + ' ' + subexps[5] + subexps[6] + '\n\t' + subexps[7]
	else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_for3(subexps):
	'for : FOR LPAREN a PUNTOCOMA v PUNTOCOMA o RPAREN bq'
	if subexps[5]["type"]=="bool":	
		subexps[0] = subexps[1] + ' ' + subexps[2] + subexps[3] + subexps[4] + ' ' + subexps[5] + subexps[6] + ' ' + subexps[7] + subexps[8] + '\n\t' + subexps[9]
	else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_b_true(subexps):
    'f : TRUE'
    subexps[0] = subexps[1]

def p_b_false(subexps):
    'f : FALSE'
    subexps[0] = subexps[1]

def p_b_not(subexps):
    'v : NOT f'
    subexps[0] = subexps[1] + subexps[2]
    
def p_b_or(subexps):
    'v : v OR f'
	if (not (subexps[1]["type"]=="bool")): raise SemanticException("Expresion no-booleana")
    subexps[0] = subexps[1] + ' ' + subexps[2] + ' ' + subexps[3]
    
def p_b_and(subexps):
    'v : v AND f'
	if (not (subexps[1]["type"]=="bool")): raise SemanticException("Expresion no-booleana")
    subexps[0] = subexps[1] + ' ' + subexps[2] + ' ' + subexps[3]

def p_b_igualigual(subexps):
    'v : v IGUALIGUAL f'
    subexps[0] = subexps[1]["value"] + ' ' + subexps[2] + subexps[3] + ' ' + subexps[4]["value"]

def p_b_desigualdad(subexps):
    'v : v DESIGUALDAD f'
    subexps[0] = subexps[1]["value"] + ' ' + subexps[2] + ' ' + subexps[3]["value"]
    
def p_b_mayor(subexps):
    'v : v MAYOR f'
    subexps[0] = subexps[1]["value"] + ' ' + subexps[2] + ' ' + subexps[3]["value"]

def p_b_menor(subexps):
    'v : v MENOR f'
    subexps[0] = subexps[1]["value"] + ' ' + subexps[2] + ' ' + subexps[3]["value"]

def p_b_colineales(subexps):
    'v : COLINEALES LPAREN v COMA v RPAREN'
	if (not (subexps[3]["type"]=="LALAvector numerico" and subexps[5]["type"]=="LALAvector numerico"): raise SemanticException("Error en los tipos de argumentos")
    subexps[0] = subexps[1] + subexps[2] + subexps[3]["value"] + subexps[4] + ' ' + subexps[5]["value"] + subexps[6]    
    
def p_v_parentesis(subexps):
    'f : LPAREN v RPAREN'
    subexps[0] = subexps[1] + subexps[2]["value"] + subexps[3]

def p_f_v(subexps):
    'v : f'
    subexps[0] = subexps[1]

def p_v_resta(subexps):
    'v : v MENOS f'
    if (subexps[1]["type"] not in ["int", "float"] and subexps[3]["type"] not in ["int", "float"]): raise SemanticException("Incompatible type")
    subexps[0] = subexps[1]["value"] + subexps[2] + subexps[3]["value"]

def p_v_suma(subexps):
    'v : v SUMA f'
    if (subexps[1]["type"] not in ["int", "float"] and subexps[3]["type"] not in ["int", "float"]): raise SemanticException("Incompatible type")
    subexps[0] = subexps[1]["value"] + subexps[2] + subexps[3]["value"]

def p_v_por(subexps):
    'v : v POR f'
    if (subexps[1]["type"] not in ["int", "float"] and subexps[3]["type"] not in ["int", "float"]): raise SemanticException("Incompatible type")
    subexps[0] = subexps[1]["value"] + subexps[2] + subexps[3]["value"]
    
def p_v_div(subexps):
    'v : v DIV f'
    if (subexps[1]["type"] not in ["int", "float"] and subexps[3]["type"] not in ["int", "float"]): raise SemanticException("Incompatible type")
    subexps[0] = subexps[1]["value"] + subexps[2] + subexps[3]["value"]
    
def p_v_potencia(subexps):
    'v : v POTENCIA f'
    if (subexps[1]["type"] not in ["int", "float"] and subexps[3]["type"] not in ["int", "float"]): raise SemanticException("Incompatible type")
    subexps[0] = subexps[1]["value"] + subexps[2] + subexps[3]["value"]
    
def p_v_mod(subexps):
    'v : v PORCENTAJE f'
    if (subexps[1]["type"] not in ["int", "float"] and subexps[3]["type"] not in ["int", "float"]): raise SemanticException("Incompatible type")
    subexps[0] = subexps[1]["value"] + subexps[2] + subexps[3]["value"]

def p_v_pregunta(subexps):
    'v : v INTERROGACION v DOSPUNTOS f'
	if (not (subexps[1]["type"]=="bool" and subexps[3]["type"]==subexps[5]["type"]): raise SemanticException("Error en los tipos de argumentos")
    subexps[0] = subexps[1] + subexps[2] + ' ' + subexps[3] + ' ' + subexps[4] + ' ' + subexps[5]
     
def p_v_num(subexps):
    'f : NUMBER'
    red = {"value": str(subexps[1]["value"]), "type": subexps[1]["type"]}
    subexps[0] = red

def p_v_var(subexps):
    'v : VARIABLE index'
    '''asegurarse que el tipo de la variable siga siendo el mismo'''
    subexps[0] = subexps[1]
    
def p_v_mEvvb(subexps):
    'v : MULTIPLICACIONESCALAR LPAREN v COMA v COMA v RPAREN'
	if (not (subexps[3]["type"]=="LALAVectornumerico" and subexps[5]["type"]=="numero" and subexps[7]["type"]=="bool")): raise SemanticException("Error en los tipos de argumentos")
	subexps[0] = subexps[1] + subexps[2] + subexps[3] + subexps[4] + subexps[5] + subexps[6] + subexps[7] + subexps[8]
        
def p_v_mEvv(subexps):
    'v : MULTIPLICACIONESCALAR LPAREN v COMA v RPAREN'
	if (not (subexps[3]["type"]=="LALAVectornumerico" and subexps[5]["type"]=="numero")): raise SemanticException("Error en los tipos de argumentos")
    subexps[0] = subexps[1] + subexps[2] + subexps[3] + subexps[4] + subexps[5] + subexps[6]

def p_v_cap(subexps):
    'v : CAPITALIZAR LPAREN v RPAREN'
    if (subexps[3]["type"] not in ["CADENA"]): raise SemanticException("Incompatible type")
    subexps[0] = subexps[1] + subexps[2] + subexps[3] + subexps[4]

def p_v_legth(subexps):
    'v : LENGTH LPAREN v RPAREN'
    subexps[0] = subexps[1] + subexps[2] + subexps[3] + subexps[4]

def p_v_cadena(subexps):
    'v : CADENA'
    subexps[0] = subexps[1]

def p_v_explicita(subexps):
    'v : CORCHETEA lista CORCHETEC'
    subexps[0] = subexps[1]

def p_v_lista(subexps):
    'lista : lista COMA v'
    subexps[0] = subexps[1]

def p_v_lista2(subexps):
    'lista : v'
    subexps[0] = subexps[1]

def p_a_var(subexps):
    'a : VARIABLE index IGUAL v'
    subexps[0] = subexps[1] + subexps[2] + ' ' + subexps[3] + ' ' + subexps[4]["value"]

########################################

def p_a_var1(subexps):
    'index : index CORCHETEA v CORCHETEC'
    subexps[0] = subexps[1] + ' ' + subexps[2] + ' ' + subexps[3]["value"]

def p_a_var2(subexps):
    'index : index PUNTO VARIABLE'
    subexps[0] = subexps[1] + ' ' + subexps[2] + ' ' + subexps[3]["value"]

def p_a_var3(subexps):
    'index : '
    subexps[0] = ""

def p_o_masigual(subexps):
    'o : VARIABLE index MASIGUAL v'
    subexps[0] = subexps[1] + ' ' + subexps[2] + subexps[3] + ' ' + subexps[4]["value"]
    
def p_o_menosigual(subexps):
    'o : VARIABLE index MENOSIGUAL v'
    subexps[0] = subexps[1] + ' ' + subexps[2] + subexps[3] + ' ' + subexps[4]["value"]
        
def p_o_porigual(subexps):
    'o : VARIABLE index PORIGUAL v'
    subexps[0] = subexps[1] + ' ' + subexps[2] + subexps[3] + ' ' + subexps[4]["value"]

def p_o_divigual(subexps):
    'o : VARIABLE index DIVIGUAL v'
    subexps[0] = subexps[1] + ' ' + subexps[2] + subexps[3] + ' ' + subexps[4]["value"]

def p_o_masmas(subexps):
    'o : VARIABLE index MASMAS'
    subexps[0] = subexps[1] + subexps[2] + subexps[3]

def p_o_menosmenos(subexps):
    'o : VARIABLE index MENOSMENOS'
    if (types[subexps[1]] not in ["int", "float"]): raise SemanticException("Incompatible type")
    subexps[0] = subexps[1] + subexps[2] + subexps[3]
        
def p_o_masmasv(subexps):
    'o : MASMAS VARIABLE index'
    subexps[0] = subexps[1] + subexps[2] + subexps[3]

def p_o_menosmenosv(subexps):
    'o : MENOSMENOS VARIABLE index'
    subexps[0] = subexps[1] + subexps[2] + subexps[3]

def p_o_print(subexps):
    'o : PRINT LPAREN v RPAREN'
    subexps[0] = subexps[1] + subexps[2] + subexps[3] + subexps[4]

def p_bq1(subexps):
	'bq : s'
	subexps[0] = subexps[1] + subexps[2] + subexps[3]
	
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


{"tipo": "vector", "subtipo": {"tipo": "vector", "subtipo": {"tipo":"int"}}}
{"tipo": "registro", "subtipo": {"campo": {"tipo": "registro", "subtipo": {"campo2": {"tipo": "int"}}}}}

def buscar(tipo, subtipo, search):
	if (search == ""): 
		return tipo;
	if search[0] == "[": 
		if (tipo != "vector"): print "Error"
		end = search.find("]")
		return buscar(subtipo["tipo"], subtipo.get("subtipo"), search[end + 1:])
	if (tipo != "registro"): print "Error"
	split = search[1:].find(".") + 1
	if split == 0: split = len(search) + 1
	if (subtipo.get(search[1:split]) == None): print "Error"
	else: return buscar(subtipo[search[1:split]]["tipo"], subtipo[search[1:split]].get("subtipo"), search[split:])

