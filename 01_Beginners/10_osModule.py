#!/usr/bin/env python3

import os
# print(os.getcwd()) # current work directory
#
# os.chdir('/Users/fabio/Estudo/Prog/Python/Python_tutorial_by_Corey_Schafer/01_Beginners/') # alterando o diretório
# print(os.getcwd()) # verificando novamente

# criando um diretório no diretório atual
# os.mkdir('os-demo') # use makedirs() caso necessite criar subfolders
#
# os.mkdir('os-demo2')

# removendo um diretório
#os.rmdir('os-demo')

# verificando o conteúdo da pasta
#print(os.listdir())

# Alterando diretorio novamente
#os.chdir('/Users/fabio/Desktop/os-demo2')

# editando/renomenando um arquivo
# Altere o diretorio para os-demo2
os.chdir('/Users/fabio/Estudo/Prog/Python/Python_tutorial_by_Corey_Schafer'
         '/01_Beginners/os-demo2')

# renomenando arquivo test.txt
#os.rename('test.txt', 'demo.txt')

# verificando o conteúdo da pasta
#print(os.listdir())

# # Meta dados do arquivo modificado
# print(os.stat('demo.txt'))
# # verificando o tamanho
# print(os.stat('demo.txt').st_size,'bytes')
# # verificando a ultima modificacao do arquivo
# print(os.stat('demo.txt').st_mtime)# retorna um timestamp, nao muito legível
#
# # para tornar mais legível
# from datetime import datetime
#
# mod_time = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))

# Verificando toda arvore do diretório
# for dirpath, dirnames, filenames in os.walk('/Users/fabio/Desktop/'):
#     print('Current Path:', dirpath)
#     print('Directories: ', dirnames)
#     print('Files:', filenames)
#     print()

# Imprimindo variáveis de ambiente
#print(os.environ.get('HOME'))

# Criando um caminho para um arquivo
# file_path = os.path.join(os.environ.get('HOME'),'test.txt')
# print(file_path)

# imprimindo caminhos e arquivos que nao existem
print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt')) # separa a extensão .txt do nome
print()
# Caso queira verificar se realmente existe
print(os.path.exists('/tmp/test.txt')) # retorna False
print(os.path.isdir('/tmp/test.txt')) # retorna False
print(os.path.isfile('/tmp/test.txt')) # retorna False
print()

# Caso queira saber todas as funções do modulo os.path
for x, i in enumerate(dir(os.path),start=1):
    print(x,i)