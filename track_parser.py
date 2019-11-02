# -*- coding: utf-8 -*-
import logging
from config import *
import paths
import json
import datetime


def load_data_today():
    day = datetime.datetime.now().strftime('%Y%m%d')
    tracking_file_path = paths.tracking_dir+day
    try:
        fd = open(tracking_file_path, 'r')
        raw_data = json.loads(fd.read())
        fd.close()
        return raw_data
    except:
        logging.error('error to parse tracking data json file')
        assert(False)


def get_total_work_length_today():
    data = load_data_today()
    work_length = 0
    for start_time,task_info in data.items():
        if task_info[u'Type'] == 'work':
            work_length += int(task_info[u'WorkLength'])
    return work_length


def get_total_break_length_today():
    data = load_data_today()
    break_length = 0
    for start_time,task_info in data.items():
        if task_info[u'Type'] == 'break':
            length = int(task_info[u'BreakLength'])
            if length < 120:
                break_length += length
    return break_length


def get_task_length_today():
    data = load_data_today()
    task_length_map = {}
    for start_time,task_info in data.items():
        if task_info['Type'] == 'break':
            continue
        if task_info['TaskName'] not in task_length_map:
            task_length_map[task_info['TaskName']] = int(task_info['WorkLength'])
        else:
            task_length_map[task_info['TaskName']] += int(task_info['WorkLength'])
    return task_length_map


if __name__ == '__main__':
    print get_total_work_length_today()
    print get_total_break_length_today()
    ret = get_task_length_today()
    for key,val in ret.items():
        print key

