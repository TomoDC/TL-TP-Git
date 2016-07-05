from lexer_rules import tokens
#from operator import add, mul
#from expressions import BinaryOperation, Number

types=dict()

class SemanticException(Exception) :
	pass

def p_inicial(subexpressions):
    'ss : s'
    subexpressions[0] = subexpressions[1]

def p_inicial2(subexpressions):
    'ss : s NEWLINE ss'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] 

def p_inicial3(subexpressions):
    'ss : s ss'
    subexpressions[0] = subexpressions[1] + '\n' + subexpressions[2] 

def p_s_if(subexpressions):
    's : if'
    subexpressions[0] = subexpressions[1]
    
def p_s_while(subexpressions):
    's : w'
    subexpressions[0] = subexpressions[1]    

def p_s_do(subexpressions):
    's : d'
    subexpressions[0] = subexpressions[1]

def p_s_for(subexpressions):
    's : f'
    subexpressions[0] = subexpressions[1]
    
def p_s_asig(subexpressions):
    's : a PUNTOCOMA'
    subexpressions[0] = subexpressions[1] + subexpressions[2] 
    
def p_s_o(subexpressions):
    's : o PUNTOCOMA'
    subexpressions[0] = subexpressions[1] + subexpressions[2] 

def p_s_r(subexpressions):
    's : RETURN r PUNTOCOMA'
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3]

def p_s_coment(subexpressions):
    's : COMENTARIO'
    subexpressions[0] = subexpressions[1]

def p_if(subexpressions):
    'if : IF LPAREN v RPAREN bq'
	if subexpressions[3]["type"]=="bool":
		subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3]["value"] + subexpressions[4] + subexpressions[5]
    else:
		raise SemanticException("Expresion no-booleana en la guarda")
		
def p_if_else(subexpressions):
    'if : IF LPAREN v RPAREN bq ELSE bq'
    if subexpressions[3]["type"]=="bool":
		subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3]["value"] + subexpressions[4] + subexpressions[5] + '\n' + subexpressions[6] + subexpressions[7]
    else:
		raise SemanticException("Expresion no-booleana en la guarda")
	
def p_while(subexpressions):
	'w : WHILE LPAREN v RPAREN bq'
	if subexpressions[3]["type"]=="bool":
		subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]["value"] + subexpressions[4] + subexpressions[5]
    else:
		raise SemanticException("Expresion no-booleana en la guarda")
	
def p_do_while(subexpressions):
	'd : DO bq WHILE LPAREN v RPAREN PUNTOCOMA'
	if subexpressions[5]["type"]=="bool":
		subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + ' ' + subexpressions[4] + subexpressions[5]["value"] + subexpressions[6] + subexpressions[7]
    else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_for1(subexpressions):
	'f : FOR LPAREN v RPAREN bq'
	if subexpressions[3]["type"]=="bool":
		subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3]["value"] + subexpressions[4] + subexpressions[5]
    else:
		raise SemanticException("Expresion no-booleana en la guarda")
	
def p_for2(subexpressions):
	'f : FOR LPAREN a PUNTOCOMA v RPAREN bq'
	if subexpressions[5]["type"]=="bool":
		subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + subexpressions[4] + ' ' + subexpressions[5]["value"] + subexpressions[6] + subexpressions[7]
    else:
		raise SemanticException("Expresion no-booleana en la guarda")

def p_for3(subexpressions):
	'f : FOR LPAREN a PUNTOCOMA v PUNTOCOMA o RPAREN bq'
	if subexpressions[5]["type"]=="bool":
		subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + subexpressions[4] + ' ' + subexpressions[5]["value"] + subexpressions[6] + ' ' + subexpressions[7] + subexpressions[8] + subexpressions[9]
    else:
		raise SemanticException("Expresion no-booleana en la guarda")

		
		
		
		
		
		
		
		
		
def p_v_true_v2(subexpressions):
    'v : TRUE v2'
	if subexpressions[2]["type"]=="empty":
		subexpressions[0] = {"value": subexpressions[1], "type": "bool"}
	else:
		if "bool" in subexpressions[2]["reqTypes"]:	
			subexpressions[0] = {"value": subexpressions[1]+subexpressions[2]["value"], "type": subexpressions[2]["type"]}
		else:
			raise SemanticException("Expresion no compatible con bool")
	
