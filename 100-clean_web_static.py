#!/usr/bin/python3
<<<<<<< HEAD
""" module for  packag web_static files then deploy """
import datetime
from fabric.api import put, env, run, local
import os


env.hosts = ['100.26.164.183', '54.237.99.32']

env.user = "ubuntu"

def do_deploy(archive_path):
    """ deploy"""
    if archive_path is None or not os.path.isfile(archive_path):
        print("NOT PATH")
        return False

    xname = os.path.basename(archive_path)
    yname = xname.split(".")[0]

    put(local_path=archive_path, remote_path="/tmp/")
    run("mkdir -p /data/web_static/releases/{}".format(yname))
    run("tar -xzf /tmp/{} \
        -C /data/web_static/releases/{}".format(xname, yname))
    run("rm /tmp/{}".format(xname))
    run("rm -rf /data/web_static/current")
    run("ln -fs /data/web_static/releases/{}/ \
        /data/web_static/current".format(yname))
    run("mv /data/web_static/current/web_static/* /data/web_static/current/")
    run("rm -rf /data/web_static/curren/web_static")

    return True


def do_pack():
    """package func"""
    if not os.path.isdir("./versions"):
        os.makedirs("./versions")
    xtime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    local("tar -czzf versions/web_static_{}.tgz web_static/*".format(xtime))
    return ("{}/versions/web_static_{}.tgz".format(os.path.dirname(
        os.path.abspath(__file__)), xtime))


def deploy():
    """package func"""
    map = do_pack()
    if map is None:
        return False
    return(do_deploy(map))
=======
# Fabfile to delete out-of-date archives.
import os
from fabric.api import *

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
>>>>>>> 6ebfb93d91a6f8b3f9f869009408f2f65e290647
