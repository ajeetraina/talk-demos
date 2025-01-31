# MCP Demo

## Demo 1: PostgreSQL MCP Server

- Install Docker Desktop
- Install Claude Desktop

## Step 1. Run a Postgres Container



```
docker run -d --name postgres2 -e POSTGRES_PASSWORD=dev -p 5433:5432 postgres:13
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


## Create some dummy tables

```
-- Create a table for Users
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a table for Orders
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a table for Products
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0
);
```

## Query the list of tables

```
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public';
```

## Using Claude Desktop

Edit and add the following JSON file. Refer https://github.com/modelcontextprotocol/servers/tree/main/src/postgres

```
{
  "mcpServers": {
    "postgres": {
      "command": "docker",
      "args": [
        "run", 
        "-i", 
        "--rm", 
        "mcp/postgres", 
        "postgresql://postgres:dev@host.docker.internal:5433/postgres"]
    }
  }
}
```

<img width="696" alt="image" src="https://github.com/user-attachments/assets/ee6f8aed-a69e-42bc-b3f3-587acbf5f2bb" />


## Prompt: Show me the schema of the existing database




## Demo 2: Neo4j

- Bring up Neo4j Docker Extension
- Login using Neo4j as username and password as password
- Select Movie Sample Database


<img width="1222" alt="image" src="https://github.com/user-attachments/assets/099a105e-211f-402e-a042-ea7d67cc35b5" />


- Open Claude Desktop Client and add the following config:

```
{
  "mcpServers": {
    "neo4j": {
      "command": "npx",
      "args": ["@alanse/mcp-neo4j-server"],
      "env": {
        "NEO4J_URI": "neo4j://localhost:7687",
        "NEO4J_USERNAME": "neo4j",
        "NEO4J_PASSWORD": "password"
      }
    }
  }
}
```

You can validate the available MCP Tools

<img width="495" alt="image" src="https://github.com/user-attachments/assets/e62e85cf-4076-4091-9036-9e55d3789c8e" />


- Enter the prompt:
  

```
Show me all the movies acted by Keanu Reeves
```

<img width="658" alt="image" src="https://github.com/user-attachments/assets/59ec18d0-2531-4802-bc57-8c000847270d" />

- Enter the prompt:

  ```
  Add Ajeet Raina as the director of all these movies
  ```

<img width="670" alt="image" src="https://github.com/user-attachments/assets/8254cbc0-3f6b-466b-aad0-f7f1c5ece7ae" />

- Verify the result:


<img width="667" alt="image" src="https://github.com/user-attachments/assets/8314a07d-9c6e-4702-ae78-a33bd2b62f78" />



## NPX + Kubernetes MCP Server + Docker Desktop


### Available MCP Tools


Claude can use tools provided by specialized servers using Model Context Protocol. Learn more about MCP.

```
cleanup
Cleanup all managed resources

From server: kubernetes

create_deployment
Create a new Kubernetes deployment

From server: kubernetes

create_pod
Create a new Kubernetes pod

From server: kubernetes

delete_pod
Delete a Kubernetes pod

From server: kubernetes

list_deployments
List deployments in a namespace

From server: kubernetes

list_namespaces
List all namespaces

From server: kubernetes

list_pods
List pods in a namespace

From server: kubernetes

list_services
List services in a namespace

From server: kubernetes
```
