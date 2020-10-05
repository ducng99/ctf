# Where’s Tron?

```
We've lost Tron on the grid, find him using this uplink!

http://chal.ctf.b01lers.com:3004
```

We were given a link to a page that executes SQL queries with a server.py file.

In server.py file, we can see that it is connected to MySQL db with database name `grid`

The first command I executed was `SHOW TABLES`, however that returned a syntax error.

I then continued with
```sql
SELECT table_name FROM information_schema.tables WHERE table_schema = 'grid'
```
to view all tables in database `grid` from `information_schema` database/schema

The page returned 3 tables with multiple entries. Looking at `server.py`, our queries are limited to show only 20 entries at a time, so the flag could be one of the entries that weren't shown.

In the task description, it tells us to find Tron, so I made a query to look for a person name Tron. And this gives me the flag in location column
```sql
SELECT * FROM programs WHERE name LIKE "%Tron%"
```