def p_v_false_v2(subexpressions):
    'v : FALSE v2'
	if subexpressions[2]["type"]=="empty":
		subexpressions[0] = {"value": subexpressions[1], "type": "bool"}
	else:
		if "bool" in subexpressions[2]["reqTypes"]:	
			subexpressions[0] = {"value": subexpressions[1]+subexpressions[2]["value"], "type": subexpressions[2]["type"]}
		else:
			raise SemanticException("Expresion no compatible con bool")


def p_v_num_v2(subexpressions):
    'v : NUMBER v2'
	if subexpressions[2]["type"]=="empty":
		subexpressions[0] = {"value": str(subexpressions[1]["value"]), "type": subexpressions[1]["type"]}
	else:
		if subexpressions[1]["type"] in subexpressions[2]["reqTypes"]:
			if (subexpressions[1]["type"]=="float" and subexpressions[2]["type"] == "int"):
				resultado_type = "float"
			else:
				resultado_type = subexpressions[2]["type"]
			subexpressions[0] = {"value": str(subexpressions[1]["value"])+subexpressions[2]["value"], "type": resultado_type}
		else:
			raise SemanticException("Expresion no compatible con numerico")

def p_v_cadena_v2(subexpressions):
    'v : CADENA v2'
	if subexpressions[2]["type"]=="empty":
		subexpressions[0] = subexpressions[1]
	else:
		if subexpressions[1]["type"] in subexpressions[2]["reqTypes"]:
			subexpressions[0] = {"value": subexpressions[1]["value"]+subexpressions[2]["value"], "type": subexpressions[2]["type"]}
		else:
			raise SemanticException("Expresion no compatible con string")
	
def p_v_var_v2(subexpressions):
    'v : VARIABLE v2'
	if subexpressions[2]["type"]=="empty":
		subexpressions[0] = {"value": subexpressions[1], "type": types[subexpressions[1]]}
	else:
		if types[subexpressions[1]] in subexpressions[2]["reqTypes"]:
			if (types[subexpressions[1]]=="float" and subexpressions[2]["type"] == "int"):
				resultado_type = "float"
			else:
				resultado_type = subexpressions[2]["type"]
			subexpressions[0] = {"value": subexpressions[1]+subexpressions[2]["value"], "type": resultado_type}
		else:
			raise SemanticException("Expresion no compatible con el tipo de la variable")		
	
def p_v_parentesis_v2(subexpressions):
    'v : LPAREN v RPAREN v2'
	if subexpressions[4]["type"]=="empty":
		subexpressions[0] = {"value": subexpressions[1] + subexpressions[2]["value"] + subexpressions[3], "type": subexpressions[2]["type"]}
	else:	
		if subexpressions[2]["type"] in subexpressions[4]["reqTypes"]:
			if (subexpressions[2]["type"]=="float" and subexpressions[4]["type"] == "int"):
				resultado_type = "float"
			else:
				resultado_type = subexpressions[4]["type"]
			subexpressions[0] = {"value": subexpressions[1] + subexpressions[2]["value"] + subexpressions[3] + subexpressions[4]["value"], "type": resultado_type}
		else:
			raise SemanticException("Expresion no compatible con el tipo de valor")

def p_v_not_v2(subexpressions):
    'v : NOT v v2'
	if subexpressions[3]["type"]=="empty":
		if subexpressions[2]["type"]=="bool":
			subexpressions[0] = {"value": subexpressions[1] + ' ' + subexpressions[2]["value"], "type": "bool"}
		else:
			raise SemanticException("Operador de bool a valor no-booleano")
	else:	
		if subexpressions[2]["type"]=="bool":
			if "bool" in subexpressions[3]["reqTypes"]:
				subexpressions[0] = {"value": subexpressions[1] + ' ' + subexpressions[2]["value"]+ subexpressions[3]["value"], "type": subexpressions[3]["type"]}
			else:
				raise SemanticException("Expresion no compatible con bool")
		else:
			raise SemanticException("Operador de bool a valor no-booleano")
		
