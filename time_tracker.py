# -*- coding: utf-8 -*-
import logging
from config import *
import msg_box
import datetime
import json
from time import *
import paths
import os


class TimeTracker():
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


    def __init__(self):
        self.record = None


    def start_work(self):
        task_name = msg_box.whatAreYouDoing()
        start_time = datetime.datetime.now().strftime(TimeTracker.DATE_FORMAT)
        self.record = {'TaskName': task_name, 'StartTime': start_time, 'Type': 'work'}

    
    def stop_work(self):
        if self.record is None:
            return
        now = datetime.datetime.now()
        stop_time = now.strftime(TimeTracker.DATE_FORMAT)
        start_time = self.record['StartTime']
        time_diff = datetime.datetime.strptime(stop_time, TimeTracker.DATE_FORMAT) -\
                   datetime.datetime.strptime(start_time, TimeTracker.DATE_FORMAT)
        work_len = time_diff.seconds / 60
        self.record.update({'StopTime':stop_time, 'WorkLength':work_len})
        self.append_record(now.strftime('%Y%m%d'))


    def start_break(self):
        start_time = datetime.datetime.now().strftime(TimeTracker.DATE_FORMAT)
        self.record = {'TaskName': 'Break', 'StartTime':start_time, 'Type': 'break'}


    def stop_break(self):
        if self.record is None:
            return
        now = datetime.datetime.now()
        stop_time = now.strftime(TimeTracker.DATE_FORMAT)
        start_time = self.record['StartTime']
        time_diff = datetime.datetime.strptime(stop_time, TimeTracker.DATE_FORMAT) -\
                   datetime.datetime.strptime(start_time, TimeTracker.DATE_FORMAT)
        work_len = time_diff.seconds / 60
        self.record.update({'StopTime':stop_time, 'BreakLength':work_len})
        self.append_record(now.strftime('%Y%m%d'))


    def append_record(self, day):
        records = self.load_records_from_json(day)
        records[self.record['StartTime']] = self.record
        self.save_records_to_json(records, day)


    def load_records_from_json(self, day):
        tracking_file_path = paths.tracking_dir+day
        if (not os.path.exists(tracking_file_path)):
            logging.info('brand new day! ' + day)
            return {}
        try:
            fd = open(tracking_file_path, 'r')
            ret = json.loads(fd.read())
            fd.close()
            return ret
        except:
            logging.error('error to open tracking file to read')
        return {}


    def save_records_to_json(self, records, day):
        tracking_file_path = paths.tracking_dir+day
        try:
            fd = open(tracking_file_path, 'w+')
            json.dump(records, fd, sort_keys=True, indent=4, separators=(', ', ': '))
            fd.close()
        except:
            logging.error('error to open tracking file to write')

tracker = TimeTracker()

if __name__ == "__main__":
    tracker.stop_work()
    tracker.start_work()
    exit()
    sleep(5)
    tracker.stop_work()
    tracker.start_break()
    sleep(3)
    tracker.stop_break()
    tracker.start_work()
    sleep(1)
    tracker.stop_work()
    tracker.start_break()
    sleep(2)
    tracker.stop_break()

