## Kubernetes Demo


## Demonstrating Pod

```
git clone https://github.com/ajeetraina/talk-demos/
cd talk-demos/kube-demo
```

## Bringing up Pod

```
kubectl apply -f pod.yaml
```

## Port forwarding

```
kubectl port-forward nginx-pod 8080:80
```

## Accessing

```
curl localhost:8080
```




