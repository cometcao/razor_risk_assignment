'''
The defintion of URI comes from:
https://en.wikipedia.org/wiki/Uniform_Resource_Identifier
https://tools.ietf.org/html/rfc3986

The core parser is implemented using Regex (RE). 
With reference to https://pypi.python.org/pypi/rfc3987#downloads
The Regex of URI was taken from http://snipplr.com/view/6889/regular-expressions-for-uri-validationparsing/
Many thanks to stackoverflow

Regex debugged by using: https://www.debuggex.com/

    ^
    ([a-z][a-z0-9+.-]*):                                                             #1 scheme
    (?:
        \/\/                                                                         it has an authority:
        
        (                                                                            #2 authority
            (?:(?=((?:[a-z0-9-._~!$&'()*+,;=:]|%[0-9A-F]{2})*))(\3)@)?               #4 userinfo
            (?=(\[[0-9A-F:.]{2,}\]|(?:[a-z0-9-._~!$&'()*+,;=]|%[0-9A-F]{2})*))\5        #5 host 
            (?::(?=(\d*))\6)?                                                        #6 port
        )
        
        (\/(?=((?:[a-z0-9-._~!$&'()*+,;=:@\/]|%[0-9A-F]{2})*))\8)?                   #7 path
    
        |                                                                            it doesn't have an authority:
        
        (\/?(?!\/)(?=((?:[a-z0-9-._~!$&'()*+,;=:@\/]|%[0-9A-F]{2})*))\10)?           #9 path
    )
    (?:
        \?(?=((?:[a-z0-9-._~!$&'()*+,;=:@\/?]|%[0-9A-F]{2})*))\11                    #11 query string
    )?
    (?:
        \#(?=((?:[a-z0-9-._~!$&'()*+,;=:@\/?]|%[0-9A-F]{2})*))\12                    #12 fragment
    )?
    $
'''

from uri_parser_error import UriParserError
from uri_parser_error import ReturnStatus
from uri_rep import *
import re

class UriParser(object):
    flags = re.X | re.I | re.L
    #pattern2 = re.compile('''^([a-z][a-z0-9+.-]*):(?:\/\/((?:(?=((?:[a-z0-9-._~!$&'()*+,;=:]|%[0-9A-F]{2})*))(\3)@)?(?=(\[[0-9A-F:.]{2,}\]|(?:[a-z0-9-._~!$&'()*+,;=]|%[0-9A-F]{2})*))\5(?::(?=(\d*))\6)?)(\/(?=((?:[a-z0-9-._~!$&'()*+,;=:@\/]|%[0-9A-F]{2})*))\8)?|(\/?(?!\/)(?=((?:[a-z0-9-._~!$&'()*+,;=:@\/]|%[0-9A-F]{2})*))\10)?)(?:\?(?=((?:[a-z0-9-._~!$&'()*+,;=:@\/?]|%[0-9A-F]{2})*))\11)?(?:#(?=((?:[a-z0-9-._~!$&'()*+,;=:@\/?]|%[0-9A-F]{2})*))\12)?$''', re.I)
    pattern=re.compile(r'''^
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
                                \#(?=((?:[a-z0-9-._~!$&'()*+,;=:@\/?]|%[0-9A-F]{2})*))\12
                            )?
                            $''', flags)
    def __init__(self):
        pass
    
    def parse(self, uri_input):
        '''
        The main parse method, return parse status and URI representation if successful
        '''
        if uri_input:
            return self.parseUri(uri_input)
        else:
            return (UriParserError("{} is an invalid URI input!".format(uri_input), ReturnStatus.Invalid_Input), None)
            
    def parseUri(self, uri_input):
        pattern_match = UriParser.pattern.fullmatch(uri_input)
        if pattern_match:
            #self.displayMatchingGroups(pattern_match)
            uri = self.constructURIcomponent(uri_input, pattern_match)
            return UriParserError("All Good", ReturnStatus.OK), uri
        else:
            return UriParserError("Invalid format of input URI".format(uri_input), ReturnStatus.Invalid_Format), None

    def constructURIcomponent(self, uri_input, pattern_match):
        uri = uri_address(uri_input)
        
        scheme = uri_scheme(pattern_match.group(1))
        uri.addScheme(scheme)
        
        if pattern_match.group(2):
            authority = uri_authority(pattern_match.group(2))
            usr = uri_usr_info(pattern_match.group(4))
            host = uri_host(pattern_match.group(5))
            port = uri_port(pattern_match.group(6))
            authority.addHost(host)
            authority.addPort(port)
            authority.addUserInfo(usr)
            uri.addAuthority(authority)
        
        if pattern_match.group(7):
            path = uri_path(pattern_match.group(7))
            uri.addPath(path)
        elif pattern_match.group(9):
            path = uri_path(pattern_match.group(9))
            uri.addPath(path)
        
        if pattern_match.group(11):
            query = uri_query(pattern_match.group(11))
            uri.addQuery(query)
            
        if pattern_match.group(12):
            fragment = uri_fragment(pattern_match.group(12))
            uri.addFragment(fragment)
        
        return uri
        

    def displayMatchingGroups(self, pattern_match):
        print("group 1 scheme: {}".format(pattern_match.group(1)))
        print("group 2 authority: {}".format(pattern_match.group(2)))
        print("group 3: {}".format(pattern_match.group(3)))
        print("group 4 user info: {}".format(pattern_match.group(4)))
        print("group 5 host: {}".format(pattern_match.group(5)))
        print("group 6 port: {}".format(pattern_match.group(6)))
        print("group 7 path: {}".format(pattern_match.group(7)))
        print("group 8: {}".format(pattern_match.group(8)))
        print("group 9 path: {}".format(pattern_match.group(9)))
        print("group 10: {}".format(pattern_match.group(10)))
        print("group 11 query: {}".format(pattern_match.group(11)))
        print("group 12 fragment: {}".format(pattern_match.group(12)))

