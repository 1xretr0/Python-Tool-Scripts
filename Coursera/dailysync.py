#!/usr/bin/env python
from multiprocessing import Pool
import subprocess
import os

def run(task):
        src = task
        dest = "data/prod_backup/"
        subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__":
        tasks = []
        for root, dirs, files in os.walk("data"):
                for name in dirs:
                        tasks.append(name)
        p = Pool(len(tasks))
        p.map(run, tasks)
