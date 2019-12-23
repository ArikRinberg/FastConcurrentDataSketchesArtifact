#!/usr/bin/python3

import sys
import matplotlib.pyplot as plt
from collections import defaultdict


def parseFile(filenames):
    data = defaultdict(lambda : dict())
    nThreads = set()
    for filename in filenames:
      currThreads = None
      with open(filename, 'r') as file:
          for line in file:
            if "CONCURRENT_THETA_numWriters" in line:
              splitline = line.split("=")
              currThreads = int(splitline[1])
              nThreads.add(currThreads)
            splitline = line.split()
            if len(splitline) == 3:
              if splitline[0] not in {"InU", "START", "ReadableDateFormat=yyyy/MM/dd", "END"}:
                print(splitline)
                InU = int(splitline[0])
                KuPs = 1000 / float(splitline[2])
                data[InU][currThreads] = KuPs
    for n in nThreads:
      plt.plot([x for x in data.keys()], [x[n] for x in data.values()], label=n)
    plt.legend()
    plt.ylim((-0.1, 0.1))
    plt.xscale("log")
    plt.show()
    
    
            
            
            
if __name__ == "__main__":
    if len(sys.argv) < 2    :
        print("USAGE: ", sys.argv[0], "ConcurrentThetaMultithreadedSpeedProfile*.txt")
        exit(1)
    parseFile(sys.argv[1:])

