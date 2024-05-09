import multiprocessing
import os
workers = multiprocessing.cpu_count()  * 2 + 1
threads = multiprocessing.cpu_count()  * 2
timeout = 3000
errorlog = '-'
loglevel = 'info'
bind='127.0.0.1:8001'
pidfile='/tmp/integrador_diariodeobra.pid'
