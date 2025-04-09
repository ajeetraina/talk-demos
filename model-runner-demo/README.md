# Model Runner Demo


## Demo #1: Introducing docker model command

- Install Docker Desktop
- Enable Model Runner (don't select TCP mode)
- Download a Model from Docker Hub

```
docker model pull ai/llama3.2:1B-Q8_0
```

- Run a Model

```
docker model run ai/llama3.2:1B-Q8_0 "Hello, how are you doing?"
```

## Demo #2: Building a ChatBot Application (using Internal DNS)

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Frontend  │ >>> │   Backend   │ >>> │ Model Runner│
│  (React/TS) │     │    (Go)     │     │  (Llama 3.2)│
└─────────────┘     └─────────────┘     └─────────────┘
      :3000              :8080              :12434
```

- Install Docker Desktop
- Enable Model Runner (don't select TCP mode)



##### Quick Start

1. Clone this repository:
   ```bash
   git clone https://github.com/ajeetraina/genai-app-demo.git
   cd genai-app-demo

   ```

2. Start the application using Docker Compose:
   ```bash
   docker compose up -d --build
   ```

3. Access the frontend at [http://localhost:3000](http://localhost:3000)


## Demo #3: Building a ChatBot Application (using TCP Mode)

##### Quick Start

1. Clone this repository:

   ```bash
   git clone https://github.com/ajeetraina/genai-app-demo.git
   cd genai-app-demo
   ```
   
3. Checkout add-tcp branch
   ```
   git checkout add-tcp-support
   ```


2. Start the application using Docker Compose:
   ```bash
   docker compose up -d -build
   ```

3. Access the frontend at [http://localhost:3000](http://localhost:3000)

4. Verify the TCP

```
netstat -ant | grep 12434
tcp4       0      0  127.0.0.1.12434        127.0.0.1.51620        ESTABLISHED
tcp4       0      0  127.0.0.1.51620        127.0.0.1.12434        ESTABLISHED
tcp4       0      0  127.0.0.1.12434        *.*                    LISTEN
```

```
lsof -i :12434
COMMAND    PID        USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
com.docke 1314 ajeetsraina  132u  IPv4 0xaf6bc8c109ba99bb      0t0  TCP localhost:12434 (LISTEN)
com.docke 1314 ajeetsraina  186u  IPv4 0xaf6bc8c109bbc01b      0t0  TCP localhost:51620->localhost:12434 (ESTABLISHED)
com.docke 1314 ajeetsraina  187u  IPv4 0xaf6bc8c10c44307b      0t0  TCP localhost:12434->localhost:51620 (ESTABLISHED)
```

<img width="1283" alt="image" src="https://github.com/user-attachments/assets/cb0a5d21-3a70-467f-812e-c3b6c71a3acf" />







