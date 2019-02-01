ps -ef | grep gunicorn | grep -v 'grep' | awk '{print $2}'
