## Getting Started

- Install Docker Desktop 4.38.+
- Enable AI

<img width="1480" alt="image" src="https://github.com/user-attachments/assets/6a591498-c8ec-4dfc-8c7f-807dec77fde0" />

## Greeting Gordon

```
how are you doing?
```


## Listing all the containers


### Prompt #1

```
list all the containers running on my system
```

<img width="1176" alt="image" src="https://github.com/user-attachments/assets/fb4592f9-08ec-4083-bd21-771fe830c207" />


### Prompt #2

```
Clean up the exited container
```

### Prompt #3

```
which container is taking up lot of space
```

<img width="1164" alt="image" src="https://github.com/user-attachments/assets/8c6fb7d3-aa0c-4a9a-bf36-e099520a02ad" />

### Prompt #4






## Gordon and MCP

Assuming that you have cloned the repo that has `gordon-mcp.yml` file with the following content:

```
services:
  time:
    image: mcp/time

  postgres:
    image: mcp/postgres
    command: postgresql://postgres:dev@host.docker.internal:5433/postgres

  git:
    image: mcp/git
    volumes:
      - /Users/ajeetsraina:/Users/ajeetsraina


  github:
    image: mcp/github
    environment:
      - GITHUB_PERSONAL_ACCESS_TOKEN=${GITHUB_PERSONAL_ACCESS_TOKEN}

  fetch:
    image: mcp/fetch

  fs:
    image: mcp/filesystem
    command:
      - /rootfs
    volumes:
      - .:/rootfs
```

## List all the MCP Tools


```
docker ai mcp
Initializing time
Initializing fs
Initializing postgres
Initializing fetch
Initializing git
Initializing github
Initialized fs
Initialized postgres
Initialized github
...
...
```


## Github MCP Server

Ensure that you add your PAT to ~/.zshrc like:

```
export GITHUB_PERSONAL_ACCESS_TOKEN='XXX'
```

Next, source the shell

```
source ~/.zshrc
```

## Prompt

```
$ docker ai can you fetch dockerlabs.collabnix.com and write the summary to a file tests.txt
```


```
    • Calling fetch ✔️
    • Calling write_file ✔️
    • Calling list_allowed_directories ✔️
    • Calling write_file ✔️

  The summary of DockerLabs has been successfully written to the file /rootfs/tests.txt. Let me know if you need further assistance
  !
```

## Validating

```
cat tests.txt
DockerLabs is a comprehensive learning platform for Docker enthusiasts, offering resources for beginners, intermediate, and advanced users. It features over 500 interactive tutorials and guides, accessible via Docker Desktop or browser. Key highlights include community engagement through Slack and Discord, a GitHub repository for contributions, and a variety of blog posts and articles on Docker-related topics. The platform also provides hands-on labs covering Docker core concepts, advanced features, and industry use cases. Additionally, it offers workshops for beginners, tutorials on Dockerfile creation, and guidance on managing Docker containers and volumes.%
```


## Using Postgres

- Start 3 Postgres container

```
docker run -d --name postgres1 -e POSTGRES_PASSWORD=dev -p 5432:5432 postgres:latest
docker run -d --name postgres2 -e POSTGRES_PASSWORD=dev -p 5433:5432 postgres:13
docker run -d --name postgres3 -e POSTGRES_PASSWORD=dev -p 5434:5432 postgres:12
```

- Create dummy tables

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

## Using Ask Gordon

```
docker ai list of all tables in the postgres database running in a postgres container named postgres2
```


