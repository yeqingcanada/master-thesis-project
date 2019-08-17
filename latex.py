import math
from decimal import *
import numpy as np
from pylatex import Document, Section, Tabular, PageStyle, Head,Figure,MiniPage
from pylatex.utils import italic



# file = "/Users/u_hamlo_admin/Desktop/qing stuff/"
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


with open("C:\Users\umroot\Desktop\\0.txt", "r") as fileread:
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


confusion_matrix = np.array([[aa_aa,aa_a,aa_c,aa_e,aa_p,aa_s,aa_o,aa_un],
                            [a_aa, a_a, a_c,aa_e, a_p, a_s, a_o, a_un],
                            [c_aa,c_a,c_c,c_e,c_p,c_s,c_o,c_un],
                            [e_aa,e_a,e_c,e_e,e_p,e_s,e_o,e_un],
                            [p_aa,p_a,p_c,p_e,p_p,p_s,p_o,p_un],
                            [s_aa,s_a,s_c,s_e,s_p,s_s,s_o,s_un],
                            [o_aa,o_a,o_c,o_e,o_p,o_s,o_o,o_un]],
                            dtype = int)


# with doc.create(MiniPage(align='c')):

            # table.add_caption('Look it\'s on its back')


raw_tp = np.array([[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]],
                    dtype = int)

for i in range(len(raw_tp) - 1):
    raw_tp[i][0] = confusion_matrix[i][i]
    raw_tp[i][1] = confusion_matrix[0][i] + confusion_matrix[1][i] + confusion_matrix[2][i] + confusion_matrix[3][i] + confusion_matrix[4][i] + \
                   confusion_matrix[5][i] + confusion_matrix[6][i] - confusion_matrix[i][i]
    raw_tp[i][2] = confusion_matrix[i][0] + confusion_matrix[i][1] + confusion_matrix[i][2] + confusion_matrix[i][3] + confusion_matrix[i][4] + \
                   confusion_matrix[i][5] + confusion_matrix[i][6] + confusion_matrix[i][7] - confusion_matrix[i][i]
    raw_tp[i][3] = 120 - raw_tp[i][0] - raw_tp[i][1] - raw_tp[i][2]
    raw_tp[i][4] = confusion_matrix[i][7]

raw_tp[7][0] = raw_tp[0][0] + raw_tp[1][0] + raw_tp[2][0] + raw_tp[3][0] + raw_tp[4][0] + raw_tp[5][0] + raw_tp[6][0]
raw_tp[7][1] = raw_tp[0][1] + raw_tp[1][1] + raw_tp[2][1] + raw_tp[3][1] + raw_tp[4][1] + raw_tp[5][1] + raw_tp[6][1]
raw_tp[7][2] = raw_tp[0][4] + raw_tp[1][4] + raw_tp[2][4] + raw_tp[3][4] + raw_tp[4][4] + raw_tp[5][4] + raw_tp[6][4]
raw_tp[7][3] = 0
raw_tp[7][4] = raw_tp[0][4] + raw_tp[1][4] + raw_tp[2][4] + raw_tp[3][4] + raw_tp[4][4] + raw_tp[5][4] + raw_tp[6][4]

geometry_options = {"tmargin": "1cm", "lmargin": "0cm"}
doc = Document(page_numbers=False, geometry_options=geometry_options)
# with doc.create(MiniPage(align='c')):
with doc.create(Section('The confusion matrix')):
    with doc.create(Tabular('||c c c c c c c c c||')) as table:
        table.add_hline()
        table.add_empty_row()
        table.add_row(" ", "Amino Acid", "Anion", "Cation", "Electron", "Protein", "Sugar", "Other", "Unclassified")
        table.add_empty_row()
        table.add_hline()
        table.add_row(("Amino Acid", aa_aa,aa_a,aa_c,aa_e,aa_p,aa_s,aa_o,aa_un))
        table.add_empty_row()
        table.add_row(("Anion", a_aa, a_a, a_c, a_e, a_p, a_s, a_o, a_un))
        table.add_empty_row()
        table.add_row(("Cation", c_aa, c_a, c_c, c_e, c_p, c_s, c_o, c_un))
        table.add_empty_row()
        table.add_row(("Electron", e_aa, e_a, e_c, e_e, e_p, e_s, e_o, e_un))
        table.add_empty_row()
        table.add_row(("Protein", p_aa, p_a, p_c, p_e, p_p, p_s, p_o, p_un))
        table.add_empty_row()
        table.add_row(("Sugar", s_aa, s_a, s_c, s_e, s_p, s_s, s_o, s_un))
        table.add_empty_row()
        table.add_row(("Other", o_aa, o_a, o_c, o_e, o_p, o_s, o_o, o_un))
        table.add_hline()
        table.add_hline()

