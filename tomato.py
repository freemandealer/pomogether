import rumps
import os
import schedule
import time
import threading


class Tomato(rumps.App):
    def __init__(self):
        super(Tomato, self).__init__("20Twenty20",icon="data/icon.tiff")
        self.work_menu = rumps.MenuItem("work", callback=self.work)
        self.rest_menu = rumps.MenuItem("rest",callback=None)
        self.menu = [self.work_menu, self.rest_menu, None]
        self.alarm_time = [5, 3, 1] # alarm when work for 25, 40 and 50 min
        self.time_idx = 0
        self.mainloopStart()


    def work(self,_):
        print "Start"
        self.work_menu.set_callback(None)
        self.rest_menu.set_callback(self.rest)
        assert(self.time_idx < len(self.alarm_time))
        self.timer = threading.Timer(self.alarm_time[self.time_idx], self.timerAction)
        self.timer.start()


    def rest(self,_):
        print "Stop"
        self.timer.cancel()
        self.rest_menu.set_callback(None)
        self.work_menu.title = "work"
        self.work_menu.set_callback(self.work)
        self.time_idx = 0

        choice = self.yesNoMsgBox('Have a rest and then click OK to start next period.')
        if choice == True:
            self.work(None)
        else:
            exit()


    def timerAction(self):
        print "timer"
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
        os.system("python2 runtimer.py 20 ./data/quotes.txt false 50")


    def notifyRest(self):
        choice = self.yesNoMsgBox('do you want to cont?')
        if choice == True:
            return True
        elif choice == False:
            return False
        else:
            assert(False)


    def yesNoMsgBox(self,s=None):
        ret = os.system(\
                "osascript -e 'Tell application \"System Events\" to display dialog \""\
                +s+"\"'")
        if ret == 0:
            return True
        else:
            return False


    def mainloopStart(self):
        job_thread = threading.Thread(target=self.mainloop)
        job_thread.start()


    def mainloop(self):
        time.sleep(1)


if __name__ == "__main__":
    Tomato().run()