def p_v_colineales_v2(subexpressions):
    'v : COLINEALES LPAREN v COMA v RPAREN v2'
	if subexpressions[7]["type"]=="empty":
		if (subexpressions[3]["type"] in ["vector de numeros"] and subexpressions[3]["type"]==subexpressions[5]["type"]):
			subexpressions[0] = {"value": subexpressions[1] + subexpressions[2] + subexpressions[3]["value"] + subexpressions[4] + subexpressions[5]["value"] + subexpressions[6], "type": "bool"}
		else:
			raise SemanticException("Colineales deberia recibir vectores del mismo tipo")
	else:	    
		if (subexpressions[3]["type"] in ["vector de numeros"] and subexpressions[3]["type"]==subexpressions[5]["type"]):
			if "bool" in subexpressions[7]["reqTypes"]:
				subexpressions[0] = {"value": subexpressions[1] + subexpressions[2] + subexpressions[3]["value"] + subexpressions[4] + subexpressions[5]["value"] + subexpressions[6] + subexpressions[7]["value"], "type": subexpressions[7]["type"]}
			else:
				raise SemanticException("Expresion no compatible con bool")
		else:
			raise SemanticException("Colineales deberia recibir vectores del mismo tipo")

def p_v_mEvvb_v2(subexpressions):
    'v : MULTIPLICACIONESCALAR LPAREN v COMA v COMA v RPAREN v2'
	if subexpressions[4]["type"]=="empty":
		if (subexpressions[3]["type"]=="vector de numeros" and subexpressions[5]["type"] in ["int", "float"] and subexpressions[7]["type"]=="bool"):
			subexpressions[0] = {"value": subexpressions[1] + subexpressions[2] + subexpressions[3]["value"] + subexpressions[4] + subexpressions[5]["value"] + subexpressions[6] + subexpressions[7]["value"] + subexpressions[8], "type": "vector de numeros"}
		else: 
			raise SemanticException("La funcion debe tomar un vector de numeros, un numero y un booleano opcional")
	else:	
		if (subexpressions[3]["type"]=="vector de numeros" and subexpressions[5]["type"] in ["int", "float"] and subexpressions[7]["type"]=="bool"):
			if	"vector de numeros" in subexpressions[9]["reqTypes"]:
				subexpressions[0] = {"value": subexpressions[1] + subexpressions[2] + subexpressions[3]["value"] + subexpressions[4] + subexpressions[5]["value"] + subexpressions[6] + subexpressions[7]["value"] + subexpressions[8] + subexpressions[9]["value"], "type": subexpressions[9]["type"]}
			else:
				raise SemanticException("Expresion no compatible con vector de numeros")
		else: 
			raise SemanticException("La funcion debe tomar un vector de numeros, un numero y un booleano opcional")
		
def p_v_mEvv_v2(subexpressions):
    'v : MULTIPLICACIONESCALAR LPAREN v COMA v RPAREN v2'
	if subexpressions[4]["type"]=="empty":
		if (subexpressions[3]["type"]=="vector de numeros" and subexpressions[5]["type"] in ["int", "float"]):
			subexpressions[0] = {"value": subexpressions[1] + subexpressions[2] + subexpressions[3]["value"] + subexpressions[4] + subexpressions[5]["value"] + subexpressions[6], "type": "vector de numeros"}
		else: 
			raise SemanticException("La funcion debe tomar un vector de numeros, un numero y un booleano opcional")
	else:		
		if (subexpressions[3]["type"]=="vector de numeros" and subexpressions[5]["type"] in ["int", "float"]):
			if	"vector de numeros" in subexpressions[7]["reqTypes"]:
				subexpressions[0] = {"value": subexpressions[1] + subexpressions[2] + subexpressions[3]["value"] + subexpressions[4] + subexpressions[5]["value"] + subexpressions[6] + subexpressions[7]["value"], "type": subexpressions[7]["type"]}
			else:
				raise SemanticException("Expresion no compatible con vector de numeros")
		else: 
			raise SemanticException("La funcion debe tomar un vector de numeros, un numero y un booleano opcional")		

