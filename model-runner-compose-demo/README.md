## Docker Model Runner + Compose Demo


## Prereq

- Install Docker Desktop
- Ensure that Compose v2.35.0 is installed and enabled
- Enable Model Runner

```
docker desktop enable model-runner --tcp 12434
```

## Getting Started

- Clone the repo

```
git clone https://github.com/ajeetraina/genai-app-demo
```

- Bring up Compose Services

```
docker compose up -d --build
```

- Access the app

Open http://localhost:3000 to access the frontend.
