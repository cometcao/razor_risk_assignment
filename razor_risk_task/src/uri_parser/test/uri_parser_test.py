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

    def testParseNone(self):
        error, _ = self.parser.parse(None)
        self.failUnless(error.status == ReturnStatus.Invalid_Input)
    
    def testParseSimpleUrl(self):
        error, _ = self.parser.parse("https://example.org/absolute/URI/with/absolute/path/to/resource.txt")
        self.failUnless(error.status == ReturnStatus.OK)
    
    def testParseSimpleFtp(self):
        error, _ = self.parser.parse("ftp://example.org/resource.txt")
        self.failUnless(error.status == ReturnStatus.OK)
    
    def testParseSimpleMailTo(self):
        error, _ = self.parser.parse("urn:ISSN:1535-3631")
        self.failUnless(error.status == ReturnStatus.OK)


    def testParseFalseUrl(self):
        pass
    
    def testParseFalseFtp(self):
        pass
    
    def testParseFalseUrn(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()