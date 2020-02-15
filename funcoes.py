import os
import shutil
from datetime import date

def copiaRefs(referencia):

    hoje = date.today().strftime("%Y-%m-%d")
    today = f'Data - {hoje}'

    prefixOriS2G = 'C:\\Users\\Pablo\\Documents\\SandBox\\Sandbox Sys Icomm\\Servidor\\S2G\\Originais'.split('\\')
    prefixOriOQV = 'C:\\Users\\Pablo\\Documents\\SandBox\\Sandbox Sys Icomm\\Servidor\\Icommgroup\\OQV\\Originais'.split('\\')
    prefixUser = 'C:\\Users\\Pablo\\Documents\\SandBox\\Sandbox Sys Icomm\\Usuario\\Pablo Lucena'.split('\\')
    # print(prefixUser)
    prefixUserS2G = prefixUser + [today] + ['S2G']
    prefixUserOQV = prefixUser + [today] + ['OQV']
    # print(prefixUserS2G)
    # print(prefixUserOQV)
    try:
        for refs in referencia:
            if refs[0] == 'S2G':
                del refs[0]
                srcPath = '\\'.join(prefixOriS2G + refs)
                dstPath = '\\'.join(prefixUserS2G + refs)
                shutil.copytree(srcPath, dstPath)
                # print(f' dstPath {dstPath}')
                # print(f' srcPath {srcPath}')
            elif refs[0] == 'OQV':
                del refs[0]
                srcPath = '\\'.join(prefixOriOQV + refs)
                dstPath = '\\'.join(prefixUserOQV + refs)
                shutil.copytree(srcPath, dstPath)
                # print(f' dstPath {dstPath}')
                # print(f' srcPath {srcPath}')
            else:
                print('Nao foi possível interpretar o caminho inserido.')
                return 'Nao foi possível interpretar o caminho inserido.'
        return 'Tarefa Finalizada'
    except FileNotFoundError:
        print('Caminho não encontrado no servidor')
        return 'Caminho não encontrado no servidor'
    except FileExistsError:
        print('Caminho ja existente no seu Mac')
        return 'Caminho ja existente no seu Mac'


def criaCaminho(referencia):
    if referencia == 'IndexError':
        return 'Nao foi possível interpretar o caminho inserido.'
    # Pega a data de hoje
    hoje = date.today().strftime("%Y-%m-%d")
    today = f'Data - {hoje}'
    # print(today)
    # Converte a lista do caminho em um caminho
    referencias = list()
    for refes in referencia:
        refs = '\\'.join(refes[:-1])
        referencias.append(refs)
    # print(referencias)
    # Defino o prefixo do caminho do User
    prefixUser = 'C:\\Users\\Pablo\\Documents\\SandBox\\Sandbox Sys Icomm\\Usuario\\Pablo Lucena'
    # Junta para o caminho do User, e Cria os caminhos
    for refs in referencias:
        caminho = os.path.join(prefixUser, today, refs)
        # print(caminho)
        if not os.path.exists(caminho):
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
        print(referencias)
        return referencias
    except IndexError:
        print('IndexError')
    return 'IndexError'


# criaPastas()
# copiaPath()
# for ref in listaCaminho():
#     print(ref)
# criaCaminho(listaCaminho())
# copiaRefs(listaCaminho())
# mapeiaPastas()
# Teste
