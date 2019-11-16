# -*- coding: utf-8 -*-
import logging
from config import *
import rumps
import os
import schedule
from time import *
import threading
import msg_box
import fullscreen
import show_off
import paths
from time_tracker import *


class Pomodoro(rumps.App):
    def __init__(self):
        super(Pomodoro, self).__init__("20Twenty20",icon="data/icon.tiff")
        self.work_menu = rumps.MenuItem("work", callback=self.work)
        self.rest_menu = rumps.MenuItem("rest",callback=None)
        self.menu = [self.work_menu, self.rest_menu, None]
        self.alarm_time = [int(i) * 60 for i in Flags.notice_interval]
        self.time_idx = 0
        self.mainloopStart()


    def work(self,_):
        logging.info('work start')
        self.work_menu.set_callback(None)
        self.rest_menu.set_callback(self.rest)
        assert(self.time_idx < len(self.alarm_time))
        self.timer = threading.Timer(self.alarm_time[self.time_idx], self.timerAction)
        self.timer.start()
        if self.time_idx == 0:
            tracker.stop_break()
            tracker.start_work()


    def rest(self,_):
        logging.info('work stop, break start')
        self.timer.cancel()
        tracker.stop_work()
        tracker.start_break()

        show_off.create_show_off_file()
        show_off.upload_show_off_file(Flags.user_name)
        show_off.download_show_off_file(Flags.partner_name)

        ## using subprocess instead of function call to avoid OSX bug
        cmd = 'python fullscreen.py --time=20 --quitable=' + str(Flags.fullscreen_quitable) + ' --flagfile=./config.txt'
        logging.info(cmd)
        os.system(cmd)


        self.rest_menu.set_callback(None)
        self.work_menu.title = "work"
        self.work_menu.set_callback(self.work)
        self.time_idx = 0

        # ask for another round
        choice = msg_box.yesNoMsgBox('click OK to work for another round', 3600)
        if choice == True:
            self.work(None)
        else:
            exit()


    def timerAction(self):
        if self.time_idx == (len(self.alarm_time)-1):
            self.mandatoryRest()
        else:
            will_cont = self.notifyRest()
            if will_cont == True:
                self.time_idx += 1
                self.work(None)
            else:
                self.rest(None)


    def mandatoryRest(self):
        self.rest(None)


    def notifyRest(self):
        choice = msg_box.yesNoMsgBox('do you want to cont?', 20)
        if choice == True:
            return True
        elif choice == False:
            return False
        else:
            assert(False)


    def mainloopStart(self):
        job_thread = threading.Thread(target=self.mainloop)
        job_thread.start()


    def mainloop(self):
        sleep(1)


if __name__ == "__main__":
    Pomodoro().run()

