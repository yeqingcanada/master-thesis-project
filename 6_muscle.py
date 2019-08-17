import os, subprocess
import re
from Bio.Align.Applications import MuscleCommandline

muscle_exe = "/Users/qingye/Downloads/muscle"
path_out = "/Users/qingye/Desktop/experiment_test/6_muscle/"
c = os.walk(r"/Users/qingye/Desktop/experiment_test/1_blast/3/3/")
list = []
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
        fasta_file_name = file_name[0:(len(file_name)-6)]
        out_put_path = path_out + fasta_file_name + '.fasta'
        muscle_cline = MuscleCommandline(muscle_exe, input=input_path, out=out_put_path)
        child = subprocess.call(str(muscle_cline), stdout=subprocess.PIPE, shell=True)