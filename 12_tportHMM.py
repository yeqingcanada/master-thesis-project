from os.path import join
import math
from decimal import *
import numpy as np

file = "C:\Users\umroot\Desktop\\"

with open(join(file,"score.txt"), "r") as fileread:
    for count, oneline in enumerate(fileread, start = 1):
        index = oneline.index(":")
        content = oneline[(index+2):]
        if int(content) == 0:
            print("unclassified")
        elif 1 <= int(content) <= 70:
            print("Amino Acid")
        elif 71 <= int(content) <= 130:
            print("Anion")
        elif 131 <= int(content) <= 390:
            print("Cation")
        elif 391 <= int(content) <= 450:
            print("Electron")
        elif 451 <= int(content) <= 520:
            print("Protein/mRNA")
        elif 521 <= int(content) <= 580:
            print("Sugar")
        elif 581 <= int(content) <= 780:
            print("Other")