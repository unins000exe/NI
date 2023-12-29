#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import argparse
from math import exp
import json
import numpy as np


class Network:
    class Layer:
        def __init__(self, w):
            self.w = np.array(w)
            shape = self.w.shape
            self.n = shape[0]
            self.m = shape[1]
            self.x = None
            self.z = None

    def __init__(self, input1, input2, output1):
        self.layers = []
        weights = read_json(input1)
        for w in weights:
            self.layers.append(Network.Layer(weights[w]))
        self.layers[0].x = np.array(read_json(input2)['x'])
        self.p = len(self.layers)

    def forward(self):
        for k in range(self.p):
            l = self.layers[k]
            print(l.w, l.x)
            y = np.dot(l.w, l.x)
            print('y', y)
            for i in range(l.n):
                y[i] = sigmoid(y[i])
            l.z = y
            if k < self.p - 1:
                self.layers[k + 1].x = y
        return self.layers[-1].z


def sigmoid(x):
    return 1 / (1 + exp(-x))


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


def write_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)
    print(f'В {filename} было записано {data}')


def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


# python3 nntask4.py input1='W.json' input2='X.json' output1='Y.json'
def main():
    input1, input2, output1 = create_parser()
    network = Network(input1, input2, output1)
    write_json(output1, {'y': list(network.forward())})


main()
