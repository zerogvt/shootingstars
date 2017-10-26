import sys
from itertools import takewhile


def is_indent(x):
    return x in ['\t', '|', ' ', '+', '-', '\\', '/']

def build_tree(lines):
    min_indent = 10000
    lines = iter(lines)
    stack = []
    for line in lines:
        if (len(line)==0 or line[0] not in ['|',  '+', '-', '\\', '/']):
            continue
        indent = len(list(takewhile(is_indent, line)))
        if (indent==0):
            continue
        if (indent <= min_indent):
            min_indent = indent
            del stack[:]
        stack.append(line[indent:])
        if (len(stack)>=2):
            print(stack[0] + ' >>> ' + stack[-1])

lines=[]
with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
build_tree(lines)
