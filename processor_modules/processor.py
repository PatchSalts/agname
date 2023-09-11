import abc

class Processor(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def process(self, inpath):
        return inpath
