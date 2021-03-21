import math


class Electre:
    def __init__(self, start_matrix, benefits, weights):
        print("Electre method")
        self.__start_matrix = start_matrix
        self.__benefits = benefits
        self.__weights = weights
        self.__rank1 = []
        self.__rank2 = []

    def calc(self):
        normalization_matrix = []
        tmp = []
        squared_matrix = []
        sqrt_sum = []
        weighted_matrix = []
        concordance_matrix = []
        concordance_index = []
        concordance_dominance = []
        discordance_set = []
        discordance_matrix = []
        discordance_max = []
        discordance_dominance = []
        max1 = []
        max2 = []
        discordance_index = []
        result_matrix1 = []
        result_matrix2 = []
        result_matrix_sum_first1 = []
        result_matrix_sum_second1 = []
        result_matrix_sum_first2 = []
        result_matrix_sum_second2 = []

        print("Начальная матрица:")
        print(self.__start_matrix)

        # Размерность матрицы
        m = len(self.__start_matrix)
        n = len(self.__start_matrix[0])

        # Считаем матрицу квадратичных значений
        for i in range(m):
            for j in range(n):
                tmp.append(self.__start_matrix[i][j] ** 2)
            squared_matrix.append(tmp.copy())
            tmp.clear()

        # Считаем корни сумм
        _sum = 0
        for i in range(n):
            for j in range(m):
                _sum += squared_matrix[j][i]
            sqrt_sum.append(math.sqrt(_sum))
            _sum = 0

        # Нормализуем матрицу
        for i in range(n):
            for j in range(m):
                tmp.append(self.__start_matrix[j][i] / sqrt_sum[i])
            normalization_matrix.append(tmp.copy())
            tmp.clear()

        print("\nНормализованная матрица:")
        print(normalization_matrix)

        # Взвешиваем нормализованную матрицу
        for i in range(n):
            for j in range(m):
                tmp.append(normalization_matrix[i][j] * self.__weights[i])
            weighted_matrix.append(tmp.copy())
            tmp.clear()

        print("\nВзвешенная матрица:")
        print(weighted_matrix)

        # Считаем индексы соответствия
        for i in range(n):
            for j in range(m):
                tmp1 = weighted_matrix[i][j]
                for k in range(m):
                    if k != j:
                        if self.__benefits[i] == 1.0:
                            if tmp1 >= weighted_matrix[i][k]:
                                tmp.append(1)
                            else:
                                tmp.append(0)
                        if self.__benefits[i] == 0.0:
                            if tmp1 <= weighted_matrix[i][k]:
                                tmp.append(1)
                            else:
                                tmp.append(0)
            concordance_matrix.append(tmp.copy())
            tmp.clear()

        print("\nconcordance matrix:")
        print(concordance_matrix)

        _sum = 0.0
        for i in range(len(concordance_matrix[0])):
            for j in range(n):
                _sum += concordance_matrix[j][i] * self.__weights[j]
            concordance_index.append(_sum)
            _sum = 0

        print("\nconcordance index")
        print(concordance_index)

        _sum = 0
        for elm in concordance_index:
            _sum += elm
        concordance_thresholdValue = _sum / (m * (m - 1))

        print("\nconcordance_thresholdValue")
        print(concordance_thresholdValue)

        for elem in concordance_index:
            if elem < concordance_thresholdValue:
                concordance_dominance.append(1)
            else:
                concordance_dominance.append(0)

        print("\nconcordance_dominance")
        print(concordance_dominance)

        # Считаем несоответствия
        for i in range(n):
            for j in range(len(concordance_matrix[0])):
                if concordance_matrix[i][j] == 0:
                    tmp.append(1)
                else:
                    tmp.append(0)
            discordance_set.append(tmp.copy())
            tmp.clear()

        print("\ndiscordance_set")
        print(discordance_set)

        for i in range(n):
            for j in range(m):
                tmp1 = weighted_matrix[i][j]
                for k in range(m):
                    if k != j:
                        tmp.append(abs(tmp1 - weighted_matrix[i][k]))
            discordance_matrix.append(tmp.copy())
            tmp.clear()

        print("\ndiscordance matrix:")
        print(discordance_matrix)

        # max1
        for i in range(n):
            for j in range(len(discordance_matrix[0])):
                tmp.append(discordance_matrix[i][j] * discordance_set[i][j])
            discordance_max.append(tmp.copy())
            tmp.clear()

        print("\ndiscordance max:")
        print(discordance_max)

        for i in range(len(discordance_matrix[0])):
            for j in range(n):
                tmp.append(discordance_max[j][i])
            max1.append(max(tmp.copy()))
            tmp.clear()

        print("\nmax1")
        print(max1)

        # max2
        for i in range(len(discordance_matrix[0])):
            for j in range(n):
                tmp.append(discordance_matrix[j][i])
            max2.append(max(tmp.copy()))
            tmp.clear()

        print("\nmax2")
        print(max2)

        # индексы несоответствия
        for i in range(len(max1)):
            discordance_index.append(max1[i] / max2[i])

        print("\ndiscordance_index")
        print(discordance_index)

        _sum = 0
        for elm in discordance_index:
            _sum += elm
        discordance_thresholdValue = _sum / (m * (m - 1))

        print("\ndiscordance_thresholdValue")
        print(discordance_thresholdValue)

        # диссонанс доминирования

        for elem in discordance_index:
            if elem > discordance_thresholdValue:
                discordance_dominance.append(0)
            else:
                discordance_dominance.append(1)

        print("\ndiscordance_dominance")
        print(discordance_dominance)

        counter = 0
        c = len(concordance_index)
        for i in range(c):
            if i % m == 0:
                tmp.append(0.0)
            tmp.append(concordance_index[i])
            if counter == m - 2:
                if i == c - 1:
                    tmp.append(0.0)
                result_matrix1.append(tmp.copy())
                tmp.clear()
                counter = 0
                continue
            counter += 1

        _sum = 0
        for i in range(len(result_matrix1[0])):
            for j in range(len(result_matrix1)):
                if i != j:
                    _sum += result_matrix1[j][i]
            result_matrix_sum_second1.append(_sum)
            _sum = 0

        _sum = 0
        for i in range(len(result_matrix1)):
            for j in range(len(result_matrix1[0])):
                if i != j:
                    _sum += result_matrix1[i][j]
            result_matrix_sum_first1.append(_sum)
            _sum = 0

        for i in range(len(result_matrix_sum_first1)):
            self.__rank1.append(result_matrix_sum_first1[i] - result_matrix_sum_second1[i])

        for i in range(len(discordance_index)):
            if i % m == 0:
                tmp.append(0.0)
            tmp.append(discordance_index[i])
            if counter == m - 2:
                if i == len(discordance_index) - 1:
                    tmp.append(0.0)
                result_matrix2.append(tmp.copy())
                tmp.clear()
                counter = 0
                continue
            counter += 1

        _sum = 0
        for i in range(len(result_matrix2[0])):
            for j in range(len(result_matrix2)):
                if i != j:
                    _sum += result_matrix2[j][i]
            result_matrix_sum_second2.append(_sum)
            _sum = 0

        _sum = 0
        for i in range(len(result_matrix2)):
            for j in range(len(result_matrix2[0])):
                if i != j:
                    _sum += result_matrix2[i][j]
            result_matrix_sum_first2.append(_sum)
            _sum = 0

        for i in range(len(result_matrix_sum_first2)):
            self.__rank2.append(result_matrix_sum_first2[i] - result_matrix_sum_second2[i])

        print("\nconcordance rank:")
        print(self.__rank1)
        print("\ndiscordance rank:")
        print(self.__rank2)


