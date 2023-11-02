#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import argparse
from lxml import etree as et


def parse_param_value(param_value_str):
    parts = param_value_str.split('=')
    if len(parts) != 2:
        raise argparse.ArgumentTypeError('Неправильный формат.')
    return parts[0], parts[1]


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('params', nargs='+', type=parse_param_value,
                        help='input1=input1.txt output1=output1.xml')
    args = parser.parse_args()
    params = dict(args.params)
    input1 = params.get('input1')
    output1 = params.get('output1')
    return input1, output1


class Vertex:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None


def height(v):
    if not v:
        return 0
    l_height = height(v.left)
    r_height = height(v.right)
    return max(l_height, r_height) + 1


def breadth_first(root):
    h = height(root)
    func = []
    for i in range(h):
        print_level(root, i, func)
    # print_level(root, h, func)
    return func, h


def print_level(root, level, func):
    if not root:
        return

    if level == 0:
        if root.left:
            rl = root.left.v
        else:
            rl = ''
        if root.right:
            rr = root.right.v
        else:
            rr = ''

        func.append([root.v, rl, rr])

    if level > 0:
        print_level(root.left, level - 1, func)
        print_level(root.right, level - 1, func)



def read_graph(xml_file):
    tree = et.parse(xml_file)
    root = tree.getroot()
    edges, color = dict(), dict()
    vs = dict()

    i = 0
    for elem in root.iter("vertex"):
        v = elem.text
        vs[v] = Vertex(v)
        edges[v] = []
        color[v] = 0
        i += 1

    for elem in root.iter("arc"):
        v = vs[elem[1].text]
        if v.left is None:
            v.left = vs[elem[0].text]
        else:
            v.right = vs[elem[0].text]
        edges[elem[0].text].append(elem[1].text)

    dfs(list(edges.keys())[0], edges, color)

    return edges, vs


def dfs(v, edges, color):
    color[v] = 1
    for u in edges[v]:
        if color[u] == 0:
            dfs(u, edges, color)
        if color[u] == 1:
            print('Найден цикл.')
            return True
    color[v] = 2


def find_root(edges, vs):
    for v in edges:
        if not edges[v]:
            return vs[v]


def main():
    # input1, output1 = create_parser()
    edges, vs = read_graph('output1.xml')
    root = find_root(edges, vs)
    func, h = breadth_first(root)
    print('func', func)
    # str_func = ''
    # for i in range(h):


main()
