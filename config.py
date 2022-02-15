# -*- coding: utf-8 -*-
import logging
from absl import flags
import sys

Flags = flags.FLAGS
flags.DEFINE_string('user_name', 'DummyUser', 'user name')
flags.DEFINE_string('partner_name', 'DummyPartner', 'partner name')
flags.DEFINE_string('server_url', 'example.com', 'server url')
flags.DEFINE_boolean('fullscreen_quitable', True, 'allow quit fullscreen')
flags.DEFINE_boolean('debug_mode', False, 'debug mode')
flags.DEFINE_list('notice_interval', '25,5', 'notice interval')
#flags.DEFINE_float()
#flags.DEFINE_integer()
#flags.DEFINE_list()
#flags.DEFINE_spaceseplist()

if __name__ == "__main__":
    Flags(sys.argv)
    print('current settings:')
    print('user name: '     + Flags.user_name)
    print('partner name: '  + Flags.partner_name)
    print('server url: '    + Flags.server_url)
    print('fullscreen quitable: ' + str(Flags.fullscreen_quitable))
    print('debug mode: '    + str(Flags.debug_mode))
    print('notice interval: ' + str(Flags.notice_interval))
