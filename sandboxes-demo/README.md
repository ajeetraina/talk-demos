## Getting Started



1. Create a directory

```
mkdir -p /Users/ajeetsraina/sandbox-testing
cd /Users/ajeetsraina/sandbox-testing
```


```
docker sandbox run
docker: 'docker sandbox run' requires at least 1 argument

Usage:  docker sandbox run [options] <agent> [agent-options]

See 'docker sandbox run --help' for more information

Available Agents:
  claude          Run Claude AI agent inside a sandbox
  gemini          Run Gemini AI agent inside a sandbox
```

```
docker sandbox run claude
```

```
docker sandbox ls
SANDBOX ID     TEMPLATE                               NAME                               WORKSPACE                            STATUS    CREATED
275d94b417bf   docker/sandbox-templates:claude-code   claude-sandbox-2026-01-11-004116   /Users/ajeetsraina/sandbox-testing   running   2026-01-10 19:12:10
```

```
docker sandbox inspect 275d94b417bf
[
  {
    "id": "275d94b417bf8f4c29f6f3c7317f20f6b9636b3f3121d303149a066d8330428e",
    "name": "claude-sandbox-2026-01-11-004116",
    "workspace": "/Users/ajeetsraina/sandbox-testing",
    "created_at": "2026-01-10T19:12:10.888151834Z",
    "status": "running",
    "template": "docker/sandbox-templates:claude-code",
    "labels": {
      "com.docker.sandbox.agent": "claude",
      "com.docker.sandbox.credentials": "sandbox",
      "com.docker.sandbox.workingDirectory": "/Users/ajeetsraina/sandbox-testing",
      "com.docker.sandbox.workingDirectoryInode": "186434127",
      "com.docker.sandboxes": "templates",
      "com.docker.sandboxes.base": "ubuntu:questing",
      "com.docker.sandboxes.flavor": "claude-code",
      "com.docker.sdk": "true",
      "com.docker.sdk.client": "0.1.0-alpha011",
      "com.docker.sdk.container": "0.1.0-alpha012",
      "com.docker.sdk.lang": "go",
      "docker/sandbox": "true",
      "org.opencontainers.image.ref.name": "ubuntu",
      "org.opencontainers.image.version": "25.10"
    }
  }
]
```

The `docker/sandbox-templates:claude-code` image includes Claude Code with automatic credential management, plus development tools (Docker CLI, GitHub CLI, Node.js, Go, Python 3, Git, ripgrep, jq). It runs as a non-root agent user with sudo access and launches Claude with --dangerously-skip-permissions by default.


Since Docker enforces one sandbox per workspace, the same sandbox is reused each time you run docker sandbox run <agent> in a given directory. To create a fresh sandbox, you need to remove the existing one first:

```
docker sandbox ls  # Find the sandbox ID
docker sandbox rm <sandbox-id>
docker sandbox run <agent>  # Creates a new sandbox
```

## Verify the isolation


Test 1: Check if SSH directory exists

```
ls -la ~/.ssh/
```


Result: 

```
Bash(ls -la ~/.ssh/)
  ⎿  Error: Exit code 2
     ls: cannot access '/home/agent/.ssh/': No such file or directory
```

That's the sandbox working! 🔒
Notice the path: /home/agent/.ssh/ — the sandbox can't see your host's SSH keys at all. They simply don't exist inside the container.


Test 2: Try to access AWS credentials

```
ls -la ~/.aws/
```

Result:

```
 Bash(ls -la ~/.aws/)
  ⎿  Error: Exit code 2                                                                                             ls: cannot access '/home/agent/.aws/': No such file or directory
```

Test 3: Try to access your Documents folder

```
ls ~/Documents/
```

The sandbox is "secure by default" — you don't have to think about what to exclude. It only sees your project folder.





