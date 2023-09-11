import processor_modules.processor
import os.path

class Addlevel(processor_modules.processor.Processor):
    def __init__(self):
        pass

    def process(self, inpath):
        head, tail = os.path.split(inpath)
        return os.path.join(head, 'a', tail)
