import math


class Topsis:

    def __init__(self, start_matrix):
        self.__start_matrix = start_matrix
        self.__rank = []

    def calc(self):
        start_matrix = self.__start_matrix
        n = len(start_matrix)
        m = len(start_matrix[0])
        matrix = []
        wight_matrix = []
        normalization_matrix = []
        squared_matrix = []
        sum_list = []
        positive_matrix = []
        negative_matrix = []
        major_values = []
        tmp = []
        si_pos = []
        si_neg = []
        cci = []
        rank = []
        # Init start matrix
        for i in range(1, n):
            for j in range(m):
                if start_matrix[i][j] != '':
                    tmp.append(start_matrix[i][j])
                else:
                    break
            matrix.append(tmp.copy())
            tmp.clear()
        # print(matrix)
        start_m = len(matrix[0]) + 1
        # print(f"n: {n}, m: {m}, start_m: {start_m}")
        # init wight matrix
        for i in range(1, n):
            for j in range(start_m, m):
                tmp.append(start_matrix[i][j])
            wight_matrix.append(tmp.copy())
            tmp.clear()
        # print(wight_matrix)
        tmp.clear()

        for j in range(m):
            if start_matrix[0][j] != "":
                major_values.append(start_matrix[0][j])
        print(major_values)

        m = len(matrix[0])
        n = len(matrix)
        for i in range(n):
            for j in range(m):
                tmp.append(matrix[i][j] ** 2)
            squared_matrix.append(tmp.copy())
            tmp.clear()

        # print("Sq")
        # print(squared_matrix)
        sum_sqrted = 0
        for i in range(m):
            for j in range(n):
                sum_sqrted += squared_matrix[j][i]
            # print(f"sum: {sum_sqrted}")
            sum_list.append(math.sqrt(sum_sqrted))
            sum_sqrted = 0
        # print("Sums")
        # print(sum_list)

        for i in range(n):
            for j in range(m):
                x = matrix[i][j]
                res = x / (sum_list[j])
                tmp.append(res)
            normalization_matrix.append(tmp.copy())
            tmp.clear()

        # print("Norm")
        # print(normalization_matrix)

        for i in range(n):
            for j in range(m):
                normalization_matrix[i][j] *= wight_matrix[i][j]

        print("Wieghted Norm")
        print(normalization_matrix)

        t_nmatrix = list(zip(*normalization_matrix))
        max_ = 0
        for i in range(len(major_values)):
            if major_values[i] == 1.0:
                positive_matrix.append(min(t_nmatrix[i]))
            if major_values[i] == 0.0:
                positive_matrix.append(max(t_nmatrix[i]))
        for i in range(len(major_values)):
            if major_values[i] == 1.0:
                negative_matrix.append(max(t_nmatrix[i]))
            if major_values[i] == 0.0:
                negative_matrix.append(min(t_nmatrix[i]))
        # print("Transpose")
        # print(t_nmatrix)
        print("Pos")
        print(positive_matrix)
        print("Neg")
        print(negative_matrix)
        sum_ = 0

        for i in range(n):
            for j in range(m):
                sum_ += ((round(normalization_matrix[i][j], 2) - round(positive_matrix[j], 2)) ** 2)
            si_pos.append(math.sqrt(sum_))
            sum_ = 0

        print("Si pos")
        print(si_pos)

        for i in range(n):
            for j in range(m):
                sum_ += ((round(normalization_matrix[i][j], 2) - round(negative_matrix[j], 2)) ** 2)
            si_neg.append(math.sqrt(sum_))
            sum_ = 0

        print("Si neg")
        print(si_neg)

        # cci
        sum_ = 0
        for i in range(len(si_pos)):
            sum_ = si_neg[i] / (si_pos[i] + si_neg[i])
            cci.append(sum_)
            sum_ = 0

        print("CCI")
        print(cci)
        cci_copy = cci.copy()
        for i in range(len(cci)):
            max_ = max(cci_copy)
            for j in range(len(cci)):
                if max_ == cci[j]:
                    rank.append(j + 1)
            cci_copy.remove(max_)

        print("Rank")
        print(rank)