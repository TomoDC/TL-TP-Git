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
    's : for'
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

def p_r_v(subexpressions):
    'r : v'
    subexpressions[0] = subexpressions[1]["value"]

def p_r_a(subexpressions):
    'r : a'
    subexpressions[0] = subexpressions[1]

def p_r_o(subexpressions):
    'r : o'
    subexpressions[0] = subexpressions[1]

def p_if(subexpressions):
    'if : IF LPAREN v RPAREN bq'
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + subexpressions[4] + subexpressions[5]
    
def p_if_else(subexpressions):
    'if : IF LPAREN v RPAREN bq ELSE bq'
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + subexpressions[4] + subexpressions[5] + '\n' + subexpressions[6] + subexpressions[7]

def p_while(subexpressions):
	'w : WHILE LPAREN v RPAREN bq'
	subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + subexpressions[4] + '\n\t' + subexpressions[5]

def p_do_while(subexpressions):
	'd : DO bq WHILE LPAREN v RPAREN PUNTOCOMA'
	subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + ' ' + subexpressions[4] + subexpressions[5] + subexpressions[6] + subexpressions[7]

def p_for1(subexpressions):
	'for : FOR LPAREN v RPAREN bq'
	subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + subexpressions[4] + '\n\t' + subexpressions[5]

def p_for2(subexpressions):
	'for : FOR LPAREN a PUNTOCOMA v RPAREN bq'
	subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + subexpressions[4] + ' ' + subexpressions[5] + subexpressions[6] + '\n\t' + subexpressions[7]

def p_for3(subexpressions):
	'for : FOR LPAREN a PUNTOCOMA v PUNTOCOMA o RPAREN bq'
	subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + subexpressions[4] + ' ' + subexpressions[5] + subexpressions[6] + ' ' + subexpressions[7] + subexpressions[8] + '\n\t' + subexpressions[9]

def p_b_true(subexpressions):
    'f : TRUE'
    subexpressions[0] = subexpressions[1]

def p_b_false(subexpressions):
    'f : FALSE'
    subexpressions[0] = subexpressions[1]

def p_b_not(subexpressions):
    'v : NOT f'
    subexpressions[0] = subexpressions[1] + subexpressions[2]
    
def p_b_or(subexpressions):
    'v : v OR f'
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + ' ' + subexpressions[3]
    
def p_b_and(subexpressions):
    'v : v AND f'
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + ' ' + subexpressions[3]

def p_b_igualigual(subexpressions):
    'v : v IGUAL IGUAL f'
    subexpressions[0] = subexpressions[1]["value"] + ' ' + subexpressions[2] + subexpressions[3] + ' ' + subexpressions[4]["value"]

def p_b_desigualdad(subexpressions):
    'v : v DESIGUALDAD f'
    subexpressions[0] = subexpressions[1]["value"] + ' ' + subexpressions[2] + ' ' + subexpressions[3]["value"]
    
def p_b_mayor(subexpressions):
    'v : v MAYOR f'
    subexpressions[0] = subexpressions[1]["value"] + ' ' + subexpressions[2] + ' ' + subexpressions[3]["value"]

def p_b_menor(subexpressions):
    'v : v MENOR f'
    subexpressions[0] = subexpressions[1]["value"] + ' ' + subexpressions[2] + ' ' + subexpressions[3]["value"]

def p_b_colineales(subexpressions):
    'v : COLINEALES LPAREN v COMA v RPAREN'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]["value"] + subexpressions[4] + ' ' + subexpressions[5]["value"] + subexpressions[6]    
    
def p_v_parentesis(subexpressions):
    'f : LPAREN v RPAREN'
    subexpressions[0] = subexpressions[1] + subexpressions[2]["value"] + subexpressions[3]

def p_f_v(subexpressions):
    'v : f'
    subexpressions[0] = subexpressions[1]

def p_v_resta(subexpressions):
    'v : v MENOS f'
    subexpressions[0] = subexpressions[1]["value"] + subexpressions[2] + subexpressions[3]["value"]

def p_v_suma(subexpressions):
    'v : v SUMA f'
    subexpressions[0] = subexpressions[1]["value"] + subexpressions[2] + subexpressions[3]["value"]

def p_v_por(subexpressions):
    'v : v POR f'
    subexpressions[0] = subexpressions[1]["value"] + subexpressions[2] + subexpressions[3]["value"]
    
def p_v_div(subexpressions):
    'v : v DIV f'
    subexpressions[0] = subexpressions[1]["value"] + subexpressions[2] + subexpressions[3]["value"]
    
def p_v_potencia(subexpressions):
    'v : v POTENCIA f'
    subexpressions[0] = subexpressions[1]["value"] + subexpressions[2] + subexpressions[3]["value"]
    
def p_v_mod(subexpressions):
    'v : v PORCENTAJE f'
    subexpressions[0] = subexpressions[1]["value"] + subexpressions[2] + subexpressions[3]["value"]

