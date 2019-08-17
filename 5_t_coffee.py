import os, subprocess
import re
from Bio.Align.Applications import TCoffeeCommandline

tcoffee_exe = "/Users/qingye/tcoffee/Version_11.00.8cbe486/bin/t_coffee"
tcoffee_out = "/Users/qingye/Desktop/experiment_test/5_tcoffee/"
t = os.walk(r"/Users/qingye/Desktop/experiment_test/1_blast/3/3/")

tcoffee_valid_file_list = []
for path,dir_list,file_list in t:
    for file_name in file_list:
        prog = re.compile('^\d')
        result = prog.match(file_name)
        if (result):
            tcoffee_valid_file_list.append(file_name)
        else:
            print ('Invalid File Name :' + file_name)
    for file_name in tcoffee_valid_file_list:
        tcoffee_input_path = path + file_name
        tcoffee_fasta_file_name = file_name[0:(len(file_name)-6)]
        tcoffee_out_put_path = tcoffee_out + tcoffee_fasta_file_name + '.fasta'
        tcoffee_cline = TCoffeeCommandline(tcoffee_exe, infile=tcoffee_input_path, outfile=tcoffee_out_put_path, output="fasta")
        child = subprocess.call(str(tcoffee_cline),stdout=subprocess.PIPE,shell=True)