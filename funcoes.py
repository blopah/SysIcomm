import os
import shutil
from datetime import date

hoje = date.today().strftime("%Y-%m-%d")
today = f'Data - {hoje}'

prefixOriS2G = 'C:\\Users\\Pablo\\Documents\\SandBox\\Sandbox Sys Icomm\\Servidor\\S2G\\Originais'.split('\\')
prefixOriOQV = 'C:\\Users\\Pablo\\Documents\\SandBox\\Sandbox Sys Icomm\\Servidor\\Icommgroup\\OQV\\Originais'.split('\\')
prefixTraS2G = 'C:\\Users\\Pablo\\Documents\\SandBox\\Sandbox Sys Icomm\\Servidor\\S2G\\Tratadas'.split('\\')
prefixTraOQV = 'C:\\Users\\Pablo\\Documents\\SandBox\\Sandbox Sys Icomm\\Servidor\\Icommgroup\\OQV\\Tratadas'.split('\\')
prefixUser = 'C:\\Users\\Pablo\\Documents\\SandBox\\Sandbox Sys Icomm\\Usuario\\Pablo Lucena'.split('\\')
prefixUserS2G = prefixUser + [today] + ['S2G']
prefixUserOQV = prefixUser + [today] + ['OQV']

# print(prefixUserS2G)
# print(prefixUserOQV)
# print(prefixOriS2G)
# print(prefixOriOQV)
# print(prefixTraS2G)
# print(prefixTraOQV)

def checkpaths(referencia, t_d):
    if t_d == 't':
        #Checar caminhos da pasta originais do servidor
        #Checa todos os prefixos originais
        if os.path.exists('\\'.join(prefixOriOQV)):
            validPrefixOriOQV = True
        else:
            validPrefixOriOQV = False
        if os.path.exists('\\'.join(prefixOriS2G)):
            validPrefixOriS2G = True
        else:
            validPrefixOriS2G = False

        #Checa os caminhos completos, e os nao encontrados guarda em uma lista
        list_of_not_found_srcs = list()
        list_of_not_found_srcs_txt = ''
        for refs in referencia:
            if refs[0] == 'S2G':
                if not validPrefixOriS2G:
                    return ('O caminho para a pasta originais da S2G não existe', False)
                del refs[0]
                srcPath = '\\'.join(prefixOriS2G + refs)
                if not os.path.exists(srcPath):
                    list_of_not_found_srcs.append(srcPath)

            elif refs[0] == 'OQV':
                if not validPrefixOriOQV:
                    return ('O caminho para a pasta originais da OQV não existe', False)
                del refs[0]
                srcPath = '\\'.join(prefixOriOQV + refs)
                if not os.path.exists(srcPath):
                    list_of_not_found_srcs.append(f'\n {srcPath}')
        for listItems in list_of_not_found_srcs:
            list_of_not_found_srcs_txt += listItems
            print(list_of_not_found_srcs_txt)
        if not len(list_of_not_found_srcs) == 0:
            return ('Não foram enconstradas as seguintes pastas: \n{}'.format(list_of_not_found_srcs_txt), False)
        return ('Todos os caminhos das pastas foram encontrados.', True)
    elif t_d == 'd':
        # Checar caminhos do usuario
        # Checa todos os prefixos do usuario
        if os.path.exists('\\'.join(prefixUserOQV)):
            validPrefixUserOQV = True
        else:
            validPrefixUserOQV = False
        if os.path.exists('\\'.join(prefixUserS2G)):
            validPrefixUserS2G = True
        else:
            validPrefixUserS2G = False

        # Checa os caminhos completos, e os nao encontrados guarda em uma lista
        list_of_not_found_srcs = list()
        list_of_not_found_srcs_txt = ''
        for refs in referencia:
            if refs[0] == 'S2G':
                if not validPrefixUserS2G:
                    return ('O caminho para a pasta do usuario da S2G não existe', False)
                del refs[0]
                srcPath = '\\'.join(prefixUserS2G + refs)
                if not os.path.exists(srcPath):
                    list_of_not_found_srcs.append(srcPath)

            elif refs[0] == 'OQV':
                if not validPrefixUserOQV:
                    return ('O caminho para a pasta do usuario da OQV não existe', False)
                del refs[0]
                srcPath = '\\'.join(prefixUserOQV + refs)
                if not os.path.exists(srcPath):
                    list_of_not_found_srcs.append(f'\n {srcPath}')
        for listItems in list_of_not_found_srcs:
            list_of_not_found_srcs_txt += listItems
            print(list_of_not_found_srcs_txt)
        if not len(list_of_not_found_srcs) == 0:
            return ('Não foram enconstradas as seguintes pastas: \n{}'.format(list_of_not_found_srcs_txt), False)
        return ('Todos os caminhos das pastas foram encontrados.', True)


