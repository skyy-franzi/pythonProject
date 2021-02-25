import argparse

    class parameter_help:
        def parseHelp(self):
            parser=argparse.ArgumentParser(
            description='''My Description. And what a lovely description it is. ''',
            epilog="""All is well that ends well.""")
            parser.add_argument('-h', help='Zeigt diese Hilfe an')
            parser.add_argument('--help', help='Zeigt Hilfe an')
            args = parser.parse_args()
