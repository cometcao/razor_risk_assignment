'''
Created on 22 Oct 2016

@author: MetalInvest
'''

class uri_component(object):
    '''
    basic brick for the uri component
    '''
    def __init__(self, value):
        '''
        Basic value
        '''
        self.value = value

class uri_address(uri_component):
    def __init__(self, value):
        super(value)
    
    def addScheme(self,scheme):
        self.scheme = scheme
    
    def addPath(self, path):
        self.path = path
    
    def addAuthority(self, authority):
        self.authority = authority
        
    def addQuery(self, query):
        self.query = query
        
    def addFragment(self, fragment):
        self.fragment = fragment

#######################################################
    
class uri_scheme(uri_component):
    def __init__(self, value):
        super(value)

class uri_usr_info(uri_component):
    def __init__(self, value):
        super(value)
        
class uri_host(uri_component):
    def __init__(self, value):
        super(value)

class uri_port(uri_component):
    def __init__(self, value):
        super(value)

class uri_authority(uri_component):
    def __init__(self, value):
        super(value)
        
    def addUserInfo(self, usrInfo):
        self.usr = usrInfo
    
    def addHost(self, host):
        self.host = host
    
    def addPort(self, port):
        self.port = port
        
class uri_path(uri_component):
    def __init__(self, value):
        super(value)
        

class uri_query(uri_component):
    def __init__(self, value):
        super(value)

class uri_fragment(uri_component):
    def __init__(self, value):
        super(value)