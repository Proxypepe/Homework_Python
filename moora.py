import math


class Moora:
    def __init__(self, start_matrix, benefits, weights):
        print("Moora method")
        self.__start_matrix = start_matrix
        self.__benefits = benefits
        self.__weights = weights
        self.__rank = []

    def calc(self):
        tmp = []
        squared_matrix = []
        sqrt_sum = []
        weighted_matrix = []
        normalization_matrix = []
        result = []

        print("Начальная матрица:")
        print(self.__start_matrix)

        # Размерность матрицы
        m = len(self.__start_matrix)
        n = len(self.__start_matrix[0])
        for i in range(m):
            for j in range(n):
                tmp.append(self.__start_matrix[i][j] ** 2)
            squared_matrix.append(tmp.copy())
            tmp.clear()
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

        # Считаем pos и neg относительно важности каждого критерия
        _sum = 0
        for i in range(m):
            for j in range(n):
                if self.__benefits[j] == 1.0:
                    _sum += weighted_matrix[j][i]
                if self.__benefits[j] == 0.0:
                    _sum -= weighted_matrix[j][i]
            result.append(_sum)
            _sum = 0

        print("\nФинальная матрица")
        print(result)

        d = {}
        for i in range(1, len(result) + 1):
            d[i] = result[i - 1]

        def compare(index):
            return d[index]
        self.__rank = sorted(d, key=compare, reverse=True)

        print("\nРанг")
        print(self.__rank)
