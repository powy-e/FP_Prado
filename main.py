"""
Fundamentos da Programacao
Projeto 2 - O Prado

Eduardo Nazário - 102415
eduardo.nazario@tecnico.ulisboa.pt
"""

"""
TAD Posicao:

Operacoes basicas:
    Construtores:
        -cria_posicao: int x int -> posicao
        -cria_copia_posicao: posicao -> posicao
    Seletores:
        -obter_pos_x: posicao -> int
        -obter_pos_y: posicao -> int
    Reconhecedor:
        -eh_posicao: universal -> booleano
    Teste:
        -posicoes_iguais: posicao x posicao -> booleano
    Transformador:
        -posicao_para_str: posicao -> str

Funcoes de Alto Nivel:
    - obter_posicoes_adjacentes: posicao -> tuplo
    - ordenar_posicoes: tuplo -> tuplo
    - posicoes_iguais_rapida: posicao x posicao -> bool

Esta TAD utiliza como representacao interna tuplos 
"""


def cria_posicao(x: int, y: int):
    """
    cria_posicao: int x int -> posicao
    esta funcao cria uma posicao a partir de dois inteiros positivos
    """
    if type(x) != int or type(y) != int or x < 0 or y < 0:
        raise ValueError("cria_posicao: argumentos invalidos")

    return (x, y)


def cria_copia_posicao(pos):
    """
    cria_copia_posicao: posicao -> posicao
    esta funcao cria uma copia de uma posicao
    """
    if not eh_posicao(pos):
        raise ValueError("cria_copia_posicao: argumentos invalidos")

    return cria_posicao(pos[0], pos[1])


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

    return isinstance(arg, tuple) and len(arg) == 2 and isinstance(obter_pos_y(arg), int) \
           and isinstance(obter_pos_x(arg), int) and obter_pos_y(arg) >= 0 and obter_pos_x(arg) >= 0


def posicoes_iguais(p1, p2):
    """
    posicoes_iguais: posicao x posicao -> booleano
    devolve True se p1 e p2 sao posicoes iguais
    """

    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2


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
        adj_pos += ((cria_posicao(x, y - 1)),)

    adj_pos += (cria_posicao(x + 1, y), cria_posicao(x, y + 1))

    if x != 0:
        adj_pos += (cria_posicao(x - 1, y),)

    return adj_pos


def ordenar_posicoes(tup):
    """
    ordenar_posicoes: tuplo -> tuplo
    retorna o tuplo original ordenado
    """
    lst = list(tup)
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i + 1, len(lst)):  # procura o menor elemento da lista
            if obter_pos_y(lst[j]) < obter_pos_y(lst[min_index]):
                min_index = j
            elif obter_pos_y(lst[j]) == obter_pos_y(lst[min_index]):
                if obter_pos_x(lst[j]) < obter_pos_x(lst[min_index]):
                    min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return tuple(lst)


def posicoes_iguais_rapida(p1, p2) -> bool:
    """
    posicoes_iguais_rapida: posicao x posicao -> bool
    Funcao mais rapida para igualar posicoes,
    requer assumir que p1 e p2 sejam posicoes
    """

    return obter_pos_y(p1) == obter_pos_y(p2) and obter_pos_x(p1) == obter_pos_x(p2)


"""
TAD Animal:

operacoes basicas:
    Construtores:
        -cria_animal: str x int x int -> animal
        -cria_copia_animal: animal -> animal
    Seletores:
        -obter_especie: animal -> str
        -obter_freq_reproducao: animal -> int
        -obter_freq_alimentacao: animal -> int
        -obter_idade: animal -> int
        -obter_fome: animal -> int
    Modificadores:
        -aumenta_idade: animal -> animal
        -reset_idade: animal -> animal
        -aumenta_fome: animal -> animal
        -reset_fome: animal -> animal
    Reconhecedores:
        -eh_animal: universal -> booleano
        -eh_predador: universal -> booleano
        -eh_presa: universal -> booleano
    Teste:
        -animais_iguais: animal x animal -> booleano
    Transformadores:    
        -animal_para_char: animal -> str
        -animal_para_str: animal -> str
        
Funcoes Alto Nivel:
    -eh_animal_fertil: animal -> booleano
    -eh_animal_faminto: animal -> booleano
    -reproduz_animal: animal -> animal


TAD animal utiliza dicionarios como representacao interna
"""