def p_v_cap_v2(subexpressions):
    'v : CAPITALIZAR LPAREN v RPAREN v2'
	if subexpressions[4]["type"]=="empty":
		if subexpressions[3]["type"]=="string":
			subexpressions[0] = {"value": subexpressions[1] + subexpressions[2] + subexpressions[3]["value"] + subexpressions[4], "type": "string"}
		else: 
			raise SemanticException("La funcion debe tomar un string")
	else:	
		if subexpressions[3]["type"]=="string":
			if "string" in subexpressions[5]["reqTypes"]:
				subexpressions[0] = {"value": subexpressions[1] + subexpressions[2] + subexpressions[3]["value"] + subexpressions[4] + subexpressions[5]["value"], "type": subexpressions[5]["type"]}
			else:
				raise SemanticException("Expresion no compatible con string")
		else: 
			raise SemanticException("La funcion debe tomar un string")		
	
def p_v_length_v2(subexpressions):
    'v : LENGTH LPAREN v RPAREN v2'
	if subexpressions[4]["type"]=="empty":
		if subexpressions[3]["type"] in ["string", "vector"]:
			subexpressions[0] = {"value": subexpressions[1] + subexpressions[2] + subexpressions[3] + subexpressions[4], "type": "int"}
		else: 
			raise SemanticException("La funcion debe tomar un string o un vector")
	else:		
		if subexpressions[3]["type"] in ["string", "vector"]:
			if "int" in subexpressions[5]["reqTypes"]:
				subexpressions[0] = {"value": subexpressions[1] + subexpressions[2] + subexpressions[3]["value"] + subexpressions[4] + subexpressions[5]["value"]  , "type":  subexpressions[5]["type"] }
			else:
				raise SemanticException("Expresion no compatible con numero entero")
		else: 
			raise SemanticException("La funcion debe tomar un string o un vector")
		
		
		
		
		
		
		
def p_v2_empty(subexpressions):
    'v2 : '
	subexpressions[0] = {"value": "", "type": "empty", "reqTypes": ["todos vectores registros todo"]}

def p_v2_vec(subexpressions):
    'v2 : CORCHETEA v CORCHETEC v2'
	if subexpressions[2]["type"]=="int":
		if subexpressions[4]["type"]=="empty":
			subexpressions[0] = {"value": subexpressions[1] + subexpressions[2]["value"] + subexpressions[3], "type": "lo de dentro del vector", "reqTypes": "vector"}
		else: 
			if "lo de dentro del vector" in subexpressions[4]["reqTypes"]:
				if ("lo de dentro del vector"=="float" and subexpressions[4]["type"] == "int"):
					resultado_type = "float"
				else:
					resultado_type = subexpressions[4]["type"]
				subexpressions[0] = {"value": subexpressions[1] + subexpressions[2]["value"] + subexpressions[3] + subexpressions[4]["value"], "type": resultado_type, "reqTypes" : "vector"}
			else: 
				raise SemanticException("Expresion no compatible con el tipo de elementos del vector")
	else:
		raise SemanticException("Debe debe estar indexado con un numero entero")
		
def p_v2_reg(subexpressions):
    'v2 : PUNTO v v2'
	if subexpressions[2]["type"]=="string":
		if subexpressions[3]["type"]=="empty":
			subexpressions[0] = {"value": subexpressions[1] + subexpressions[2]["value"], "type": "lo de dentro del registro", "reqTypes": "registro"}
		else: 
			if "lo de dentro del registro" in subexpressions[3]["reqTypes"]:
				if ("lo de dentro del registro"=="float" and subexpressions[3]["type"] == "int"):
					resultado_type = "float"
				else:
					resultado_type = subexpressions[3]["type"]
				subexpressions[0] = {"value": subexpressions[1] + subexpressions[2]["value"] + subexpressions[3]["value"], "type": resultado_type, "reqTypes" : "registro"}
			else: 
				raise SemanticException("Expresion no compatible con el tipo de elementos del campo del registro")
	else:
		raise SemanticException("Debe debe estar indexado con un string")
	
	
def p_v2_or(subexpressions):
    'v2 : OR v v2'
	if subexpressions[2]["type"]=="bool":
		if subexpressions[3]["type"]=="empty":
			subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"], "type": "bool", "reqTypes": ["bool"]}
		else: 
			if "bool" in subexpressions[3]["reqTypes"]:
				subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"] + subexpressions[3]["value"], "type": subexpressions[3]["type"], "reqTypes": ["bool"]}
			else:
				raise SemanticException("Expresion no compatible con bool")
	else:
		raise SemanticException("Operador de bool a valor no-booleano")
	
    
