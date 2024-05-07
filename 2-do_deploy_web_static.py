#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py)"""
import os
from fabric.api import env, put, run

env.hosts = ['54.237.62.80', '54.236.33.150']


def do_deploy(archive_path):
    """Distributes an archive to my web servers"""
    if not os.path.exists(archive_path):
        return False
    nam_fl = os.path.basename(archive_path)
    name_fldr = nam_fl.replace(".tgz", "")
    path_fldr = "/data/web_static/releases/{}/".format(name_fldr)
    success_arr_path = False
    try:
        put(archive_path, "/tmp/{}".format(nam_fl))
        run("mkdir -p {}".format(path_fldr))
        run("tar -xzf /tmp/{} -C {}".format(nam_fl, path_fldr))
        run("rm -rf /tmp/{}".format(nam_fl))
        run("mv {}web_static/* {}".format(path_fldr, path_fldr))
        run("rm -rf {}web_static".format(path_fldr))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path_fldr))
        print("New version deployed!")
        success_arr_path = True
    except Exception:
        success_arr_path = False
    return success_arr_path
