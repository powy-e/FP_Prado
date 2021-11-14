from functools import reduce

#### Prado Dim Horizontal X Dim Vertical Y

### TAD

#def cria_PRADOTTTT(x: int, y: int):


    #if type(x) != int or type(y) != int or x < 2 or y < 2:
    #    raise ValueError("cria_posicao: argumentos invalidos")

    #lst = []

    #for j in range(len(y)):
    #    lst.append([0]*(x))


def cria_posicao(x: int, y: int):
    """
    cria_posicao: int x int -> posicao
    esta funcao cria uma posicao a partir de dois inteiros positivos
    """
    if type(x) != int or type(y) != int or x < 0 or y < 0:
        raise ValueError("cria_posicao: argumentos invalidos")

    return (x,y)

#### isto pode n ser a melhor maneira mas tuplos sao imutaveis logo tecnicamente isto deve funcionar
def cria_copia_posicao(pos):
    """
    cria_copia_posicao: posicao -> posicao
    esta funcao cria uma copia de uma posicao
    """
    if not eh_posicao(pos):
        raise ValueError("cria_copia_posicao: argumentos invalidos")

    return pos


def obter_pos_x(pos):
    """
    obter_pos_x: posicao -> int
    retorna a componente x da posicao
    """
    return pos[0]


def obter_pos_y(pos):
    """
    obter_pos_y: posicao -> int
    retorna a componente y da posicao
    """
    return pos[1]


def eh_posicao(arg):
    """
    eh_posicao: universal -> booleano
    retorna True se o argumento passado for uma posicao, caso contrario retorna False
    """

    return isinstance(arg, tuple) and len(arg) == 2 and obter_pos_y(arg) >= 0 and obter_pos_x(arg) >= 0

def posicoes_iguais(p1,p2):
    """
    posicoes_iguais: posicao x posicao -> booleano
    devolve True se p1 e p2 sao posicoes iguais
    """

    return eh_posicao(p1) == eh_posicao(p2) and p1 == p2


def posicao_para_str(pos):
    """
    posicao_para_str: posicao -> str
    devolve uma string que representa a posicao
    """

    return str(pos)


def obter_posicoes_adjacentes(pos):
    """
    obter_posicoes_adjacentes: posicao -> tuplo
    devolve um tuplo com as posicoes adjacentes ordenadas
    """
    x = obter_pos_x(pos)
    y = obter_pos_y(pos)
    adj_pos = ()
    if y != 0:
        adj_pos += ((cria_posicao(x,y-1)),)
    adj_pos += (cria_posicao(x+1,y), cria_posicao(x,y+1))
    if x != 0:
        adj_pos += (cria_posicao(x-1,y), )

    return adj_pos


def ordenar_posicoes(tup):
    """
    ordenar_posicoes: tuplo -> tuplo
    retorna o tuplo original ordenado
    """

    lst = list(tup)

    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i + 1, len(lst)):                #procura o menor elemento da lista (isto é menor y, menor x)
            if obter_pos_y(lst[j]) < obter_pos_y(lst[min_index]):
                min_index = j

            elif obter_pos_y(lst[j]) == obter_pos_y(lst[min_index]):
                if obter_pos_x(lst[j]) < obter_pos_x(lst[min_index]):
                    min_index = j

        lst[i], lst[min_index] = lst[min_index], lst[i]


    return tuple(lst)

