import numpy as np
import random


from problem.problem import Problem
from solution.one_dimension_solution import OneDimensionSolution


class Zdt1(Problem):

    def __init__(self, size):
        self.n = size
        super().__init__()

    def f(self, function_id, solution):
        x = solution[:]

        if function_id == 0:
            return x[0]
        else:
            g = 1 + 9.0 / (self.n - 1) * np.sum(x[1:])
            return g * (1 - np.power((x[0] / g), 0.5))

    def generate_random_solution(self):
        solution = []
        for i in range(0, self.n):
            solution.append(random.random())

        return self.generate_solution(solution)

    def generate_solution(self, array):
        x = OneDimensionSolution(array)

        for j in range(self.function_numbers):
            x.F.append(self.f(j, x.solution))

        return x
