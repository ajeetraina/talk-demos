## Getting Started

- Install Docker Desktop 4.38.+
- Enable AI

<img width="1480" alt="image" src="https://github.com/user-attachments/assets/6a591498-c8ec-4dfc-8c7f-807dec77fde0" />

## Listing all the containers


Prompt #1
```
list all the containers running on my system
```






## Gordon and MCP

Assuming that you have cloned the repo that has `gordon-mcp.yml` file with the following content:





```
docker ai mcp
```

List of MCP servers

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

## Prompt 1

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
