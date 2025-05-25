# Sample Demo - Product Catalog

## Step 1: Running Multiple Postgres Containers


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


You can also query:

```
psql -d catalog -U postgres -W -c "\dt"
Password: 
          List of relations
 Schema |   Name   | Type  |  Owner   
--------+----------+-------+----------
 public | products | table | postgres
(1 row)
```

To see the items in the database

```
psql -d catalog -U postgres -w -c "SELECT * FROM products;"
```




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


Create some dummy tables

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

## Method 2: Using "Ask Gordon"

```
Run a multiple version of postgres with the standard port and POSTGRES_PASSWORD set to dev
```

## Remove the container

```
Delete or remove the running container"
```

## Step 2: 

### Clone the repo

```
git clone https://github.com/dockersamples/catalog-service-node
```

### Run the Compose

```
docker compose up -d
```

## Setting up the Demo


Open up ProductServices and add the following explanation:

```
This file is part of a Node.js application that manages a product catalog service.
The code provides functions to interact with a PostgreSQL database, retrieve product information,
manage product images, and publish events related to product operations.
The file exports several functions:
getProducts: Retrieves all products from the database.
createProduct: Creates a new product in the database and publishes an event.
getProductById: Retrieves a product by its ID, including inventory information.
getProductImage: Retrieves the image associated with a product using the StorageService.
uploadProductImage: Uploads an image for a product and updates the database.
teardown: Closes the database connection.
The code uses the pg library for PostgreSQL connectivity, and it imports functions from other
services (InventoryService, StorageService, and PublisherService) to perform related operations.

Let's pick up the piece of code and ensure that UPC is not reflected.


This code snippet is calling a function named publishEvent with two arguments:
"products" and an object containing event details.

The publishEvent function is likely defined in the PublisherService file and is
responsible for publishing events related to product operations.
The event being published is "product_created", and it includes the following details:
- id: The ID of the newly created product.
- name: The name of the product.
- price: The price of the product.

The purpose of publishing this event could be to notify other services or systems about the creation of a
new product, allowing them to perform additional actions or updates. In this case,
the event is likely used to trigger downstream processes or integrate with other systems.


```

### Bring up the API service 


```
npm install
npm run dev
```

### What happens when you run `npm install`?

When you run `npm install` in a project directory, it reads the `package.json` file and installs all the dependencies listed in the `dependencies` section. 
It also installs any dependencies listed in the devDependencies section if the --save-dev or -D flag is used.

Here's a step-by-step explanation of what happens when you run `npm install`:

1. It checks if the package-lock.json file exists. If it does, npm uses the versions specified in the lock file to install the dependencies. If the lock file is missing or out of date, npm generates a new lock file based on the current package.json and installed dependencies.
2. It creates a node_modules directory if it doesn't exist.
3. It installs the dependencies listed in the package.json file. For each dependency, it checks if it's already installed in the node_modules directory. If not, it downloads the dependency from the npm registry and installs it.
4. It installs any dependencies listed in the dependencies section.
5. If the --save or -S flag is used, npm adds the installed dependency to the dependencies section in the package.json file.
6. If the --save-dev or -D flag is used, npm adds the installed dependency to the devDependencies section in the package.json file.
7. It runs any scripts specified in the scripts section of the package.json file with the preinstall and install keys.
8. It updates the package-lock.json file with the installed dependencies and their versions.
In your case, when you run npm install, it will install all the dependencies listed in the dependencies and devDependencies sections of the package.json file. It will also create a node_modules directory and download the dependencies into it.

When you run `npm run dev` in a project directory, it executes the script associated with the dev key in the scripts section of the package.json file.


## Apply the patch:

```
git apply demo/e2e.patch
```

### Accessing the Web Client

