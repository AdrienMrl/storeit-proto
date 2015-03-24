#! /usr/bin/python3

import os
from client import Client

if __name__ == '__main__':

    os.chdir('demo')
    
    cli = Client()
    cli.run()
