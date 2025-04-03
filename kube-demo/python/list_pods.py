from kubernetes import client, config

def list_running_pods(namespace="default"):
    # Load kubeconfig from default location (~/.kube/config)
    config.load_kube_config()

    # Initialize CoreV1Api to interact with core Kubernetes resources (pods, services, etc.)
    v1 = client.CoreV1Api()
    
    # Fetch all Pods in the given namespace
    pods = v1.list_namespaced_pod(namespace=namespace)

    # Print only the pods that are in 'Running' status
    print(f"Running Pods in namespace: {namespace}")
    for pod in pods.items:
        if pod.status.phase == "Running":
            print(f" - {pod.metadata.name}")

if __name__ == "__main__":
    list_running_pods()
