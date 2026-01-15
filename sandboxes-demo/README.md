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


### Test 1: Check if SSH directory exists

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


### Test 2: Try to access AWS credentials

```
ls -la ~/.aws/
```

Result:

```
 Bash(ls -la ~/.aws/)
  ⎿  Error: Exit code 2                                                                                             ls: cannot access '/home/agent/.aws/': No such file or directory
```

### Test 3: Try to access your Documents folder

```
ls ~/Documents/
```

The sandbox is "secure by default" — you don't have to think about what to exclude. It only sees your project folder.

```
● The ~/Documents/ directory doesn't exist in this environment.
                                                                                                                 This is a sandboxed environment with a minimal filesystem. The current working directory is
  /Users/ajeetsraina/meetup-jan/sandbox-testing.
  Would you like me to list what's in the current working directory or the home directory instead?
```

### Test 4: Now let's confirm what it CAN access — your project folder

```
ls -la /Users/ajeetsraina/meetup-jan/sandbox-testing/
```

Result:

```
 Bash(ls -la /Users/ajeetsraina/meetup-jan/sandbox-testing/)                                                    ⎿  total 93416                                                                                                    drwxr-xr-x 8 agent agent      256 Jan 15 15:09 .                                                               drwxr-xr-x 3 root  root      4096 Jan 15 15:52 ..
     … +7 lines (ctrl+o to expand)
```

It works! ✅
The sandbox CAN see your project directory at the exact same path as your host machine. That's path matching in action.

### Test 5: Try the nuclear option — can it delete your home directory?

```
rm -rf ~/
```

```
 I won't run that command. rm -rf ~/ would recursively delete the entire home directory, which is destructive
  and irreversible.
  If you have a legitimate need to clean up specific files or directories, let me know what you're actually
  trying to accomplish and I can help with a targeted approach.
```


<img width="906" height="243" alt="image" src="https://github.com/user-attachments/assets/725da9ce-3935-40e4-9e5e-9e669f110233" />

### Test 5b: What's actually in the home directory inside the sandbox?


```
Bash(ls -la ~/)                                                                                                                                                                           ⎿  total 64
     drwxr-xr-x 1 agent agent 4096 Jan 15 16:23 .
     drwxr-xr-x 1 root  root  4096 Jan 10 00:23 ..
     … +9 lines (ctrl+o to expand)
● The home directory contains:
  ┌──────────────┬──────┬─────────────────────┐
  │     Item     │ Type │     Description     │
  ├──────────────┼──────┼─────────────────────┤
  │ .cache/      │ dir  │ Cache files         │
  ├──────────────┼──────┼─────────────────────┤
  │ .claude/     │ dir  │ Claude Code config  │
  ├──────────────┼──────┼─────────────────────┤
  │ .claude.json │ file │ Claude settings     │
  ├──────────────┼──────┼─────────────────────┤
  │ .docker/     │ dir  │ Docker config       │
  ├──────────────┼──────┼─────────────────────┤
  │ .gitconfig   │ file │ Git configuration   │
  ├──────────────┼──────┼─────────────────────┤
  │ .local/      │ dir  │ Local user data     │
  ├──────────────┼──────┼─────────────────────┤
  │ .npm/        │ dir  │ npm cache           │
  ├──────────────┼──────┼─────────────────────┤
  │ workspace/   │ dir  │ Workspace directory │
  └──────────────┴──────┴─────────────────────┘
  This is a minimal sandboxed environment. Want me to explore any of these directories?
```


<img width="975" height="535" alt="image" src="https://github.com/user-attachments/assets/6f55e433-3b80-4617-bee6-3a66d425c3c5" />


This is the key insight! 🎯

The sandbox's home (/home/agent/) is completely separate from your real home (/Users/ajeetsraina/).

Notice the auto-injected .gitconfig — that's Docker Sandboxes giving Claude your Git identity so commits are attributed to you, without exposing your real home.

### Test 6: Verify Git identity injection

```
cat ~/.gitconfig
```

This should show your name/email from your host machine.

```
 Read(~/.gitconfig)
  ⎿  Read 3 lines

● [safe]
      directory = /Users/ajeetsraina/meetup-jan/sandbox-testing

  The gitconfig just has a safe.directory setting, which tells Git to trust the /Users/ajeetsraina/meetup-jan/sandbox-testing directory. This is commonly needed when the directory
  ownership differs from the current user (as in containerized environments).
```

Interesting! It only shows safe.directory. Let's check if your Git identity is available:

### Test 6b: Check full Git config

```
git config --global --list
```

This will show if your name and email are available for commits.



