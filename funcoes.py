import os
import shutil
from datetime import date

hoje = date.today().strftime("%Y-%m-%d")
today = f'Data - {hoje}'

prefix_ori_S2G = 'C:\\Users\\Pablo\\Documents\\SandBox\\Sandbox Sys Icomm\\Servidor\\S2G\\Originais'.split('\\')
prefix_ori_OQV = 'C:\\Users\\Pablo\\Documents\\SandBox\\Sandbox Sys Icomm\\Servidor\\Icommgroup\\OQV\\Originais'.split('\\')
prefix_tra_S2G = 'C:\\Users\\Pablo\\Documents\\SandBox\\Sandbox Sys Icomm\\Servidor\\S2G\\Tratadas'.split('\\')
prefix_tra_OQV = 'C:\\Users\\Pablo\\Documents\\SandBox\\Sandbox Sys Icomm\\Servidor\\Icommgroup\\OQV\\Tratadas'.split('\\')
prefix_user = 'C:\\Users\\Pablo\\Documents\\SandBox\\Sandbox Sys Icomm\\Usuario\\Pablo Lucena'.split('\\')
prefix_user_S2G = prefix_user + [today] + ['S2G']
prefix_user_OQV = prefix_user + [today] + ['OQV']

def check_paths(reference, t_d):

    """
    :param reference: receives what is returned by the list_way function
    :param t_d: arg that defines if it is a take or a drop operation
    :return: returns the result of the verification of all paths and prefixes
    """
    if t_d == 't':
        # Checks original's paths from server
        # Checks all original's prefixes
        if os.path.exists('\\'.join(prefix_ori_OQV)):
            validprefix_ori_OQV = True
        else:
            validprefix_ori_OQV = False
        if os.path.exists('\\'.join(prefix_ori_S2G)):
            validprefix_ori_S2G = True
        else:
            validprefix_ori_S2G = False

        # Checks each complete path, and if that is not found, is saved in a list
        list_of_not_found_srcs = list()
        list_of_not_found_srcs_txt = ''
        for refs in reference:
            if refs[0] == 'S2G':
                if not validprefix_ori_S2G:
                    return ('O caminho para a pasta originais da S2G não existe', False)
                del refs[0]
                src_path = '\\'.join(prefix_ori_S2G + refs)
                if not os.path.exists(src_path):
                    list_of_not_found_srcs.append(src_path)

            elif refs[0] == 'OQV':
                if not validprefix_ori_OQV:
                    return ('O caminho para a pasta originais da OQV não existe', False)
                del refs[0]
                src_path = '\\'.join(prefix_ori_OQV + refs)
                if not os.path.exists(src_path):
                    list_of_not_found_srcs.append(f'\n {src_path}')
        for list_items in list_of_not_found_srcs:
            list_of_not_found_srcs_txt += list_items
            print(list_of_not_found_srcs_txt)
        if not len(list_of_not_found_srcs) == 0:
            return ('Não foram enconstradas as seguintes pastas: \n{}'.format(list_of_not_found_srcs_txt), False)
        return ('Todos os caminhos das pastas foram encontrados.', True)
    elif t_d == 'd':
        # Checks user's local paths
        # Checks all user's prefixes
        if os.path.exists('\\'.join(prefix_user_OQV)):
            validprefix_user_OQV = True
        else:
            validprefix_user_OQV = False
        if os.path.exists('\\'.join(prefix_user_S2G)):
            validprefix_user_S2G = True
        else:
            validprefix_user_S2G = False

        # Checks each complete path, and if that is not found, is saved in a list
        list_of_not_found_srcs = list()
        list_of_not_found_srcs_txt = ''
        for refs in reference:
            if refs[0] == 'S2G':
                if not validprefix_user_S2G:
                    return ('O caminho para a pasta do usuario da S2G não existe', False)
                del refs[0]
                src_path = '\\'.join(prefix_user_S2G + refs)
                if not os.path.exists(src_path):
                    list_of_not_found_srcs.append(src_path)

            elif refs[0] == 'OQV':
                if not validprefix_user_OQV:
                    return ('O caminho para a pasta do usuario da OQV não existe', False)
                del refs[0]
                src_path = '\\'.join(prefix_user_OQV + refs)
                if not os.path.exists(src_path):
                    list_of_not_found_srcs.append(f'\n {src_path}')
        for list_items in list_of_not_found_srcs:
            list_of_not_found_srcs_txt += list_items
            print(list_of_not_found_srcs_txt)
        if not len(list_of_not_found_srcs) == 0:
            return ('Não foram enconstradas as seguintes pastas: \n{}'.format(list_of_not_found_srcs_txt), False)
        return ('Todos os caminhos das pastas foram encontrados.', True)


