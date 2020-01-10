#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static. It must
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "test nginx" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current/
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "37i\\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
