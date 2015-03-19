#! /usr/bin/python3

from log import Log
from arbo import Arbo
from protocol import Proto
import json

import os

def get_last_update():
    return open('.storeit/last_update').read()

if __name__ == '__main__':

    try:
        os.makedirs('.storeit')
    except IOError as e:
        Log.log('cannot make base directory', Log.WARN) # check for errors here

    arbo = Arbo.get()
    print(arbo)
    exit(0)

    com = Proto()
    com.send('HELO Sevauk')
    com.send('LAST ' + get_last_update())
    com.send('ARBO ' + json.dumps(arbo))
