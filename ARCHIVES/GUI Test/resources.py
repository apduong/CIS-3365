import pyodbc


def server_connection():
    conn = pyodbc.connect('Driver={SQL Server};'  # Leave this as is
                          'Server=LAPTOP-S6PL64NB;'  # Enter your local Server Name
                          'Database=Project_Data;'  # Enter your Database Name
                          'Trusted_Connection=yes;')  # Leave this as is
    return conn
