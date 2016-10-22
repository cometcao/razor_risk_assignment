from uri_parser_error import UriParserError
from uri_parser_error import ReturnStatus

class UriParser(object):
    def __init__(self, uri_input):
            self.uri = uri_input
        
    
    def parse(self):
        if self.uri:
            return self.parseUri(self.uri)
        else:
            return (UriParserError("{} is an invalid URI input!".format(self.uri), ReturnStatus.Invalid_Input), None)
            
    def parseUri(self, uriStr):
        return UriParserError("All Good", ReturnStatus.OK), None