def copy_refs(reference, t_d):

    """
    :param reference: receives what is returned by the list_way function
    :param t_d: arg that defines if it is a take or a drop operation
    :return: copys the references from src_path to dst_path
    """

    if t_d == 't':
        list_of_not_found_srcs = list()
        list_of_not_found_dsts = list()
        list_of_not_found_srcs_txt = ''
        list_of_not_found_dsts_txt = ''
        for refs in reference:
            src_path = ''
            dst_path = ''
            try:
                if refs[0] == 'S2G':
                    del refs[0]
                    src_path = '\\'.join(prefix_ori_S2G + refs)
                    dst_path = '\\'.join(prefix_user_S2G + refs)
                    shutil.copytree(src_path, dst_path)

                elif refs[0] == 'OQV':
                    # print('refs[0] = OQV')
                    del refs[0]
                    src_path = '\\'.join(prefix_ori_OQV + refs)
                    dst_path = '\\'.join(prefix_user_OQV + refs)
                    shutil.copytree(src_path, dst_path)
                else:
                    print('Nao foi possível interpretar se o caminho é para S2G ou OQV')
                    return 'Nao foi possível interpretar se o caminho é para S2G ou OQV.'
            except FileNotFoundError:
                list_of_not_found_srcs.append(f'\n {src_path}')
                continue
            except FileExistsError:
                list_of_not_found_dsts.append(f'\n {dst_path}')
                continue
        for list_items in list_of_not_found_srcs:
            list_of_not_found_srcs_txt += list_items
            print(list_of_not_found_srcs_txt)
        for list_items in list_of_not_found_dsts:
            list_of_not_found_dsts_txt += list_items
            print(list_of_not_found_dsts_txt)
        if len(list_of_not_found_srcs) == 0 and len(list_of_not_found_dsts) == 0:
            return 'Tarefa Finalizada\n'
        elif not len(list_of_not_found_srcs) == 0 and not len(list_of_not_found_dsts) == 0:
            return 'Tarefa Finalizada \nCaminhos não encontrados no servidor: {} \nCaminho ja existente no seu Mac: \n {}'.format(list_of_not_found_srcs_txt, list_of_not_found_dsts_txt)
        elif not len(list_of_not_found_srcs) == 0:
            return 'Tarefa Finalizada \nCaminhos não encontrados no servidor: \n {}'.format(list_of_not_found_srcs_txt)
        elif not len(list_of_not_found_dsts) == 0:
            return 'Tarefa Finalizada \nCaminhos ja existentes no seu Mac: \n {}'.format(list_of_not_found_dsts_txt)


    elif t_d == 'd':
        list_of_not_found_srcs = list()
        list_of_not_found_dsts = list()
        list_of_not_found_srcs_txt = ''
        list_of_not_found_dsts_txt = ''
        for refs in reference:
            src_path = ''
            dst_path = ''
            try:
                if refs[0] == 'S2G':
                    del refs[0]
                    src_path = '\\'.join(prefix_user_S2G + refs)
                    dst_path = '\\'.join(prefix_tra_S2G + refs)
                    shutil.copytree(src_path, dst_path)
                    # print(f' dst_path {dst_path}')
                    # print(f' src_path {src_path}')

                elif refs[0] == 'OQV':
                    # print('refs[0] = OQV')
                    del refs[0]
                    src_path = '\\'.join(prefix_user_OQV + refs)
                    dst_path = '\\'.join(prefix_tra_OQV + refs)
                    shutil.copytree(src_path, dst_path)
                    # print(f' dst_path {dst_path}')
                    # print(f' src_path {src_path}')
                else:
                    print('Nao foi possível interpretar se o caminho é para S2G ou OQV.')
                    return 'Nao foi possível interpretar se o caminho é para S2G ou OQV.'
            except FileNotFoundError:
                list_of_not_found_srcs.append(f'\n {src_path}')
                continue
            except FileExistsError:
                list_of_not_found_dsts.append(f'\n {dst_path}')
                continue
        for list_items in list_of_not_found_srcs:
            list_of_not_found_srcs_txt += list_items
            print(list_of_not_found_srcs_txt)
        for list_items in list_of_not_found_dsts:
            list_of_not_found_dsts_txt += list_items
            print(list_of_not_found_dsts_txt)
        if len(list_of_not_found_srcs) == 0 and len(list_of_not_found_dsts) == 0:
            return 'Tarefa Finalizada0\n'
        elif not len(list_of_not_found_srcs) == 0 and not len(list_of_not_found_dsts) == 0:
            return 'Tarefa Finalizada1 \nCaminhos não encontrados no seu Mac: {} \nCaminho ja existente no servidor: \n {}'.format(list_of_not_found_srcs_txt, list_of_not_found_dsts_txt)
        elif not len(list_of_not_found_srcs) == 0:
            return 'Tarefa Finalizada2 \nCaminhos não encontrados no seu Mac: \n {}'.format(list_of_not_found_srcs_txt)
        elif not len(list_of_not_found_dsts) == 0:
            return 'Tarefa Finalizada3 \nCaminhos ja existentes no servidor: \n {}'.format(list_of_not_found_dsts_txt)


