#!/usr/bin/env python3

from threading import Thread


def f(name):
    print("Hello", name)


th = Thread(target=f, args=("Bob",))
th.start()
th.join()
