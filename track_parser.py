# -*- coding: utf-8 -*-
import logging
from config import *
import datetime
import json
import os

import paths


def load_data_today():
    day = datetime.datetime.now().strftime('%Y%m%d')
    tracking_file_path = paths.tracking_dir + day
    if not paths.tracking_dir or not os.path.exists(tracking_file_path):
        return {}

    try:
        fd = open(tracking_file_path, 'r')
        raw_data = json.loads(fd.read())
        fd.close()
        return raw_data
    except Exception:
        logging.exception('error to parse tracking data json file: %s', tracking_file_path)
        return {}


def get_total_work_length_today():
    data = load_data_today()
    work_length = 0
    for start_time,task_info in data.items():
        if task_info.get(u'Type') == 'work':
            work_length += int(task_info.get(u'WorkLength', 0))
    return work_length


def get_total_break_length_today():
    data = load_data_today()
    break_length = 0
    for start_time,task_info in data.items():
        if task_info.get(u'Type') == 'break':
            length = int(task_info.get(u'BreakLength', 0))
            if length < 120:
                break_length += length
    return break_length


def get_task_length_today():
    data = load_data_today()
    task_length_map = {}
    for start_time,task_info in data.items():
        if task_info.get('Type') == 'break':
            continue
        task_name = task_info.get('TaskName')
        if not task_name:
            continue
        work_length = int(task_info.get('WorkLength', 0))
        if task_name not in task_length_map:
            task_length_map[task_name] = work_length
        else:
            task_length_map[task_name] += work_length
    return task_length_map


if __name__ == '__main__':
    print(get_total_work_length_today())
    print(get_total_break_length_today())
    ret = get_task_length_today()
    for key,val in ret.items():
        print(key)
