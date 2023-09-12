#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse
from lxml import etree as et


def parse_param_value(param_value_str):
    parts = param_value_str.split('=')
    if len(parts) != 2:
        raise argparse.ArgumentTypeError('Invalid parameter value format')
    return parts[0], parts[1]


# TODO: ещё подумать как это красивее сделать
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('params', nargs='+', type=parse_param_value)
    args = parser.parse_args()
    params = dict(args.params)
    input1 = params.get('input1')
    output1 = params.get('output1')
    input2 = params.get('input2')
    output2 = params.get('output2')
    return input1, input2, output1, output2


def parse_input(input1):
    with open(input1, 'r') as in1:
        str = in1.read()

    str = ''.join(str.split())
    print(str)



def main():
    # input1, input2, output1, output2 = create_parser()
    # graph = et.Element('graph')
    # et.SubElement(graph, 'vertex').text = 'v1'
    # et.SubElement(graph, 'vertex').text = 'v2'
    # arc = et.SubElement(graph, 'arc')
    # et.SubElement(arc, 'from').text = 'v1'
    # et.SubElement(arc, 'to').text = 'v2'
    # et.SubElement(arc, 'order').text = '1'
    #
    # tree = et.ElementTree(graph)
    # tree.write('output1.xml', encoding='utf-8', pretty_print=True)
    parse_input('input1.txt')

main()
