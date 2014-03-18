#!/bin/sh


tmpPath="/home/wenshin/ks/yanwenxu/gulosity/.tmp/"
if [ ! -x "$tmpPath" ]; then
  mkdir $tmpPath
else
  echo "Directory access permission denied or already exist!"
fi


# Nginx scripts
sudo ln -f -s /home/wenshin/ks/yanwenxu/gulosity/server_conf/nginx.conf /etc/nginx/sites-enabled/gulosity_nginx.conf

sudo /etc/init.d/nginx restart


# Uwsgi scripts
pidfile=${tmpPath}"gulosity-master.pid"
if [ -f "$pidfile" ]; then
  uwsgi --stop $pidfile
fi
  uwsgi --ini server_conf/uwsgi.ini
