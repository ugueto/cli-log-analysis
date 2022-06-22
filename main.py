# argparse is a standard Python library for command line interfaces.
import argparse
# import datetime
# import json
# import os
# import sys


log_parser = argparse.ArgumentParser(prog="Swiss Re log analyzer", description="Analyze the content of log files.",
                                     usage="%(prog)s [options]",
                                     epilog="At least one optional argument must be chosen in order "
                                            "to perform an operation.")
log_parser.add_argument("input_path", nargs="+", type=argparse.FileType("r", encoding="UTF-8"),
                        help="Path to one or more plain text files, or a directory.")
log_parser.add_argument("-a", "--all", action="store_true",
                        help="Perform all operations (--mfip, --lfip, -s, --be) to the log file.")
log_parser.add_argument("-s", action="store_true", help="Events per second in the log file.")
# Assumption: The following operations are directed to the Client IP address, and not the destination.
log_parser.add_argument("--mfip", action="store_true", help="Most frequent IP address in the log file.")
log_parser.add_argument("--lfip", action="store_true", help="Least frequent IP address in the log file.")
# Assumption: The total amount of bytes is equal to response header size + response size.
log_parser.add_argument("--be", action="store_true", help="Total amount of bytes exchanged in the log file.")
log_parser.add_argument("output_path", nargs=1, type=argparse.FileType("w", encoding="UTF-8"),
                        help="Path to a file to save output in plain text JSON format.")

args = log_parser.parse_args()
print(vars(args))
