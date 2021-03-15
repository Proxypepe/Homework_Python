import sys
import xlrd

from topsis import Topsis
from moora import Moora


def main():
    if sys.argv[2] == "--Topsis" or sys.argv[2] == "-t":
        if ".xls" in sys.argv[1]:
            rb = xlrd.open_workbook(sys.argv[1], formatting_info=True)
            sheet = rb.sheet_by_index(0)
            start_matrix = [sheet.row_values(row_num) for row_num in range(sheet.nrows)]
            topsis = Topsis(start_matrix)
            topsis.calc()
    elif sys.argv[2].lower() == "--moora" or sys.argv[2] == "-m":
        rb = xlrd.open_workbook(sys.argv[1], formatting_info=True)
        sheet = rb.sheet_by_index(0)
        start_matrix = [sheet.row_values(row_num) for row_num in range(sheet.nrows)]
        moora = Moora(start_matrix)
        moora.calc()


if __name__ == '__main__':
    main()
