# -*- coding: utf-8 -*-
import logging
from config import *
from subprocess import Popen, PIPE
import os
from tasklist import tasklist


def whatAreYouDoing():
    tasks = tasklist.get_tasklist()
    prompt = 'select a task by number or type in new one:\n\n'
    for idx in range(len(tasks)):
        prompt += '\t' + str(idx+1) + ' ' + tasks[idx] + '\n'
    select = _whatAreYouDoing(prompt).rstrip()
    try:
        idx = int(select)
        task_name = tasks[idx-1]
    except:
        task_name = select
        tasklist.add_task(task_name)
    return task_name


def _whatAreYouDoing(prompt):
    command = '''
        tell application "System Events"
            activate
            set thefilename to (display dialog "%(prompt)s" default answer "")
        end tell
        set thefilename to the text returned of thefilename as string
        return thefilename
        EOT
    ''' % {'prompt':prompt}

    proc = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    answer,err = proc.communicate(command)
    return answer


def yesNoMsgBox(s, timeout):
    ret = os.system(\
            "osascript -e 'Tell application \"System Events\" to display dialog \""\
            +s+"\" giving up after " + str(timeout) +"'")
    if ret == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(_whatAreYouDoing('''
    make your choice:
    1: apple
    2: banana
    3: android

    leave blank if same as last 
    '''))

