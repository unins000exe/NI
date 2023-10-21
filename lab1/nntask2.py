#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import argparse
from lxml import etree as et


def parse_param_value(param_value_str):
    parts = param_value_str.split('=')
    if len(parts) != 2:
        raise argparse.ArgumentTypeError('Неправильный формат.')
    return parts[0], parts[1]


# TODO: ещё подумать как это красивее сделать
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('params', nargs='+', type=parse_param_value,
                        help='input1=input1.txt output1=output1.xml')
    args = parser.parse_args()
    params = dict(args.params)
    input1 = params.get('input1')
    output1 = params.get('output1')
    return input1, output1


def read_graph(xml_file):
    tree = et.parse(xml_file)
    root = tree.getroot()
    edges = dict()
    vs = dict()
    i = 0
    for elem in root.iter("vertex"):
        vs[elem.text] = i
        edges[i] = []
        i += 1
    for elem in root.iter("arc"):
        edges[vs[elem[0].text]].append(vs[elem[1].text])

    color = len(edges) * [0]
    dfs(0, edges, color)

    return edges


def dfs(v, edges, color):
    color[v] = 1
    for u in edges[v]:
        if color[u] == 0:
            dfs(u, edges, color)
        if color[u] == 1:
            print('Найден цикл.')
            return True
    color[v] = 2


def main():
    # input1, output1 = create_parser()
    edges = read_graph('output1.xml')

main()
