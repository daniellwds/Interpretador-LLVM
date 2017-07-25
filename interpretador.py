"""
	Nomes: Daniel Welter da Silva, Gardel Batista, Luis Henrique Wasem de Oliveira
"""

class analisadorLexico():
	variaveis = {} #dicionario que armazena o nome e o valor das variaveis do codigo de entrada

	def ehVariavel(self, palavra, palavra1): 
		if(palavra == "inteiro"): #analisa uma instancia de variavel do tipo inteira
			self.variaveis[palavra1] = "0" #armazena no dicionario de variaveis, o nome da variavel com o valor 0
			return True 
		else:
			return False 	

	def ehVariavelExistente(self, palavra):
		var = 0 #cria uma variavel do tipo inteiro
		var = self.ehNumero(self.variaveis[palavra]) #captura o valor da variavel correspondente
		return var #retorna o valor da variavel

	def ehNumero(self, palavra):
		try: 
			palavra = int(palavra) #tenta transformar a palavra lida em inteiro
			return palavra #se conseguir retorna a palavra
		except ValueError:	
			return False #se nao conseguir, retorna falso

	def ehPrint(self, palavra):
		if(palavra == "imprimir"): 
			return True
		else:
			return False

	def ehIgual(self, palavra):
		if(palavra == "="): 
			return True
		else:
			return False

	def ehDelimitador(self, palavra):
		if(palavra == ";"):
			return True
		else:
			return False

	def defineSomaVariavel(self, palavra, palavra1, palavra2, palavra3, palavra4): #função para executar uma soma
		if(palavra3 == "+"): 
			var = 0; #cria uma variavel do tipo inteiro
			if(self.ehNumero(palavra2)): #verifica se é numero
				var += self.ehNumero(palavra2) #adiciona o numero a variavel de controle
			else: #se nao for numero
				var += self.ehVariavelExistente(palavra2) #pega o valor da variavel correspondente no dicionario de variaveis
			if(self.ehNumero(palavra4)): #verifica se é numero
				var += self.ehNumero(palavra4)
			else: #se nao for numero
				var += self.ehVariavelExistente(palavra4)#pega o valor da variavel correspondente no dicionario de variaveis
			self.variaveis[palavra] = var

	def defineSubVariavel(self, palavra, palavra1, palavra2, palavra3, palavra4): #função para executar uma subtração
		if(palavra3 == "-"):
			var = 0; #o funcionamento é igual as função defineSomaVariavel()
			if(self.ehNumero(palavra2)):
				var = self.ehNumero(palavra2)
			else:
				var = self.ehVariavelExistente(palavra2)
			if(self.ehNumero(palavra4)):
				var -= self.ehNumero(palavra4)
			else:
				var -= self.ehVariavelExistente(palavra4)
			self.variaveis[palavra] = var

	def defineMultiVariavel(self, palavra, palavra1, palavra2, palavra3, palavra4): #função para executar uma multiplicação
		if(palavra3 == "*"):
			var = 0;  #o funcionamento é igual as função defineSomaVariavel()
			if(self.ehNumero(palavra2)):
				var = self.ehNumero(palavra2)
			else:
				var = self.ehVariavelExistente(palavra2)
			if(self.ehNumero(palavra4)):
				var *= self.ehNumero(palavra4)
			else:
				var *= self.ehVariavelExistente(palavra4)
			self.variaveis[palavra] = var

	def defineDiviVariavel(self, palavra, palavra1, palavra2, palavra3, palavra4): #função para executar uma divisão
		if(palavra3 == "/"):
			var = 0;  #o funcionamento é igual as função defineSomaVariavel()
			if(self.ehNumero(palavra2)):
				var = self.ehNumero(palavra2)
			else:
				var = self.ehVariavelExistente(palavra2)
			if(self.ehNumero(palavra4)):
				var /= self.ehNumero(palavra4)
			else:
				var /= self.ehVariavelExistente(palavra4)
			self.variaveis[palavra] = int(var)

	def defineValorVariavel(self, palavra, palavra1, palavra2): #função para armazenar o valor fornecido em uma variavel
		if(self.ehIgual(palavra1)): #verifica se na frase existe o operador "="
			if(self.ehNumero(palavra2)): #se for um numero, armazena esse valor no dicionario de variaveis
				self.variaveis[palavra] = self.ehNumero(palavra2)
			else: #se for outra variavel:
				self.variaveis[palavra] = self.ehVariavelExistente(palavra2)#le o valor dessa variavel, e armazena em um novo espaço no dicionario de variaveis

	def alocaVariaveis(self): #função para criar os registradores no codigo llvm
		string = "" #variavel do tipo string
		for i in range(0, len(self.variaveis)+1): #laço de repetição para percorrer o dicionario de variaveis
			string += "%" + str(i+1) + " = alloca i32, align 4\n" #cada iteração, é uma variavel e uma linha de codigo llvm
		return string 

	def storeVariaveis(self):#função para definir os valores dos registradores no codigo llvm
		string = "" #variavel do tipo string
		lista = list(self.variaveis.values()) #cria uma lista com os valores das variaveis do dicionarios
		for i in range(0, len(lista)):
			string += "store i32 " + str(lista[i]) + ", i32* %" + str(i+2) + ", align 4\n" #adiciona o valor da variavel no registrador correspondente
		return string

	def definePrint(self, palavra, num):#função para gerar o codigo llvm responsavel por imprimir variaveis
		string = "" #variavel do tipo string
		lista = list(self.variaveis.keys()) #lista que armazena os nomes das variaveis do dicionario de variaveis
		for i in range(0, len(lista)): #função para percorrer a lista criada acima
			if(palavra == lista[i]): #se existe a variavel indicada para impressao gera o codigo de impressao llvm a seguir:
				string += "%" + str(len(lista) + 2 + num) + " = load i32, i32* %" + str(i+2) + ", align 4\n"
		string +=  "%" + str(len(lista) + 3 + num) + " = call i32 (i8*, ...) @printf" + "(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %" + str(len(lista) + 2 + num) + ")\n"
		return string #retorna o codigo gerado


	def analisa(self):
		entrada = open("entrada.txt", "r") #arquivo de entrada com o codigo a ser executado
		codigo = entrada.read() #leitura do arquivo de entrada, transforma em string
		lista = codigo.split() #divide a string do arquivo de entrada em uma lista, cada palavra é um elemento
		saida = open("saida.ll", "w") #abre arquivo de saida
		impressao = "" #variavel String para armazenar a parte do codigo llvm responsavel pela impressao de variaveis
		num = 0 #variavel de controle para criação de registradores no codigo de saida
		defineStr = "\n"
		definePrint = ""

		for i in range(0, len(lista)-1): #for para registrar em um dicionario as variaveis definidas no codigo de entrada
			self.ehVariavel(lista[i-1], lista[i]) #analisa se é uma instancia de variavel e armazena no dicionario de variaveis
			self.defineSomaVariavel(lista[i-4], lista[i-3], lista[i-2], lista[i-1], lista[i]) #analisa somas e atualiza o valor no dicionario 
			self.defineSubVariavel(lista[i-4], lista[i-3], lista[i-2], lista[i-1], lista[i]) #analisa subtrações e atualiza o valor
			self.defineMultiVariavel(lista[i-4], lista[i-3], lista[i-2], lista[i-1], lista[i]) #analisa multiplicações e atualiza o valor
			self.defineDiviVariavel(lista[i-4], lista[i-3], lista[i-2], lista[i-1], lista[i]) #analiza divisoes e atualiza o valor
			self.defineValorVariavel(lista[i-2], lista[i-1], lista[i]) #define o valor de uma variavel no dicionario
		
		for i in range(0, len(lista)-1): #for para registrar o codigo llvm de impressao
			if(self.ehPrint(lista[i])): #procura pela palavra "imprimir" no codigo de entrada
				impressao += self.definePrint(lista[i+1], num)
				num += 2 #variavel de controle para criação de registradores no codigo de saida
				defineStr = '\n@.str = private unnamed_addr constant [3 x i8] c"%d\00", align 1\n\n' #codigo llvm que define o tipo str
				definePrint = '\ndeclare i32 @printf(i8*, ...) #1\n\n' #codigo que declara o metodo print
				print (self.variaveis[lista[i+1]]) #imprime na tela as variaveis que o usuário solicitar

		
		saida.write(defineStr)
		cabecalho = "; Function Attrs: noinline nounwind uwtable\ndefine i32 @main() #0 {\n" #cria o cabeçalho do codigo llvm
		saida.write(cabecalho) #escreve na saida o cabeçalho
		a = self.alocaVariaveis() #codigo llvm que aloca registradores
		saida.write(a) #aloca no codigo de saida os registres
		variavelPadrao = "store i32 0, i32* %1, align 4\n" #variavel padrao do llvm
		saida.write(variavelPadrao) #escreve no codigo variavel padrao
		variaveisValor = self.storeVariaveis() #armazena os valores das variaveis nos registradores do llvm
		saida.write(variaveisValor) #escreve no codigo a parte que guarda os valores nos registradores
		saida.write(impressao) #escreve no codigo o que deve ser imprimido na tela
		rodape = "ret i32 0\n}\n" #rodape de fechamento do codigo llvm
		saida.write(rodape) #escreve o rodape no arquivo de saida
		saida.write(definePrint)
		entrada.close() #fecha o arquivo de entrada
		saida.close() #fecha o arquivo de saida


teste = analisadorLexico() #chama a classe analisadorLexico, que contem as funções de analise do codigo
teste.analisa() #chama o metodo que analisa todo o codigo, e escreve a saida