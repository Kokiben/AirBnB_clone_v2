#!/usr/bin/python3
"""Print a Fabric script for generates a .tgz"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """the web_static folder of your AirBnB Clone repo"""
    local("mkdir -p versions")
    ph = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    rst = local("tar -cvzf {} web_static"
                   .format(ph))

    if rst.failed:
        return None
    return ph
