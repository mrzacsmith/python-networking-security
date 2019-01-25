__author__ = 'silverback'

import os
from subprocess import call

print(os.getcwd())
print(os.getpid())
print(os.getenv("PATH"))

os.system("dir")

input = input("Hit enter")
# call(["dir"]