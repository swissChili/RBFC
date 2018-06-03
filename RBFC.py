import sys
import os
from tqdm import tqdm
import math

args = sys.argv
class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
colors = bcolors()
if (len(args) < 2) or (args[1] == "-help") or (args[1] == "-h"):
	print(colors.HEADER + "RBFC Usage:" + colors.ENDC)
	print(colors.BOLD + "The first parameter should be the path to the file you wish to write to" + colors.ENDC)
	print(colors.BOLD + "The second parameter should be the amount of megabytes you wish the file to be" + colors.ENDC)
	print(colors.UNDERLINE + "EG: rbfc.py /path/to/file.txt 100" + colors.ENDC)
elif len(args) == 3:
	m = args[2]
	b = float(m) * 1000000
	p = args[1]
	print("Writing to " + p)
	i = 0
	with open(p, "x") as f:
			f.write("0")
			f.close()
	bp = int(b) / 10000
	for i in tqdm(range(math.floor(bp))):
		with open(p, "a") as f:
			f.write("0" * 10000)
			f.close()
		i = i + 1
	print(colors.BOLD + colors.UNDERLINE + colors. HEADER + "COMPLETE! " + m + " MB FILE CREATED")
	
