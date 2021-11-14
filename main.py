from functools import reduce

#### Prado Dim Horizontal X Dim Vertical Y

### TAD

#def cria_PRADOTTTT(x: int, y: int):


    #if type(x) != int or type(y) != int or x < 2 or y < 2:
    #    raise ValueError("cria_posicao: argumentos invalidos")

    #lst = []

    #for j in range(len(y)):
    #    lst.append([0]*(x))


#### TAD POSICAO


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


######   TAD ANIMAL

def cria_animal(especie, repro, comida):
    """
    cria_animal: str x int x int -> animal
    esta funcao cria um animal com base nos argumentos dados (especie, frequencia de reproducao e de alimentacao)
    """

    if not especie or repro <= 0 or comida < 0:
        raise ValueError("cria_animal: argumentos invalidos")


    animal = {"especie": especie, "repro": [0,repro], "idade": 0}

    if comida != 0:
        animal["comida"] = [0, comida]
        animal["tipo"] = "predador"
    else:
        animal["tipo"] = "presa"

    return animal


def cria_animal_copia(animal):
    """
    cria_copia_animal: animal -> animal
    cria uma copia de um animal
    """

    animal_novo = {key: animal[key] for key in animal}
    try:
        animal_novo["comida"] = animal_novo["comida"][:]
    except KeyError:
        pass
    finally:
        animal_novo["repro"] = animal_novo["repro"][:]

    return animal_novo


def obter_especie(animal):
    """
    obter_especie: animal -> str
    devolve a especie de um animal
    """

    return animal["especie"]



def obter_freq_reproducao(animal):
    """
    obter_freq_reproducao: animal -> int
    retorna a frequencia de reproducao de um animal
    """

    return animal["repro"][1]


def obter_freq_alimentacao(animal):
    """
    obter_freq_alimentacao: animal -> int
    retorna a frequencia de alimentacao de um animal
    """
    try:
        return animal["comida"][1]
    except KeyError:
        return 0

def obter_idade(animal):
    """
    obter_idade: animal -> int
    devolve a idade do animal
    """

    return animal["idade"]


def obter_fome(animal):
    """
    obter_fome: animal -> int
    retorna a fome do animal
    """
    try:
        return animal["comida"][0]
    except KeyError:
        return 0

def aumenta_idade(animal):
    """
    aumenta_idade: animal -> animal
    devolve o animal com a idade incrementada por 1
    """
    animal["idade"] += 1

    return animal


def reset_idade(animal):
    """
    reset_idade: animal -> animal
    devolve o animal com a idade definida a 0
    """

    animal["idade"] = 0

    return animal

def aumenta_fome(animal):
    """
    aumenta_fome: animal -> animal
    devolve o animal com a fome incrementada por 1 se este for um predador, caso contrario devolve o animal
    """
    try:
        animal["comida"][0] += 1
    except KeyError:
        pass
    return animal


def reset_fome(animal):
    """
    reset_idade: animal -> animal
    devolve o animal com a fome definifa a 0 se este for um predador, caso contrario devolve o animal
    """
    try:
        animal["comida"][0] = 0
    except KeyError:
        pass

    return animal


def eh_animal(arg):
    def elementos_na_lista(arg: iter,lista: iter)-> bool:
        """
        retorna True se todos os elementos de arg estiverem contidos em lista
        """
        return reduce(lambda x, y: x and y, map(lambda x: x in lista, arg))

    if type(arg) != dict or not elementos_na_lista(arg,["tipo", "especie", "repro","idade","comida"]):
        return False

    ####### DEVE HAVER algo REDUNDANTE COM O CHECK EM CIMA E AS LENGTHS TOO BAD

    if not elementos_na_lista(["tipo", "especie", "repro", "idade"], arg) or not(len(arg) == 4 or len(arg) ==5):
        return False


    #### verificar tipo
    if arg["tipo"] == "predador":
        ### verificar comida
        if "comida" not in arg:
            return False
        elif type(arg["comida"]) != list or len(arg["comida"]) != 2 or type(arg["comida"][0]) != int or \
                type(arg["comida"][1]) != int or arg["comida"][0] < 0 or arg["comida"][1] <= 0:
            return False
    elif arg["tipo"] == "presa":
        if len(arg) != 4:
            return False
    else:
        return False

    ##verificar especie
    if type(arg["especie"]) != str or not arg["especie"]:
        return False

    # verificar isto e igual a verificar comida aparentemente
    if type(arg["repro"]) != list or len(arg["repro"]) != 2 or type(arg["repro"][0]) != int or \
            type(arg["repro"][1]) != int or arg["repro"][0] < 0 or arg["repro"][1] <= 0:
        return False


    ### verificar idade
    if type(arg["idade"]) != int or arg["idade"] < 0:
        return False

    return True

