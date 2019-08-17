import subprocess
import re
from os.path import join, isfile
import os

# hmmbuild
def hmmbuild():
    # path_out = "/Users/qingye/Desktop/experiment_test/11_hmmer/output/"
    # c = os.walk(r"/Users/qingye/Desktop/experiment_test/11_hmmer/input/")

    path_out = "/home/ye_qin/data/11_hmmer/output/"
    c = os.walk(r"/home/ye_qin/data/11_hmmer/input/")

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
            file_name = file_name[0:(len(file_name)-6)]
            out_put_path = path_out + file_name
            # os.chdir("/Users/qingye/Downloads/hmmer-3.2/src/")
            os.chdir("/usr/bin/")
            subprocess.call(["./hmmbuild",  out_put_path, input_path])

#hmmpress
def hmmpress():
    # c = os.walk(r"/Users/qingye/Desktop/experiment_test/11_hmmer/output/")

    c = os.walk(r"/home/ye_qin/data/11_hmmer/output/")

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
            # os.chdir("/Users/qingye/Downloads/hmmer-3.2/src/")
            os.chdir("/usr/bin/")
            subprocess.call(["./hmmpress", input_path])

def hmmscan():
    # path_out = "/Users/qingye/Desktop/experiment_test/11_hmmer/output/"
    # path_ou2="/Users/qingye/Desktop/experiment_test/11_hmmer/output2/"
    # a = os.walk(r"/Users/qingye/Desktop/experiment_test/0_data/2/")

    path_out = "/home/ye_qin/data/11_hmmer/output/"
    path_ou2 = "/home/ye_qin/data/11_hmmer/output2/"
    a = os.walk(r"/home/ye_qin/data/0_data/2/")

    list = []

    for path,dir_list,file_list in a:
        for file_name in file_list:
            prog = re.compile('^\d')
            result = prog.match(file_name)
            if (result):
                list.append(file_name)
            else:
                print ('Invalid File Name :' + file_name)
        for file_name_2 in list:
            file=path + file_name_2
            path_out_2=path_ou2 + file_name_2
            os.mkdir(path_out_2)
            pathout2=path_out_2 + "/"
            for i in range(1,781,1):
                # os.chdir("/Users/qingye/Downloads/hmmer-3.2/src/")
                os.chdir("/usr/bin/")
                path_3=path_out + str(i)
                pathout3=pathout2 + str(i)
                subprocess.call(["./hmmscan", "-o", pathout3, "-E", "0.1", path_3, file,])

path_splitor = "/"
# outer_folder_path = "/Users/qingye/Desktop/experiment_test/11_hmmer/output2/"
outer_folder_path = "/home/ye_qin/data/11_hmmer/output2/"


def get_folders():
    return [join(outer_folder_path, each_file) for each_file in os.listdir(outer_folder_path)
            if not isfile(join(outer_folder_path, each_file)) and not each_file.startswith('.')]


def get_files(basic_path):
    return [join(basic_path, each_file) for each_file in os.listdir(basic_path)
             if isfile(join(basic_path, each_file)) and not each_file.startswith('.')]

def start():
    result = []

    folders = sorted(get_folders(), key=lambda x: int(x.split(path_splitor)[-1].split(".")[0]))
    for folder_number in range(len(folders)):
        print "Processing folder %s" % folders[folder_number]
        index = [-1.0]
        files = sorted(get_files(folders[folder_number]), key=lambda x: int(x.split(path_splitor)[-1]))
        for i in range(len(files)):
            content = ''
            contentSpare = ''
            with open(files[i], "r") as fileread:
                oneline = fileread.readline()
                while oneline:
                    if oneline.strip().startswith("--- full sequence ---"):
                        contentList = fileread.readlines()
                        content = contentList[2]
                        contentSpare = contentList[3]
                        break
                    oneline = fileread.readline()

            if not content.strip('\n'):
                index.append(0.0)
                continue

            try:
                index.append(float(content.split()[1]))
            except ValueError:
                index.append(float(contentSpare.split()[1]))

        # index[folder_number + 1] = -1.0
        max_number = max(index)
        print index
        if max_number == 0.0:
            print "0"
            result.append(': '.join([str(folder_number + 1), "0"]) + '\n')
            continue

        for i in range(len(index)):
            if index[i] == max_number:
                result.append(': '.join([str(folder_number + 1), str(i)]) + '\n')

    with open(join(outer_folder_path, "score.txt"), 'w') as writefile:
        writefile.writelines(result)


if __name__ == '__main__':
    hmmbuild()
    hmmpress()
    hmmscan()
    start()