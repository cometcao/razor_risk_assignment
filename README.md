# razor_risk_assignment

Due to implied mutual confidential agreement, this file will not provide description of the task.


1. project summary:
TDD was employed during the implementation of this project. This python component implemented a simple URI parser (full description in uri_parser.py). Regex is used to match URI format and matching data are passed from regex capturing groups.
The data structure are described on the top of uri_rep.py file, and the uri_parser_error.py defines the parser return status. Unittests are defined in uri_parser_test.py
Current solution have this draw-back of being unable to provide meaningful error message precisely to the element of the URI address

2. possible alternative implementations:
a. full hand code of string manipulation (this could take a lot of time)
b. using pyparsing module
c. using a python parser generator

3. performances:
The performance of current implementation will be dependent on the regex engine and the regex pattern employed.

4. possible improvements:
The regex pattern could certainly be revised and improved to be more robost/efficient