def cria_animal(especie, repro, comida):
    """
    cria_animal: str x int x int -> animal
    esta funcao cria um animal com base nos argumentos dados (especie, frequencia de reproducao e de alimentacao)
    """

    # validacao de elementos
    if type(especie) != str or type(repro) != int or type(comida) != int or \
            not especie or repro <= 0 or comida < 0:
        raise ValueError("cria_animal: argumentos invalidos")

    # Cria o dicionario
    animal = {"especie": especie, "repro": [0, repro]}

    # Classifica o animal
    if comida != 0:
        animal["comida"] = [0, comida]
        animal["tipo"] = "predador"
    else:
        animal["tipo"] = "presa"

    return animal


def cria_copia_animal(animal):
    """
    cria_copia_animal: animal -> animal
    cria uma copia de um animal
    """

    # Validacao de argumento
    if not eh_animal(animal):
        raise ValueError("cria_copia_animal: argumentos invalidos")

    # Fazer copia dos elementos (shallow)
    animal_novo = {key: animal[key] for key in (animal)}

    # Fazer copia dos dicionarios
    if animal_novo["tipo"] == "predador":
        animal_novo["comida"] = animal_novo["comida"][:]
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

    if animal["tipo"] == "predador":
        return animal["comida"][1]
    return 0


def obter_idade(animal):
    """
    obter_idade: animal -> int
    devolve a idade do animal
    """

    return animal["repro"][0]


def obter_fome(animal):
    """
    obter_fome: animal -> int
    retorna a fome do animal
    """

    if animal["tipo"] == "predador":
        return animal["comida"][0]
    return 0


def aumenta_idade(animal):
    """
    aumenta_idade: animal -> animal
    devolve o animal com a idade incrementada por 1
    """

    animal["repro"][0] += 1

    return animal


def reset_idade(animal):
    """
    reset_idade: animal -> animal
    devolve o animal com a idade definida a 0
    """

    animal["repro"][0] = 0

    return animal


def aumenta_fome(animal):
    """
    aumenta_fome: animal -> animal
    devolve o animal com a fome incrementada por 1 se este for um predador, caso contrario devolve o animal
    """

    if animal["tipo"] == "predador":
        animal["comida"][0] += 1

    return animal


def reset_fome(animal):
    """
    reset_fome: animal -> animal
    devolve o animal com a fome definifa a 0 se este for um predador, caso contrario devolve o animal
    """

    if animal["tipo"] == "predador":
        animal["comida"][0] = 0

    return animal


def eh_animal(arg):
    """
    eh_animal: universal -> booleano
    Esta funcao verifica se o argumento passado corresponde a um animal
    """
    # Valida Argumentos
    if type(arg) != dict or not all(map(lambda x: x in ["tipo", "especie", "repro", "comida"], arg)) or \
            not all(map(lambda x: x in arg, ["tipo", "especie", "repro"])):
        return False

    # Verificar tipo
    if arg["tipo"] == "predador":
        # Verificar comida
        if "comida" in arg:
            if type(arg["comida"]) != list or len(arg["comida"]) != 2 or type(arg["comida"][0]) != int or \
                    type(arg["comida"][1]) != int or arg["comida"][0] < 0 or arg["comida"][1] <= 0:
                return False
        else:
            return False

    elif arg["tipo"] == "presa":
        if len(arg) != 3:
            return False
    else:
        return False

    # Verificar especie
    if type(arg["especie"]) != str or not arg["especie"]:
        return False

    # Idade/Reproducao
    if type(arg["repro"]) != list or len(arg["repro"]) != 2 or type(arg["repro"][0]) != int or \
            type(arg["repro"][1]) != int or arg["repro"][0] < 0 or arg["repro"][1] <= 0:
        return False

    return True


def eh_predador(arg):
    """
    eh_predador: universal -> booleano
    retorna True se for um predador
    """

    return eh_animal(arg) and arg["tipo"] == "predador"


def eh_presa(arg):
    """
    eh_presa: universal -> booleano
    retorna True se for uma presa
    """

    return eh_animal(arg) and arg["tipo"] == "presa"


