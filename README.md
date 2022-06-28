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
6. If all went well, you should see something like this:
![help](https://github.com/ugueto/cli-log-analysis/blob/master/img/help.jpg?raw=true)
7. Read through the help page and you are ready to get started.


NOTES: 
The application includes (compressed) sample data for testing purposes. First, extract the .log file and use it for testing.
For example, after extracting, try this command from the app directory: "python main.py "./sample_data/access.log" "./results.json" -s" and see the results in the results.json file.

In order to use this app, you must have a log file in the same format as the sample data. If not, please use the sample data.

_To be developed in future versions_:
- Bug fixes.
- Multiple files/directory as input_path.
- Different log formats will be supported.
- Clean up software design.
- Implement unit testing.
- Implement an -a (all) operation.

(Different formats will be supported in later versions)

