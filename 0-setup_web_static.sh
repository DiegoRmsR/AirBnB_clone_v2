#!/usr/bin/python3
#script that sets up your web servers for the deployment of web_static. It must
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "test Nginx" >> /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i "37i\\\n\tlocation hbnb_static/ {\n\t\t alias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
