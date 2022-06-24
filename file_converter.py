import pandas as pd


def process_input(file_path):
    """This function will take the original format, parse it into a list of dictionaries (JSON format),
    then it will take the JSON-like object and convert it to a Pandas DataFrame object."""

    data = []

    # Original testing log format is hardcoded - NOT ideal. Must think of a solution for this.
    log_format = ["timestamp", "response_header_size", "client_ip_address", "http_response_code", "response_size",
                  "http_request_method", "url", "username", "destination_ip", "response_type"]

    with open(file_path, encoding="UTF-8") as f:
        f = f.readlines()

    for line in f:
        # Separators might change depending on log format, another issue to consider.
        details = line.split(" ")
        details = [x.strip() for x in details if x]
        structure = {key: value for key, value in zip(log_format, details)}
        print(structure)
        data.append(structure)

    # Pandas is an ideal Python library for performing operations/calculations on tabular data.
    df = pd.json_normalize(data)

    return df