def copiaRefs(referencia, t_d):

    if t_d == 't':
        list_of_not_found_srcs = list()
        list_of_not_found_dsts = list()
        list_of_not_found_srcs_txt = ''
        list_of_not_found_dsts_txt = ''
        for refs in referencia:
            srcPath = ''
            dstPath = ''
            try:
                if refs[0] == 'S2G':
                    del refs[0]
                    srcPath = '\\'.join(prefixOriS2G + refs)
                    dstPath = '\\'.join(prefixUserS2G + refs)
                    shutil.copytree(srcPath, dstPath)
                    # print(f' dstPath {dstPath}')
                    # print(f' srcPath {srcPath}')

                elif refs[0] == 'OQV':
                    # print('refs[0] = OQV')
                    del refs[0]
                    srcPath = '\\'.join(prefixOriOQV + refs)
                    dstPath = '\\'.join(prefixUserOQV + refs)
                    shutil.copytree(srcPath, dstPath)
                    # print(f' dstPath {dstPath}')
                    # print(f' srcPath {srcPath}')
                else:
                    print('Nao foi possível interpretar se o caminho é para S2G ou OQV')
                    return 'Nao foi possível interpretar se o caminho é para S2G ou OQV.'
            except FileNotFoundError:
                list_of_not_found_srcs.append(f'\n {srcPath}')
                continue
            except FileExistsError:
                list_of_not_found_dsts.append(f'\n {dstPath}')
                continue
        for listItems in list_of_not_found_srcs:
            list_of_not_found_srcs_txt += listItems
            print(list_of_not_found_srcs_txt)
        for listItems in list_of_not_found_dsts:
            list_of_not_found_dsts_txt += listItems
            print(list_of_not_found_dsts_txt)
        if len(list_of_not_found_srcs) == 0 and len(list_of_not_found_dsts) == 0:
            return 'Tarefa Finalizada0\n'
        elif not len(list_of_not_found_srcs) == 0 and not len(list_of_not_found_dsts) == 0:
            return 'Tarefa Finalizada1 \nCaminhos não encontrados no servidor: {} \nCaminho ja existente no seu Mac: \n {}'.format(list_of_not_found_srcs_txt, list_of_not_found_dsts_txt)
        elif not len(list_of_not_found_srcs) == 0:
            return 'Tarefa Finalizada2 \nCaminhos não encontrados no servidor: \n {}'.format(list_of_not_found_srcs_txt)
        elif not len(list_of_not_found_dsts) == 0:
            return 'Tarefa Finalizada3 \nCaminhos ja existentes no seu Mac: \n {}'.format(list_of_not_found_dsts_txt)


    elif t_d == 'd':
        list_of_not_found_srcs = list()
        list_of_not_found_dsts = list()
        list_of_not_found_srcs_txt = ''
        list_of_not_found_dsts_txt = ''
        for refs in referencia:
            srcPath = ''
            dstPath = ''
            try:
                if refs[0] == 'S2G':
                    del refs[0]
                    srcPath = '\\'.join(prefixUserS2G + refs)
                    dstPath = '\\'.join(prefixTraS2G + refs)
                    shutil.copytree(srcPath, dstPath)
                    # print(f' dstPath {dstPath}')
                    # print(f' srcPath {srcPath}')

                elif refs[0] == 'OQV':
                    # print('refs[0] = OQV')
                    del refs[0]
                    srcPath = '\\'.join(prefixUserOQV + refs)
                    dstPath = '\\'.join(prefixTraOQV + refs)
                    shutil.copytree(srcPath, dstPath)
                    # print(f' dstPath {dstPath}')
                    # print(f' srcPath {srcPath}')
                else:
                    print('Nao foi possível interpretar se o caminho é para S2G ou OQV.')
                    return 'Nao foi possível interpretar se o caminho é para S2G ou OQV.'
            except FileNotFoundError:
                list_of_not_found_srcs.append(f'\n {srcPath}')
                continue
            except FileExistsError:
                list_of_not_found_dsts.append(f'\n {dstPath}')
                continue
        for listItems in list_of_not_found_srcs:
            list_of_not_found_srcs_txt += listItems
            print(list_of_not_found_srcs_txt)
        for listItems in list_of_not_found_dsts:
            list_of_not_found_dsts_txt += listItems
            print(list_of_not_found_dsts_txt)
        if len(list_of_not_found_srcs) == 0 and len(list_of_not_found_dsts) == 0:
            return 'Tarefa Finalizada0\n'
        elif not len(list_of_not_found_srcs) == 0 and not len(list_of_not_found_dsts) == 0:
            return 'Tarefa Finalizada1 \nCaminhos não encontrados no seu Mac: {} \nCaminho ja existente no servidor: \n {}'.format(list_of_not_found_srcs_txt, list_of_not_found_dsts_txt)
        elif not len(list_of_not_found_srcs) == 0:
            return 'Tarefa Finalizada2 \nCaminhos não encontrados no seu Mac: \n {}'.format(list_of_not_found_srcs_txt)
        elif not len(list_of_not_found_dsts) == 0:
            return 'Tarefa Finalizada3 \nCaminhos ja existentes no servidor: \n {}'.format(list_of_not_found_dsts_txt)


