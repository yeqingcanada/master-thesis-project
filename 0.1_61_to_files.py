from Bio import SeqIO
import os

# original dataset 61datas to 61files
file_type = "fasta"
# origianl_input = "/Users/qingye/Desktop/experiment_test/0_data/2.fasta"
# original_output = "/Users/qingye/Desktop/experiment_test/0_data/2/"

origianl_input = "/Users/qingye/Desktop/experiment_test/0_data/dataset.fasta"
original_output = "/Users/qingye/Desktop/experiment_test/0_data/2/"

os.makedirs(original_output)
f=0

for seq_record in SeqIO.parse(origianl_input, file_type):
    f=f+1
    e=str(f)
    o_output = original_output + e + ".fasta"
    SeqIO.write(seq_record, o_output, "fasta")

