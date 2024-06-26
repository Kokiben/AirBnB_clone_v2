#!/usr/bin/python3
'''Generates a .tgz archive from the contents of the web_static'''

from fabric.api import local
from datetime import datetime


def do_pack():
    '''web_static folder'''
    local("mkdir -p versions")
    ph = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    rst = local("tar -cvzf {} web_static"
                   .format(ph))

    if rst.failed:
        return None
    return ph
