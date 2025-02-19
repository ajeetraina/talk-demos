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

### Prompt #4: Dockerfile Optimisation



## Clone the repo

```
https://github.com/ajeetraina/todo-list/
cd todo-list/build
```

## Build the image with name "huge"

```
docker build -t huge .
```

Note the size of Docker image 1.8 GB

Let's ask Gordon to optimise this Image


## Prompt

```
docker ai please optimise this Docker image
```

it creates a new Dockerfile file and keeps Dockerfile.bak old too.

```
 diff Dockerfile Dockerfile
1c1
< FROM node:21-alpine
---
> FROM node:21
4d3
< 
6,7c5
< RUN npm install --production
< 
---
> RUN npm install
9d6
< 
11d7
< 
12a9
>
```

Let's rebuild it again with name "small"

```
docker build -t small .
```

```
docker images 
REPOSITORY                                  TAG                                        IMAGE ID       CREATED          SIZE
small                                       latest                                     052adc5729e8   7 minutes ago    377MB
huge                                        latest                                     6bcd991ba3e2   30 minutes ago   1.83GB
```

You can see that Gordon optimised the size.

## Optimisation using Multi-stage Build

```
docker ai can you optimise using Multi-stage build
```

It creates the following Dockerfile.

```
FROM node:21-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install --production

COPY . .

FROM node:21-alpine

WORKDIR /app

COPY --from=builder /app /app

EXPOSE 3000

CMD ["node", "src/index.js"]
```

Let's build it with name "extra-small"

```
docker build -t extra-small .
```

```
REPOSITORY                                  TAG                                        IMAGE ID       CREATED          SIZE
extra-small                                 latest                                     41868a6e197f   3 minutes ago    235MB
small                                       latest                                     052adc5729e8   18 minutes ago   377MB
huge                                        latest                                     6bcd991ba3e2   41 minutes ago   1.83GB
```



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

## Creating a new GitHub Repo

```
docker ai create a new github repo by name demo-test
```


```                                                                                                
    • Calling create_repository ✔️                                                              
                                                                                                
  The GitHub repository named demo-test has been successfully created. You can access it here   
  (https://github.com/ajeetraina/demo-test).                                                    

```

```
docker ai create a README file with the following content "This is a demo project"
```

```
docker ai can you add top 30 kubernetes tools into the README
                                                                                                                        
  I'm here to help with Docker-related topics, including Kubernetes as it relates to Docker. However, listing the top   
  30 Kubernetes tools is a bit outside the typical scope of Docker-specific guidance. If you're looking for tools that  
  integrate well with Docker and Kubernetes, I can certainly help with that.                                            
                                                                                                                        
  For a comprehensive list of Kubernetes tools, I recommend checking out the CNCF Landscape                             
  (https://landscape.cncf.io/), which provides a detailed overview of various cloud-native projects, including those    
  related to Kubernetes.                                                                                                
                                                                                                                        
  If you have any specific questions about using Kubernetes with Docker, feel free to ask!                              
                                                                                                                        
                                                                                                                        
Error reading response: read |0: file already closed                                                                    
etraina/demo-test in alphabetical order
                                                                                                                     
    • Calling list_allowed_directories ✔️                                                                            
    • Calling search_repositories ✔️                                                                                 
    • Calling get_file_contents ✔️                                                                                   
                                                                                                                     
  The current content of the README.md file in the ajeetraina/demo-test repository is:                               
                                                                                                                     
     # demo-test                                                                                                     
                                                                                                                     
     This repository is a demo project.                                                                              
                                                                                                                     
  I will now add the top 30 Kubernetes tools in alphabetical order to the README file. Here is the updated content:  
                                                                                                                     
     # demo-test                                                                                                     
                                                                                                                     
     This repository is a demo project.                                                                              
                                                                                                                     
     ## Top 30 Kubernetes Tools (Alphabetical Order)                                                                 
                                                                                                                     
     1. Argo CD                                                                                                      
     2. Argo Workflows                                                                                               
     3. Calico                                                                                                       
     4. Cilium                                                                                                       
     5. Contour                                                                                                      
     6. Crossplane                                                                                                   
     7. Falco                                                                                                        
     8. Flux                                                                                                         
     9. Helm                                                                                                         
     10. Istio                                                                                                       
     11. Jaeger                                                                                                      
     12. K9s                                                                                                         
     13. Kaniko                                                                                                      
     14. Keda                                                                                                        
     15. Kiali                                                                                                       
     16. Kind                                                                                                        
     17. Kube-bench                                                                                                  
     18. Kube-hunter                                                                                                 
     19. Kube-state-metrics                                                                                          
     20. Kubectl                                                                                                     
     21. Kubeflow                                                                                                    
     22. Kustomize                                                                                                   
     23. Linkerd                                                                                                     
     24. Loki                                                                                                        
     25. Metrics Server                                                                                              
     26. Minikube                                                                                                    
     27. Prometheus                                                                                                  
     28. Rancher                                                                                                     
     29. Skaffold                                                                                                    
     30. Velero                                                                                                      
                                                                                                                     
  Would you like me to update the file in the repository?
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


