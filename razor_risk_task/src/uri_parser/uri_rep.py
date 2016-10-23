'''
Created on 22 Oct 2016

@author: MetalInvest
'''


class uri_address():
    def __init__(self, raw_input):
        self.raw_input = raw_input
        self.scheme = None
        self.path = None
        self.authority = None
        self.query = None
        self.fragment = None


    def scheme(self):
        return self.scheme
    
    def addScheme(self,scheme):
        self.scheme = scheme
    
    def path(self):
        return self.path
    
    
    def addPath(self, path):
        self.path = path
    

    def authority(self):
        return self.authority
    
    
    def addAuthority(self, authority):
        self.authority = authority
        
    def query(self):
        return self.query
    
    def addQuery(self, query):
        self.query = query
        
    def fragment(self):
        return self.fragment
    
    
    def addFragment(self, fragment):
        self.fragment = fragment
        
    
        
    def __repr__(self, *args, **kwargs):
        '''
        this method reconstructs the full address from each component
        '''
        #return uri_component.__repr__(self, *args, **kwargs)
        pass

#######################################################
class uri_component(object):
    '''
    basic brick for the uri component
    '''
    def __init__(self, value):
        '''
        Basic value
        '''
        self.value = value


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
        self.usr = None
        self.host = None
        self.port = None
        
    def addUserInfo(self, usrInfo):
        self.usr = usrInfo
        
    def userInfo(self):
        return self.usr
    
    def addHost(self, host):
        self.host = host
        
    def host(self):
        return self.host
    
    def addPort(self, port):
        self.port = port
        
    def port(self):
        return self.port
        
class uri_path(uri_component):
    def __init__(self, value):
        super(value)
        
class uri_query(uri_component):
    def __init__(self, value):
        super(value)

class uri_fragment(uri_component):
    def __init__(self, value):
        super(value)