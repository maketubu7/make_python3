python_source = """\
SEVENTEEN = 17

def three():
    return 3
"""
global_namespace = {}
exec(python_source, global_namespace)

print(global_namespace['SEVENTEEN'])
print(global_namespace['three']())

code = []
code.extend([" " * 4, 'line', "\n"])
print(code)