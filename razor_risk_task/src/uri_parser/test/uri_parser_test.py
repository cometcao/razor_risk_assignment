'''
Created on 22 Oct 2016

@author: MetalInvest
'''
import unittest
from uri_parser.uri_parser import UriParser
from uri_parser.uri_parser_error import UriParserError
from uri_parser.uri_parser_error import ReturnStatus
from uri_parser.uri_rep import *



class BasicTest(unittest.TestCase):


    def setUp(self):
        self.parser = UriParser(None)

    def testParse(self):
        error, _ = self.parser.parse()
        self.failUnless(error.status == ReturnStatus.Invalid_Input)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()