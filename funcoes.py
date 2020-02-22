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


def copiaRefs(referencia, t_d):


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


def criaCaminho(referencia, t_d):
    if referencia == 'IndexError':
        return 'Nao foi possível interpretar o caminho inserido.'

    # Converte a lista do caminho em um caminho
    referencias = list()
    for refes in referencia:
        refs = '\\'.join(refes[:-1])
        referencias.append(refs)
    # print(referencias)
    # Junta para o caminho do User, e Cria os caminhos
    if t_d == 't':
        for refs in referencias:
            caminho = os.path.join('\\'.join(prefixUser), today, refs)
            # print(caminho)
            if not os.path.exists(caminho):
                os.makedirs(caminho)
    elif t_d == 'd':
        # print(t_d)
        for refs in referencias:
            # print(refs[:3])
            if refs[:3] == 'S2G':
                caminho = os.path.join('\\'.join(prefixTraS2G), refs[4:])
                # print(caminho)
                if not os.path.exists(caminho):
                    os.makedirs(caminho)
            elif refs[:3] == 'OQV':
                caminho = os.path.join('\\'.join(prefixTraOQV), refs[4:])
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
        # print(referencias)
        return referencias
    except IndexError:
        print('IndexError')
    return 'IndexError'

sec = '''VERAO 20	ADIDAS	2020	157ART12Verde	MODELO E STILL	OQV
Inverno 20	nike	8098	bshabshabsh	MODELO E STILL	OQV'''

criaCaminho(listaCaminho(sec), 'd')
copiaRefs(listaCaminho(sec), 'd')
# mapeiaPastas()
# Teste
