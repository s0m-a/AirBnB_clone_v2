#!/usr/bin/python3
<<<<<<< HEAD
"""
module for package web_static file
"""
import os
import datatime
=======
# Fabfile to generates a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
>>>>>>> 6ebfb93d91a6f8b3f9f869009408f2f65e290647
from fabric.api import local


def do_pack():
    """ package function """
<<<<<<< HEAD
    if not os.path.isdir("./versions"):
        os.makedirs("./versions")
    xtime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    local("tar -czzf versions/web_static_{}.tgz web_static/*".format(xtime))
    return ("{}/versions/web_static_{}.tgz".format(os.path.dirname(
        os.path.abspath(__file__)), xtime))
=======
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
>>>>>>> 6ebfb93d91a6f8b3f9f869009408f2f65e290647
