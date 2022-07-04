# cli-log-analysis
 A command line tool to analyze the content of logs.

## Getting started:

1. Download and install PyCharm -> https://www.jetbrains.com/pycharm/download/
2. Download and install Docker (Desktop preferably) -> https://docs.docker.com/get-docker/
3. Connect GitHub to Pycharm & clone repo.
4. Docker commands:
    -> docker build --tag cli-log-analysis .
    -> docker run cli-log-analysis
5. Once the project is set up and you are in the correct directory, run the following command on your terminal: "python main.py -h".
   1. If all went well, you should see the following text:
       >usage: Swiss Re log analyzer [options]
        Analyze the content of log files. 
        positional arguments:
        input_path   Path to one or more plain text files, or a directory.
        output_path  Path to a file to save output in plain text JSON format. 
        optional arguments:
     -h, --help   show this help message and exit
     -s           Events per second in the log file.
     --mfip       Most frequent IP address in the log file.
     --lfip       Least frequent IP address in the log file.
     --be         Total amount of bytes exchanged in the log file.
     --version    show program's version number and exit 
        NOTE: At least one optional argument must be chosen in order to perform an operation.

6. Read through the help page and you are ready to get started.


NOTES: 
The application includes (compressed) sample data for testing purposes. Extract the .log file and use it for testing.
For example, try this command from the app directory: "python main.py "./sample_data/access.log" "./results.json" -s" and see the results in the results.json file.

In order to use this app, you must have a log file in the same format as the sample data. If not, please use the sample data.

_Being developed for future versions_:
- Bug fixes [ ]
- Multiple files/directory as input_path [X]
- Different log formats will be supported. [ ]
- Clean up software design [ ]
- Implement unit testing [ ]
- Implement an -a (all) operation [ ]

