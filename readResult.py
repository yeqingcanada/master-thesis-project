import subprocess
import re
from os.path import join, isfile
import os

file = "C:\Users\umroot\Desktop\\"

aa_un = 0
aa_aa = 0
aa_a = 0
aa_c = 0
aa_e = 0
aa_p = 0
aa_s = 0
aa_o = 0
a_un = 0
a_aa = 0
a_a = 0
a_c = 0
a_e = 0
a_p = 0
a_s = 0
a_o = 0
c_un = 0
c_aa = 0
c_a = 0
c_c = 0
c_e = 0
c_p = 0
c_s = 0
c_o = 0
e_un = 0
e_aa = 0
e_a = 0
e_c = 0
e_e = 0
e_p = 0
e_s = 0
e_o = 0
p_un = 0
p_aa = 0
p_a = 0
p_c = 0
p_e = 0
p_p = 0
p_s = 0
p_o = 0
s_un = 0
s_aa = 0
s_a = 0
s_c = 0
s_e = 0
s_p = 0
s_s = 0
s_o = 0
o_un = 0
o_aa = 0
o_a = 0
o_c = 0
o_e = 0
o_p = 0
o_s = 0
o_o = 0


with open(join(file,"score.txt"), "r") as fileread:
    for count, oneline in enumerate(fileread, start = 1):

        if 1 <= count <= 15:
            index = oneline.index(":")
            content = oneline[(index+2):]
            if int(content) == 0:
                aa_un+=1
            elif 1 <= int(content) <= 70:
                aa_aa+=1
            elif 71 <= int(content) <= 130:
                aa_a+=1
            elif 131 <= int(content) <= 390:
                aa_c+=1
            elif 391 <= int(content) <= 450:
                aa_e+=1
            elif 451 <= int(content) <= 520:
                aa_p+=1
            elif 521 <= int(content) <= 580:
                aa_s+=1
            elif 581 <= int(content) <= 780:
                aa_o+=1

        if 16 <= count <= 27:
            index = oneline.index(":")
            content = oneline[(index + 2):]
            if int(content) == 0:
                a_un += 1
            elif 1 <= int(content) <= 70:
                a_aa += 1
            elif 71 <= int(content) <= 130:
                a_a += 1
            elif 131 <= int(content) <= 390:
                a_c += 1
            elif 391 <= int(content) <= 450:
                a_e += 1
            elif 451 <= int(content) <= 520:
                a_p += 1
            elif 521 <= int(content) <= 580:
                a_s += 1
            elif 581 <= int(content) <= 780:
                a_o += 1

        if 28 <= count <= 63:
            index = oneline.index(":")
            content = oneline[(index + 2):]
            if int(content) == 0:
                c_un += 1
            elif 1 <= int(content) <= 70:
                c_aa += 1
            elif 71 <= int(content) <= 130:
                c_a += 1
            elif 131 <= int(content) <= 390:
                c_c += 1
            elif 391 <= int(content) <= 450:
                c_e += 1
            elif 451 <= int(content) <= 520:
                c_p += 1
            elif 521 <= int(content) <= 580:
                c_s += 1
            elif 581 <= int(content) <= 780:
                c_o += 1

        if 64 <= count <= 73:
            index = oneline.index(":")
            content = oneline[(index + 2):]
            if int(content) == 0:
                e_un += 1
            elif 1 <= int(content) <= 70:
                e_aa += 1
            elif 71 <= int(content) <= 130:
                e_a += 1
            elif 131 <= int(content) <= 390:
                e_c += 1
            elif 391 <= int(content) <= 450:
                e_e += 1
            elif 451 <= int(content) <= 520:
                e_p += 1
            elif 521 <= int(content) <= 580:
                e_s += 1
            elif 581 <= int(content) <= 780:
                e_o += 1

        if 74 <= count <= 88:
            index = oneline.index(":")
            content = oneline[(index + 2):]
            if int(content) == 0:
                p_un += 1
            elif 1 <= int(content) <= 70:
                p_aa += 1
            elif 71 <= int(content) <= 130:
                p_a += 1
            elif 131 <= int(content) <= 390:
                p_c += 1
            elif 391 <= int(content) <= 450:
                p_e += 1
            elif 451 <= int(content) <= 520:
                p_p += 1
            elif 521 <= int(content) <= 580:
                p_s += 1
            elif 581 <= int(content) <= 780:
                p_o += 1

        if 89 <= count <= 100:
            index = oneline.index(":")
            content = oneline[(index + 2):]
            if int(content) == 0:
                s_un += 1
            elif 1 <= int(content) <= 70:
                s_aa += 1
            elif 71 <= int(content) <= 130:
                s_a += 1
            elif 131 <= int(content) <= 390:
                s_c += 1
            elif 391 <= int(content) <= 450:
                s_e += 1
            elif 451 <= int(content) <= 520:
                s_p += 1
            elif 521 <= int(content) <= 580:
                s_s += 1
            elif 581 <= int(content) <= 780:
                s_o += 1

        if 101 <= count <= 120:
            index = oneline.index(":")
            content = oneline[(index + 2):]
            if int(content) == 0:
                o_un += 1
            elif 1 <= int(content) <= 70:
                o_aa += 1
            elif 71 <= int(content) <= 130:
                o_a += 1
            elif 131 <= int(content) <= 390:
                o_c += 1
            elif 391 <= int(content) <= 450:
                o_e += 1
            elif 451 <= int(content) <= 520:
                o_p += 1
            elif 521 <= int(content) <= 580:
                o_s += 1
            elif 581 <= int(content) <= 780:
                o_o += 1

    resultList = [
        'aa_aa: ' + str(aa_aa) + '\n',
        'aa_a: ' + str(aa_a) + '\n',
        'aa_c: ' + str(aa_c) + '\n',
        'aa_e: ' + str(aa_e) + '\n',
        'aa_p: ' + str(aa_p) + '\n',
        'aa_s: ' + str(aa_s) + '\n',
        'aa_o: ' + str(aa_o) + '\n',
        'aa_un: ' + str(aa_un) + '\n',

        'a_aa: ' + str(a_aa) + '\n',
        'a_a: ' + str(a_a) + '\n',
        'a_c: ' + str(a_c) + '\n',
        'a_e: ' + str(a_e) + '\n',
        'a_p: ' + str(a_p) + '\n',
        'a_s: ' + str(a_s) + '\n',
        'a_o: ' + str(a_o) + '\n',
        'a_un: ' + str(a_un) + '\n',

        'c_aa: ' + str(c_aa) + '\n',
        'c_a: ' + str(c_a) + '\n',
        'c_c: ' + str(c_c) + '\n',
        'c_e: ' + str(c_e) + '\n',
        'c_p: ' + str(c_p) + '\n',
        'c_s: ' + str(c_s) + '\n',
        'c_o: ' + str(c_o) + '\n',
        'c_un: ' + str(c_un) + '\n',

        'e_aa: ' + str(e_aa) + '\n',
        'e_a: ' + str(e_a) + '\n',
        'e_c: ' + str(e_c) + '\n',
        'e_e: ' + str(e_e) + '\n',
        'e_p: ' + str(e_p) + '\n',
        'e_s: ' + str(e_s) + '\n',
        'e_o: ' + str(e_o) + '\n',
        'e_un: ' + str(e_un) + '\n',

        'p_aa: ' + str(p_aa) + '\n',
        'p_a: ' + str(p_a) + '\n',
        'p_c: ' + str(p_c) + '\n',
        'p_e: ' + str(p_e) + '\n',
        'p_p: ' + str(p_p) + '\n',
        'p_s: ' + str(p_s) + '\n',
        'p_o: ' + str(p_o) + '\n',
        'p_un: ' + str(p_un) + '\n',

        's_aa: ' + str(s_aa) + '\n',
        's_a: ' + str(s_a) + '\n',
        's_c: ' + str(s_c) + '\n',
        's_e: ' + str(s_e) + '\n',
        's_p: ' + str(s_p) + '\n',
        's_s: ' + str(s_s) + '\n',
        's_o: ' + str(s_o) + '\n',
        's_un: ' + str(s_un) + '\n',

        'o_aa: ' + str(o_aa) + '\n',
        'o_a: ' + str(o_a) + '\n',
        'o_c: ' + str(o_c) + '\n',
        'o_e: ' + str(o_e) + '\n',
        'o_p: ' + str(o_p) + '\n',
        'o_s: ' + str(o_s) + '\n',
        'o_o: ' + str(o_o) + '\n',
        'o_un: ' + str(o_un) + '\n',
    ]

with open(join(file, "result.txt"), 'w') as writefile:
    writefile.writelines(resultList)