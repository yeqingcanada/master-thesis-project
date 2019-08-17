import sys,os, subprocess
import re
from Bio.Align.Applications import ClustalOmegaCommandline
from os.path import isfile, join
import shutil

clustalw_exe = "/Users/qingye/Downloads/clustalo"
path_out = "/Users/qingye/Desktop/experiment_test/3_clustalomega/"
blast_output = "/Users/qingye/Desktop/experiment_test/1_blast/3/3/"
c = os.walk(blast_output)

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
        clustalomega_cline = ClustalOmegaCommandline(clustalw_exe,infile=input_path, outfile=out_put_path)
        child = subprocess.call(str(clustalomega_cline), stdout=subprocess.PIPE, shell=True)


org_files = [each_file for each_file in os.listdir(blast_output)
             if isfile(join(blast_output, each_file)) and not each_file.startswith('.')]

out_files = [each_file for each_file in os.listdir(path_out)
             if isfile(join(path_out, each_file)) and not each_file.startswith('.')]

index_dict = {}

for i in range(len(org_files)):
    if org_files[i] not in out_files:
        index_dict.update({join(blast_output, org_files[i]): join(path_out, org_files[i])})

for key in index_dict:
    shutil.copyfile(key, index_dict[key])