def p_v2_and(subexpressions):
    'v2 : AND v v2'
	if subexpressions[2]["type"]=="bool":
		if subexpressions[3]["type"]=="empty":
			subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"], "type": "bool", "reqTypes": ["bool"]}
		else: 
			if "bool" in subexpressions[3]["reqTypes"]:
				subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"] + subexpressions[3]["value"], "type": subexpressions[3]["type"], "reqTypes": ["bool"]}
			else:
				raise SemanticException("Expresion no compatible con bool")
	else:
		raise SemanticException("Operador de bool a valor no-booleano")

def p_v2_igualigual(subexpressions):
    'v2 : IGUAL IGUAL v v2'
	if subexpressions[4]["type"]=="empty":
		subexpressions[0] = {"value": ' ' + subexpressions[1] + subexpressions[2] + ' ' + subexpressions[3]["value"], "type": "bool", "reqTypes": [subexpressions[3]["type"]]}
	else:
		if "bool" in subexpressions[4]["reqTypes"]:
			subexpressions[0] = {"value": ' ' + subexpressions[1] + subexpressions[2] + ' ' + subexpressions[3]["value"] + subexpressions[4]["value"], "type": subexpressions[4]["type"], "reqTypes": [subexpressions[3]["type"]]}
		else:
			raise SemanticException("Expresion no compatible con bool")
		
def p_v2_desigualdad(subexpressions):
    'v2 : DESIGUALDAD v v2'
	if subexpressions[3]["type"]=="empty":
		subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"], "type": "bool", "reqTypes": [subexpressions[2]["type"]]}
	else:
		if "bool" in subexpressions[3]["reqTypes"]:
			subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"] + subexpressions[3]["value"], "type": subexpressions[3]["type"], "reqTypes": [subexpressions[2]["type"]]}
		else:
			raise SemanticException("Expresion no compatible con bool")
    
def p_v2_mayor(subexpressions):
    'v2 : MAYOR v v2'
	if subexpressions[2]["type"] in ["string", "int", "float"]:
		if subexpressions[3]["type"]=="empty":
			subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"], "type": "bool", "reqTypes": [subexpressions[2]["type"]]}
		else:
			if "bool" in subexpressions[3]["reqTypes"]:
				subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"] + subexpressions[3]["value"], "type": subexpressions[3]["type"], "reqTypes":[subexpressions[2]["type"]]}
			else:
				raise SemanticException("Expresion no compatible con bool")
	else: 
		raise SemanticException("Operador para numericos o string usado con algo de otro tipo")	
		
def p_v2_menor(subexpressions):
    'v2 : MENOR v v2'
	if subexpressions[2]["type"] in ["string", "int", "float"]:
		if subexpressions[3]["type"]=="empty":
			subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"], "type": "bool", "reqTypes": [subexpressions[2]["type"]]}
		else:
			if "bool" in subexpressions[3]["reqTypes"]:
				subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"] + subexpressions[3]["value"], "type": subexpressions[3]["type"], "reqTypes":[subexpressions[2]["type"]]}
			else:
				raise SemanticException("Expresion no compatible con bool")
	else: 
		raise SemanticException("Operador para numericos o string usado con algo de otro tipo")

def p_v2_suma(subexpressions):
    'v2 : SUMA v v2'
	if subexpressions[2]["type"] in ["int", "float", "string"]:
		if subexpressions[2]["type"]="string":
			requisito_types = ["string"]
		elif subexpressions[2]["type"] in ["int", "float"]:
			requisito_types = ["int", "float"]
		
		if subexpressions[3]["type"]=="empty":
			subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"], "type": subexpressions[2]["type"], "reqTypes": requisito_types}
		else:
			if subexpressions[2]["type"] in subexpressions[3]["reqTypes"]:
				subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"] + subexpressions[3]["value"], "type": subexpressions[3]["type"], "reqTypes": requisito_types}
			else:
				raise SemanticException("Expresion no compatible con el resultado de la suma")
	else: 
		raise SemanticException("Operador de numeros o string aplicadp a valor de otro tipo")		
		
