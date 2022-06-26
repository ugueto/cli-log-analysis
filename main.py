import argparse
import json
from file_processor import process_input
from operations import Operations


def main():

    log_parser = argparse.ArgumentParser(prog="Swiss Re log analyzer", description="Analyze the content of log files.",
                                         usage="%(prog)s [options]",
                                         epilog="At least one optional argument must be chosen in order "
                                                "to perform an operation.")
    log_parser.add_argument("input_path", nargs="+", type=argparse.FileType("r", encoding="UTF-8"),
                            help="Path to one or more plain text files, or a directory.")
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

    # Process the input file given.
    data = process_input(args_dict["input_path"][0].name)

    # Pass the sample_data into a Operations object.
    ops_data = Operations(data)

    # Operations to perform based on arguments, perform a certain operation if value is equal to True.
    with open(args_dict["output_path"][0].name, "a") as f:
        if args_dict["s"]:
            json.dump(ops_data.events_per_second(), f)
        elif args_dict["mfip"]:
            json.dump(ops_data.most_frequent_ip(), f)
        elif args_dict["lfip"]:
            json.dump(ops_data.least_frequent_ip(), f)
        elif args_dict["be"]:
            json.dump(ops_data.total_bytes_exchanged(), f)


if __name__ == "__main__":
    main()
