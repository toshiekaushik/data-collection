from abc import ABC,abstractmethod

class Accumulate(ABC):

    @abstractmethod
    def execute(self):
        pass