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

## Running Multiple Pods

```
kubectl apply -f multiple-pods.yaml
```

```
kubectl get po -o wide
NAME        READY   STATUS    RESTARTS   AGE     IP           NODE                    NOMINATED NODE   READINESS GATES
nginx-pod   1/1     Running   0          8m18s   10.244.0.5   desktop-control-plane   <none>           <none>
webserver   2/2     Running   0          79s     10.244.0.6   desktop-control-plane   <none>           <none>
```






