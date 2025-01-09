# Sample Demo

## Run #1:


```
docker run -d --name postgres1 -e POSTGRES_PASSWORD=dev -p 5432:5432 postgres:latest
docker run -d --name postgres2 -e POSTGRES_PASSWORD=dev -p 5433:5432 postgres:13
docker run -d --name postgres3 -e POSTGRES_PASSWORD=dev -p 5434:5432 postgres:12
```


Open Docker Dashboard and run the following commands:

```
# psql -d postgres -U postgres -W
Password: 
psql (17.2 (Debian 17.2-1.pgdg120+1))
Type "help" for help.

postgres=# 
```

The above command includes three flags:

- -d - specifies the name of the database to connect to
- -U - specifies the name of the user to connect as
- -W - forces psql to ask for the user password before connecting to the database

## Listing all the databases - \l

```

                                                    List of databases
   Name    |  Owner   | Encoding | Locale Provider |  Collate   |   Ctype    | Locale | ICU Rules |   Access privileges   
-----------+----------+----------+-----------------+------------+------------+--------+-----------+-----------------------
 postgres  | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           | 
 template0 | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           | =c/po
stgres          +
           |          |          |                 |            |            |        |           | postg
res=CTc/postgres
 template1 | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           | =c/po
stgres          +
           |          |          |                 |            |            |        |           | postg
res=CTc/postgres
(3 rows)
```

## List all schemas

The `\dn` psql command lists all the database schemas.

```
postgres=# \dn
      List of schemas
  Name  |       Owner       
--------+-------------------
 public | pg_database_owner
(1 row)

postgres=#
```

## Run the following command to show the database activity:

```
SELECT * from pg_stat_activity;  <--- DONT FORGET ";"
```

## Result:

```
datid | datname  | pid | leader_pid | usesysid | usename  | application_name | client_addr | client_host
name | client_port |         backend_start         |          xact_start           |          query_start
          |         state_change          | wait_event_type |     wait_event      | state  | backend_xid 
| backend_xmin | query_id |              query              |         backend_type         
-------+----------+-----+------------+----------+----------+------------------+-------------+------------
-----+-------------+-------------------------------+-------------------------------+---------------------
----------+-------------------------------+-----------------+---------------------+--------+-------------
+--------------+----------+---------------------------------+------------------------------
     5 | postgres |  85 |            |       10 | postgres | psql             |             |            
     |          -1 | 2025-01-08 11:40:22.778949+00 |                               | 2025-01-08 11:40:56.
590114+00 | 2025-01-08 11:41:26.598462+00 | Client          | ClientRead          | idle   |             
|              |          | SELECT pg_sleep(30);            | client backend
     5 | postgres |  92 |            |       10 | postgres | psql             |             |            
     |          -1 | 2025-01-08 11:41:14.359414+00 | 2025-01-08 11:43:52.615603+00 | 2025-01-08 11:43:52.
615603+00 | 2025-01-08 11:43:52.61561+00  |                 |                     | active |             
|          750 |          | SELECT * FROM pg_stat_activity; | client backend
       |          |  64 |            |          |          |                  |             |            
     |             | 2025-01-08 11:38:28.74611+00  |                               |                     
          |                               | Activity        | AutovacuumMain      |        |             
|              |          |                                 | autovacuum launcher
       |          |  65 |            |       10 | postgres |                  |             |            
:
```


## Method 2: Using "Ask Gordon"

```
Run a multiple version of postgres with the standard port and POSTGRES_PASSWORD set to dev
```



<img width="902" alt="image" src="https://github.com/user-attachments/assets/9f9eec12-a488-488c-9e82-99a7c8eb3e24" />





