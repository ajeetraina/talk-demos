## Compose-Bridge Demo

### Clone the repository


```
git clone https://github.com/dockersamples/example-voting-app
```


### Build Container images

```
cd example-voting-app
docker compose build
```

## Using compose-bridge

```
compose-bridge convert
```

```
compose-bridge convert
alpine: Pulling from library/redis
1e66f2df0912: Pulling fs layer
080f8dfc707b: Pulling fs layer
bbb44351440e: Pulling fs layer
91d0c6f66299: Pulling fs layer
cd9b8f71c9cf: Pulling fs layer
a745a150c6e8: Pulling fs layer
4f4fb700ef54: Pulling fs layer
Digest: sha256:02419de7eddf55aa5bcf49efb74e88fa8d931b4d77c07eff8a6b2144472b6952
Status: Downloaded newer image for redis:alpine
Kubernetes resource db-deployment.yaml created
Kubernetes resource redis-deployment.yaml created
Kubernetes resource result-deployment.yaml created
Kubernetes resource vote-deployment.yaml created
Kubernetes resource worker-deployment.yaml created
Kubernetes resource db-expose.yaml created
Kubernetes resource redis-expose.yaml created
Kubernetes resource result-expose.yaml created
Kubernetes resource vote-expose.yaml created
Kubernetes resource 0-example-voting-app-namespace.yaml created
Kubernetes resource back-tier-network-policy.yaml created
Kubernetes resource front-tier-network-policy.yaml created
Kubernetes resource db-db-data-persistentVolumeClaim.yaml created
Kubernetes resource db-/Users/ajeetsraina/example-voting-app/healthchecks-persistentVolumeClaim.yaml created
Kubernetes resource redis-/Users/ajeetsraina/example-voting-app/healthchecks-persistentVolumeClaim.yaml created
Kubernetes resource result-/Users/ajeetsraina/example-voting-app/result-persistentVolumeClaim.yaml created
Kubernetes resource vote-/Users/ajeetsraina/example-voting-app/vote-persistentVolumeClaim.yaml created
Kubernetes resource result-service.yaml created
Kubernetes resource vote-service.yaml created
Kubernetes resource kustomization.yaml created
Kubernetes resource db-db-data-persistentVolumeClaim.yaml created
Kubernetes resource db-/Users/ajeetsraina/example-voting-app/healthchecks-persistentVolumeClaim.yaml created
Kubernetes resource redis-/Users/ajeetsraina/example-voting-app/healthchecks-persistentVolumeClaim.yaml created
Kubernetes resource result-/Users/ajeetsraina/example-voting-app/result-persistentVolumeClaim.yaml created
Kubernetes resource vote-/Users/ajeetsraina/example-voting-app/vote-persistentVolumeClaim.yaml created
Kubernetes resource result-service.yaml created
Kubernetes resource vote-service.yaml created
Kubernetes resource kustomization.yaml created
```



