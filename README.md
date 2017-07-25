# Interpretador LLVM
Interpretador que lê um codigo de entrada, executa esse código e gera uma saida LLVM.

## Começando

As seguintes instruções irão lhe auxiliar a executar uma cópia do projeto e fazer testes em sua 
maquina local.

### Pré-requisitos
* Python 3
* Os arquivos que estão nesse repositório
* Preferencialmente um ambiente linux
* LLVM

### Informações importantes
O arquivo de entrada deve estar salvo na mesma pasta que o interpretador, com o seguinte nome
```
entrada.txt
```
O arquivo gerado pelo interpretador é LLVM, pode ser compilado com o clang. Ele será gerado na 
mesma pasta que o interpretador com o seguinte nome
```
saida.ll
```
O interpretador não tem um debugger, então, mesmo se o arquivo de entrada estiver errrado, o
interpretador ira executar normalmente e gerar uma saida.

## Sobre o código de entrada
A linguagem utilizada no codigo de entrada foi criada especialmente para esse interpretador.

### Sintaxe basica
É necessário um espaço entre cada palavra do código, inclusive antes do delimitador ";". Um exemplo de código está
disponível abaixo.

#### Variáveis
Para instanciar uma variável, devemos usar o identificador de tipo "inteiro" seguido do nome da variavel:
```
inteiro variavel ;
```
Para criar variáveis e ja atribuir um valor, não é necessário do identificador:
```
variavel = 10 ;
```
#### Operações
O interpretador trabalha com as operações matemáticas basicas, sendo elas: adição, subtração, divisão
e multiplicação:
```
variavelA = 10 + 20 ;
variavelB = 20 - 10 ;
variavelC = variavelA * variavelB ;
variavelD = variavelC / variavelB ;
```
#### Output
A linguagem permite que você imprima as variáveis na tela, com o seguinte comando:
```
imprimir variavel ;
```
#### Exemplo de código
```
    inteiro a ;
    b = 20 ;
    a = 200 ;
    c = a * b ;
    imprimir c ;
```

## Executando testes
Depois que o codigo de entrada estiver devidamente criado, basta apenas executar o arquivo python:
```
interpretador.py
```
Para fazer isso em ambiente linux, basta abrir o terminal na pasta que o arquivo está salvo e executar o seguinte comando:
```
$ python3 interpretador.py
```
Em ambiente windows, será necessário a IDLE Python disponivel nesse [link](https://www.python.org/download/releases/3.0/).

Feito isso, o arquivo LLVM será criado na mesma pasta, para vizualizar esse arquivo em ambiente linux, basta executar
o seguinte comando no terminal:
```
$ cat saida.ll
```
Podemos também compilar esse arquivo e gerar um executavel, com o seguinte comando no terminal:
```
$ clang saida.ll -o executavel
```
## Autores
### Desenvolvedores
* Daniel Luis Welter da Silva
* Gardel Gomes Batista Filho
* Luis Henrique Wasem de Oliveira

### Orientador
* Emilio Wuerges

##### Informações adicionais
Esse interpretador foi desenvolvido para a disciplina de Sistemas Digitais do curso de Ciência da Computação, na Universidade Federal da Fronteira Sul, campus Chapecó.