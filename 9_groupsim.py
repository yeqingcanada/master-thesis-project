import subprocess
import re
import os
from groupsim import readFileList
from groupsim import startPoint

c = os.walk(r"/Users/qingye/Desktop/experiment_test/9_groupsim/input/")
groupsim = "/Users/qingye/Downloads/group_sim_sdp/group_sim_sdp.py"
path_out="/Users/qingye/Desktop/experiment_test/9_groupsim/output/"
metric = "/Users/qingye/Downloads/group_sim_sdp/blosum62.bla"
list = []


# >,| fasta, clustal
def char():
    count = 0
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
            fs = open(input_path, 'r+')
            lines = fs.readlines()
            for i in range(0, len(lines)):
                line2=lines[i]
                if line2[:1] == ">":
                    line2 = line2.replace("\n", "")
                    count +=1
                    if count<=6:
                        line2 = line2 +"|group1\n"
                    else: line2 = line2 + "|group2\n"
                f= open(out_put_path,'a')
                f.writelines(line2)
            count = 0
def GroupSim():
    list2 = []
    out2 = "/Users/qingye/Desktop/experiment_test/9_groupsim/output2/"
    groupsim = "/Users/qingye/Downloads/group_sim_sdp/group_sim_sdp.py"
    path_out="/Users/qingye/Desktop/experiment_test/9_groupsim/output/"
    b = os.walk(path_out)
    for path2, dir_list2, file_list2 in b:
        for file_name2 in file_list2:
            prog2 = re.compile('^\d')
            result = prog2.match(file_name2)
            if (result):
                list2.append(file_name2)
            else:
                print ('Invalid File Name :' + file_name2)
        for file_name2 in list2:
            input_path2 = path2 + file_name2
            out_put_path2 = out2 + file_name2
            subprocess.call(["python", groupsim, "-n", "-m", metric, "-w", "1", "-o", \
                             out_put_path2, input_path2, "group1", "group2"])


if __name__ == '__main__':
    # char()
    GroupSim()
    startPoint()