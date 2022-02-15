# -*- coding: utf-8 -*-
import logging
from absl import flags
from config import *
import time
import random
import libs.ptext as ptext
import sys
import pygame
import json
from time import *
import paths

flags.DEFINE_boolean('quitable', True, 'quitable')
flags.DEFINE_integer('time', 20, 'time')
ptext.DEFAULT_FONT_NAME = "data/Roboto-Light.ttf"


def get_info(who):
    s = ''
    if who == 'user':
        s = Flags.user_name
        show_off_file = paths.user_showoff_path
    elif who == 'partner':
        s = Flags.partner_name
        show_off_file = paths.partner_showoff_path

    try:
        fd = open(show_off_file, 'r')
        data = json.loads(fd.read())
        fd.close()
    except:
        logging.error('error to parse show off json file of ' + who)
        return s

    s += '\nWorkLength: '
    wl = data['WorkLength']
    for i in range(0, int(wl/5)):
        s += '|'
    s += str(wl)
    s += '\nBreakLength: '
    bl = data['BreakLength']
    for i in range(0, int(bl/5)):
        s += '|'
    s += str(bl)

    s += '\n\nTasks:\n'
    t = data['Tasks']
    for task,length in t.items():
        s += '   |- ' + task + ' : ' + str(length) + '\n'

    s += '\n'
    s += data['slogan']
    return s


def render_multi_line(text, x, y, fsize, screen, font):
        lines = text.splitlines()
        for i, l in enumerate(lines):
            screen.blit(font.render(l, 0, (255,255,255)), (x, y + fsize*i))


def fullscreen_display(time,escapable):
    pygame.init()
    pygame.font.init()
    font=pygame.font.SysFont('arialunicodems',20)
    try:
        pygame.mouse.set_visible(False)
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        w, h = screen.get_size()
        timeMS = time*1000
        startTime = pygame.time.get_ticks()
        user_info = get_info('user')
        partner_info = get_info('partner')
        while True:
            for event in pygame.event.get():
                if escapable:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                            pygame.quit()
                            return
            now = pygame.time.get_ticks()
            delta = now-startTime
            if delta > timeMS + 15*1000*60:
                # must quit after timeMS+15mins to avoid system hangup
                break
            elif delta > timeMS + 900:
                #allow quit after timeMS
                escapable = True
                ptext.draw("press 'Enter' to continue",midtop=(w/2,9*h/10),fontsize=30,align="center",color="grey")
                pygame.display.update()
            else:
                screen.fill((0, 0, 0))
                time_str = str(time-int(delta/1000))
                ptext.draw(time_str,midtop=(w/2,8*h/10),fontsize=60,align="center",color="grey")

            render_multi_line(user_info, 0, 0, 30, screen, font)
            render_multi_line(partner_info, w/2, 0, 30, screen, font)
            pygame.display.update()
            sleep(1) # slow down the loop to save CPU

    finally:
        pygame.quit()


def main(argv):
    Flags(argv)
    paths.path_init()
    logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='fullscreen.log',
                filemode='a')
    fullscreen_display(Flags.time , Flags.quitable)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
