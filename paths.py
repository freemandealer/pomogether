# -*- coding: utf-8 -*-
import logging
from config import *
import os
from os.path import expanduser


'''
Example:
    pomogether
    |- tasklist.txt
    |- slogan.txt
    |- .user_showoff
    |- .partner_showoff
    |- tracking_data
        |- 20191001.txt
        |- 20191002.txt
        |- 20191003.txt
        |- 20191004.txt
'''


home = expanduser("~")
working_dir = home + u"/pomogether"

user_dir = ''
tracking_dir = ''
tasklist_path = ''
slogan_path = ''
user_showoff_path = ''
partner_showoff_path = ''


def path_init():
    # asign after gflags initilized
    global user_dir
    global tracking_dir
    global tasklist_path
    global slogan_path
    global user_showoff_path
    global partner_showoff_path
    user_dir = working_dir + u'/' + Flags.user_name + u'/'
    tracking_dir = user_dir + u'/tracking_data/'
    tasklist_path = user_dir + u'tasklist.txt'
    slogan_path = user_dir + u'slogan.txt'
    user_showoff_path = user_dir + u'.user_showoff'
    partner_showoff_path = user_dir + u'.partner_showoff'

    create_dir_tree()


def create_dir_tree():
    if os.path.isdir(user_dir) and os.path.exists(user_dir):
        pass
    else:
        os.makedirs(user_dir)

    if os.path.isdir(tracking_dir) and os.path.exists(tracking_dir):
        pass
    else:
        os.makedirs(tracking_dir)

