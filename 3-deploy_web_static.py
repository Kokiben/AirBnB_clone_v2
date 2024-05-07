#!/usr/bin/python3
"""Print a Fabric script (based on the file 2-do_deploy_web_static.py)"""

import os
from datetime import datetime
from fabric.api import env, local, put, run


env.hosts = ['54.237.62.80', '54.236.33.150']


def do_pack():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    run_tim = datetime.now()
    rst = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        run_tim.year,
        run_tim.month,
        run_tim.day,
        run_tim.hour,
        run_tim.minute,
        run_tim.second
    )
    try:
        print("Packing web_static to {}".format(rst))
        local("tar -cvzf {} web_static".format(rst))
        size_arrch = os.stat(rst).st_size
        print("web_static packed: {} -> {} Bytes".format(rst, size_arrch))
    except Exception:
        rst = None
    return rst


def do_deploy(archive_path):
    """Creates and distributes an archive to my web servers"""
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
        print('New version is now LIVE!')
        success_arr_path = True
    except Exception:
        success_arr_path = False
    return success_arr_path


def deploy():
    """Deploy the web_static archive"""
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False
