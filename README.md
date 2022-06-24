# cli-log-analysis
 A command line tool to analyze the content of logs.

## Getting started:

1. Download and install PyCharm -> https://www.jetbrains.com/pycharm/download/
2. Download and install Docker (Desktop preferably) -> https://docs.docker.com/get-docker/
3. Connect GitHub to Pycharm & clone repo.
4. Docker commands:
    -> docker build --tag cli-log-analysis .
    -> docker run cli-log-analysis
5. Once the project is set up, run the following command on your terminal: "python main.py -h".
6. If all went well, you should see something like this:
![help](https://github.com/ugueto/cli-log-analysis/blob/master/help.png?raw=true)
7. Read through the help page and you are ready to get started.

NOTES: 
The application includes sample data for testing purposes.
In order to begin, you must have a sample log file in the same format as the sample data. If not, please use the sample data (Different formats will be supported in later versions).


In order to better understand functionality, read the comments on instructions.txt file.