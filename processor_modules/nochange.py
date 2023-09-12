import processor_modules.processor

class Nochange(processor_modules.processor.Processor):
    def __init__(self, arguments):
        if arguments != str():
            raise ValueError('this processor does not support arguments')

    def process(self, inpath):
        return inpath
