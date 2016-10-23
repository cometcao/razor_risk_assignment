'''
The defintion of URI comes from:
https://en.wikipedia.org/wiki/Uniform_Resource_Identifier
https://tools.ietf.org/html/rfc3986


The core parser is implemented using Regex (RE). 
With reference to https://pypi.python.org/pypi/rfc3987#downloads
The Regex of URI was taken from http://snipplr.com/view/6889/regular-expressions-for-uri-validationparsing/
Many thanks to stackoverflow
'''

from uri_parser_error import UriParserError
from uri_parser_error import ReturnStatus
import re

class UriParser(object):
    
    pattern = re.compile("""^
                            ([a-z][a-z0-9+.-]*):
                            (?:\/\/((?:(?=((?:[a-z0-9-._~!$&'()*+,;=:]|%[0-9A-F]{2})*))(\3)@)?(?=(\[[0-9A-F:.]{2,}\]|(?:[a-z0-9-._~!$&'()*+,;=]|%[0-9A-F]{2})*))\5(?::(?=(\d*))\6)?)(\/(?=((?:[a-z0-9-._~!$&'()*+,;=:@\/]|%[0-9A-F]{2})*))\8)?|(\/?(?!\/)(?=((?:[a-z0-9-._~!$&'()*+,;=:@\/]|%[0-9A-F]{2})*))\10)?)(?:\?(?=((?:[a-z0-9-._~!$&'()*+,;=:@\/?]|%[0-9A-F]{2})*))\11)?(?:#(?=((?:[a-z0-9-._~!$&'()*+,;=:@\/?]|%[0-9A-F]{2})*))\12)?$""", re.VERBOSE)
    #pattern_delimiter = re.compile("""^(?:([a-z0-9+.-]+:\/\/)((?:(?:[a-z0-9-._~!$&'()*+,;=:]|%[0-9A-F]{2})*)@)?((?:[a-z0-9-._~!$&'()*+,;=]|%[0-9A-F]{2})*)(:(?:\d*))?(\/(?:[a-z0-9-._~!$&'()*+,;=:@\/]|%[0-9A-F]{2})*)?|([a-z0-9+.-]+:)(\/?(?:[a-z0-9-._~!$&'()*+,;=:@]|%[0-9A-F]{2})+(?:[a-z0-9-._~!$&'()*+,;=:@\/]|%[0-9A-F]{2})*)?)(\?(?:[a-z0-9-._~!$&'()*+,;=:\/?@]|%[0-9A-F]{2})*)?(#(?:[a-z0-9-._~!$&'()*+,;=:\/?@]|%[0-9A-F]{2})*)?$""", re.VERBOSE)
    pattern_2=re.compile(r'''^
                            ([a-z][a-z0-9+.-]*):
                            (?:
                                \/\/
                                (
                                    (?:(?=((?:[a-z0-9-._~!$&'()*+,;=:]|%[0-9A-F]{2})*))(\3)@)?
                                    (?=(\[[0-9A-F:.]{2,}\]|(?:[a-z0-9-._~!$&'()*+,;=]|%[0-9A-F]{2})*))\5
                                    (?::(?=(\d*))\6)?
                                )
                                (\/(?=((?:[a-z0-9-._~!$&'()*+,;=:@\/]|%[0-9A-F]{2})*))\8)?
                                |
                                (\/?(?!\/)(?=((?:[a-z0-9-._~!$&'()*+,;=:@\/]|%[0-9A-F]{2})*))\10)?
                            )
                            (?:
                                \?(?=((?:[a-z0-9-._~!$&'()*+,;=:@\/?]|%[0-9A-F]{2})*))\11
                            )?
                            (?:
                                #(?=((?:[a-z0-9-._~!$&'()*+,;=:@\/?]|%[0-9A-F]{2})*))\12
                            )?
                            $''', re.VERBOSE)
    def __init__(self):
        pass
    
    def parse(self, uri_input):
        if uri_input:
            return self.parseUri(uri_input)
        else:
            return (UriParserError("{} is an invalid URI input!".format(uri_input), ReturnStatus.Invalid_Input), None)
            
    def parseUri(self, uri_input):
        pattern_match = UriParser.pattern_2.fullmatch(uri_input)
        if pattern_match:
            return UriParserError("All Good", ReturnStatus.OK), None
        else:
            return UriParserError("Invalid format of input URI".format(uri_input), ReturnStatus.Invalid_Format), None



