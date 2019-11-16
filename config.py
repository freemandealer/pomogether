# -*- coding: utf-8 -*-
import logging
import gflags
import sys

Flags = gflags.FLAGS 
gflags.DEFINE_string('user_name', 'DummyUser', 'user name')
gflags.DEFINE_string('partner_name', 'DummyPartner', 'partner name')
gflags.DEFINE_string('server_url', 'example.com', 'server url')
gflags.DEFINE_boolean('fullscreen_quitable', True, 'allow quit fullscreen')
gflags.DEFINE_boolean('debug_mode', False, 'debug mode')
gflags.DEFINE_list('notice_interval', '25,5', 'notice interval')
#gflags.DEFINE_float()
#gflags.DEFINE_integer()
#gflags.DEFINE_list()
#gflags.DEFINE_spaceseplist()

if __name__ == "__main__":
    Flags(sys.argv)
    print('current settings:')
    print('user name: '     + Flags.user_name)
    print('partner name: '  + Flags.partner_name)
    print('server url: '    + Flags.server_url)
    print('fullscreen quitable: ' + str(Flags.fullscreen_quitable))
    print('debug mode: '    + str(Flags.debug_mode))
    print('notice interval: ' + str(Flags.notice_interval))
