import sys
import psycopg2

try:
    conn = psycopg2.connect(user="USER",
                            password="PASSWORD",
                            host="localhost",
                            port="5432",
                            database="news")
    c = conn.cursor()
    print(c)
    # Open and read the file as a single buffer
    with open('master.sql', 'r') as fd:
        sqlFile = fd.read()
    # all SQL commands (split on ';')
    sqlCommands = sqlFile.splitlines()
    # Execute every command from the input file
    # This will skip and report errors
    # For example, if the tables do not yet exist, this will skip over
    # the DROP TABLE commands
    for command in sqlCommands:
        try:
            c.execute(command)
            print(c.fetchall())
        except psycopg2.DatabaseError, e:
            print "Command skipped: ", e
except psycopg2.DatabaseError, e:
    print('I am unable to connect the database: %s ', e)
    sys.exit(1)
