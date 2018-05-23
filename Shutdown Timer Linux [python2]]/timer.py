#!/usr/bin/python
import os
import time
import progressbar
import sys

os.system('clear')

# print isinstance(int(sys.argv[2]), int)
# print sys.argv[2].is_integer()

if sys.argv[1] == '-h':
	waktu = int(sys.argv[2]) * 3600
elif sys.argv[1] == '-m':
	waktu = int(sys.argv[2]) * 60
elif sys.argv[1] == '-s':
	waktu = int(sys.argv[2])
else:
	print "ERROR"
	sys.exit()

# result = commands.getstatusoutput(command)
# print result


widgets=['[',progressbar.Percentage(),'] ',progressbar.Bar(marker='#',fill='.',left='',right =''),' [', progressbar.ETA(format = '%(eta)8s'), ']',
]

for i in progressbar.progressbar(range(waktu), redirect_stdout=True,widgets=widgets):
    # print('Some text', waktu *)
    time.sleep(1)

os.system('poweroff')
