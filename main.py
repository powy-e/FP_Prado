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
    devolve True se p1 e p2 sao posicoes iguais             FAZEMOS VALUEERROR????
    """




