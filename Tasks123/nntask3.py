#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import argparse
from lxml import etree as et
from math import exp


def parse_param_value(param_value_str):
    parts = param_value_str.split('=')
    if len(parts) != 2:
        raise argparse.ArgumentTypeError('Неправильный формат.')
    return parts[0], parts[1]


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('params', nargs='+', type=parse_param_value)
    args = parser.parse_args()
    params = dict(args.params)
    input1 = params.get('input1')
    input2 = params.get('input2')
    output1 = params.get('output1')
    return input1, input2, output1


class Vertex:
    def __init__(self, v):
        self.name = v
        self.parents = []
        self.operation = None
        self.value = None


def read_graph(xml_file, ops_file):
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
        v1.parents.append(v0)

        edges[elem[0].text].append(elem[1].text)

    dfs(list(edges.keys())[0], edges, color)

    ops = open(ops_file, 'r')
    while True:
        line = ops.readline()
        if not line:
            break
        op = line[2:].strip()
        v = vs[line[0]]
        if op.isdigit():
            v.value = int(op)
            if v.parents:
                print(f'{v.name} не должна иметь родителей (аргументов)!')
                exit()
        else:
            v.operation = op
            if op == '+' or op == '*':
                if len(v.parents) != 2:
                    print(f'{v.name} должна иметь 2 родителей (аргументов)!')
                    exit()
            elif op == 'exp' and len(v.parents) != 1:
                print(f'{v.name} должна иметь 1 родителя (аргумент)!')
                exit()

    return edges, vs


def dfs(v, edges, color):
    color[v] = 1
    for u in edges[v]:
        if color[u] == 0:
            dfs(u, edges, color)
        if color[u] == 1:
            print('Найден цикл. Работа программы остановлена')
            exit()
    color[v] = 2


def find_root(edges, vs):
    for v in edges:
        if not edges[v]:
            return vs[v]


def evaluate(v):
    if v.operation is None:
        return v.value

    if v.operation == '+':
        result = 0
        for p in v.parents:
            result += evaluate(p)
        return result

    if v.operation == '*':
        result = 1
        for p in v.parents:
            result *= evaluate(p)
        return result

    if v.operation == 'exp':
        return exp(evaluate(v.parents[0]))


def main():
    input1, input2, output1 = create_parser()
    edges, vs = read_graph(input1, input2)
    root = find_root(edges, vs)
    z = evaluate(root)
    with open(output1, 'w') as out:
        print(f'Значение {z} функции записано в {output1}')
        out.write(str(z))

main()
