#!/usr/bin/python3

import sys
import matplotlib.pyplot as plt
from collections import defaultdict


def parseFile(filenames):
    data = defaultdict(lambda : dict())
    nThreads = set()
    for filename in filenames:
      currThreads = None
      type = None
      with open(filename, 'r') as file:
          for line in file:
            if "CONCURRENT_THETA_ThreadSafe" in line and type is None:
              splitline = line.strip().split("=")
              type = "Concurrent" if splitline[1] == "true" else "Lock-Based"
            if "CONCURRENT_THETA_numWriters" in line and currThreads is None:
              splitline = line.strip().split("=")
              currThreads = int(splitline[1])
              nThreads.add(currThreads)
            splitline = line.split()
            if len(splitline) == 3:
              if splitline[0] not in {"InU", "START", "ReadableDateFormat=yyyy/MM/dd", "END"}:
                print(splitline)
                InU = int(splitline[0])
                KuPs = 1000 / float(splitline[2])
                data[type][currThreads] = KuPs
    for type in data.keys():
      throughputs = [x for x in data[type].values()]
      threads = [x for x in data[type].keys()]
      print(threads)
      print(throughputs)
      plt.plot(threads, throughputs, label=type)
    plt.legend()
    plt.show()
    
    
            
            
            
if __name__ == "__main__":
    if len(sys.argv) < 2    :
        print("USAGE: ", sys.argv[0], "ConcurrentThetaMultithreadedSpeedProfile*.txt")
        exit(1)
    parseFile(sys.argv[1:])

