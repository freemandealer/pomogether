#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from config import *
import sys
from pomodoro import *


def main(argv):
    argv.append('--flagfile=./config.txt')
    Flags(argv)
    logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='pogether.log',
                filemode='w')
    paths.path_init()
    Pomodoro().run()
    exit()

if __name__ == "__main__":
    sys.exit(main(sys.argv))

