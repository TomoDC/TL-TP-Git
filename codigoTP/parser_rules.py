from lexer_rules import tokens
#from operator import add, mul
#from expressions import BinaryOperation, Number

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

def p_r_b(subexpressions):
    'r : b'
    subexpressions[0] = subexpressions[1]

def p_r_v(subexpressions):
    'r : v'
    subexpressions[0] = subexpressions[1]

def p_r_a(subexpressions):
    'r : a'
    subexpressions[0] = subexpressions[1]

def p_r_o(subexpressions):
    'r : o'
    subexpressions[0] = subexpressions[1]

def p_if(subexpressions):
    'if : IF LPAREN b RPAREN bq'
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + subexpressions[4] + subexpressions[5]
    
def p_if_else(subexpressions):
    'if : IF LPAREN b RPAREN bq ELSE bq'
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + subexpressions[4] + subexpressions[5] + '\n' + subexpressions[6] + subexpressions[7]

def p_while(subexpressions):
	'w : WHILE LPAREN b RPAREN bq'
	subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + subexpressions[4] + '\n\t' + subexpressions[5]

def p_do_while(subexpressions):
	'd : DO bq WHILE LPAREN b RPAREN PUNTOCOMA'
	subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + ' ' + subexpressions[4] + subexpressions[5] + subexpressions[6] + subexpressions[7]

def p_for1(subexpressions):
	'f : FOR LPAREN b RPAREN bq'
	subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + subexpressions[4] + '\n\t' + subexpressions[5]

def p_for2(subexpressions):
	'f : FOR LPAREN a PUNTOCOMA b RPAREN bq'
	subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + subexpressions[4] + ' ' + subexpressions[5] + subexpressions[6] + '\n\t' + subexpressions[7]

def p_for3(subexpressions):
	'f : FOR LPAREN a PUNTOCOMA b PUNTOCOMA o RPAREN bq'
	subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + subexpressions[4] + ' ' + subexpressions[5] + subexpressions[6] + ' ' + subexpressions[7] + subexpressions[8] + '\n\t' + subexpressions[9]

def p_b_true(subexpressions):
    'b : TRUE'
    subexpressions[0] = subexpressions[1]

def p_b_false(subexpressions):
    'b : FALSE'
    subexpressions[0] = subexpressions[1]

def p_b_not(subexpressions):
    'b : NOT b'
    subexpressions[0] = subexpressions[1] + subexpressions[2]
    
def p_b_or(subexpressions):
    'b : b OR b'
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + ' ' + subexpressions[3]
    
def p_b_and(subexpressions):
    'b : b AND b'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]

def p_b_pregunta(subexpressions):
    'b : b INTERROGACION b DOSPUNTOS b'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + subexpressions[4] + subexpressions[5]

def p_b_igualigual(subexpressions):
    'b : v IGUAL IGUAL v'
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + ' ' + subexpressions[4]

def p_b_desigualdad(subexpressions):
    'b : v DESIGUALDAD v'
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + ' ' + subexpressions[3]
    
def p_b_mayor(subexpressions):
    'b : v MAYOR v'
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + ' ' + subexpressions[3]

def p_b_menor(subexpressions):
    'b : v MENOR v'
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + ' ' + subexpressions[3]

def p_b_b(subexpressions):
    'b : LPAREN b RPAREN'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]
    
def p_b_variable(subexpressions):
    'b : VARIABLE'
    subexpressions[0] = subexpressions[1]

def p_b_colineales(subexpressions):
    'b : COLINEALES LPAREN v COMA v RPAREN'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + subexpressions[4] + ' ' + subexpressions[5] + subexpressions[6]    
    
def p_v_parentesis(subexpressions):
    'v : LPAREN v RPAREN'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]

def p_v_resta(subexpressions):
    'v : v MENOS v'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]

def p_v_suma(subexpressions):
    'v : v SUMA v'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]

def p_v_por(subexpressions):
    'v : v POR v'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]
    
def p_v_div(subexpressions):
    'v : v DIV v'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]
    
def p_v_potencia(subexpressions):
    'v : v POTENCIA v'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]
    
def p_v_mod(subexpressions):
    'v : v PORCENTAJE v'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]

def p_v_pregunta(subexpressions):
    'v : b INTERROGACION v DOSPUNTOS v'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + ' ' + subexpressions[3] + ' ' + subexpressions[4] + ' ' + subexpressions[5]
     
def p_v_num(subexpressions):
    'v : NUMBER'
    subexpressions[0] = str(subexpressions[1])
    
def p_v_var(subexpressions):
    'v : VARIABLE'
    subexpressions[0] = subexpressions[1]
    
def p_v_vec(subexpressions):
    'v : VARIABLE CORCHETEA v CORCHETEC'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + subexpressions[4]

def p_v_reg(subexpressions):
    'v : VARIABLE PUNTO v'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]
    
def p_v_mEvvb(subexpressions):
    'v : MULTIPLICACIONESCALAR LPAREN v COMA v COMA b RPAREN'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + subexpressions[4] + subexpressions[5] + subexpression[6] + subexpressions[7] + subexpressions[8]
        
def p_v_mEvv(subexpressions):
    'v : MULTIPLICACIONESCALAR LPAREN v COMA v RPAREN'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + subexpressions[4] + subexpressions[5] + subexpressions[6]

def p_v_cap(subexpressions):
    'v : CAPITALIZAR LPAREN v RPAREN'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + subexpressions[4]

def p_v_legth(subexpressions):
    'v : LENGTH LPAREN v RPAREN'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + subexpressions[4]

def p_v_cadena(subexpressions):
    'v : CADENA'
    subexpressions[0] = subexpressions[1]
    
def p_v_bool(subexpressions):
    'v : b'
    subexpressions[0] = subexpressions[1]

def p_a_reg(subexpressions):
    'a : VARIABLE PUNTO v IGUAL v'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + subexpressions[4] + subexpressions[5]
    
def p_a_vec(subexpressions):
    'a : VARIABLE CORCHETEA v CORCHETEC IGUAL v'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] + subexpressions[4] + subexpressions[5] + subexpression[6]

def p_a_var(subexpressions):
    'a : VARIABLE IGUAL v'
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + ' ' + subexpressions[3]

def p_o_masigual(subexpressions):
    'o : VARIABLE SUMA IGUAL v'
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + ' ' + subexpressions[4]
    
def p_o_menosigual(subexpressions):
    'o : VARIABLE MENOS IGUAL v'
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + ' ' + subexpressions[4]
        
def p_o_porigual(subexpressions):
    'o : VARIABLE POR IGUAL v'
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + ' ' + subexpressions[4]

def p_o_divigual(subexpressions):
    'o : VARIABLE DIV IGUAL v'
    subexpressions[0] = subexpressions[1] + ' ' + subexpressions[2] + subexpressions[3] + ' ' + subexpressions[4]

def p_o_masmas(subexpressions):
    'o : VARIABLE SUMA SUMA'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]

def p_o_menosmenos(subexpressions):
    'o : VARIABLE MENOS MENOS'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]
        
def p_o_masmasv(subexpressions):
    'o : SUMA SUMA VARIABLE'
    subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3]

def p_o_menosmenosv(subexpressions):
    'o : MENOS MENOS VARIABLE'
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
