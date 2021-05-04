#!/usr/bin/env python3

from multiprocessing import Process


def f(name):
    print("Hello", name)


if __name__ == '__main__':
    p = Process(target=f, args=("Bob",))
    p.start()
    p.join()
