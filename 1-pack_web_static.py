#!/usr/bin/python3
"""" Fabric script that generates a .tgz archive from the
contents of theweb_staticfolder of your AirBnB Clone repo,
using the function do_pack. """

from datetime import datetime
from fabric.api import *
import os


def do_pack():
    """ Do the pack to Fabric """
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")

        date = datetime.now()
        date = dat.strftime("%Y%m%d%H%M%S")
        comstr = "versions/web_static_{}.tgz".format(date)

        local("tar -cvzf {} web_static".format(comstr))
        return comstr

    except:
        return None
