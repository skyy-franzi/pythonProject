import unittest

from sqlConnector import sql_Connector

class Test_Connector(unittest.TestCase):
    def test_connector(self):
        sqlCon = sql_Connector()

        assert sqlCon.generate("output") == False
        assert sqlCon.generate("output.csv") == True


if __name__ == '__main__':
            unittest.main()
