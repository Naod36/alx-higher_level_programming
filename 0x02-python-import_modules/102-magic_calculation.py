#!/usr/bin/python3

def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    add, sub = __import__('magic_calculation_102', fromlist=('add', 'sub'))

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)
    else:
        return (sub(a, b))

# Test
result = magic_calculation(3, 7)
print(result)

