#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ["3.238.28.101", "3.209.82.116"]


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        print("False")
        return False

    filename = archive_path.split("/")
    filename = filename[1]
    fname = filename.split(".")
    fname = fname[0]

    newpath = "/data/web_static/releases/{}/".format(fname)

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(newpath))
        run("tar -xzf /tmp/{} -C {}".format(filename, newpath))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(newpath, newpath))
        run("rm -rf {}web_static".format(newpath))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(newpath))
        print("New version deployed!")
        return True
    except Exception:
        print("False 2")
        return False
