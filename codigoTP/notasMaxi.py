-Antes teníamos una producción como la siguiente y ya no está, se chispoteó (?) o está bien haberla sacado?
	def p_inicial2(subexpressions):
		'ss : s NEWLINE ss'
		subexpressions[0] = subexpressions[1] + subexpressions[2] + subexpressions[3] 

	

-Que son las siguientes?

	def p_r_v(subexps):
		'r : v'
		subexps[0] = subexps[1]["value"]

	def p_r_a(subexps):
		'r : a'
		subexps[0] = subexps[1]

	def p_r_o(subexps):
		'r : o'
		subexps[0] = subexps[1]

-Por qué a veces indexar por "subtype" y a veces hacer el .get? Tiene que ver con que no se rompa si no hay un subtype? desconozco.

		
-Modificaciiones que hice (aca estan las funciones como estaban antes de que las modificara):
	
	General: En algunos lados usaba "subtipo" y en otros lados "subtype", lo unifique todo en "subtype".
	
	Detalles:
	
	def p_while(subexps):
			'w : WHILE LPAREN v RPAREN bq'
			if subexps[3]["type"]=="bool":
				subexps[0] = subexps[1] + subexps[2] + subexps[3]["value"] + subexps[4] + '\n\t' + subexps[5]
			else:
				raise SemanticException("Expresion no-booleana en la guarda")

		y en 
		def p_for1(subexps):
		def p_for2(subexps):
		def p_for3(subexps):
				
		creo yo que sacar el '\n\t', pensa que te tiene que poder quedar algo asi:

		while(true){
			a = 2;
		}

		donde el primer corchete esta en la misma linea que el RPAREN

	def p_b_not(subexps):
			'v : NOT f'
			subexps[0] = dict()
			subexps[0]["type"] = "bool"
			subexps[0]["value"] = subexps[1] + subexps[2]["value"]
			
		falta un ' ' entre las subexps y un chequeo de bool de f
		
	def p_b_and_or(subexps):
		'''v : v OR f
		v : v AND f'''
		if (not (subexps[1]["type"]=="bool")): raise SemanticException("Expresion no-booleana")
		subexps[0] = dict()
		subexps[0]["type"] = "bool"
		subexps[0]["value"] = subexps[1]["value"] + ' ' + subexps[2] + ' ' + subexps[3]["value"]
		
		chequear que f tambien sea de tipo bool
		
	def p_b_igualigual(subexps):
		agregue comparacion directa de subtipos
		
	def p_b_mayor(subexps):
		'''v : v MAYOR f
		v : v MENOR f'''
		subexps[0] = dict()
		subexps[0]["type"] = "bool"
		subexps[0]["value"] = subexps[1]["value"] + ' ' + subexps[2] + ' ' + subexps[3]["value"]
		
		agregar chequeo de tipos. Yo imagino que solo se pueden comparar asi numeros o strings, pero el enunciado parece decir que cualquier par de cosas del mismo tipo. A chequear.
		
	def p_v_pregunta(subexps):
		'v : v INTERROGACION v DOSPUNTOS f'
		if (not (subexps[1]["type"]=="bool" and subexps[3]["type"]==subexps[5]["type"])): 
			if (not (subexps[3]["type"] in ["int", "float"] and subexps[5]["type"] in ["int", "float"])):
				raise SemanticException("Error en los tipos de argumentos")
		subexps[0] = dict()
		subexps[0]["type"] = subexps[3]["type"]
		subexps[0]["value"] = subexps[1]["value"] + subexps[2] + ' ' + subexps[3]["value"] + ' ' + subexps[4] + ' ' + subexps[5]["value"]
		
		El chequeo de tipos falla si los tres "valores" son numericos. Entra en el primer if, porque el primer valor no es un bool, pero despues como el segundo y tercer valor son numericos NO entra en el segundo if y por lo tanto no tira la excepcion.
		
	def p_v_mEvvb(subexps):
		'f : MULTIPLICACIONESCALAR LPAREN v COMA v COMA v RPAREN'
		if (not (subexps[3]["type"]=="vector")): raise SemanticException("Error en los tipos de argumentos")
		if (not (subexps[3]["subtipo"]["type"] in ["int", "float"])): raise SemanticException("Error en los tipos de argumentos")
		if (not (subexps[5]["type"] in ["int", "float"]=="numero" and subexps[7]["type"]=="bool")): raise SemanticException("Error en los tipos de argumentos")
		subexps[0] = dict()
		subexps[0]["type"] = "int"
		subexps[0]["value"] = subexps[1] + subexps[2] + subexps[3] + subexps[4] + subexps[5] + subexps[6] + subexps[7] + subexps[8]
		
		Habia una flasheada ahi en el =="numero" del tercer if. Ademas el tipo de f en este caso es vector y subtipo int o float porque la funcion devuelve un vector de numeros. Y faltan unos ["value"] en el final
		
	def p_v_mEvv(subexps):
		'f : MULTIPLICACIONESCALAR LPAREN v COMA v RPAREN'
		if (not (subexps[3]["type"]=="vector")): raise SemanticException("Error en los tipos de argumentos")
		if (not (subexps[3]["subtipo"]["type"] in ["int", "float"])): raise SemanticException("Error en los tipos de argumentos")
		if (not (subexps[5]["type"] in ["int", "float"])): raise SemanticException("Error en los tipos de argumentos")
		subexps[0] = dict()
		subexps[0]["type"] = "float"
		subexps[0]["value"] = subexps[1] + subexps[2] + subexps[3] + subexps[4] + subexps[5] + subexps[6]
		
		f es tipo vector y el subtipo es int o float dependiendo, y faltan unos value al final.

	def p_v_lista(subexps):
		'lista : lista COMA v'
		if (subexps[1]["type"] != subexps[3]["type"]): 
		if not(subexps[1]["type"] in ["int", "float"], subexps[3]["type"] in ["int", "float"]):
			raise SemanticException("Los vectores solo pueden tener un tipo")
		subexps[0] = dict()
		subexps[0]["type"] = subexps[1]["type"]
		subexps[0]["subtype"] = subexps[1]["subtype"]
		subexps[0]["value"] = subexps[1]["value"] + subexps[2] + ' ' + subexps[3]["value"]
		
		la lista de la derecha va a tener tipo vector, hay que verle el subtipo para comparar con el valor v
		
	def p_v_listareg(subexps):
		'listareg : listareg COMA VARIABLE DOSPUNTOS v'
		subexps[0] = dict()
		subexps[0]["type"] = "registro"
		subexps[0]["subtype"] = dict()
		subexps[0]["subtype"][subexps[3]] = {"type": subexps[5]["type"], "subtype": subexps[5].get("subtype")} ### mejorar
		subexps[0]["value"] = subexps[1]["value"] + subexps[2] + ' ' + subexps[3] + subexps[4] + subexps[5]["value"]

		falta poner en el subtype de subexprs[0] los campos que venian arrastrados en subexprs[1]
	
	def p_o_masigual(subexps):
		'''o : VARIABLE index MASIGUAL v
		o : VARIABLE index MENOSIGUAL v
		o : VARIABLE index PORIGUAL v
		o : VARIABLE index DIVIGUAL v'''
		
		if (types[subexps[1]] == "vector" or types[subexps[1]] == "registro"):
			asigtype = buscar(types[subexps[1]], subtypes[subexps[1]], subexps[2]["value"])[0]
		else: asigtype = types[subexps[1]]
		if (asigtype not in ["int", "float"] or subexps[4]["type"] not in ["int", "float"]): raise SemanticException("Valor no numerico")

		subexps[0] = subexps[1] + ' ' + subexps[2]["value"] + subexps[3] + ' ' + subexps[4]["value"]
		
		saco el espacio entre la subexp 1 y la 2 que es el indexado, y lo paso para entre el 2 y el 3 que es el operador.

	def p_o_masmasv(subexps):
		'''o : MASMAS VARIABLE index
		o : MENOSMENOS VARIABLE index'''
		if (types[subexps[2]] == "vector" or types[subexps[2]] == "registro"):
			asigtype = buscar(types[subexps[2]], subtypes[subexps[2]], subexps[3]["value"])[0]
		else: asigtype = types[subexps[1]]
		if (asigtype not in ["int", "float"]): raise SemanticException("Valor no numerico")
		subexps[0] = subexps[1] + subexps[2] + subexps[3]["value"]
		
		en el else tiene que ser subexprs 2
		
		
		
