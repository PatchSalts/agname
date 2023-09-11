import processor_modules.processor

class Nochange(processor_modules.processor.Processor):
    def __init__(self):
        pass

    def process(self, inpath):
        return inpath
