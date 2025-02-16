## Gordon + MCP Server

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
export GITHUB_PERSONAL_ACCESS_TOKEN="XXX"
```

Next, source the shell

```
source ~/.zshrc
```

## Prompt 1

```
docker ai can you fetch collabnix.com and add a description in collabnixweb.txt
```

Results:

```
    • Calling list_allowed_directories ✔️
    • Calling fetch ✔️
    • Calling write_file ✔️

  I have fetched the content from Collabnix and added a description to the file collabnixweb.txt. Let me know if you need anything
  else!
```

## Verification

                                                                            
```
ls
LICENSE          chatbot          dell.txt         gordon-mcp.yml   test.txt
README.MD        collabnixweb.txt docs             guide.md         text
```

```
cat collabnixweb.txt
Collabnix is a platform that provides insights and guides on Docker, Kubernetes, IoT, and other cutting-edge technologies. It features articles on topics like Testcontainers, Playwright, Docker and Wasm containers, NVIDIA Jetson Nano, and more. The site also delves into technical SEO, cloud computing, AI, and innovative tools transforming various industries.%
```

