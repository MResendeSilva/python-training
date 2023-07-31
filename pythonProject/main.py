
def cont_by (x,n):
    cont = 1
    list = []

    while cont < n + 1:
        list.append(cont * x)
        cont += 1
    print(list)

def list_training () :
    arr = ['O carro azul', 'peixe', 123, 111, 'pedra']
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    'peixe' in arr # Booleano que verifica se possui esse contexto na variavel

    min(numeros) # Retorna o menor numero do arr
    max(numeros) # Retorna o maior numero do arr
    sum(numeros) # Soma todos os numeros do arr

    arr.append("Catapimbas") # Adiciona um elemento no final da lista
    arr.insert(0,"O carro preto") # Adiciona um elemento em uma posição especifica da lista
    numeros.pop() # Retira da lista o ultimo elemento
    numeros.pop(3) # Passada uma posição como argumento, será retirado o elemento da posição especifica
    arr.remove('peixe') # Remove a primeira ocorrencia do elemento passado em argumento
    arr.reverse() # Inverte a lista
    arr.sort() # Ordena de forma aleatoria o array
    arr.count('pedra') # Retorna o numero de ocorrencias de um item passado em argumento

    numeros = [1, 2, 3, 4, 5]
    dobro_numeros = [numero * 2 for numero in numeros]
    print(dobro_numeros)  # Output: [2, 4, 6, 8, 10]

    numeros = [1, 2, 3, 4, 5]
    dobro_numeros = list(map(lambda x: x * 2, numeros))
    print(dobro_numeros)  # Output: [2, 4, 6, 8, 10]

    numeros = [1, 2, 3, 4, 5]
    pares = list(filter(lambda x: x % 2 == 0, numeros))
    print(pares)  # Output: [2, 4]



def testing_newArray() :
    arr = [6, 0, 1, 10, 10]

    if arr is None or len(arr) <= 1:
        return 0
    else:
        arr.remove(max(arr))
        arr.remove(min(arr))
        print(sum(arr))

    7 // 3 # Divide um número ja arredondando para baixo (igual math.floor())



def remove_char(s):
    if len(s) > 2:
        arr = list(s)
        arr.pop(0)
        arr.pop()
        return ''.join(arr)


#remove_char('eloquent')

def enough(cap, on, wait):
   print(0 if cap - on >= wait else wait - on) # fazendo if em apenas uma linha
    #max(0, wait - (cap - on))
    #max(wait + on - cap, 0)
    #enough = lambda c, o, w: max(0, w - (c - o))


def twice_as_old(dad_years_old, son_years_old):
    print(dad_years_old - son_years_old * 2)
    #return abs(dad_years_old - son_years_old * 2) ABS é uma função que retorna o valor absoluto de um elemento, ignorando o seu sinal

def smash(words):
    print(" ".join(words)) # Concatena as palavras .
    # O argumento " " passado para join() especifica que um espaço em branco deve ser usado como separador entre as palavras.

    """
        a = "Hello"
        b = "world"
        c = a + " " + b
        print(c)
        
            result = ""
    for i in range(len(words)):
        if i != len(words)-1:
            result = result + words[i] + " "
        else:
            result = result + words[i]
    return result              
    """

def check_for_factor(base, factor):
    #return base % factor == 0
    #return not base%factor
    pass

def no_space(x):
    print(x.replace(" ",""))
    #nova_string = string_original.replace(valor_antigo, valor_novo)
    # A função replace() retorna uma nova string com todas as substituições feitas.
    # É importante notar que as strings em Python são imutáveis, o que significa que a função replace()
    # não altera a string original, mas cria uma nova string com as substituições

def century(year):
     #return year // 100 if year % 100 == 0 else (year // 100) + 1
     #return (year + 99) // 100
     #return math.ceil(year / 100) # Verificar sobre essa funcao
     pass

def get_count(sentence):
    cont = 0
    for letter in sentence:
        if letter == 'a' or letter == 'e' or  letter == 'i' or  letter == 'o' or  letter == 'u':
            cont += 1

    #return sum(1 for let in inputStr if let in "aeiouAEIOU")
    """
    Este código retorna a contagem de vogais em uma string inputStr.

    Vamos analisar o código por partes:

    for let in inputStr: Isso cria um loop que itera sobre cada caractere da string inputStr. A cada iteração, o caractere atual é atribuído à variável let.

    if let in "aeiouAEIOU": Esta é uma condição que verifica se o caractere atual let é uma vogal. Aqui, estamos verificando se let está presente na sequência de vogais "aeiouAEIOU".

    1 for let in inputStr if let in "aeiouAEIOU": Esta é uma expressão de gerador que retorna 1 para cada caractere da string inputStr que é uma vogal.

    sum(...): A função sum() é usada para somar todos os valores retornados pela expressão de gerador. Neste caso, somamos 1 para cada vogal encontrada na string inputStr.

    return: A declaração return é usada para retornar o resultado da soma, ou seja, a contagem de vogais na string inputStr.

    Em resumo, o código itera sobre cada caractere da string inputStr, verifica se o caractere é uma vogal e retorna a contagem total de vogais encontradas na string.
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    #return sum(c in 'aeiou' for c in s)
    #return len(re.findall('[aeiou]', str, re.IGNORECASE))
    #return sum(inputStr.count(char) for char in ['a', 'e', 'i', 'o', 'u'])


def solution(s):
        #https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python
    pass

def listFiltering():
    l = [1, 2, 'aasf', '1', '123', 123]
    nl= list(filter(lambda x: isinstance(x,int) ,l)) #isintance tem o mesmo proposito do isInstance do Java
    #[x for x in l if type(x) is not str]
    #[i for i in l if not isinstance(i, str)]
    #lembrar que ao utilizar lambda, ja se supoem que é a expressão!!!
    print(nl)

import math

def find_next_square(n):
    x = n ** 0.5
    x + 1 ** 2
    print(x)

    #if not math.sqrt(n).is_integer():
     #   print("-1")
    #else:
    #    while True:
     #       n += 1
     #       if math.sqrt(n).is_integer():
      #          print(n)
       #         break
    #Nessa eu procurei a raiz através do maior numero


    #root = sq ** 0.5
    #if root.is_integer():
    #    return (root + 1)**2
    #return -1

    #x = sq**0.5
    #return -1 if x % 1 else (x+1)**2
    # Aqui ele encontra a raiz do primeiro numero, soma mais um e faz a potenciação
    # Isso permite encontrar a próxima raiz se utilizar for
    # Podemos pensar nisso mais vezes

    # return (math.sqrt(sq) + 1) ** 2 if (math.sqrt(sq)).is_integer() else -1
