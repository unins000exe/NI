#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import argparse
from math import exp
import json
import numpy as np


class Network:
    def __init__(self, input1, input2, output1):
        self.weights = []
        layers = read_json(input1)
        for w in layers:
            self.weights.append(layers[w])
        self.weights = np.array(self.weights)

        self.input_vector = np.array(read_json(input2)['x'])
        try:
            shape = self.weights.shape
        except:
            raise ValueError('Неверное заданы входные параметры.')
        self.p = shape[0]
        self.m = shape[1]
        self.n = shape[2]

        # self.p = np.size(self.weights)
        # self.n = np.size(self.input_vector)
        # self.m = np.size(self.weights[0])

        # for layer in self.weights:
        #     print('layer', layer)
        #     if np.size(layer) != self.m:
        #         raise ValueError('Число нейронов в каждом слое должно быть одинаковым.')
        #     for neuron in layer:
        #         if np.size(neuron) != self.n:
        #             raise ValueError('Число весов каждого нейрона должно совпадать с размером входного вектора.')

        print('веса')
        print(self.weights)
        print('входной вектор', self.input_vector)
        print(f'p = {self.p}, n = {self.n}, m = {self.m}')

    def func(self):
        output = np.array([0] * self.n)
        for i in range(self.p):
            y = self.weights * self.input_vector
            # print('y', y)


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


def main():
    # input1, input2, output1 = create_parser()
    input1, input2, output1 = 'W.json', 'X.json', 'Y.json'
    # w1 = [[0.1, 0.5, 0.9], [0.2, 0.4, 0.8], [0.1, 0.1, 0.1], [0.3, 0.6, 0.9], [0.0, 0.5, 1]]
    # w2 = [[0.1, 0.2, 0.3], [0.15, 0.25, 0.35], [0.9, 0.8, 0.7], [0.5, 0.5, 0.5], [1, 1.5, 1]]
    # write_json(input1, {'w1': w1, 'w2': w2})
    # write_json(input2, {'x': [2.47, 1.2, 9.6]})
    network = Network(input1, input2, output1)
    network.func()


main()
