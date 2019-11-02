# -*- coding: utf-8 -*-
import logging
from config import *
import os
import json
import track_parser
import paths


def get_slogan():
    if not os.path.exists(paths.slogan_path):
        return ''

    try:
        file = open(paths.slogan_path, 'r')
        return file.read()
    except:
        logging.error('error to open ' + paths.slogan_path)
        return ''


def create_show_off_file():
    logging.info('creating user show off file')
    content = {}
    content['slogan'] = get_slogan()
    content['WorkLength'] = track_parser.get_total_work_length_today()
    content['BreakLength'] = track_parser.get_total_break_length_today()
    content['Tasks'] = track_parser.get_task_length_today()
    try:
        fd = open(paths.user_showoff_path, 'w+')
        json.dump(content, fd, sort_keys=True, indent=4, separators=(', ', ': '))
        fd.close()
    except:
        logging.error('error to open to write ' + paths.user_showoff_path)


def upload_show_off_file(user):
    logging.info('upload show off file of user')
    cmd = 'curl ' + Flags.server_url + '/' + user + ' -T ' + paths.user_showoff_path
    logging.info(cmd)
    os.system(cmd)

def download_show_off_file(partner):
    logging.info('download show off file of partner')
    cmd = 'curl ' + Flags.server_url + '/' + partner + ' > ' + paths.partner_showoff_path
    logging.info(cmd)
    os.system(cmd)


if __name__ == "__main__":
    create_show_off_file()
    upload_show_off_file(Flags.user_name)
    download_show_off_file(Flags.user_name)
    #download_show_off_file(Flags.partner_name)

