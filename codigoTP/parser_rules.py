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
		subexps[0] = subexps[1] + subexps[2] + subexps[3]["value"] + subexps[4] + subexps[5]
	else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_do_while(subexps):
	'd : DO bq WHILE LPAREN v RPAREN PUNTOCOMA'
	if subexps[5]["type"]=="bool":
		subexps[0] = subexps[1] + '\n' + subexps[2] + subexps[3] + ' ' + subexps[4] + subexps[5]["value"] + subexps[6] + subexps[7]
	else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_for1(subexps):
	'for : FOR LPAREN PUNTOCOMA v PUNTOCOMA RPAREN bq'

	if subexps[4]["type"]=="bool":
		subexps[0] = subexps[1] + ' ' + subexps[2] + subexps[3] + ' '  + subexps[4]["value"] + subexps[5] + subexps[6] + subexps[7]
	else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_for2(subexps):
	'for : FOR LPAREN a PUNTOCOMA v PUNTOCOMA RPAREN bq'
	if subexps[5]["type"]=="bool":
		subexps[0] = subexps[1] + ' ' + subexps[2] + subexps[3] + subexps[4] + ' ' + subexps[5]["value"] + subexps[6] + subexps[7] + subexps[8]
	else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_for3(subexps):
	'for : FOR LPAREN a PUNTOCOMA v PUNTOCOMA o RPAREN bq'
	if subexps[5]["type"]=="bool":	
		subexps[0] = subexps[1] + ' ' + subexps[2] + subexps[3] + subexps[4] + ' ' + subexps[5]["value"] + subexps[6] + ' ' + subexps[7] + subexps[8] + subexps[9]
	else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_for4(subexps):
	'for : FOR LPAREN a PUNTOCOMA v PUNTOCOMA a RPAREN bq'
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
    if subexps[2]["type"]=="bool":
        subexps[0] = dict()
        subexps[0]["type"] = "bool"
        subexps[0]["value"] = subexps[1] + ' ' + subexps[2]["value"]
    else:
        raise SemanticException("Expresion no compatible con bool")

def p_b_and_or(subexps):
    '''v : v OR f
    v : v AND f'''
    if (not ((subexps[1]["type"]=="bool") and (subexps[3]["type"]=="bool"))): raise SemanticException("Expresion no-booleana")
    subexps[0] = dict()
    subexps[0]["type"] = "bool"
    subexps[0]["value"] = subexps[1]["value"] + ' ' + subexps[2] + ' ' + subexps[3]["value"]
    
def p_b_igualigual(subexps):
    '''v : v IGUALIGUAL f
    v : v DESIGUALDAD f'''
    if not (subexps[1]["type"]==subexps[3]["type"]): 
        if not(subexps[1]["type"] in ["int", "float"] and subexps[3]["type"] in ["int", "float"]):
            raise SemanticException("Comparacion entre valores de distinto tipo") 
    if ((subexps[1]["type"]=="vector" and subexps[3]["type"]=="vector") or (subexps[1]["type"]=="registro" and subexps[3]["type"]=="registro")):
        if not(subexps[1]["subtype"]==subexps[3]["subtype"]): #comentarioMaxi: es una comparacion grosera porque si internamente la diferencia fuera de un int a un float, deberia tomarlo igual. Pero bueno :/
			raise SemanticException("Comparacion entre valores de distinto tipo") 
    subexps[0] = dict()
    subexps[0]["type"] = "bool"
    subexps[0]["value"] = subexps[1]["value"] + ' ' + subexps[2] + ' ' + subexps[3]["value"]

