#!/usr/bin/env python3

from threading import Thread


class PrintThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("Hello", self.name)


if __name__=="__main__":
    th = PrintThread("Mike")
    th.start()
    th.join()