def creates_paths(reference, t_d):

    """
    :param reference: receives what is returned by the list_way function
    :param t_d: arg that defines if it is a take or a drop operation
    :return: creates the folders
    """

    if reference == 'IndexError':
        return 'Nao foi possível interpretar o caminho inserido.'

    # Converts the path's list to a path
    references = list()
    for refes in reference:
        refs = '\\'.join(refes[:-1])  # This '[:-1]' is to exclude the last reference's folder
        references.append(refs)
    # Form the path and creates the paths
    # In case of 't'(take) there is only one block of code
    if t_d == 't':
        for refs in references:
            caminho = os.path.join('\\'.join(prefix_user), today, refs)
            if not os.path.exists(caminho):
                os.makedirs(caminho)
    # In case of 'd'(drop) there are 2 blocks of code possibles
    elif t_d == 'd':
        for refs in references:
            if refs[:3] == 'S2G':
                caminho = os.path.join('\\'.join(prefix_tra_S2G), refs[4:])
                if not os.path.exists(caminho):
                    print('caminho nao existe. (ta ok)')
                    os.makedirs(caminho)
            elif refs[:3] == 'OQV':
                caminho = os.path.join('\\'.join(prefix_tra_OQV), refs[4:])
                if not os.path.exists(caminho):
                    os.makedirs(caminho)


def list_way(section):

    """
    :param section: Receives the raw paths inserted in the text area, copied from the spreadsheet 'Produtividade'
    :return: Returns a list, created from the processed section param
    """

    section_list = section.split('\n')
    section_list_ref = list()
    for refe in section_list:
        ref = refe.split('\t')  # Makes the line a list
        section_list_ref.append(ref)  # Appends the whole created list
    references = list()
    try:
        for ref in section_list_ref:
            ref.insert(0, ref[5])
            references.append(ref[:5])
        return references
    except IndexError:
        print('IndexError')
    return 'IndexError'
