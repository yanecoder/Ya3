class missingEoS(Exception):
    pass

class unrecognizedVariable(Exception):
    
    def __init__(self, message):
        self.message = message