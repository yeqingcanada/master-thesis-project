from Bio.Align.Applications import ClustalwCommandline
import sys,os, subprocess
import re

import shutil

# copy folder because .dnd
# shutil.copytree('/Users/qingye/Desktop/experiment_test/1_blast/3/3/', '/Users/qingye/Desktop/experiment_test/2_clustalW/input/')

my_mac_path = "/Users/qingye/Desktop/experiment_test/"
# kronos_path = "/home/ye_qin/"

clustalw_exe = "/Users/qingye/Downloads/clustalw-2.1-macosx/clustalw2"
# clustalw_exe = "/usr/bin/blastp"

path_out = my_mac_path + "2_clustalW/output/"
c = os.walk(my_mac_path + "2_clustalW/input/")

# path_out = kronos_path + "2_clustalW/output/"
# c = os.walk(kronos_path + "2_clustalW/input/")

os.makedirs(path_out)
clustalw_valid_file_list = []
for path,dir_list,file_list in c:
    for file_name in file_list:
        prog = re.compile('^\d')
        result = prog.match(file_name)
        if (result):
            clustalw_valid_file_list.append(file_name)
        else:
            print ('Invalid File Name :' + file_name)
    for file_name in clustalw_valid_file_list:
        clustalw_input_path = path + file_name
        clustalw_fasta_file_name = file_name[0:(len(file_name)-6)]
        clustalw_out_put_path = path_out + clustalw_fasta_file_name + '.fasta'
        clustalw_cline = ClustalwCommandline(clustalw_exe, infile=clustalw_input_path, outfile=clustalw_out_put_path, OUTPUT="FASTA")
        child = subprocess.call(str(clustalw_cline),stdout=subprocess.PIPE,shell=True)