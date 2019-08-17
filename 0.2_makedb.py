import subprocess
import os

# larget_file_path = "/home/ye_qin/project/new_ordered_file.fasta"
# small_file_path = "/home/ye_qin/project/original_dataset.fasta"
# new_large_file_name = "/home/ye_qin/project/new_larget_file.fasta"

larget_file_path = "/Users/qingye/Desktop/experiment_test/0_data/new_larget_file.fasta"
small_file_path = "/Users/qingye/Desktop/experiment_test/0_data/2.fasta"
x="/Users/qingye/Desktop/experiment_test/1_blast/2/"
new_large_file_name = x+"new_larget_file.fasta"

def removedup():
    small_content = []
    larget_content = {}

    with open(small_file_path, "r") as smallFile:
        oneline = smallFile.readline()
        temp = []
        while oneline:

            if not oneline.strip("\n").strip():
                oneline = smallFile.readline()
                continue

            if oneline.startswith(">"):
                if temp:
                    small_content.append("".join(temp))
                    temp = []
            else:
                temp.append(oneline.strip('\n'))

            oneline = smallFile.readline()
    small_content.append("".join(temp))

    with open(larget_file_path, "r") as largeFile:
        oneline = largeFile.readline()
        temp = []
        entire = []
        while oneline:

            if not oneline.strip("\n").strip():
                oneline = largeFile.readline()
                continue

            if oneline.startswith(">"):
                if entire:
                    larget_content.update({"".join(temp): "".join(entire)})
                    temp = []
                    entire = []
            else:
                temp.append(oneline.strip("\n"))

            entire.append(oneline)
            oneline = largeFile.readline()
    larget_content.update({"".join(temp): "".join(entire)})

    print "Before removing, the number of larget dataset is %d" % len(larget_content)

    for each in small_content:
        if each in larget_content:
            del larget_content[each]

    print "After removing duplicate records, the number of larget dataset is %d" % len(larget_content)

    with open(new_large_file_name, "w") as result:
        result.writelines(larget_content.values())

    print "done!"

def makedb():

    make_db_output= x+ "clean_swiss_prot_2.fasta"
    subprocess.call(["makeblastdb","-in",new_large_file_name,"-out",make_db_output,"-dbtype","prot"])

if __name__ == '__main__':
    removedup()
    makedb()