def p_b_mayor(subexps):
    '''v : v MAYOR f
    v : v MENOR f'''
	#comentarioMaxi: esta tiene la misma funcion que la de comparar por IGUALIGUAL etc. Si mantenemos este chequeo de tipos podriamos unir las reglas; si aca solo aceptamos string o numerico habria que cambiar este codigo.
    if not (subexps[1]["type"]==subexps[3]["type"]): 
        if not(subexps[1]["type"] in ["int", "float"] and subexps[3]["type"] in ["int", "float"]):
            raise SemanticException("Comparacion entre valores de distinto tipo") 
    subexps[0] = dict()
    subexps[0]["type"] = "bool"
    subexps[0]["value"] = subexps[1]["value"] + ' ' + subexps[2] + ' ' + subexps[3]["value"]

def p_v_parentesis(subexps):
    'f : LPAREN v RPAREN'
    subexps[0] = dict()
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
    if (not (subexps[1]["type"]=="bool" and subexps[3]["type"]==subexps[5]["type"])): 
        if (not (subexps[1]["type"]=="bool" and subexps[3]["type"] in ["int", "float"] and subexps[5]["type"] in ["int", "float"])):
            raise SemanticException("Error en los tipos de argumentos")
    subexps[0] = dict()
    subexps[0]["type"] = subexps[3]["type"]
    subexps[0]["value"] = subexps[1]["value"] + subexps[2] + ' ' + subexps[3]["value"] + ' ' + subexps[4] + ' ' + subexps[5]["value"]
     
def p_v_num(subexps):
    'f : NUMBER'
    red = {"value": str(subexps[1]["value"]), "type": subexps[1]["type"]}
    subexps[0] = red

def p_v_mnum(subexps):
    'f : MENOS NUMBER'
    red = {"value": subexps[1] + str(subexps[2]["value"]), "type": subexps[2]["type"]}
    subexps[0] = red

def p_v_var(subexps):
    'f : VARIABLE index'

    print subexps[1]
    print subexps[2]

    subexps[0] = dict()
    subexps[0]["type"], subexps[0]["subtype"] = buscar(types[subexps[1]], subtypes.get(subexps[1]), subexps[2]["value"])
    subexps[0]["value"] = subexps[1] + subexps[2]["value"]

def p_b_colineales(subexps):
    'f : COLINEALES LPAREN v COMA v RPAREN'
    if (not (subexps[3]["type"]=="vector" and subexps[5]["type"]=="vector")): raise SemanticException("Error en los tipos de argumentos")
    if (not (subexps[3]["subtype"]["type"] in ["int", "float"] and subexps[5]["subtype"]["type"] in ["int", "float"])): raise SemanticException("Error en los tipos de argumentos")
    subexps[0] = dict()
    subexps[0]["type"] = "bool"
    subexps[0]["value"] = subexps[1] + subexps[2] + subexps[3]["value"] + subexps[4] + ' ' + subexps[5]["value"] + subexps[6]    
    
def p_v_mEvvb(subexps):
    'f : MULTIPLICACIONESCALAR LPAREN v COMA v COMA v RPAREN'
    if (not (subexps[3]["type"]=="vector")): raise SemanticException("Error en los tipos de argumentos")
    if (not (subexps[3]["subtype"]["type"] in ["int", "float"])): raise SemanticException("Error en los tipos de argumentos")
    if (not (subexps[5]["type"] in ["int", "float"] and subexps[7]["type"]=="bool")): raise SemanticException("Error en los tipos de argumentos")
    subexps[0] = dict()
    subexps[0]["type"] = "vector"
    subexps[0]["subtype"] = dict()
    subexps[0]["subtype"]["type"] = "int" if subexps[3]["type"]["subtype"]["type"]=="int" and subexps[5]["type"]=="int" else "float"
	#comentarioMaxi: aca al no saber el valor del bool no podemos usar eso para saber si devolvemos un vector de enteros o de floats. Ante la duda ponemos float que es mas general (excepto claro que las cosas que se multiplican sean todos int's)
    subexps[0]["value"] = subexps[1] + subexps[2] + subexps[3]["value"] + subexps[4] + subexps[5]["value"] + subexps[6] + subexps[7]["value"] + subexps[8]
        
