import os
from os.path import isfile, join

original_path = 'C:\Users\umroot\Desktop\\2\\'

if __name__ == '__main__':
    org_files = [join(original_path, each_file) for each_file in os.listdir(original_path)
                 if isfile(join(original_path, each_file)) and not each_file.startswith('.')]
    ten = nine = eight = seven = six = five = four = three = two = one = zero = 0
    for i in range(len(org_files)):
        with open(org_files[i], 'r') as inputfile:
            count = 0
            oneline = inputfile.readline()
            while oneline:
                if oneline.startswith('>'):
                 count = count + 1
                oneline = inputfile.readline()
        if count == 10:
            ten = ten + 1
        elif count == 9:
            nine = nine + 1
        elif count == 8:
            eight = eight + 1
        elif count == 7:
            seven = seven + 1
        elif count == 6:
            six = six + 1
        elif count == 5:
            five = five + 1
        elif count == 4:
            four = four + 1
        elif count == 3:
            three = three + 1
        elif count == 2:
            two = two + 1
        elif count == 1:
            one = one + 1
        elif count == 0:
            zero = zero + 1
            print(i)
    recordList = [ten, nine, eight, seven, six, five, four, three, two, one, zero]
    print(recordList)