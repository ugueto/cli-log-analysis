# argparse is a standard Python library for command line interfaces.
import argparse
# import datetime
import itertools
# import json
# import os
# import sys


def main():

    log_parser = argparse.ArgumentParser(prog="Swiss Re log analyzer", description="Analyze the content of log files.",
                                         usage="%(prog)s [options]",
                                         epilog="At least one optional argument must be chosen in order "
                                                "to perform an operation.")
    log_parser.add_argument("input_path", nargs="+", type=argparse.FileType("r", encoding="UTF-8"),
                            help="Path to one or more plain text files, or a directory.")
    log_parser.add_argument("-a", "--all", action="store_true",
                            help="Perform all operations (--mfip, --lfip, -s, --be) to the log file.")
    log_parser.add_argument("-s", action="store_true", help="Events per second in the log file.")
    # Assumption: The following operations are directed to the Client IP address, and not the destination IP.
    log_parser.add_argument("--mfip", action="store_true", help="Most frequent IP address in the log file.")
    log_parser.add_argument("--lfip", action="store_true", help="Least frequent IP address in the log file.")
    # Assumption: The total amount of bytes is equal to response header size + response size.
    log_parser.add_argument("--be", action="store_true", help="Total amount of bytes exchanged in the log file.")
    log_parser.add_argument("output_path", nargs=1, type=argparse.FileType("w", encoding="UTF-8"),
                            help="Path to a file to save output in plain text JSON format.")
    log_parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    args = log_parser.parse_args()
    args_dict = dict(vars(args))
    print(args_dict)
    operation_args = itertools.islice(args_dict.items(), 1, len(args_dict) - 1)

    # Operations to perform based on arguments.
    '''for key, val in operation_args:
        # Perform a certain operation if value is equal to True.
        if operation_args['all']:
            pass
        elif operation_args['s']:
            pass
        elif operation_args['mfip']:
            pass
        elif operation_args['lfip']:
            pass
        elif operation_args['be']:
            pass'''


if __name__ == "__main__":
    main()
