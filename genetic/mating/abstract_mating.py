from abc import ABC, abstractmethod


class GeneticMating(ABC):

    def __init__(self, algorithm_instance):
        self.algorithm = algorithm_instance

    @abstractmethod
    def run(self, population_indexes):
        pass
