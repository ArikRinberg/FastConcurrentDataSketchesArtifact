#!/usr/bin/python3

import sys
import matplotlib.pyplot as plt


InU = 0
MeanRelErr = 2
Q1 = 7
Q2 = 8
Q3 = 9
Q4 = 10
Q5 = 11
Q6 = 12
Q7 = 13

LEGEND= ["MeanRelErr", "Q(.00135)", "Q(.02275)", "Q(.15866)", "Q(.5)", "Q(.84134)", "Q(.97725)", "Q(.99865)"]

def parseFile(filename):
    data = dict()
    with open(filename, 'r') as file:
        for line in file:
            splitline = line.split()
            if len(splitline) == 18:
                if splitline[4] == "4096":
                    data[splitline[InU]] = [splitline[MeanRelErr]] + splitline[Q1:Q7+1]
    for valIndex in range(8):
        plt.plot([float(x) for x in list(data.keys())], [float(x[valIndex]) for x in list(data.values())], label=LEGEND[valIndex])
    plt.legend()
    plt.ylim((-0.1, 0.1))
    plt.xscale("log")
    plt.show()
    
    
            
            
            
if __name__ == "__main__":
    if len(sys.argv) < 2    :
        print("USAGE: ", sys.argv[0], "ConcurrentThetaAccuracyProfile*.txt")
        exit(1)
    parseFile(sys.argv[1])

