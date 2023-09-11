import os.path
import processor_modules.processor

class Swapcase(processor_modules.processor.Processor):
    def __init__(self):
        pass

    def process(self, inpath):
        head, tail = os.path.split(inpath)
        return os.path.join(head, tail.swapcase())
