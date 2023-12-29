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
                        help='input1=arcs1.txt output1=output1.xml')
    args = parser.parse_args()
    params = dict(args.params)
    input1 = params.get('input1')
    output1 = params.get('output1')
    return input1, output1


class Vertex:
    def __init__(self, v):
        self.name = v
        self.children = []
        self.parents = []


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
        v0 = vs[elem[0].text]
        v1 = vs[elem[1].text]
        v0.children.append(v1)
        v1.parents.append(v0)

        edges[elem[0].text].append(elem[1].text)

    dfs(list(edges.keys())[0], edges, color)

    return edges, vs


def dfs(v, edges, color):
    color[v] = 1
    for u in edges[v]:
        if color[u] == 0:
            dfs(u, edges, color)
        if color[u] == 1:
            print('Найден цикл. Работа программы остановлена.')
            exit()
    color[v] = 2


def find_root(edges, vs):
    for v in edges:
        if not edges[v]:
            return vs[v]


def make_func(v, vs):
    parents = [make_func(c, vs) for c in v.parents]
    return f'{v.name}({", ".join(parents)})'


def main():
    input1, output1 = create_parser()
    edges, vs = read_graph(input1)
    root = find_root(edges, vs)
    z = make_func(root, vs)
    with open(output1, 'w') as out:
        out.write(z)
        print(f'Префиксная функция успешно записана в {output1}')


main()
