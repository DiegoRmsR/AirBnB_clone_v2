#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the
function do_deploy """

from fabric.api import *
import os


env.hosts = ['34.73.121.160', '35.185.87.206']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ Do deploy """
    if not os.path.exists(archive_path):
            return False
    try:
        file_name = os.path.basename(archive_path)
        filename = file_name.split(".")
        web_name = filename[0]
        dire_file = "/data/web_static/releases/{}/".format(web_name)
        put(archive_path, '/tmp/')
        run("mkdir -p {}{}/".format(dire_file))
        run("tar -xzf /tmp/{} -C {}{}/".format(file_name, dire_file))
        run("rm /tmp/{}".format(file_name))
        run("mv {}{}/web_static/* {}{}/".format(dire_file, dire_file))
        run("rm -rf {}{}web_static".format(dire, web_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(dire_file))
        print("New version deployed!")
        return True

    except:
        return False
