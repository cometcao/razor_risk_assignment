from enum import unique, IntEnum

@unique
class ReturnStatus(IntEnum):
    OK = 0,
    Invalid_Input = 1, 
    Invalid_Format = 2
    


class UriParserError():
    def __init__(self, msg, status):
        self.message = msg
        self.status = status
    
    def __repr__(self):
        return "return code:{} with message: {}".format(self.status, self.message)
        
