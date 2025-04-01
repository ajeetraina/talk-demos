## Option 1: Using YAML specification

## Prerequisite

- Install Docker Desktop
- Enable 3 node K8s Kind cluster

## Getting Started

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

- See where Pods are running? on which node?

```
kubectl get po -o wide
NAME                      READY   STATUS    RESTARTS   AGE    IP           NODE              NOMINATED NODE   READINESS GATES
db-5b8f566868-j9g5m       1/1     Running   0          103s   10.244.1.2   desktop-worker    <none>           <none>
redis-5b65678587-gdszd    1/1     Running   0          103s   10.244.2.2   desktop-worker2   <none>           <none>
result-6894cfb789-sjdf5   1/1     Running   0          103s   10.244.2.3   desktop-worker2   <none>           <none>
vote-6fc94b9897-w9rzt     1/1     Running   0          103s   10.244.1.3   desktop-worker    <none>           <none>
worker-765456c688-cvnk5   1/1     Running   0          103s   10.244.2.4   desktop-worker2   <none>           <none>
```


- Access the frontend voting app by port forwarding

```
kubectl port-forward svc/vote 5000:8080
```

- Cleaning up Pods and other via namespace

```
kubectl delete ns example-voting-app
```

