#! /usr/bin/python3

from math import pi
import sys

def circulo(raio):
    return pi * float(raio) ** 2



if __name__=='__main__':
    if len(sys.argv) < 2:
        print('E necessario informarar o raio do circulo')
    raio = sys.argv[0]
    area = circulo(raio)
    print('Area do circulo', area)