def p_v2_resta(subexpressions):
    'v2 : MENOS v v2'
	if subexpressions[2]["type"] in ["int", "float"]:
		if subexpressions[3]["type"]=="empty":
			subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"], "type": subexpressions[2]["type"], "reqTypes": ["int", "float"]}
		else:
			if "float" in subexpressions[3]["reqTypes"]:
				subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"] + subexpressions[3]["value"], "type": subexpressions[3]["type"], "reqTypes": ["int", "float"]}
			else:
				raise SemanticException("Expresion no compatible con numericos")
	else: 
		raise SemanticException("Operador de numeros a valor no-numerico")

def p_v2_por(subexpressions):
    'v2 : POR v v2'
	if subexpressions[2]["type"] in ["int", "float"]:
		if subexpressions[3]["type"]=="empty":
			subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"], "type": subexpressions[2]["type"], "reqTypes": ["int", "float"]}
		else:
			if "float" in subexpressions[3]["reqTypes"]:
				subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"] + subexpressions[3]["value"], "type": subexpressions[3]["type"], "reqTypes": ["int", "float"]}
			else:
				raise SemanticException("Expresion no compatible con numericos")
	else: 
		raise SemanticException("Operador de numeros a valor no-numerico")
    
def p_v2_div(subexpressions):
    'v2 : DIV v v2'
	if subexpressions[2]["type"] in ["int", "float"]:
		if subexpressions[3]["type"]=="empty":
			subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"], "type": subexpressions[2]["type"], "reqTypes": ["int", "float"]}
		else:
			if "float" in subexpressions[3]["reqTypes"]:
				subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"] + subexpressions[3]["value"], "type": subexpressions[3]["type"], "reqTypes": ["int", "float"]}
			else:
				raise SemanticException("Expresion no compatible con numericos")
	else: 
		raise SemanticException("Operador de numeros a valor no-numerico")
    
def p_v2_potencia(subexpressions):
    'v2 : POTENCIA v v2'
	if subexpressions[2]["type"] in ["int", "float"]:
		if subexpressions[3]["type"]=="empty":
			subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"], "type": subexpressions[2]["type"], "reqTypes": ["int", "float"]}
		else:
			if "float" in subexpressions[3]["reqTypes"]:
				subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"] + subexpressions[3]["value"], "type": subexpressions[3]["type"], "reqTypes": ["int", "float"]}
			else:
				raise SemanticException("Expresion no compatible con numericos")
	else: 
		raise SemanticException("Operador de numeros a valor no-numerico")
    
def p_v2_mod(subexpressions):
    'v2 : PORCENTAJE v v2'
	if subexpressions[2]["type"] in ["int", "float"]:
		if subexpressions[3]["type"]=="empty":
			subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"], "type": subexpressions[2]["type"], "reqTypes": ["int", "float"]}
		else:
			if "float" in subexpressions[3]["reqTypes"]:
				subexpressions[0] = {"value": ' ' + subexpressions[1] + ' ' + subexpressions[2]["value"] + subexpressions[3]["value"], "type": subexpressions[3]["type"], "reqTypes": ["int", "float"]}
			else:
				raise SemanticException("Expresion no compatible con numericos")
	else: 
		raise SemanticException("Operador de numeros a valor no-numerico")

def p_v2_pregunta(subexpressions):
    'v2 : INTERROGACION v DOSPUNTOS v v2'
	if subexpressions[2]["type"]==subexpressions[4]["type"]:
		if subexpressions[5]["type"]=="empty":
			subexpressions[0] = {"value": subexpressions[1] + ' ' + subexpressions[2]["value"] + ' ' + subexpressions[3] + ' ' + subexpressions[4]["value"], "type": subexpressions[2]["type"], "reqTypes": ["bool"]}
		else:
			if subexpressions[2]["type"] in subexpressions[5]["reqTypes"]:
				subexpressions[0] = {"value": subexpressions[1] + ' ' + subexpressions[2]["value"] + ' ' + subexpressions[3] + ' ' + subexpressions[4]["value"] + subexpressions[5]["value"], "type": subexpressions[5]["type"], "reqTypes": ["bool"]}
			else:
				raise SemanticException("Expresion no compatible con el resultado del operador ternario")
	else: 
		raise SemanticException("Los dos posibles resultados del operador ternario deben tener el mismo tipo")	

		
		

		
		
		
		
		
