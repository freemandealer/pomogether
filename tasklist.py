# -*- coding: utf-8 -*-
import logging
from config import *
import os
import paths


class TaskList:
    def __init__(self):
        pass


    def get_tasklist(self):
        if not os.path.exists(paths.tasklist_path):
            return []

        try:
            file = open(paths.tasklist_path, 'r')
        except:
            logging.error('error to open ' + paths.tasklist_path)
            return []

        l = []
        for line in file:
            line = line.rstrip()
            l.append(line)
        file.close()
        return l


    def add_task(self, task):
        try:
            file = open(paths.tasklist_path, 'a+')
        except:
            logging.error('error to open and write ' + paths.tasklist_path)
        file.write(task)
        file.write('\n')
        file.close()

tasklist = TaskList()

if __name__ == "__main__":
    tasklist = TaskList()
    tasklist.add_task('我觉得很好\n')
    l = tasklist.get_tasklist()
    for each in l:
        print each

