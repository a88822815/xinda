#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import sys
import numpy as np


def sayHi():
    print('Hello, world!')


def main():
    sayHi()


if __name__ == '__main__':
    # sys.exit(main())
    a = np.array([[1,2,3],[4,5,6]])
    print(a[1][1])