def animais_iguais(animal_1, animal_2):
    """
    animais_iguais: animal x animal -> booleano
    devolve True apenas se a1 e a2 sao animais e sao iguais.
    """

    return eh_animal(animal_1) and eh_animal(animal_2) and animal_1 == animal_2


def animal_para_char(animal):
    """
    animal_para_char: animal -> str
    devolve uma string do primeiro caracter correspondente a especie do animal, em maiuscula se for Predador,
    minuscula se for presa
    """

    if animal["tipo"] == "predador":
        return animal["especie"][0].upper()
    else:
        return animal["especie"][0].lower()


def animal_para_str(animal):
    """
    animal_para_str: animal -> cadeia de caracteres
    devolve o animal em formato de string
    """

    if eh_predador(animal):
        string = f"{obter_especie(animal)} [{obter_idade(animal)}/{obter_freq_reproducao(animal)};\
{obter_fome(animal)}/{obter_freq_alimentacao(animal)}]"
    else:
        string = f"{obter_especie(animal)} [{obter_idade(animal)}/{obter_freq_reproducao(animal)}]"

    return string


 ### ALTO NIVEl

def eh_animal_fertil(animal):
    """
    eh_animal_fertil: animal -> booleano
    retorna True se o animal atingiu a idade fertil
    """

    return obter_idade(animal) == obter_freq_reproducao(animal)


def eh_animal_faminto(animal):
    """
    eh_animal_faminto: animal -> booleano
    retorna true se o animal tiver fome maior que a sua frequencia de alimentacao
    """

    if eh_predador(animal):
        return obter_fome(animal) >= obter_freq_alimentacao(animal)
    else:
        return False


def reproduz_animal(animal):
    """
    reproduz_animal: animal -> animal
    retorna um novo animal baseado nas caracteristicas do animal fornecido como argumento mas com idade e fome a 0,
    a idade do animal fornecido como argumento passa a 0
    """

    reset_idade(animal)
    animal_novo = cria_copia_animal(animal)
    if eh_predador(animal_novo):
        reset_fome(animal_novo)

    return animal_novo


"""
TAD Prado:

operacoes basicas:
    Construtores:
        -cria_prado: posicao x tuplo x tuplo x tuplo -> prado
        -cria_copia_prado: prado -> prado
    Seletores:
        -obter_tamanho_x: prado -> int
        -obter_tamanho_y: prado -> int
        -obter_numero_predadores: prado -> int
        -obter_numero_presas: prado -> int
        -obter_posicao_animais: prado -> tuplo posicoes
        -obter_animal: prado x posicao -> animal
    Modificadores:
        -eliminar_animal: prado x posicao -> prado
        -mover_animal: prado x posicao x posicao -> prado
        -inserir_animal: prado x animal x posicao -> prado
    Reconhecedores:    
        -eh_prado: universal -> booleano
        -eh_posicao_animal: prado x posicao -> booleano
        -eh_posicao_obstaculo: prado x posicao -> booleano
        -eh_posicao_livre: prado x posicao -> booleano
    Teste:
        -prados_iguais: prado x prado -> booleano
    Transformador:
        -prado_para_str: prado -> str

Este TAD utiliza como representacao interna uma lista
"""


def verificar_rochas_animais(limite, rochas, ani_pos) -> bool:
    """
    funcao auxiliar
    verificar_rochas_animais: pos x tuplo x tuplo
    esta funcao retorna True se todas as rochas/animais se encontram dentro dos
                                                                        limites
    """

    if rochas:
        for rochedo in rochas:
            if not (0 < obter_pos_x(rochedo) < obter_pos_x(limite)) \
                    or not (0 < obter_pos_y(rochedo) < obter_pos_y(limite)):
                return False
            for animal in ani_pos:
                if not (0 < obter_pos_x(animal) < obter_pos_x(limite)) \
                        or not (0 < obter_pos_y(animal) < obter_pos_y(limite)) \
                        or posicoes_iguais(animal, rochedo):
                    return False
    else:
        for animal in ani_pos:
            if not (0 < obter_pos_x(animal) < obter_pos_x(limite)) \
                    or not (0 < obter_pos_y(animal) < obter_pos_y(limite)):
                return False
    return True


