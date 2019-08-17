from os.path import isfile, join
import sys
import os

# pass_threshold = -1.7

# relace folder path and run #####
speer_server_original_path = "/Users/qingye/Desktop/experiment_test/10_xdet/input"
speer_server_output_path = "/Users/qingye/Desktop/experiment_test/10_xdet/output"
output_path = "/Users/qingye/Desktop/experiment_test/10_xdet/output2/"

path_splitor = "/"
def readFileList():
    # get original input files for the speer server
    org_files = [join(speer_server_original_path, each_file) for each_file in os.listdir(speer_server_original_path)
                 if isfile(join(speer_server_original_path, each_file)) and not each_file.startswith('.')]

    # get speer server output files
    out_files = [join(speer_server_output_path, each_file) for each_file in os.listdir(speer_server_output_path)
                 if isfile(join(speer_server_output_path, each_file)) and not each_file.startswith('.')]

    if len(org_files) != len(out_files):
        print "The number of input files is not same as the number of output files"
        sys.exit(0)

    return org_files, out_files


def readOriInput(filename):
    recordList = []
    temp = []
    key = ''
    with open(filename, 'r') as inputfile:
        oneline = inputfile.readline()
        while oneline:
            if oneline.startswith('>'):
                if not temp:
                    key = oneline.replace('\n', '')
                else:
                    recordList.append({key: ''.join(temp)})
                    key = oneline.replace('\n', '')
                    temp = []
            else:
                temp.append(oneline.replace('\n', ''))

            oneline = inputfile.readline()

    recordList.append({key: ''.join(temp)})

    return recordList


def readOutputFile(filename):

    positions = []

    with open(filename, 'r') as outputfile:
        oneline = outputfile.readline()
        while oneline:
            parts = oneline.replace('\n', '').split()
            # if float(parts[8]) * 1000 > float(pass_threshold) * 1000:
            positions.append(int(parts[0]))
            # else:
            #     pass
            oneline = outputfile.readline()

    positions = set(positions)
    return positions


def writeToFile(data, filename):
    filename = output_path + filename
    with open(filename, 'w') as outputfile:
        for eachData in data:
            outputfile.writelines(eachData)
        outputfile.flush()


# if __name__ == '__main__':
def startPoint():
    output = []
    dashStat = []
    original_files, output_files = readFileList()
    for i in range(len(original_files)):
        positions = readOutputFile(output_files[i])
        recordList = readOriInput(original_files[i])
        counter = 0
        length = 0
        counting = True
        for eachRecord in recordList:
            original = ['dummy']
            item = eachRecord.items()[0]
            key = item[0]
            value = item[1]
            original += list(value)
            target = []

            for j in range(len(original)):
                if j in positions:
                    target.append(original[j])
                    if counting:
                        counter += 1
                else:
                    target.append('-')
            output.append({key: ''.join(target)})

            if counting:
                length = (len(original) - 1)
                counting = False

        toFile = []
        for element in output:
            item = element.items()[0]
            toFile.append('\n'.join([item[0], item[1], '']))

        writeToFile(toFile, original_files[i].split(path_splitor)[-1])
        dashStat.append({original_files[i].split(path_splitor)[-1]: '/'.join([str(counter), str(length)])})

        print "Replace characters to '-' is done for %s" % original_files[i].split(path_splitor)[-1]
        output = []

    statistics = []
    for element in dashStat:
        item = element.items()[0]
        statistics.append(': '.join([item[0], item[1]]) + '\n')

    writeToFile(statistics, "dash_statistics.txt")