with doc.create(Section(italic('raw result'))):
    with doc.create(Tabular('||c c c c c c||')) as table:
        table.add_hline()
        table.add_empty_row()
        table.add_row("", "TP", "FP", "FN", "TN", "Unclassified")
        table.add_empty_row()
        table.add_hline()
        # table.add_empty_row()
        table.add_row(("Amino Acid", raw_tp[0][1], raw_tp[0][1], raw_tp[0][2], raw_tp[0][3], raw_tp[0][4]))
        table.add_empty_row()
        table.add_row(("Anion", raw_tp[1][0], raw_tp[1][1], raw_tp[1][2], raw_tp[1][3], raw_tp[1][4]))
        table.add_empty_row()
        table.add_row(("Cation", raw_tp[2][0], raw_tp[2][1], raw_tp[2][2], raw_tp[2][3], raw_tp[2][4]))
        table.add_empty_row()
        table.add_row(("Electron", raw_tp[3][0], raw_tp[3][1], raw_tp[3][2], raw_tp[3][3], raw_tp[3][4]))
        table.add_empty_row()
        table.add_row(("Protein", raw_tp[4][0], raw_tp[4][1], raw_tp[4][2], raw_tp[4][3], raw_tp[4][4]))
        table.add_empty_row()
        table.add_row(("Sugar", raw_tp[5][0], raw_tp[5][1], raw_tp[5][2], raw_tp[5][3], raw_tp[5][4]))
        table.add_empty_row()
        table.add_row(("Other", raw_tp[6][0], raw_tp[6][1], raw_tp[6][2], raw_tp[6][3], raw_tp[6][4]))
        table.add_empty_row()
        table.add_row(("Overall", raw_tp[7][0], raw_tp[7][1], raw_tp[7][2], raw_tp[7][3], raw_tp[7][4]))
        table.add_hline()
with doc.create(Section(italic('detailed performance'))):
    with doc.create(Tabular('||c c c c c c||')) as table:
        table.add_hline()
        table.add_empty_row()
        table.add_row("Class", "Sensivity", "Specificity", "Accuracy", "MCC", "Unclassified")
        table.add_empty_row()
        table.add_hline()
        detailed_performance = np.array(["Amino Acid","Anion","Cation","Electron","Protein","Sugar","Other","Overall"])
        for i in range(len(detailed_performance)):
            tp = Decimal(float(raw_tp[i][0]))
            fp = Decimal(float(raw_tp[i][1]))
            fn = Decimal(float(raw_tp[i][2]))
            tn = Decimal(float(raw_tp[i][3]))
            un = Decimal(float(raw_tp[i][4]))

            sensitivity = "{0:.5f}".format(tp / (tp + fn))
            specificity = "{0:.5f}".format(tn / (tn + fp))
            accuracy = "{0:.5f}".format((tp + tn) / (tp + tn + fp + fn))
            mcc = "{0:.5f}".format(float(tp * tn - fp * fn) / math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)))
            unclassified = "{0:.5f}".format(un / (tp + fn))
            # table.add_empty_row()
            table.add_row(detailed_performance[i], sensitivity, specificity, accuracy, mcc, unclassified)
            table.add_empty_row()
        table.add_hline()

doc.generate_pdf('full', clean_tex=False)