def cria_prado(limite, rochas, animais, ani_pos):
    """
    cria_prado: posicao x tuplo x tuplo x tuplo -> prado
    retorna um prado
    """

    # Validacao de Argumentos
    if not eh_posicao(limite) or type(rochas) != tuple or any(map(lambda x: not eh_posicao(x), rochas)) or \
            type(animais) != tuple or not animais or any(map(lambda x: not eh_animal(x), animais)) or \
            type(ani_pos) != tuple or len(ani_pos) != len(animais) or any(map(lambda x: not eh_posicao(x), ani_pos)) \
            or not verificar_rochas_animais(limite, rochas, ani_pos):
        raise ValueError("cria_prado: argumentos invalidos")

    lista_animais = []
    for i in range(len(animais)):
        lista_animais.append([animais[i], ani_pos[i]])

    prado = [limite, rochas, lista_animais]

    return prado


def cria_copia_prado(prado):
    """
    cria_copia_prado: prado -> prado
    retorna uma copia do prado
    """

    if not eh_prado(prado):
        raise ValueError("cria_copia_prado: argumentos invalidos")

    novo_prado = [
        cria_copia_posicao(prado[0]),
        tuple([cria_copia_posicao(x) for x in prado[1]]),
        [[cria_copia_animal(prado[2][x][0]), cria_copia_posicao(prado[2][x][1])] for x in range(len(prado[2]))]
    ]

    return novo_prado


def obter_tamanho_x(prado):
    """
    obter_tamanho_x: prado -> int
    devolve a dimensao X do prado
    """

    return obter_pos_x(prado[0]) + 1


def obter_tamanho_y(prado):
    """
    obter_tamanho_y: prado -> int
    devolve a dimensao Y do prado
    """

    return obter_pos_y(prado[0]) + 1


def obter_numero_predadores(prado):
    """
    obter_numero_predadores: prado -> int
    retorna o numero de predadores no prado
    """

    return len(tuple(filter(lambda animal: eh_predador(animal), map(lambda x: x[0], prado[2]))))


def obter_numero_presas(prado):
    """
    obter_numero_presas: prado -> int
    retorna o numero de presas no prado
    """
    return len(tuple(filter(lambda animal: eh_presa(animal), map(lambda x: x[0], prado[2]))))


def obter_posicao_animais(prado):
    """
    obter_posicao_animais: prado -> tuplo posicoes
    devolve um tuplo com as posicoes do prado ocupadas por animais,
     ordenadas em ordem de leitura do prado.
    """
    ani_pos = []
    for animal in prado[2]:
        ani_pos.append(animal[1])

    return ordenar_posicoes(ani_pos)


def obter_animal(prado, pos):
    """
    obter_animal: prado x posicao -> animal
    devolve o animal que esta na posicao pos
    """

    for animal in prado[2]:  # posicoes_iguais e uma funcao muito cara
        if posicoes_iguais_rapida(pos, animal[1]):
            return animal[0]


def eliminar_animal(prado, pos):
    """
    eliminar_animal: prado x posicao -> prado
    retorna o prado com a posicao, onde se encontrava o animal, livre
    """

    for animal in prado[2]:
        if posicoes_iguais_rapida(pos, animal[1]):
            prado[2].remove(animal)
            break

    return prado


def mover_animal(prado, pos_antiga, pos):
    """
    mover animal: prado x posicao x posicao -> prado
    modifica o prado, movendo o animal da posicao antiga para a posicao nova, deixando a posicao
    antiga livre
    """

    for animal in prado[2]:
        if posicoes_iguais_rapida(pos_antiga, animal[1]):
            animal[1] = pos
            break

    return prado


def inserir_animal(prado, animal, pos):
    """
    inserir_animal: prado x animal x posicao -> prado
    retorna o prado com um animal na posicao pos
    """

    prado[2].append([animal, pos])

    return prado


