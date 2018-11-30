#!/usr/bin/env python3

# Functions with one argument
# def hello_func(greeting):
#     return '{}, Function.'.format(greeting)
#
#
# print(hello_func('Hi'))


# Default Value
def hello_func(greeting, name='Python'):
    return '{}, {}.'.format(greeting, name)
#
#
# print(hello_func('Hi'))  # mesmo passando apenas um argumento (greeting)
# print(hello_func('Hi', name='Java'))  # Parametro nomeado
# print(hello_func('Hi', 'Go'))


# args and kwargs
# args - recebe uma tupla e kwargs - um dicionario

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# student_info('Math', 'Sci', 'Chemis', name='John', age=43, ID='orange')

# OR

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ('Math', 'Sci', 'Chemis')
info = {'name': 'John', 'age': 43, 'ID': 'orange'}

#student_info(courses, info) # Nao exatamente
student_info(*courses, **info) # Agora sim!


