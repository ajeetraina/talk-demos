## Model Runner Demo


## Demo #1: Introducing docker model command

- Install Docker Desktop
- Enable Model Runner (don't select TCP mode)
- Download a Model from Docker Hub

```
docker model pull ignaciolopezluna020/llama3.2:1B
```

- Run a Model

```
docker model run ignaciolopezluna020/llama3.2:1B "Hello, how are you doing?"
```

## Demo #2: Building a ChatBot Application (using Internal DNS)

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Frontend  │ >>> │   Backend   │ >>> │    Ollama   │
│  (React/TS) │     │    (Go)     │     │  (Llama 3.2)│
└─────────────┘     └─────────────┘     └─────────────┘
      :3000              :8080              :11434
```

- Install Docker Desktop
- Enable Model Runner (don't select TCP mode)
- Download a Model from Docker Hub

```
docker model pull ignaciolopezluna020/llama3.2:1B
```

##### Quick Start

1. Clone this repository:
   ```bash
   git clone https://github.com/ajeetraina/genai-app-demo.git
   cd genai-app-demo

   ```

2. Start the application using Docker Compose:
   ```bash
   docker compose up -d -build
   ```

3. Access the frontend at [http://localhost:3000](http://localhost:3000)


## Demo #3: Building a ChatBot Application (using TCP Mode)






