## Option 1: Using YAML specification

- Clone the repository


```
git clone https://github.com/ajeetraina/example-voting-app
cd example-voting-app
```

- Bring up Compose Services

```
docker compose up -d
```


- Bring down compose services

```
docker compose down -v
```

- Bring up K8s objects

```
kubectl apply -f k8s-specification/
```

- Check the Pods

```
kubectl get po -A
```

- Access the frontend voting app by port forwarding

```
kubectl port-forward svc/vote 5000:8080
```

