#!/usr/bin/python3
"""" Fabric script that generates a .tgz archive from the
contents of theweb_staticfolder of your AirBnB Clone repo,
using the function do_pack. """
from datetime import datetime
from fabric.api import *
import os


def do_pack()
    """ pack to fabric"""
    try:
        if os.path.exits("versions"):
            local("mkdir versions")
        date = datetime.now()
        date = date.strftime("%Y%m%d%H%M%S")
        comstr = "versions/web_static_" + date + ".tgz"
        local("tar -cvzf {} web_static".format(comstr))
        return comstr
    except:
        return None
