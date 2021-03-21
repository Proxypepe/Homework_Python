import sys
import xlrd

from topsis import Topsis
from moora import Moora
from electre import Electre


def get_table(file):
    start_matrix = []
    tmp = []
    weights = []
    benefits = []
    rb = xlrd.open_workbook(file, formatting_info=True)
    sheet = rb.sheet_by_index(0)
    tmp_sheet = [sheet.row_values(row_num) for row_num in range(sheet.nrows)]
    m = len(tmp_sheet)
    n = len(tmp_sheet[0])
    for i in range(1, m - 3):
        for j in range(1, n):
            if tmp_sheet[i][j] != '':
                tmp.append(tmp_sheet[i][j])
        start_matrix.append(tmp.copy())
        tmp.clear()
    for j in range(1, n):
        if tmp_sheet[m - 3][j] != '':
            benefits.append(tmp_sheet[m - 3][j])

    for j in range(1, n):
        if tmp_sheet[m - 2][j] != '':
            weights.append(tmp_sheet[m - 2][j])

    return start_matrix, benefits, weights


def main():
    method = None
    if ".xls" in sys.argv[1]:
        if sys.argv[2] == "--Topsis" or sys.argv[2] == "-t":
            method = Topsis(*get_table(sys.argv[1]))
        elif sys.argv[2].lower() == "--Moora" or sys.argv[2] == "-m":
            method = Moora(*get_table(sys.argv[1]))
        elif sys.argv[2].lower() == "--Electre" or sys.argv[2] == "-e":
            method = Electre(*get_table(sys.argv[1]))
        if method is not None:
            method.calc()


if __name__ == '__main__':
    main()
