import subprocess
import re
import os.path

from xdet import startPoint

path_out = "/Users/qingye/Desktop/experiment_test/10_xdet/output/"
c = os.walk(r"/Users/qingye/Desktop/experiment_test/10_xdet/input/")
# metrix_path = "/Applications/JDet/conf/Maxhom_McLachlan.metric"
metrix_path = "/Applications/JDet/conf/blosum62.txt"

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
        filename = file_name[0:(len(file_name)-6)]
        out_put_path = path_out + filename + '.fasta'
        with open(out_put_path, 'w') as outputFile:
            os.chdir("/Applications/JDet/programs/")
            subprocess.call(["./xdet_osx", input_path, metrix_path, out_put_path, "-S", "10"], stdout=outputFile)
startPoint()
