class Operations:
    """The Operations class is created with a NameSpace object and includes all methods to perform operations."""

    def __init__(self, obj):
        # After processing the input log file, we can create an Operations object that accepts a DataFrame as argument.
        self.obj = obj

    def all_operations(self):
        events_per_second = 0  # self.events_per_second()
        mfip = self.most_frequent_ip()
        lfip = self.least_frequent_ip()
        total_bytes_exchanged = self.total_bytes_exchanged()
        return events_per_second, mfip, lfip, total_bytes_exchanged

    def events_per_second(self):
        self.obj['timestamp'] = self.obj['timestamp'].apply(lambda x: int(float(x)) if x else 0)
        return 0

    def most_frequent_ip(self):
        # The mode (most frequent value) of the Client IP Address column in the Pandas DataFrame.
        return self.obj['client_ip_address'].mode()

    def least_frequent_ip(self):
        # Calculate the frequency of all values in the Client IP Address column and returning the least frequent.
        return self.obj['client_ip_address'].value_counts().index[-1]

    def total_bytes_exchanged(self):
        # Change NaN values in both columns to zero.
        self.obj['response_header_size'] = self.obj['response_header_size'].fillna(0)
        self.obj['response_size'] = self.obj['response_size'].fillna(0)

        # Change column data type to int64.
        self.obj['response_header_size'] = self.obj['response_header_size'].astype('int64')
        self.obj['response_size'] = self.obj['response_size'].astype('int64')

        # Calculate total sum of both columns.
        bytes_exchanged = self.obj['response_header_size'].sum() + self.obj['response_size'].sum()

        return bytes_exchanged