def p_a_reg(subexpressions):
    'a : VARIABLE PUNTO v IGUAL v'
	if subexpressions[3]["type"]=="string":
		types[subexpressions[1]]="registro ¿de? .."
		subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]["value"] + ' ' + subexpressions[4] + ' ' + subexpressions[5]["value"]
    else:
		raise SemanticException("Se accede a los campos mediante strings")
		
def p_a_vec(subexpressions):
    'a : VARIABLE CORCHETEA v CORCHETEC IGUAL v'
	if subexpressions[3]["type"]=="int":
		types[subexpressions[1]]="vector de .."
		subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]["value"] + subexpressions[4] + ' ' + subexpressions[5] + ' ' + subexpressions[6]["value"]
    else:
		raise SemanticException("Se accede a los valores mediante ints")

def p_a_var(subexpressions):
    'a : VARIABLE IGUAL v'
    types[subexpressions[1]] = subexpressions[3]["type"]
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + ' ' + subexpressions[3]["value"]

def p_o_masigual(subexpressions):
    'o : VARIABLE SUMA IGUAL v'
    if ((types[subexpressions[1]] in ["int", "float"] and subexpressions[4]["type"] in ["int", "float"]) or (types[subexpressions[1]]=="string" and subexpressions[4]["type"]=="string")):
		subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + ' ' + subexpressions[4]["value"]
	else:
		raise SemanticException("Operacion valida para variables numericas o de strings solamente")
    
def p_o_menosigual(subexpressions):
    'o : VARIABLE MENOS IGUAL v'
    if (types[subexpressions[1]] in ["int", "float"] and subexpressions[4]["type"] in ["int", "float"]):
		subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + ' ' + subexpressions[4]["value"]
    else:
		raise SemanticException("Operacion valida para variables numericas solamente")

def p_o_porigual(subexpressions):
    'o : VARIABLE POR IGUAL v'
    if (types[subexpressions[1]] in ["int", "float"] and subexpressions[4]["type"] in ["int", "float"]):
		subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + ' ' + subexpressions[4]["value"]
    else:
		raise SemanticException("Operacion valida para variables numericas solamente")

def p_o_divigual(subexpressions):
    'o : VARIABLE DIV IGUAL v'
    if (types[subexpressions[1]] in ["int", "float"] and subexpressions[4]["type"] in ["int", "float"]):
		subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + ' ' + subexpressions[4]["value"]
    else:
		raise SemanticException("Operacion valida para variables numericas solamente")

def p_o_masmas(subexpressions):
    'o : VARIABLE SUMA SUMA'
    if types[subexpressions[1]] in ["int", "float"]: 
		subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]
	else:
		raise SemanticException("Operacion valida para variables numericas solamente")
    

def p_o_menosmenos(subexpressions):
    'o : VARIABLE MENOS MENOS'
    if types[subexpressions[1]] in ["int", "float"]: 
		subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]
	else:
		raise SemanticException("Operacion valida para variables numericas solamente")
        
def p_o_masmasv(subexpressions):
    'o : SUMA SUMA VARIABLE'
    if types[subexpressions[3]] in ["int", "float"]: 
		subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]
	else:
		raise SemanticException("Operacion valida para variables numericas solamente")

def p_o_menosmenosv(subexpressions):
    'o : MENOS MENOS VARIABLE'
    if types[subexpressions[3]] in ["int", "float"]: 
		subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]
	else:
		raise SemanticException("Operacion valida para variables numericas solamente")

def p_o_print(subexpressions):
    'o : PRINT LPAREN v RPAREN'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + subexpressions[4]

def p_bq1(subexpressions):
	'bq : s'
	subexpressions[0] = '\n\t' + subexpressions[1]
	
def p_bq2(subexpressions):
	'bq : LLAVEABIERTA ss LLAVECERRADA'
	subexpressions[0] = subexpressions[1] + "\n" + "\t".join(subexpressions[2].split("\n")) + '\n' + subexpressions[3]

def p_error(token):
    message = "[Syntax error]"
    if token is not None:
        message += "\ntype:" + token.type
        message += "\nvalue:" + str(token.value)
        message += "\nline:" + str(token.lineno)
        message += "\nposition:" + str(token.lexpos)
    raise Exception(message)
