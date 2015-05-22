#!/usr/bin/python

import subprocess

subprocess.call( ["sudo","apt-get", "-fy", "update"])
subprocess.call( ["sudo","apt-get", "-fy", "install" , "transmission-daemon"])