def p_v_pregunta(subexpressions):
    'v : v INTERROGACION v DOSPUNTOS f'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + ' ' + subexpressions[3] + ' ' + subexpressions[4] + ' ' + subexpressions[5]
     
def p_v_num(subexpressions):
    'f : NUMBER'
    red = {"value": str(subexpressions[1]["value"]), "type": subexpressions[1]["type"]}
    subexpressions[0] = red
    
def p_v_var(subexpressions):
    'asig : VARIABLE'
    '''asegurarse que el tipo de la variable siga siendo el mismo'''
    subexpressions[0] = subexpressions[1]
    
def p_v_mEvvb(subexpressions):
    'v : MULTIPLICACIONESCALAR LPAREN v COMA v COMA v RPAREN'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + subexpressions[4] + subexpressions[5] + subexpressions[6] + subexpressions[7] + subexpressions[8]
        
def p_v_mEvv(subexpressions):
    'v : MULTIPLICACIONESCALAR LPAREN v COMA v RPAREN'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + subexpressions[4] + subexpressions[5] + subexpressions[6]

def p_v_cap(subexpressions):
    'v : CAPITALIZAR LPAREN v RPAREN'
    if (types[subexpressions[1]] not in ["CADENA"]): raise SemanticException("Incompatible type")
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + subexpressions[4]

def p_v_legth(subexpressions):
    'v : LENGTH LPAREN v RPAREN'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + subexpressions[4]

def p_v_cadena(subexpressions):
    'v : CADENA'
    subexpressions[0] = subexpressions[1]

def p_v_asignable(subexpressions):
    'asig : VARIABLE'
    subexpressions[0] = subexpressions[1]

def p_v_asignable(subexpressions):
    'asig : asig CORCHETEA v CORCHETEC'
    if (subexpressions[3]["type"] not in ["int", "float"]): raise SemanticException("Incompatible type")
    subexpressions[0] = subexpressions[1]

def p_v_asignable2(subexpressions):
    'asig : asig PUNTO VARIABLE'
    subexpressions[0] = subexpressions[1]
    
def p_a_var(subexpressions):
    'a : asig IGUAL v'
    types[subexpressions[1]] = subexpressions[3]["type"]
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + ' ' + subexpressions[3]["value"]

def p_o_masigual(subexpressions):
    'o : asig SUMA IGUAL v'
    if (types[subexpressions[1]] not in ["int", "float"]): raise SemanticException("Incompatible type")
    if (types[subexpressions[4]] not in ["int", "float"]): raise SemanticException("Incompatible type")
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + ' ' + subexpressions[4]["value"]
    
def p_o_menosigual(subexpressions):
    'o : asig MENOS IGUAL v'
    if (types[subexpressions[1]] not in ["int", "float"]): raise SemanticException("Incompatible type")
    if (types[subexpressions[4]] not in ["int", "float"]): raise SemanticException("Incompatible type")
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + ' ' + subexpressions[4]["value"]
        
def p_o_porigual(subexpressions):
    'o : asig POR IGUAL v'
    if (types[subexpressions[1]] not in ["int", "float"]): raise SemanticException("Incompatible type")
    if (types[subexpressions[4]] not in ["int", "float"]): raise SemanticException("Incompatible type")
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + ' ' + subexpressions[4]["value"]

def p_o_divigual(subexpressions):
    'o : asig DIV IGUAL v'
    if (types[subexpressions[1]] not in ["int", "float"]): raise SemanticException("Incompatible type")
    if (types[subexpressions[4]] not in ["int", "float"]): raise SemanticException("Incompatible type")
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + ' ' + subexpressions[4]["value"]

def p_o_masmas(subexpressions):
    'o : asig SUMA SUMA'
    if (types[subexpressions[1]] not in ["int", "float"]): raise SemanticException("Incompatible type")
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]

def p_o_menosmenos(subexpressions):
    'o : asig MENOS MENOS'
    if (types[subexpressions[1]] not in ["int", "float"]): raise SemanticException("Incompatible type")
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]
        
def p_o_masmasv(subexpressions):
    'o : SUMA SUMA asig'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]

def p_o_menosmenosv(subexpressions):
    'o : MENOS MENOS asig'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]

def p_o_print(subexpressions):
    'o : PRINT LPAREN v RPAREN'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + subexpressions[4]

def p_bq1(subexpressions):
	'bq : s'
	subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]
	
def p_bq2(subexpressions):
	'bq : LLAVEABIERTA ss LLAVECERRADA'
	subexpressions[0] = subexpressions[1] + '\n\t' + "\n\t".join(subexpressions[2].split("\n")) + '\n' + subexpressions[3]

def p_error(token):
    message = "[Syntax error]"
    if token is not None:
        message += "\ntype:" + token.type
        message += "\nvalue:" + str(token.value)
        message += "\nline:" + str(token.lineno)
        message += "\nposition:" + str(token.lexpos)
    raise Exception(message)
