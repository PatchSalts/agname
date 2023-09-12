import abc

class Processor(abc.ABC):
    @abc.abstractmethod
    def __init__(self, arguments):
        pass

    @abc.abstractmethod
    def process(self, inpath):
        return inpath
