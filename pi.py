#!/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

import random
import multiprocessing
from multiprocessing import Pool

def pi(n):
    contador = 0
    x_dentro = []
    y_dentro = []
    x_fora = []
    y_fora = []
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if (x ** 2 + y ** 2) < 1.0:
            contador += 1
            x_dentro.append(x)
            y_dentro.append(y)
        else:        
            x_fora.append(x)
            y_fora.append(y)        

    return contador, x_dentro, y_dentro, x_fora, y_fora

workers = 8
totalPontos = 20000
divisaoWorker = [totalPontos/workers for i in range(workers)]
pool = Pool(processes = workers)
resultado = pool.map(pi, divisaoWorker)

dict = {
    0: { 'cor': 'tab:blue', 'nome': 'Worker 1' },
    1: { 'cor': 'tab:green', 'nome': 'Worker 2' },
    2: { 'cor': 'tab:cyan', 'nome': 'Worker 3' },
    3: { 'cor': 'tab:purple', 'nome': 'Worker 4' },
    4: { 'cor': 'tab:brown', 'nome': 'Worker 5' },
    5: { 'cor': 'tab:pink', 'nome': 'Worker 6' },
    6: { 'cor': 'tab:olive', 'nome': 'Worker 7' },
    7: { 'cor': 'tab:orange', 'nome': 'Worker 8' },
}

fig, ax = plt.subplots()
circulo = plt.Circle((0, 0), 1, fill=False)
ax.set_aspect(1)
ax.add_artist(circulo)

contador = []
for idx, tupla in enumerate(resultado):
    contador.append(tupla[0]) # tupla 0 -> quantidade dentro
    ax.set_aspect('equal')
    legenda = dict.get(idx)['nome']

    ax.scatter(tupla[1], tupla[2],
        color='{}'.format(dict.get(idx)['cor']),
        marker='s',
        s=0.5,
        label=legenda)

    ax.scatter(tupla[3], tupla[4],
        color='{}'.format(dict.get(idx)['cor']),
        marker='s',
        s=0.5)

fig.legend()
fig.savefig('Workers.pdf')


fig, ax = plt.subplots()
circulo = plt.Circle((0, 0), 1, fill=False)
ax.set_aspect(1)
ax.add_artist(circulo)

for idx, tupla in enumerate(resultado):
    ax.set_aspect('equal')
    ax.scatter(tupla[1], tupla[2], color='green', marker='s', s=0.5)
    ax.scatter(tupla[3], tupla[4], color='red', marker='s', s=0.5)

fig.savefig('Total.pdf')

print('Valor estimado do PI: {:.20f}'.format(sum(contador)/float(totalPontos)*4))
