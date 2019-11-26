#!/usr/bin/python3

import sys
from os import listdir
from os.path import isfile, join
import subprocess

CMD = 'java -cp "./*" com.yahoo.sketches.characterization.Job {}'

TESTS = ["figure_1", "figure_6_a", "figure_6_b", "figure_7", "figure_8", "figure_9", "table_2"]


def createTest(testName):
    path = join("conf_files", testName)
    confFiles = [join(path, f) for f in listdir(path) if f.endswith(".conf")]
    print(confFiles)
    for confFile in confFiles:
        subprocess.run(CMD.format(confFile), shell=True)
    


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in TESTS:
        print("USAGE: ", sys.argv[0], TESTS)
        exit(1)
    
    createTest(sys.argv[1])