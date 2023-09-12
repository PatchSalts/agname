import processor_modules.processor
import os.path

class Addlevel(processor_modules.processor.Processor):
    def __init__(self, arguments):
        if arguments == str():
            raise ValueError(('this processor requires arguments: '
                             'the directory name to add to the filepath'))
        self.level = arguments

    def process(self, inpath):
        head, tail = os.path.split(inpath)
        return os.path.join(head, self.level, tail)
