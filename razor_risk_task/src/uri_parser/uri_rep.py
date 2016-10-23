'''
Created on 22 Oct 2016

@author: MetalInvest

data structure:
    uri_address
        scheme
        authority
            userinfo
            host
            port
        path
        query
        fragment


'''


class uri_address:
    def __init__(self, raw_input):
        self.raw_input = raw_input
        self.scheme = None
        self.path = None
        self.authority = None
        self.query = None
        self.fragment = None


    def getScheme(self):
        return self.scheme
    
    def getSchemeValue(self):
        if self.scheme:
            return self.scheme.getValue()
        else:
            return ""
    
    def addScheme(self,scheme):
        self.scheme = scheme
    
    def getPath(self):
        return self.path
    
    def getPathValue(self):
        if self.path:
            return self.path.getValue()
        else:
            return ""
    
    def addPath(self, path):
        self.path = path
    
    def getAuthority(self):
        return self.authority
    
    def getAuthorityValue(self):
        if self.authority:
            return self.authority.getValue()
        else:
            return ""
    
    def getUserInfoValue(self):
        if self.authority and self.authority.getUserInfo():
            return self.authority.getUserInfo().getValue()
        else:
            return ""
    
    def getHostValue(self):
        if self.authority and self.authority.getHost():
            return self.authority.getHost().getValue()
        else:
            return ""
    
    def getPortValue(self):
        if self.authority and self.authority.getPort():
            return self.authority.getPort().getValue()
        else:
            return ""
    
    def addAuthority(self, authority):
        self.authority = authority
        
    def getQuery(self):
        return self.query
    
    def getQueryValue(self):
        if self.query:
            return self.query.getValue()
        else:
            return ""
    
    def addQuery(self, query):
        self.query = query
        
    def getFragment(self):
        return self.fragment
    
    def getFragmentValue(self):
        if self.fragment:
            return self.fragment.getValue()
        else:
            return ""
    
    def addFragment(self, fragment):
        self.fragment = fragment
        
    def __repr__(self):
        '''
        this method reconstructs the full address from each component
        '''
        return "{}{}{}{}{}".format(self.scheme, self.authority, self.path, self.query, self.fragment)

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

    def getValue(self):
        return self.value

    def __repr__(self):
        return str(self.value)

class uri_scheme(uri_component):
    delimiter_full = "://"
    delimiter = ":"
    def __repr__(self):
        if self.value == "urn":
            return "{}{}".format(self.value, uri_scheme.delimiter)
        else:
            return "{}{}".format(self.value, uri_scheme.delimiter_full)

class uri_usr_info(uri_component):
    delimiter = "@"
    def __repr__(self):
        return "{}{}".format(self.value, uri_usr_info.delimiter)
        
class uri_host(uri_component):
    pass

class uri_port(uri_component):
    delimiter = ":"
    def __repr__(self):
        if self.value:
            return "{}{}".format(uri_port.delimiter, self.value)
        else:
            return ""

class uri_authority(uri_component):
    def __init__(self, value):
        super().__init__(value)
        self.usr = None
        self.host = None
        self.port = None
        
    def addUserInfo(self, usrInfo):
        self.usr = usrInfo
        
    def getUserInfo(self):
        return self.usr
    
    def addHost(self, host):
        self.host = host
        
    def getHost(self):
        return self.host
    
    def addPort(self, port):
        self.port = port
        
    def getPort(self):
        return self.port
    
    def getValue(self):
        return self.__repr__()
    
    def __repr__(self):
        if self.usr and self.usr.getValue():
            return "{}{}{}".format(self.usr, self.host, self.port)
        elif self.host and self.host.getValue():
            return str(self.host)
        else:
            return ""
        
class uri_path(uri_component):
    pass
#     delimiter = "/"
#     def __repr__(self):
#         return uri_component.__repr__(self)
    
        
class uri_query(uri_component):
    delimiter = "?"
    delimiter_and = "&"
    def __repr__(self):
        if self.value:
            return "{}{}".format(uri_query.delimiter, self.value)
        else:
            return ""

class uri_fragment(uri_component):
    delimiter = "#"
    def __repr__(self):
        if self.value:
            return "{}{}".format(uri_fragment.delimiter, self.value)
        else:
            return ""