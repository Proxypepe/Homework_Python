import math


class Moora:
    def __init__(self, start_matrix):
        self.__start_matrix = start_matrix
        self.__rank = []

    def calc(self):
        start_matrix = self.__start_matrix
        # print(start_matrix)
        n = len(start_matrix)
        m = len(start_matrix[0])
        matrix = []
        wight_matrix = []
        tmp = []
        squared_matrix = []
        major_values = []
        sum_list = []
        normalization_matrix = []
        result = []
        rank = []
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

        for i in range(1, n):
            for j in range(start_m, m):
                tmp.append(start_matrix[i][j])
            wight_matrix.append(tmp.copy())
            tmp.clear()
            # print(wight_matrix)
        tmp.clear()

        # print(wight_matrix[0])

        m = len(matrix[0])
        n = len(matrix)
        for i in range(n):
            for j in range(m):
                tmp.append(matrix[i][j] ** 2)
            squared_matrix.append(tmp.copy())
            tmp.clear()
        # print(squared_matrix)

        for j in range(m):
            if start_matrix[0][j] != "":
                major_values.append(start_matrix[0][j])
        # print(major_values)
        sum_sqrted = 0
        for i in range(m):
            for j in range(n):
                sum_sqrted += squared_matrix[j][i]
            # print(f"sum: {sum_sqrted}")
            sum_list.append(math.sqrt(sum_sqrted))
            sum_sqrted = 0
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
                # print(type(wight_matrix[0][j]))
                normalization_matrix[i][j] *= wight_matrix[0][j]

        # print(normalization_matrix)

        print(m)
        print(len(major_values))
        print(major_values)

        sum_major = 0
        for i in range(n):
            for j in range(m):
                if major_values[j] == 1:
                    sum_major += normalization_matrix[i][j]
                else:
                    sum_major -= normalization_matrix[i][j]
            result.append(sum_major)
            sum_major = 0

        # print(result)

        result_copy = result.copy()
        for i in range(len(result)):
            max_ = max(result_copy)
            for j in range(len(result)):
                if max_ == result[j]:
                    rank.append(j + 1)
            result_copy.remove(max_)

        print("Rank")
        print(rank)
