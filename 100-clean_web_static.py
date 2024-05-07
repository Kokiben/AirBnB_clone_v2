#!/usr/bin/python3
""" the function do_clean """
from fabric.api import *


env.hosts = ['54.237.62.80', '54.236.33.150']
env.user = "ubuntu"


def do_clean(number=0):
    """ deletes out-of-date archives """

    nbr = int(number)

    if nbr == 0:
        nbr = 2
    else:
        nbr += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(nbr))
    ph = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(ph, nbr))
