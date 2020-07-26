from lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')    # Abre o arquivo para leitura de texto
        a.close()   # Fecha o arquivo
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')    # Escreve um arquigo de texto, e caso ele não exista, é criado (+).
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:     # Para cada linha em arquivo
            dado = linha.split(';')     # Separando a idade do nome pelo ";"
            dado[1] = dado[1].replace('\n', '')     # Removendo o "\n" que existe depois da idade
            print(f' {dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')     # a = append / t = text
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
