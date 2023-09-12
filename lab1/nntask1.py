#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse


def parse_param_value(param_value_str):
    parts = param_value_str.split('=')
    if len(parts) != 2:
        raise argparse.ArgumentTypeError('Invalid parameter value format')
    return parts[0], parts[1]


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('params', nargs='+', type=parse_param_value)
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    params = dict(args.params)
    input1 = params.get('input1')
    output1 = params.get('output1')
    print(input1, output1)

main()
