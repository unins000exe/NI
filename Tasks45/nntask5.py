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
            self.x = np.zeros(self.m)
            self.z = np.zeros(self.n)
            self.df = np.zeros(self.n)

    def __init__(self, input1, input2):
        self.layers = []
        weights = read_json(input1)
        for w in weights:
            self.layers.append(Network.Layer(weights[w]))
        self.p = len(self.layers)

        self.deltas = [[]] * self.p
        self.alpha = 0.5
        self.x = np.array(read_json(input2)['x'])
        self.y = np.array(read_json(input2)['y'])

    def forward(self, input):
        for k in range(self.p):
            l = self.layers[k]
            if k == 0:
                l.x = input

            for i in range(l.n):
                y = 0
                for j in range(l.m):
                    y += l.w[i][j] * l.x[j]

                l.z[i] = sigmoid(y)
                l.df[i] = l.z[i] * (1 - l.z[i])
            if k < self.p - 1:
                self.layers[k + 1].x = l.z

        return self.layers[-1].z

    def backward(self, output):
        error = 0
        last = self.layers[-1]
        olen = len(output)
        self.deltas[-1] = np.zeros(olen)
        for i in range(olen):
            e = last.z[i] - output[i]
            self.deltas[-1][i] = e * last.df[i]
            error += e * e / 2

        for k in range(self.p - 1, 0, -1):
            lk = self.layers[k]
            self.deltas[k - 1] = np.zeros(lk.m)
            for i in range(lk.m):
                for j in range(lk.n):
                    self.deltas[k - 1][i] += lk.w[j][i] * self.deltas[k][j]
                self.deltas[k - 1][i] *= self.layers[k - 1].df[i]

        return error

    def update(self):
        for k in range(self.p):
            lk = self.layers[k]
            for i in range(lk.n):
                for j in range(lk.m):
                    lk.w[i][j] -= self.alpha * self.deltas[k][i] * lk.x[j]

    def train(self):
        eps = 0.0000001
        epoch = 100000
        ep = 0
        error = 1
        while ep < epoch and error > eps:
            ep += 1
            errors = []
            for i in range(len(self.x)):
                a = self.forward(self.x[i])
                errors.append(self.backward(self.y[i]))
                self.update()
                # print(f'X: {self.x[i]}, Y: {self.y[i]}, out: {a}')
                error = np.mean(np.array(errors))
            # print(f'Итерация {ep}, ошибки {error}')

        for i in range(len(self.x)):
            print(f'X: {self.x[i]}, Y: {self.y[i]}, out: {self.forward(self.x[i])}')




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
    # input1, input2, output1 = create_parser()
    input1 = 'W2.json'
    input2 = 'XY.json'
    output1 = 'Y2.json'
    network = Network(input1, input2)
    # write_json(output1, {'y': list(network.forward())})

    x = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y = [[0.0], [1.0], [1.0], [0.0]]
    network.train()


main()
