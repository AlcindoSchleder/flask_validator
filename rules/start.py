import sys
import argparse
import fileinput


class ValidateTrannsactions:
    """
    Class that initialize application.
    App can be starting with [-i, --input] parameters
    informing transaction commands or use pipe '<'
    with file name to standard input
    """

    _parser = None
    _args = None
    _filename = None
    testing = False

    def __init__(self, test: bool = False):
        """
        constructor
        """
        self._args = None
        self._filename = None
        self.testing = test
        if not test:    # if not running test configure argparser
            self._parser = self._configure_parser()    # configure parser arguments
            self._args = self._parser.parse_args()

    def _configure_parser(self):
        """
        Configure all parsers parameters and get argv informed
        :return: parser object
        """
        parser = argparse.ArgumentParser(
            prog='python inputredir.py',
            description='run a API with file of commands or not!',
        )
        parser.add_argument(
            '-i', dest='input',
            help='File with input commands to process',
            type=str
        )
        parser.add_argument(
            '--input', dest='input',
            help='File with input commands to process',
            type=str
        )
        return parser

    def _open_pipe(self):
        """
        Generator from standard input lines
        :return: string with json transaction
        """
        for line in fileinput.input():
            yield line.replace('\n', '')

    def _open_param_file(self):
        """
        open file name informed with paramenter on [-i, --input] options
        :return: string with json transaction
        """
        with open(self._filename, 'r') as fd:
            for line in fd.readlines():
                yield line.replace('\n', '')

    def start(self):
        """
        Start Configurations reading and processing data from given prompt files
        :return: void
        """
        gen = None
        self._filename = self._args.input
        if self._filename is not None:
            gen = self._open_param_file()
        elif not sys.stdin.line_buffering:
            gen = self._open_pipe()
        else:
            return False
        while True:
            try:
                line = next(gen)
                # implement transaction operations here
                print(f'File Data: {line}')
            except StopIteration:
                break
        if gen is not None:
            gen.close()
        return True
