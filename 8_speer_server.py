import subprocess
import re
import os
import sys

from speer import startPoint

path_out = "/Users/qingye/Desktop/experiment_test/8_speer_server/output/"
c=os.walk("/Users/qingye/Desktop/experiment_test/8_speer_server/input/")

# path_out = "/home/ye_qin/8_speer_server/output/"
# c=os.walk("/home/ye_qin/8_speer_server/input/")

list = []
def speer():
    for path,dir_list,file_list in c:
        for file_name in file_list:
            prog = re.compile('^\d')
            result = prog.match(file_name)
            if (result):
                list.append(file_name)
            else:
                print ('Invalid File Name :' + file_name)
        for file_name in list:
            input_path = path + file_name
            filename = file_name[0:(len(file_name)-6)]
            out_put_path = path_out + filename + '.fasta'
            os.chdir("/Users/qingye/Downloads/Speer/")
            subprocess.call(["./SPEER","-wRE", "1", "-wEDist", "1", "-wERate", "0",\
                             "-i",input_path,"-o",out_put_path,"6","5"])

if __name__ == '__main__':
    speer()
    startPoint()