def eh_prado(arg):
    """
    eh_prado: universal -> booleano
    Devolve True se o argumento passado for do TAD prado
    """

    if type(arg) != list or len(arg) != 3 or not eh_posicao(arg[0]) or type(arg[1]) != tuple or \
            any(map(lambda x: not eh_posicao(x), arg[1])) or type(arg[2]) != list or \
            any(map(lambda x: not eh_animal(x[0]) or not eh_posicao(x[1]), arg[2])) or \
            not verificar_rochas_animais(arg[0], arg[1], map(lambda x: x[1], arg[2])):
        return False

    return True


def eh_posicao_animal(prado, pos):
    """
    eh_posicao_animal: prado x posicao -> booleano
    Devolve True caso a posicao do prado esteja ocupada por um animal.
    """

    for animal in prado[2]:
        if posicoes_iguais_rapida(animal[1], pos):
            return True

    return False


def eh_posicao_obstaculo(prado, pos):
    """
    eh_posicao_obstaculo: prado x posicao -> booleano
    Devolve True caso a posicao do prado esteja ocupada por um obstaculo.
    """

    return obter_pos_x(pos) == 0 or obter_pos_y(pos) == 0 \
           or obter_pos_x(pos) == obter_tamanho_x(prado) - 1 or obter_pos_y(pos) == obter_tamanho_y(prado) - 1 \
           or any(map(lambda rochedo: posicoes_iguais_rapida(rochedo, pos), prado[1]))


def eh_posicao_livre(prado, pos):
    """
    eh_posicao_livre: prado x posicao -> booleano
    Devolve True caso a posicao do prado nao esteja ocupada por nada.
    """

    return not eh_posicao_animal(prado, pos) and not eh_posicao_obstaculo(prado, pos)


def prados_iguais(prado1, prado2):
    """
    prados_iguais: prado x prado -> booleano
    devolve True se os prados forem prados e forem iguais
    """

    if eh_prado(prado1) and eh_prado(prado2) and obter_tamanho_y(prado1) == obter_tamanho_y(prado2) \
            and obter_tamanho_x(prado1) == obter_tamanho_x(prado1):

        # Verifica se os rochedos sao iguas

        pos_prado1 = ordenar_posicoes(prado1[1])
        pos_prado2 = ordenar_posicoes(prado2[1])
        if len(pos_prado1) != len(pos_prado2):
            return False
        for i in range(len(pos_prado1)):
            if not posicoes_iguais(pos_prado1[i], pos_prado2[i]):
                return False

        # Verificar os animais e as suas posicoes

        if len(prado1[2]) != len(prado2[2]):
            return False

        for animal1 in prado1[2]:  # por animal
            passa_prox = False
            for animal2 in prado2[2]:
                if posicoes_iguais(animal1[1], animal2[1]) and animais_iguais(animal1[0], animal2[0]):
                    passa_prox = True
                    break
            if not passa_prox:
                return False
    else:
        return False

    return True


def prado_para_str(prado):
    """
    prado_para_str: prado -> str
    devolve uma string que representa o prado
    """

    prado_str = ""
    borda = "+" + "-" * (obter_tamanho_x(prado) - 2) + "+"
    prado_str += borda + "\n"
    for i in range(obter_tamanho_y(prado) - 2):
        prado_str += "|" + "." * (obter_tamanho_x(prado) - 2) + "|" + "\n"

    prado_str += borda

    for animal in obter_posicao_animais(prado):
        pos = obter_pos_y(animal) * (obter_tamanho_x(prado) + 1) + obter_pos_x(animal)
        prado_str = prado_str[:pos] + animal_para_char(obter_animal(prado, animal)) + prado_str[pos + 1:]

    for rochedo in prado[1]:
        pos = obter_pos_y(rochedo) * (obter_tamanho_x(prado) + 1) + obter_pos_x(rochedo)
        prado_str = prado_str[:pos] + "@" + prado_str[pos + 1:]

    return prado_str


##alto nivel


def obter_valor_numerico(prado, pos):
    """
    obter_valor_numerico: prado x posicao -> int
    retorna o numero da posicao que corresponde a ordem de leitura no prado.
    """

    return obter_tamanho_x(prado) * obter_pos_y(pos) + obter_pos_x(pos)


