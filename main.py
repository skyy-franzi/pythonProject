#!/usr/bin/python

from sqlConnector import sql_Connector
#! from sql_connect_unittest import Test_Connector
#! from parsePara import parameter_help
#! import logging

sqlCon = sql_Connector()
sqlCon.generate("output.csv")


#! logging.basicConfig(
   #! filename="test.log",
    #! level=logging.INFO,
    #! format="%(asctime)s:%(levelname)s:%(message)s")


#! parsePa = parameter_help
#! parsePa.parseHelp()

#! testCase = Test_Connector
#! testCase.test_connector()