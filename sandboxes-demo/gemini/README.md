
## 

```
 docker sandbox
Usage:  docker sandbox [OPTIONS] COMMAND

Local sandbox environments for AI agents, using Docker.

Options:
  -D, --debug   Enable debug logging

Commands:
  inspect     Display detailed information on one or more sandboxes
  ls          List sandboxes
  rm          Remove one or more sandboxes
  run         Run an AI agent inside a sandbox
  version     Show sandboxd version information

Run 'docker sandbox COMMAND --help' for more information on a command.
```



```
docker sandbox run gemini
```





<img width="1272" height="552" alt="image" src="https://github.com/user-attachments/assets/f04e91e0-1174-4d9b-82ce-0450c0079026" />


```
docker sandbox ls
SANDBOX ID     TEMPLATE                               NAME                               WORKSPACE                            STATUS    CREATED
431546f2bf76   docker/sandbox-templates:gemini        gemini-sandbox-2026-01-13-210410   /Users/ajeetsraina/sandbox-testing   running   2026-01-13 15:34:49
275d94b417bf   docker/sandbox-templates:claude-code   claude-sandbox-2026-01-11-004116   /Users/ajeetsraina/sandbox-testing   exited    2026-01-10 19:12:10

```

The docker/sandbox-templates:claude-code image includes Gemini with automatic credential management, plus development tools (Docker CLI, GitHub CLI, Node.js, Go, Python 3, Git, ripgrep, jq). It runs as a non-root agent user with sudo access and launches Gemini with --dangerously-skip-permissions by default.