def p_v_mEvv(subexps):
    'f : MULTIPLICACIONESCALAR LPAREN v COMA v RPAREN'
    if (not (subexps[3]["type"]=="vector")): raise SemanticException("Error en los tipos de argumentos")
    if (not (subexps[3]["subtype"]["type"] in ["int", "float"])): raise SemanticException("Error en los tipos de argumentos")
    if (not (subexps[5]["type"] in ["int", "float"])): raise SemanticException("Error en los tipos de argumentos")
    subexps[0] = dict()
    subexps[0]["type"] = "vector"
    subexps[0]["subtype"] = dict()
    subexps[0]["subtype"]["type"] = "int" if subexps[3]["type"]["subtype"]["type"]=="int" and subexps[5]["type"]=="int" else "float"
    subexps[0]["value"] = subexps[1] + subexps[2] + subexps[3]["value"] + subexps[4] + subexps[5]["value"] + subexps[6]

def p_v_cap(subexps):
    'f : CAPITALIZAR LPAREN v RPAREN'
    if (subexps[3]["type"] not in ["CADENA"]): raise SemanticException("Capitalizar solo aplica a CADENA")
    subexps[0] = dict()
    subexps[0]["type"] = "CADENA"
    subexps[0]["value"] = subexps[1] + subexps[2] + subexps[3]["value"] + subexps[4]

def p_v_length(subexps):
    'f : LENGTH LPAREN v RPAREN'
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
    subexps[0]["type"] = subexps[2]["type"]
    subexps[0]["subtype"] = subexps[2]["subtype"]
    subexps[0]["value"] = subexps[1] + subexps[2]["value"] + subexps[3]

def p_v_explicita_2(subexps):
    'expl : LLAVEABIERTA listareg LLAVECERRADA'
    subexps[0] = dict()
    subexps[0]["type"] = subexps[2]["type"]
    subexps[0]["subtype"] = subexps[2].get("subtype")
    subexps[0]["value"] = subexps[1] + subexps[2]["value"] + subexps[3]

def p_v_lista(subexps):
    'lista : lista COMA v'
    if (subexps[1]["subtype"]["type"] != subexps[3]["type"]):
		if not(subexps[1]["subtype"]["type"] in ["int", "float"], subexps[3]["type"] in ["int", "float"]):
			raise SemanticException("Los vectores solo pueden tener un tipo")
    subexps[0] = dict()
    subexps[0]["type"] = subexps[1]["type"]
    subexps[0]["subtype"] = subexps[1]["subtype"]
    subexps[0]["value"] = subexps[1]["value"] + subexps[2] + ' ' + subexps[3]["value"]

def p_v_lista2(subexps):
    'lista : v'
    subexps[0] = dict()
    subexps[0]["type"] = "vector"
    subexps[0]["subtype"] = {"type": subexps[1]["type"], "subtype": subexps[1].get("subtype")} ### mejorar
    subexps[0]["value"] = subexps[1]["value"]

def p_v_listareg(subexps):
    'listareg : listareg COMA VARIABLE DOSPUNTOS v'
    subexps[0] = dict()
    subexps[0]["type"] = "registro"
    subexps[0]["subtype"] = dict()
    subexps[0]["subtype"] = subexps[1]["subtype"] #comentarioMaxi: aca primero le van todos los campos que venian arrastrados
    subexps[0]["subtype"][subexps[3]] = {"type": subexps[5]["type"], "subtype": subexps[5].get("subtype")} ### mejorar #comentarioMaxi: aca agrego el nuevo.
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
    subexps[0]["type"], subexps[0]["subtype"] = buscar(subexps[1]["type"], subexps[1]["subtype"], subexps[2]["value"])
    subexps[0]["value"] = subexps[1]["value"] + subexps[2]["value"]