Open the web client (http://localhost:5173) and create a few products.

### Accessing the database visualizer 

Open [http://localhost:5050](http://localhost:5050) and validate the products exist in the database. 
"Good! We see the UPCs are persisted in the database"


Use the following Postgres CLI to check if the products are added or not.

```
# psql -U postgres
psql (17.1 (Debian 17.1-1.pgdg120+1))
Type "help" for help
postgres=# \c catalog
You are now connected to database "catalog" as user "postgres".
catalog=# SELECT * FROM products;
  1 | New Product | 100000000001 | 100.00 | f
  2 | New Product | 100000000002 | 100.00 | f
  3 | New Product | 100000000003 | 100.00 | f
```



### Access the Kafka Visualizer

Before we access visualizer, let's apply the patch:



Open the Kafka visualizer [http://localhost:8080](http://localhost:8080) and look at the published messages. 
"Ah! We see the messages don't have the UPC"

<img width="1213" alt="image" src="https://github.com/user-attachments/assets/a3e3ff3d-f08c-4168-bfb2-e59800be4d58" />



## Let's fix it...


### Configuring 

In VS Code, open the `src/services/ProductService.js` file and add the following to the publishEvent on line ~52:

```
upc: product.upc,
```

Save the file and create a new product using the web UI. 


<img width="1191" alt="image" src="https://github.com/user-attachments/assets/32c5ba6c-60c1-403b-9962-50c501a5e996" />

Validate the message has the expected contents.


## Testing

```
npm run unit-test
npm run integration-test
```

```
The script includes the following key components:

Test > src > integration > 
kAfkaSupport
containerSupport
productCreation.integration.*.js



1.Importing required modules:


fs for reading image files.
containerSupport for creating and managing Docker containers for testing.
kafkaSupport for consuming messages from Kafka.


2.Setting up and tearing down test environment:


Starting Docker containers for PostgreSQL, Kafka, and Localstack using the containerSupport module.
Creating an instance of the KafkaConsumer for consuming messages from Kafka.
Importing the ProductService and PublisherService for testing the product creation feature.
Disconnecting from Kafka and tearing down the test environment after all tests have completed.


3.Defining unit and integration tests:


"Product creation" test suite:
"should publish and return a product when creating a product": Tests the creation of a product, verification of the product's properties, and retrieval of the product from the product service.
"should publish a Kafka message when creating a product": Tests the creation of a product and verification of the corresponding Kafka message.
"should upload a file correctly": Tests the upload of an image file, verification of the corresponding Kafka message, and retrieval of the image file from the product service.
"doesn't allow duplicate UPCs": Tests the prevention of creating products with duplicate UPCs.

The script also includes a timeout value for starting the Docker containers and waiting for messages from Kafka, ensuring that the tests have enough time to complete.

Overall, the script provides a comprehensive set of unit and integration tests for the "Product creation" feature, ensuring that the functionality is working as expected and providing valuable feedback on the overall system.
```

Open Testcontainer Desktop app and you'll notice that 3 containers appear and disppear.

<img width="940" alt="image" src="https://github.com/user-attachments/assets/9277a932-2227-4cf2-97ab-758e1dd3ea38" />


## Using Docker Build Cloud

Method: 1 : Running it locally

```
docker buildx create --driver cloud dockerdevrel/demo-builder
docker buildx build --builder cloud-dockerdevrel-demo-builder .
```

<img width="1160" alt="image" src="https://github.com/user-attachments/assets/cefc21ac-d15b-444a-81f9-8bcfc46bfd4a" />


Method:2 =- Running it using GitHub Workflow

Open dockersamples/ repo and show them workflow

## Secure - Scout

```
docker build -t newcatalog .
```

<img width="1128" alt="image" src="https://github.com/user-attachments/assets/bd5a0dfd-8580-4b39-951f-7f7d920887c8" />


## Apply the patches

```
patch -p1 < /demo/scout.patch
```

<img width="1141" alt="image" src="https://github.com/user-attachments/assets/d95fe357-aad2-45ba-ae0d-b81fe743a898" />

How to revert back to the fixed vulnerabilities:

```
patch -R -p1 < demo/scout.patch
```





