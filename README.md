# Python / SQL Exercise

This repository contains the files to run tests against an existing PostgreSQL database. 

For an example of an output of the `reportGen.py` file, click [here](output.md)

## Running the script

The `reportGen.py` file utilizes three queries to generate reports for the following three questions:

  1. What are the most popular three articles of all time? `topArticles.sql`
  1. Who are the most popular article authors of all time? `topAuthors.sql`
  1. On which days did more than 1% of requests lead to errors? `totalErrors.sql`

**NOTE:** Before running the `reportGen.py` file, there are some required views.
**NOTE:** Modify the `reportGen.py` file with your user and password. 

## Views Needed

The python script expects the following views to exist within the database:

#### vw_httpStatusError

```sql
CREATE VIEW vw_httpStatusError AS
SELECT count(*), status, DATE(TIME), SUBSTRING(status, 1, 3) as httpStatus
FROM log
WHERE status = '404 NOT FOUND'
GROUP BY status, DATE(TIME)
ORDER BY DATE(TIME)
```

#### vw_httpStatusOK

```sql
CREATE VIEW vw_httpStatusOK AS
SELECT count(*), status, DATE(TIME), SUBSTRING(status, 1, 3) as httpStatus
FROM log
WHERE status = '200 OK'
GROUP BY status, DATE(TIME)
ORDER BY DATE(TIME)
```

#### vw_topArticles

```sql
CREATE VIEW vw_topArticles AS 
SELECT DISTINCT count(*), A.title, FORMAT('"%s" - %s views', A.title, count(*)) AS POPULAR 
FROM log l INNER JOIN articles A ON SUBSTRING(l.path, 10, 100) = A.SLUG
GROUP BY A.title 
ORDER BY count(*) desc
LIMIT 3
```

#### vw_topAuthors

```sql
CREATE VIEW vw_topAuthors AS
SELECT DISTINCT count(*), AU.name, FORMAT('%s - %s views', AU.name, count(*)) AS POPULAR 
FROM log l INNER JOIN articles A ON SUBSTRING(l.path, 10, 100) = A.SLUG
INNER JOIN Authors AU ON AU.ID = A.author
GROUP BY AU.name
ORDER BY count(*) desc
```