-Dudas:
	def p_a_var1(subexps):
		'index : index CORCHETEA v CORCHETEC'
		subexps[0] = dict()
		subexps[0]["type"] = "vector"
		subexps[0]["subtype"] = {"type" : subexps[1]["type"], "subtype" : subexps[1].get("subtype")}
		if (subexps[3]["type"] not in ["int", "float"]): raise SemanticException("Vector index not a number")
		subexps[0]["value"] = subexps[1]["value"] + subexps[2] + subexps[3]["value"] + subexps[4]
		
		aca subexps[0]["type"] no deberia ser subexps[1]["type"]? por ejemplo si tengo VAR.hola[2] esto es un VAR index [2] y ese "index" tiene tipo registro (porque internamente es un "index PUNTO VARIABLE"). Osea el que primero indexa es el de mas a la izquierda.

	def p_a_var2(subexps):
		'index : index PUNTO VARIABLE'
		subexps[0] = dict()
		subexps[0]["type"] = "registro"
		subexps[0]["subtype"] = {subexps[3]: {"type": subexps[1]["type"], "subtype": subexps[1].get("subtype")}}
		subexps[0]["value"] = subexps[1]["value"] + subexps[2] + subexps[3]
		
		idem anterior

	def p_a_var3(subexps):
		'index : '
		subexps[0] = dict()
		subexps[0]["type"] = {"type" : "empty"}
		subexps[0]["value"] = ""
		
		ver si al cambiar las anteriores esto hay que modificarlo o no. Osea habria que agregar el if en las otras considerando que puede venir un empty.
		
		
		
