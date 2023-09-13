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
    parser.add_argument('params', nargs='+', type=parse_param_value)
    args = parser.parse_args()
    params = dict(args.params)
    input1 = params.get('input1')
    output1 = params.get('output1')
    return input1, output1


def parse_input(input1):
    with open(input1, 'r') as in1:
        str = in1.read()

    str = ''.join(str.split())
    arcs = [tuple(x.split(',')) for x in str[1:-1].split('),(')]
    arcs = [(x[0], x[1], int(x[2])) for x in arcs]

    visits = dict()
    vs = set()
    for arc in arcs:
        vs.add(arc[0])
        vs.add(arc[1])
        if arc[1] not in visits.keys():
            visits[arc[1]] = [arc[2]]
        else:
            visits[arc[1]].append(arc[2])

    for orders in visits.values():
        if list(set(orders)) != orders:
            raise ValueError('Неправильно заданы порядковые номера заходящих дуг.')

    return arcs, vs


def make_xml(arcs, vs, output1):
    graph = et.Element('graph')
    for v in vs:
        et.SubElement(graph, 'vertex').text = v
    for a in arcs:
        arc = et.SubElement(graph, 'arc')
        et.SubElement(arc, 'from').text = a[0]
        et.SubElement(arc, 'to').text = a[1]
        et.SubElement(arc, 'order').text = str(a[2])

    tree = et.ElementTree(graph)
    tree.write(output1, encoding='utf-8', pretty_print=True)
    print('Граф успешно записан в', output1)


def main():
    input1, output1 = create_parser()
    arcs, vs = parse_input(input1)
    make_xml(arcs, vs, output1)

main()
