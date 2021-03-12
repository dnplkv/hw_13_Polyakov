import argparse
import os


class Parser():
    """Class for getting parser
    """
    def parse_args(self):
        """Adding a parser for directory with pictures
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('--path',
                            metavar="path",
                            type=str,
                            required=True,
                            help="path to directory with .txt file")
        return parser.parse_args()

    def final_text(self):
        f = open(os.path.join(self.parse_args().path), "r")
        a = f.read()
        a = a.replace('\n', ' ')
        return a
