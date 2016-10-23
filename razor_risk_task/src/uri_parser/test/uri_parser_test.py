# -*- coding: utf-8 -*-
'''
Created on 22 Oct 2016

@author: MetalInvest
'''
import unittest
from uri_parser.uri_parser import UriParser
from uri_parser.uri_parser_error import UriParserError
from uri_parser.uri_parser_error import ReturnStatus
from uri_parser.uri_rep import *



class UriTest(unittest.TestCase):

    def setUp(self):
        self.parser = UriParser()

    def testURIRep(self):
        uri = uri_address("www.google.com")
        scheme = uri_scheme("http")
        uri.addScheme(scheme)
          
        authority = uri_authority("cometcao@www.google.com:8080")
        usr = uri_usr_info("cometcao")
        host = uri_host("www.google.com")
        port = uri_port("8080")
        authority.addHost(host)
        authority.addPort(port)
        authority.addUserInfo(usr)
        uri.addAuthority(authority)
          
        path = uri_path("/testpath")
        query = uri_query("param=1")
        fragment = uri_fragment("testFag")
        uri.addPath(path)
        uri.addQuery(query)
        uri.addFragment(fragment)
        self.failUnless(str(uri) == "http://cometcao@www.google.com:8080/testpath?param=1#testFag")
 
    def testParseNone(self):
        error, _ = self.parser.parse(None)
        self.failUnless(error.status == ReturnStatus.Invalid_Input)
         
    def testParseURI(self):
        error, _ = self.parser.parse("abc://username:password@example.com:123/path/data?key=value&key2=value2#fragid1")
        self.failUnless(error.status == ReturnStatus.OK)
         
    def testParseURI2(self):
        error, _ = self.parser.parse("urn:example:mammal:monotreme:echidna")
        self.failUnless(error.status == ReturnStatus.OK)
     
    def testParseSimpleUrl(self):
        error, _ = self.parser.parse("https://example.org/absolute/URI/with/absolute/path/to/resource.txt")
        self.failUnless(error.status == ReturnStatus.OK)
     
    def testParseSimpleFtp(self):
        error, _ = self.parser.parse("ftp://example.org/resource.txt")
        self.failUnless(error.status == ReturnStatus.OK)
     
    def testParseSimpleMailTo(self):
        error, _ = self.parser.parse("urn:ISSN:1535-3631")
        self.failUnless(error.status == ReturnStatus.OK)
 
    def testParseURIComponent(self):
        _, uri = self.parser.parse("abc://username:password@example.com:123/path/data?key=value&key2=value2#fragid1")
        self.failUnless(uri.getSchemeValue() == "abc")
        self.failUnless(uri.getAuthorityValue() == "username:password@example.com:123")
        self.failUnless(uri.getPathValue() == "/path/data")
        self.failUnless(uri.getQueryValue() == "key=value&key2=value2")
        self.failUnless(uri.getFragmentValue() == "fragid1")

    def testParseURIComponent2(self):
        _, uri = self.parser.parse("urn:ISSN:1535-3631")
        self.failUnless(uri.getSchemeValue() == "urn")
        self.failUnless(uri.getAuthorityValue() == "")
        self.failUnless(uri.getPathValue() == "ISSN:1535-3631")
        self.failUnless(uri.getQueryValue() == "")
        self.failUnless(uri.getFragmentValue() == "")

    def testParseFalseUrl(self):
        pass
    
    def testParseFalseFtp(self):
        pass
    
    def testParseFalseUrn(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()