#!/usr/bin/env python

print("Modulo my_module importado com sucesso...")

test = 'Test String'

def find_index(to_search, target):
    """Find the index of a value in a sequence"""
    for i, value in enumerate(to_search):
        if value == target:
            return 1
    return -1


