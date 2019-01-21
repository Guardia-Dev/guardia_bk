#!/bin/bash

gunicorn gua.wsgi:application --bind 127.0.0.1:8002

NAME='gua'
DJANGODIR=/home/ubuntu/guardia/guardia_bk/gua
SOCKFILE=/home/ubuntu/guardia/guardia_bk/gunicorn.sock
USER=ubuntu # 运行此应用的用户
NUM_WORKERS=3 # gunicorn使用的工作进程数
DJANGO_SETTINGS_MODULE=gua.settings # django的配置文件
DJANGO_WSGI_MODULE=gua.wsgi # wsgi模块
LOG_DIR=/home/ubuntu/logs # 日志目录

echo "starting $NAME as `whoami`"

# 激活python虚拟运行环境
cd $DJANGODIR
source /home/ubuntu/.local/share/virtualenvs/guardia_bk-m8H9oeng/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# 如果gunicorn.sock所在目录不存在则创建
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# 启动Django

/home/ubuntu/.local/share/virtualenvs/guardia_bk-m8H9oeng/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
    --daemon \
    --name $NAME \
    --workers $NUM_WORKERS \
    --user=$USER --group=$GROUP \
    --log-level=debug \
    --bind=unix:$SOCKFILE \
    --access-logfile=${LOG_DIR}/gunicorn_access.log \
