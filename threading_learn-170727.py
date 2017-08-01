#!/usr/bin/env Python

import threading
import time


import logging


import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

t = threading.Thread(name='non-daemon', target=non_daemon)




def main():


    d.start()
    t.start()

    d.join()
    t.join()


    print threading.active_count()
    print threading.enumerate()
    print threading.current_thread()

if __name__ == '__main__':
    main()
