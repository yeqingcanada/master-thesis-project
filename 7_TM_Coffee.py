import os, subprocess
import re

tm_coffee_out = "/home/ye_qin/data/7_tm_coffee/output/"
make_db_output="/home/ye_qin/data/1_blast/2/clean_swiss_prot_2.fasta"
d = os.walk(r"/home/ye_qin/data/7_tm_coffee/input/")

# tm_coffee_out = "/Users/qingye/Desktop/experiment_test/7_tm_coffee/"
# make_db_output="/Users/qingye/Desktop/experiment_test/1_blast/2/clean_swiss_prot_2.fasta"
# d = os.walk(r"/Users/qingye/Desktop/experiment_test/1_blast/3/3/")

tm_coffee_valid_file_list = []
for path,dir_list,file_list in d:
    for file_name in file_list:
        prog = re.compile('^\d')
        result = prog.match(file_name)
        if (result):
            tm_coffee_valid_file_list.append(file_name)
        else:
            print ('Invalid File Name :' + file_name)
    for file_name in tm_coffee_valid_file_list:
        tm_coffee_input_path = path + file_name
        tm_coffee_fasta_file_name = file_name[0:(len(file_name)-6)]
        tm_coffee_out_put_path = tm_coffee_out + tm_coffee_fasta_file_name + '.fasta'
        subprocess.call(["t_coffee", tm_coffee_input_path, "-outfile", tm_coffee_out_put_path, "-output", "fasta", "-mode", "psicoffee",
                         "-blast_server", "LOCAL", "-protein_db", make_db_output])


        # t_coffee /Users/qingye/Desktop/experiment_test/1_blast/3/3/1.fasta -outfile /Users/qingye/Desktop/experiment_test/7_tm_coffee/1.fasta -output fasta -mode psicoffee -blast_server LOCAL -protein_db /Users/qingye/Desktop/experiment_test/1_blast/2/clean_swiss_prot_2.fasta
