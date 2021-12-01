from subprocess import Popen
from time import sleep

Popen('python webpage.py')
sleep(5)
Popen('python api_test.py')