def criaCaminho(referencia, t_d):
    # print(f'cria caminho >')
    if referencia == 'IndexError':
        return 'Nao foi possível interpretar o caminho inserido.'

    # Converte a lista do caminho em um caminho
    referencias = list()
    for refes in referencia:
        refs = '\\'.join(refes[:-1])  # Esse '[:-1]' é para excluir a ultima pasta da referencia
        referencias.append(refs)
    # print(referencias)
    # Forma o caminho e Cria os caminhos
    # Em caso de 't'(take) só há 1 fluxo
    if t_d == 't':
        # print('td = t')
        for refs in referencias:
            caminho = os.path.join('\\'.join(prefixUser), today, refs)
            # print(caminho)
            if not os.path.exists(caminho):
                os.makedirs(caminho)
    # Em caso de 'd' (drop) há 2 fluxos possiveis
    elif t_d == 'd':
        # print('td = d >')
        for refs in referencias:
            # print(refs[:3])
            if refs[:3] == 'S2G':
                caminho = os.path.join('\\'.join(prefixTraS2G), refs[4:])
                # print(caminho)
                if not os.path.exists(caminho):
                    print('caminho nao existe. (ta ok)')
                    os.makedirs(caminho)
            elif refs[:3] == 'OQV':
                caminho = os.path.join('\\'.join(prefixTraOQV), refs[4:])
                # print(caminho)
                if not os.path.exists(caminho):
                    # print('caminho nao existe. (ta ok)')
                    os.makedirs(caminho)


def listaCaminho(secao):
#     secao = '''INVERNO 20	HAIGHT	1416	01030006_VERDECACT	MODELO E STILL	S2G
# INVERNO 20	HAIGHT	1416	01040006_VERDECACT	MODELO E STILL	S2G'''
    # print(secao)
    secaolist = secao.split('\n')
    # print(secaolist)
    secaolistref = list()
    for refe in secaolist:
        ref = refe.split('\t')  #Isso torna a linha, uma lista
        secaolistref.append(ref)  #Isso appends a lista que foi criada inteira.
        # print(secaolistref)
    # print('-' * 40)
    # print(secaolistref)
    referencias = list()
    try:
        for ref in secaolistref:
            ref.insert(0, ref[5])
            # print(f'{ref[:5]}')
            referencias.append(ref[:5])
        # print('-' * 40)
        # print(referencias)
        return referencias
    except IndexError:
        print('IndexError')
    return 'IndexError'

# sec = '''VERAO 20	ADIDAS	2020	157ART12Verde	MODELO E STILL	OQV
# Inverno 20	nike	8098	bshabs4absh	MODELO E STILL	OQV'''

# print(checkpaths(listaCaminho(sec), 't'))

# criaCaminho(listaCaminho(sec), 'd')
# copiaRefs(listaCaminho(sec), 'd')
# mapeiaPastas()
# Testee
