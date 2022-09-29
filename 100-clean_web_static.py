#!/usr/bin/python3
from fabric.api import *

env.hosts = ["3.238.28.101", "3.209.82.116"]


def do_clean(number=0):
    """deletes out of data archives"""

    number = int(number)
    if number == 1 or number == 0:
        local("cd versions; ls | head -n -1 | xargs rm -rf")
        run("cd /data/web_static/releases; ls | head -n -1 | xargs rm -rf")
    else:
        local("cd versions; ls | head -n -{} | xargs rm -rf".format(number))
        run(
            "cd /data/web_static/releases; ls | head -n -{} | xargs rm -rf".format(
                number
            )
        )