def p_a_var(subexps):
    'a : VARIABLE index IGUAL v' # mejorar
    types[subexps[1]], subtypes[subexps[1]] = procesar(subexps[4]["type"], subexps[4].get("subtype"), subexps[2]["value"])
    subexps[0] = subexps[1] + subexps[2]["value"] + ' ' + subexps[3] + ' ' + subexps[4]["value"]

def procesar(tipo, subtipo, search) :
    if (search == ""): 
        return [tipo, subtipo]
    last = len(search) - minaux(search[::-1].find('['), search[::-1].find('.')) - 1
    if (search[last] == '['): 
        return procesar("vector", {"type": tipo, "subtipo": subtipo}, search[:last])
    else: return procesar("registro", {search[last + 1:]: {"type": tipo, "subtipo": subtipo}}, search[:last])

def minaux(int1, int2):
	if int1 == -1: return int2
	if int2 == -1: return int1
	return min(int1, int2)


########################################

def p_a_var1(subexps):
    'index : index CORCHETEA v CORCHETEC'
    subexps[0] = dict()
    subexps[0]["type"] = "vector"
    subexps[0]["subtype"] = {"type" : subexps[1]["type"], "subtype" : subexps[1].get("subtype")}
    if (subexps[3]["type"] not in ["int", "float"]): raise SemanticException("Vector index not a number")
    subexps[0]["value"] = subexps[1]["value"] + subexps[2] + subexps[3]["value"] + subexps[4]

def p_a_var2(subexps):
    'index : index PUNTO VARIABLE'
    subexps[0] = dict()
    subexps[0]["type"] = "registro"
    subexps[0]["subtype"] = {subexps[3]: {"type": subexps[1]["type"], "subtype": subexps[1].get("subtype")}}
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
	    asigtype = buscar(types[subexps[1]], subtypes[subexps[1]], subexps[2]["value"])[0]
    else: asigtype = types[subexps[1]]
    if (asigtype not in ["int", "float"] or subexps[4]["type"] not in ["int", "float"]): raise SemanticException("Valor no numerico")
	#comentarioMaxi: para el MASIGUAL podriamos considerar las cadenas tambien, pero no se si vale la pena hacer el cambio ahora.
    subexps[0] = subexps[1] + subexps[2]["value"] + ' ' +  subexps[3] + ' ' + subexps[4]["value"]
    
def p_o_masmas(subexps):
    '''o : VARIABLE index MASMAS
    o : VARIABLE index MENOSMENOS'''

    if (types[subexps[1]] == "vector" or types[subexps[1]] == "registro"):
	    asigtype = buscar(types[subexps[1]], subtypes[subexps[1]], subexps[2]["value"])[0]
    else: asigtype = types[subexps[1]]
    if (asigtype not in ["int", "float"]): raise SemanticException("Valor no numerico")
    subexps[0] = subexps[1] + subexps[2]["value"] + subexps[3]

def p_o_masmasv(subexps):
    '''o : MASMAS VARIABLE index
    o : MENOSMENOS VARIABLE index'''
    if (types[subexps[2]] == "vector" or types[subexps[2]] == "registro"):
	    asigtype = buscar(types[subexps[2]], subtypes[subexps[2]], subexps[3]["value"])[0]
    else: asigtype = types[subexps[2]]
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
	print search, tipo, subtype
	if (search == ""): 
		return [tipo, subtype];
	if search[0] == "[": 
		if (tipo != "vector"): print "Error"
		end = (match(search[1:],"]") + 1)
		return buscar(subtype["type"], subtype.get("subtype"), search[end + 1:])
	if (tipo != "registro"): print "Error"
	split = search[1:].find(".") + 1
	if split == 0: split = len(search) + 1
	if (subtype.get(search[1:split]) == None): print "Error"
	else: return buscar(subtype[search[1:split]]["type"], subtype[search[1:split]].get("subtype"), search[split:])

def match(st, char) :
	i=1
	for char in range(len(st)):
		if st[char] == '[': i+=1
		if st[char] == ']': i-=1
		if i==0: return char
