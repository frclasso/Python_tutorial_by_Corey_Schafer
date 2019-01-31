#!/usr/bin/env python 3

''' Reading and wirting files:
    modes => r = reading
             w = writing
             a = appenfing
             r+ =  reading and writing'''

# f = open('arquivo.txt', 'r')
# print(f.name) # imprime o nome do arquivo
# print(f.mode) # imprime o modo o qual o arquivo foi aberto
#
# f.close()

'''with context manager'''
# Nao é ncessário fechar/close()
# with open('arquivo.txt', 'r') as f:
#     pass
#
# print(f.closed) # retorna True porque o arquivo é fechado automaticamente

#with open('arquivo.txt', 'r') as f:
    #f_contents = f.read() # para pequenos arquivos
    #f_contents = f.readlines() # retorna todas linhas em uma unica
    #f_contents = f.readline() # retorna uma unica linha, primeira
    #print(f_contents, end='')
    #
    # f_contents = f.readline() # retorna uma unica linha, segunda
    # print(f_contents, end='')

    # para ler todas linhas sem usar read/readlines (ocupam mais memoria)
    # for line in f:
    #     print(line, end='')

    # para ler apenas uma parte do texto/arquivo
    # f_contents = f.readline(100) # os 100 primeiros caracteres
    # print(f_contents, end='')
    #
    # f_contents = f.readline(100) # os proximos 100 caracteres
    # print(f_contents, end='')


# definindo um tamanho a ser lido
# with open('arquivo.txt', 'r') as f:
#     size_to_read = 30 # 300 primeiros caracteres
#     f_contents = f.read(size_to_read)
#     print(f.tell())
#     print(f_contents)
#
#     #f.seek(0)  # volta pro inicio
#     size_to_read = 30 # 300 primeiros caracteres
#     f_contents = f.read(size_to_read)
#     print(f.tell())
#     print(f_contents)

# Escrevendo

with open('arquivo2.txt', 'w') as f: # use a (append) caso nao queira perder dados
    f.write('Hello World!!')
    # f.seek(0)
    # f.write('Z')