def obter_movimento(prado, pos):
    """
    obter_movimento: prado x posicao -> posicao
    retorna a posicao seguinte do animal na posicao de acordo com as regras de movimento dos animais.
    """

    possibilidades = [x for x in obter_posicoes_adjacentes(pos) if not eh_posicao_obstaculo(prado, x)]

    if possibilidades:  # Animal pode-se movimentar
        if eh_predador(obter_animal(prado, pos)):  # animal e predador
            novas_poss = tuple(filter(lambda n_p: not eh_posicao_livre(prado, n_p)
                                                  and eh_presa(obter_animal(prado, n_p)), possibilidades))
            if novas_poss:  # verifica se existem presas ao redor do animal
                return novas_poss[obter_valor_numerico(prado, pos) % len(novas_poss)]

        # caso seja presa ou nao existam presas ao redor do predador

        novas_poss = tuple(filter(lambda x: eh_posicao_livre(prado, x), possibilidades))
        if novas_poss:
            return novas_poss[obter_valor_numerico(prado, pos) % len(novas_poss)]

    return pos


def geracao(prado):
    """
    geracao: prado -> prado
     funcao auxiliar que modifica o prado fornecido como argumento,
    de acordo com a evolucao correspondente a uma geracao completa, devolvendo o prado
    """

    posicoes = list(obter_posicao_animais(prado))

    while posicoes:
        pos = posicoes[0]  # escolhe a primeira posicao
        animal = obter_animal(prado, pos)  # pega no animal dessa posicao

        if not eh_animal_fertil(animal):
            aumenta_idade(animal)  # aumenta a idade

        mov = obter_movimento(prado, pos)  # calcula o movimento que o animal devera efetuar
        mexe = not posicoes_iguais(mov, pos)

        if eh_predador(animal):  # verifica se e predador
            aumenta_fome(animal)  # aumenta a fome do predador
            if mexe and eh_posicao_animal(prado, mov):  # se existir uma presa
                eliminar_animal(prado, mov)

                for posicao in posicoes:
                    if posicoes_iguais(mov, posicao):
                        posicoes.remove(posicao)
                        break

                reset_fome(animal)

        if eh_animal_faminto(animal):
            eliminar_animal(prado, pos)
        elif mexe:
            mover_animal(prado, pos, mov)

        if eh_animal_fertil(animal) and mexe:
            inserir_animal(prado, reproduz_animal(animal), pos)
            reset_idade(animal)

        posicoes = posicoes[1:]

    return prado


def simula_ecossistema(fich: str, geracoes, v: bool) -> tuple:
    """
    simula_ecossistema: str x int x booleano -> tuplo

    esta simula o ecossistema, retornando um tuplo contendo o
    numero de presas e predadores da ultima geracao
    """

    # Ler Ficheiro

    with open(fich, "r") as ficheiro:
        canto = eval(ficheiro.readline())
        rochas = eval(ficheiro.readline())
        animais = [eval(linha) for linha in ficheiro.readlines()]

    # Criar Prado

    prado = cria_prado(
        cria_posicao(canto[0], canto[1]),
        tuple(map(lambda x: (cria_posicao(x[0], x[1])), rochas)),
        tuple(map(lambda x: (cria_animal(x[0], x[1], x[2])), animais)),
        tuple(map(lambda x: (cria_posicao(x[3][0], x[3][1])), animais))
    )

    # Executar as Geracoes

    ultimos_pred = obter_numero_predadores(prado)
    ultimas_presas = obter_numero_presas(prado)
    print(F"Predadores: {ultimos_pred} vs Presas: {ultimas_presas} (Gen. 0)")
    print(prado_para_str(prado))

    if v:  # Verboso
        for g in range(geracoes):
            geracao(prado)

            presas = obter_numero_presas(prado)
            predadores = obter_numero_predadores(prado)
            if presas != ultimas_presas or predadores != ultimos_pred:
                ultimos_pred = predadores
                ultimas_presas = presas
                print(F"Predadores: {predadores} vs Presas: {presas} (Gen. {g + 1})")
                print(prado_para_str(prado))
    else:  # Quiet
        for g in range(geracoes):
            geracao(prado)

        presas = obter_numero_presas(prado)
        predadores = obter_numero_predadores(prado)
        print(f"Predadores: {predadores} vs Presas: {presas} (Gen. {geracoes})")
        print(prado_para_str(prado))

    return predadores, presas
