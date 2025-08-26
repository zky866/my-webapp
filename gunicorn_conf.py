import multiprocessing
import os

import gunicorn

bind = '0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
reload = True
loglevel = 'info'
timeout = 600
wsgi_app = config.wsgi.application

log_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
accesslog = os.path.join(log_path, 'access.log')
errorlog = os.path.join(log_path, 'error.log')