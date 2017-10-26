""" Get a txt file hosting a text output tree
    and print out all the root-leaves nodes
"""
import sys
from itertools import takewhile


def is_indent(xxx):
    """is character xxx part of indentation?"""
    return xxx in ['\t', '|', ' ', '+', '-', '\\', '/']


def print_root_leaf(lines):
    """print the root of every leaf"""
    min_indent = 10000
    lines = iter(lines)
    stack = []
    for line in lines:
        if (len(line) == 0 or line[0] not in ['|', '+', '-', '\\', '/']):
            continue
        indent = len(list(takewhile(is_indent, line)))
        if indent == 0:
            continue
        if indent <= min_indent:
            min_indent = indent
            del stack[:]
        stack.append(line[indent:])
        if len(stack) >= 2:
            print(stack[0] + ' >>> ' + stack[-1])


def main():
    """self-expl"""
    with open(sys.argv[1]) as tree_file:
        tree_lines = tree_file.read().splitlines()
        print_root_leaf(tree_lines)


main()