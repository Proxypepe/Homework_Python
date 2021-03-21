import math


class Topsis:
    def __init__(self, start_matrix, benefits, weights):
        self.__start_matrix = start_matrix
        self.__benefits = benefits
        self.__weights = weights
        self.__rank = []

    def calc(self):
        normalization_matrix = []
        temp = []
        squared_matrix = []
        sqrt_sum = []
        weighted_matrix = []
        positive_matrix = []
        negative_matrix = []
        si_pos = []
        si_neg = []
        cci = []

        print("Начальная матрица:")
        print(self.__start_matrix)

        # Размерность матрицы
        m = len(self.__start_matrix)
        n = len(self.__start_matrix[0])
        # Считаем матрицу квадратичных значений
        for i in range(0, m):
            for j in range(n):
                temp.append(self.__start_matrix[i][j] ** 2)
            squared_matrix.append(temp.copy())
            temp.clear()

        # Считаем корни сумм
        _sum = 0
        for i in range(0, n):
            for j in range(0, m):
                _sum += squared_matrix[j][i]
            sqrt_sum.append(math.sqrt(_sum))
            _sum = 0

        # Нормализуем матрицу
        for i in range(0, n):
            for j in range(0, m):
                temp.append(self.__start_matrix[j][i] / sqrt_sum[i])
            normalization_matrix.append(temp.copy())
            temp.clear()

        # Взвешиваем нормализованную матрицу
        for i in range(0, n):
            for j in range(0, m):
                temp.append(normalization_matrix[i][j] * self.__weights[i])
            weighted_matrix.append(temp.copy())
            temp.clear()

        print("\nВзвешенная матрица:")
        print(weighted_matrix)

        # Считаем pos и neg относительно важности каждого критерия
        for i in range(len(weighted_matrix)):
            if self.__benefits[i] == 1.0:
                positive_matrix.append(max(weighted_matrix[i]))
            if self.__benefits[i] == 0.0:
                positive_matrix.append(min(weighted_matrix[i]))
        for i in range(len(weighted_matrix)):
            if self.__benefits[i] == 1.0:
                negative_matrix.append(min(weighted_matrix[i]))
            if self.__benefits[i] == 0.0:
                negative_matrix.append(max(weighted_matrix[i]))

        _sum = 0
        # Считаем Si pos и Si net
        for i in range(m):
            for j in range(n):
                _sum += (weighted_matrix[j][i] - positive_matrix[j]) ** 2
            si_pos.append(math.sqrt(_sum))
            _sum = 0

        print("\nSi positive:")
        print(si_pos)

        for i in range(m):
            for j in range(n):
                _sum += (weighted_matrix[j][i] - negative_matrix[j]) ** 2
            si_neg.append(math.sqrt(_sum))
            _sum = 0

        print("\nSi negative:")
        print(si_neg)

        for i in range(len(si_neg)):
            cci.append(si_neg[i] / (si_pos[i] + si_neg[i]))

        print("\nФинальная матрица")
        print(cci)
        d = {}
        for i in range(1, len(cci) + 1):
            d[i] = cci[i - 1]

        def compare(index):
            return d[index]
        self.__rank = sorted(d, key=compare, reverse=True)

        print("\nРанг")
        print(self.__rank)
