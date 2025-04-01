


## Demonstrating Pod

```
git clone https://github.com/ajeetraina/talk-demos/
cd talk-demos/kube-demo
```

### Bringing up Pod

```
kubectl apply -f pod.yaml
```

### Port forwarding

```
kubectl port-forward nginx-pod 8080:80
```

### Accessing

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

## Scaling Pods

```
kubectl apply -f scale-pods.yaml
```

```
kubectl get po -o wide
NAME                              READY   STATUS    RESTARTS   AGE   IP           NODE              NOMINATED NODE   READINESS GATES
nginx-deployment-96b9d695-dmrs5   1/1     Running   0          11s   10.244.1.3   desktop-worker    <none>           <none>
nginx-deployment-96b9d695-drlxp   1/1     Running   0          11s   10.244.2.2   desktop-worker2   <none>           <none>
nginx-deployment-96b9d695-tf7nb   1/1     Running   0          11s   10.244.1.2   desktop-worker    <none>           <none>
```

## Scale Multicontainer Pods


```
kubectl apply -f scale-multicontainer-pods.yaml
```


```
kubectl get po -o wide
NAME                                   READY   STATUS              RESTARTS   AGE     IP           NODE              NOMINATED NODE   READINESS GATES
nginx-deployment-96b9d695-dmrs5        1/1     Running             0          2m58s   10.244.1.3   desktop-worker    <none>           <none>
nginx-deployment-96b9d695-drlxp        1/1     Running             0          2m58s   10.244.2.2   desktop-worker2   <none>           <none>
nginx-deployment-96b9d695-tf7nb        1/1     Running             0          2m58s   10.244.1.2   desktop-worker    <none>           <none>
webserver-deployment-8d544b76b-454wb   0/2     ContainerCreating   0          4s      <none>       desktop-worker2   <none>           <none>
webserver-deployment-8d544b76b-56frq   0/2     ContainerCreating   0          4s      <none>       desktop-worker2   <none>           <none>
webserver-deployment-8d544b76b-r9wpr   0/2     ContainerCreating   0          4s      <none>       desktop-worker    <none>           <none>
```

## Expose your Nginx deployment

```
kubectl apply -f svc-pod.yaml
```

```
kubectl get po,svc,deploy -o wide
NAME                                       READY   STATUS    RESTARTS   AGE     IP           NODE              NOMINATED NODE   READINESS GATES
pod/nginx-deployment-96b9d695-dmrs5        1/1     Running   0          6m33s   10.244.1.3   desktop-worker    <none>           <none>
pod/nginx-deployment-96b9d695-drlxp        1/1     Running   0          6m33s   10.244.2.2   desktop-worker2   <none>           <none>
pod/nginx-deployment-96b9d695-tf7nb        1/1     Running   0          6m33s   10.244.1.2   desktop-worker    <none>           <none>
pod/webserver-deployment-8d544b76b-454wb   2/2     Running   0          3m39s   10.244.2.3   desktop-worker2   <none>           <none>
pod/webserver-deployment-8d544b76b-56frq   2/2     Running   0          3m39s   10.244.2.4   desktop-worker2   <none>           <none>
pod/webserver-deployment-8d544b76b-r9wpr   2/2     Running   0          3m39s   10.244.1.4   desktop-worker    <none>           <none>

NAME                    TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE   SELECTOR
service/kubernetes      ClusterIP   10.96.0.1      <none>        443/TCP   43m   <none>
service/nginx-service   ClusterIP   10.96.117.66   <none>        80/TCP    12s   app=nginx

NAME                                   READY   UP-TO-DATE   AVAILABLE   AGE     CONTAINERS             IMAGES                                   SELECTOR
deployment.apps/nginx-deployment       3/3     3            3           6m33s   nginx                  nginx:latest                             app=nginx
deployment.apps/webserver-deployment   3/3     3            3           3m39s   webserver,webwatcher   nginx:latest,afakharany/watcher:latest   app=webserver
```






