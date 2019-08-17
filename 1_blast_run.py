import subprocess
from Bio.Blast.Applications import NcbiblastpCommandline
from Bio import SeqIO
from Bio import SearchIO
import re
from os.path import isfile, join
import os
import sys

my_mac_path = "/Users/qingye/Desktop/experiment_test/"
kronos_path = "/home/ye_qin/"

# x = kronos_path + "1_blast/3/1/"
# y = kronos_path + "1_blast/3/2/"
# z = kronos_path + "1_blast/3/3/"
# o = kronos_path + "1_blast/2/clean_swiss_prot_2.fasta"
# p = kronos_path + "1_blast/1/"

x = my_mac_path + "1_blast/3/1/"
y = my_mac_path + "1_blast/3/2/"
z = my_mac_path + "1_blast/3/3/"
o = my_mac_path + "1_blast/2/clean_swiss_prot_2.fasta"
p = my_mac_path + "1_blast/1/"
# blast run
def run():
    blast_exe = "/usr/bin/blastp"
    # blast_exe="/Users/qingye/Downloads/ncbi-blast-2.7.1+/bin/blastp"
    make_db_output = o
    blast_out_path = x
    a = os.walk(p)

    blast_valid_file_list_first = []
    for path,dir_list,file_list in a:
        for file_name in file_list:
            prog = re.compile('^\d')
            result = prog.match(file_name)
            if (result):
                blast_valid_file_list_first.append(file_name)
            else:
                print ('Invalid File Name :' + file_name)
        for file_name in blast_valid_file_list_first:
            blast_query_path = path + file_name
            blast_name = file_name[0:(len(file_name)-6)]
            des_blast_file = blast_out_path + blast_name + '.xml'
            blastp_cline = NcbiblastpCommandline(blast_exe, query=blast_query_path, db=make_db_output, evalue=0.001,outfmt=5,out=des_blast_file,max_target_seqs=10)
            subprocess.call(str(blastp_cline), stdout=subprocess.PIPE, shell=True)
# blast xml to fasta
def xml():
    blast_out_path = x
    blast_fasta = y
    b = os.walk(blast_out_path)
    blast_valid_file_list = []
    for path,dir_list,file_list in b:
        for file_name in file_list:
            prog = re.compile('^\d')
            result = prog.match(file_name)
            if (result):
                blast_valid_file_list.append(file_name)
            else:
                print ('Invalid File Name :' + file_name)
        for file_name in blast_valid_file_list:
            blast_xml_file = path + file_name
            fasta_file_name = file_name[0:(len(file_name)-4)]
            des_fasta_file = blast_fasta + fasta_file_name + '.fasta'
            blast_qresult = SearchIO.read(blast_xml_file,'blast-xml')
            records = []
            for hit in blast_qresult:
                records.append(hit[0].hit)
            SeqIO.write(records, des_fasta_file, "fasta")
            del records[:]

path_splitor = "/"
one_sequence_file_folder = p
multiple_seqs_file_folder = y
target_file_folder = z

def merge_file(filename):
    with open(join(one_sequence_file_folder, filename), "r") as singlefile:
        s = singlefile.read()

    with open(join(multiple_seqs_file_folder, filename), "r") as multiplefile:
        m = multiplefile.read()

    with open(join(target_file_folder, filename), 'w') as targetfile:
        targetfile.write(s + m)

def merge():
    if os.path.exists(target_file_folder):
        os.rmdir(target_file_folder)

    os.makedirs(target_file_folder)

    one_sequence_files = [join(one_sequence_file_folder, each_file) for each_file in
                          os.listdir(one_sequence_file_folder)
                          if isfile(join(one_sequence_file_folder, each_file)) and not each_file.startswith('.')]

    multi_sqs_files = [join(multiple_seqs_file_folder, each_file) for each_file in os.listdir(multiple_seqs_file_folder)
                       if isfile(join(multiple_seqs_file_folder, each_file)) and not each_file.startswith('.')]

    if len(one_sequence_files) != len(multi_sqs_files):
        print 'the length of one sequence files does not match the length of multiple sequence files'
        print "the length of single sequence files is %d " % len(one_sequence_files)
        print "the length of multiple sequence files is %d " % len(multi_sqs_files)
        sys.exit(1)

    one_sequence_files = {each.split(path_splitor)[-1]: 0 for each in one_sequence_files}
    multi_sqs_files = {each.split(path_splitor)[-1]: 0 for each in multi_sqs_files}

    for each in one_sequence_files:
        if each not in multi_sqs_files:
            print "the file %s doesn't in the multiple sequence folder" % each
            continue

        merge_file(each)

    print "Done!"

if __name__ == '__main__':
    # os.makedirs(x)
    # os.makedirs(y)
    # os.makedirs(z)
    # run()
    xml()
    merge()