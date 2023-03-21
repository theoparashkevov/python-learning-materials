"""
The Common Reuse Component Cohesion principle states that components should contain classes that can be easily reused
in other projects or parts of the same project. In Python, this can be achieved by creating classes that are modular,
independent, and can be easily integrated into different systems.

In this example, we have three classes: Database, Email, and Logger.
These classes can be used in different projects or parts of the same project, as they are modular and can be easily
integrated into different systems.

For example, the Database class can be used in a web application to connect to a database and execute queries,
while the Email class can be used in a script to send an email notification, and the Logger class can be used
in a data processing system to log messages to a file.

By separating these functionalities into different classes, we achieve a higher level of cohesion within each class,
and we can easily reuse them in different projects or parts of the same project, which aligns with
the Common Reuse Component Cohesion principle.
"""

class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def connect(self):
        # code to connect to the database
        pass

    def execute_query(self, query):
        # code to execute a query on the database
        pass


class Email:
    def __init__(self, subject, body, to, from_email):
        self.subject = subject
        self.body = body
        self.to = to
        self.from_email = from_email

    def send_email(self):
        # code to send an email
        pass


class Logger:
    def __init__(self, log_file):
        self.log_file = log_file

    def log(self, message):
        # code to log a message to a file
        pass
