# Guide to getting Ray running on your local cluster.

This is a step by step guild setting a local cluster setup to develop ray app.

The job submission is through ray client instead of K8S job.

## Installation

### K8S cluster setup

On producttion enviroment K8S cluster is usually set up by your infra guy. In dev environement, we need a cluster to start with. `minikube` is a good option. Here is the guide of installing [minikube](https://minikube.sigs.k8s.io/docs/start/)
One linner installation tips for Mac user:

```bash
brew install minikube
```

### Install package management

Suggest to use [heml](https://helm.sh/), and the setup guide is [here](https://helm.sh/).
One linner installation tips for Mac user:

```bash
brew install helm
```

## Boostrap

### Start minikube

Start K8S locally (for shared cluster user case, this is not necessary)

make sure the local cluster with sufficient resource

```bash
minikube config set cpus 6
minikube config set memory 16384
```

Start the cluster

```bash
minikube start
```

Run this in ray_cluster_demo/deploy folder according [this guide](https://docs.ray.io/en/master/cluster/kubernetes.html).

Please note, Ray and Python version both need to be matched across client and server side. We use image tag `1.4.0-py38`, that means 1.4.0 Ray version on 3.8.x Python environment, and your client code is expected to be Ray `1.4.0`. Please see the combination available on [Ray DockerHub](https://hub.docker.com/r/rayproject/ray).

```bash
> cd ray_cluster_demo/deploy/charts
> helm -n ray install ray-cluster --set image=rayproject/ray-ml:1.4.1-py38-cpu ./ray --create-namespace 
NAME: ray-cluster
LAST DEPLOYED: Fri May 14 11:44:06 2021
NAMESPACE: ray
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

If you need advanced guide please see [here](https://docs.ray.io/en/master/cluster/kubernetes-advanced.html#k8s-advanced).

### Inspect the resources, artifacts and learn

View the resource, it is called `raycluster(s)`

```bash
> kubectl -n ray get rayclusters
NAME          STATUS    RESTARTS   AGE
ray-cluster   Running   0          15m
```

View the controller (Ray Operator)

```bash
> kubectl get deployment ray-operator
NAME           READY   UP-TO-DATE   AVAILABLE   AGE
ray-operator   1/1     1            1           15m
```

View the head node and worker nodes.
```bash
> kubectl -n ray get pods
NAME                                READY   STATUS    RESTARTS   AGE
ray-cluster-ray-head-type-llts6     1/1     Running   0          54m
ray-cluster-ray-worker-type-g5ljk   1/1     Running   0          53m
ray-cluster-ray-worker-type-m8km9   1/1     Running   0          53m
```

View the service - `ray-cluster-ray-head` is the name of the service here
```bash
> kubectl -n ray get service
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP PORT(S) AGE
ray-cluster-ray-head   ClusterIP   10.106.50.170   <none>        10001/TCP,8265/TCP,8000/TCP   22m
```

### Enable port forwarding so you code can talk to head node.

Port forwading to make sure local (dev box) can access the node
service name `ray-cluster-ray-head` as shown above.

Respectively, `8265` is the dashboard port and `10001` is the RPC port.

```bash
kubectl -n ray port-forward service/ray-cluster-ray-head 8265:8265 10001:10001 8000:8000

Forwarding from 127.0.0.1:8265 -> 8265
Forwarding from [::1]:8265 -> 8265
Forwarding from 127.0.0.1:10001 -> 10001
Forwarding from [::1]:10001 -> 10001
...
... more logs
...

```

### Run the job!

```bash
> ./pants run ray_cluster_demo::
Iteration 0
Counter({('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-worker-type-nh2ms'): 33, ('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-head-type-bhpwg'): 23, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-worker-type-wntp4'): 11, ('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-worker-type-wntp4'): 11, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-head-type-bhpwg'): 10, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-worker-type-nh2ms'): 9, ('ray-cluster-ray-worker-type-wntp4', 'ray-cluster-ray-worker-type-wntp4'): 3})
Iteration 1
Counter({('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-head-type-bhpwg'): 29, ('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-worker-type-wntp4'): 18, ('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-worker-type-nh2ms'): 14, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-worker-type-nh2ms'): 13, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-head-type-bhpwg'): 9, ('ray-cluster-ray-worker-type-wntp4', 'ray-cluster-ray-head-type-bhpwg'): 8, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-worker-type-wntp4'): 8, ('ray-cluster-ray-worker-type-wntp4', 'ray-cluster-ray-worker-type-nh2ms'): 1})
Iteration 2
Counter({('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-head-type-bhpwg'): 30, ('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-worker-type-nh2ms'): 20, ('ray-cluster-ray-worker-type-wntp4', 'ray-cluster-ray-head-type-bhpwg'): 11, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-worker-type-wntp4'): 10, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-head-type-bhpwg'): 9, ('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-worker-type-wntp4'): 8, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-worker-type-nh2ms'): 5, ('ray-cluster-ray-worker-type-wntp4', 'ray-cluster-ray-worker-type-wntp4'): 4, ('ray-cluster-ray-worker-type-wntp4', 'ray-cluster-ray-worker-type-nh2ms'): 3})
Iteration 3
Counter({('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-head-type-bhpwg'): 33, ('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-head-type-bhpwg'): 25, ('ray-cluster-ray-worker-type-wntp4', 'ray-cluster-ray-head-type-bhpwg'): 13, ('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-worker-type-wntp4'): 9, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-worker-type-nh2ms'): 6, ('ray-cluster-ray-worker-type-wntp4', 'ray-cluster-ray-worker-type-wntp4'): 5, ('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-worker-type-nh2ms'): 4, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-worker-type-wntp4'): 4, ('ray-cluster-ray-worker-type-wntp4', 'ray-cluster-ray-worker-type-nh2ms'): 1})
Iteration 4
Counter({('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-head-type-bhpwg'): 25, ('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-worker-type-nh2ms'): 20, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-head-type-bhpwg'): 14, ('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-worker-type-wntp4'): 11, ('ray-cluster-ray-worker-type-wntp4', 'ray-cluster-ray-head-type-bhpwg'): 9, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-worker-type-wntp4'): 8, ('ray-cluster-ray-worker-type-wntp4', 'ray-cluster-ray-worker-type-wntp4'): 5, ('ray-cluster-ray-worker-type-wntp4', 'ray-cluster-ray-worker-type-nh2ms'): 4, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-worker-type-nh2ms'): 4})
Iteration 5
Counter({('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-head-type-bhpwg'): 27, ('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-worker-type-nh2ms'): 19, ('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-worker-type-wntp4'): 15, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-head-type-bhpwg'): 11, ('ray-cluster-ray-worker-type-wntp4', 'ray-cluster-ray-head-type-bhpwg'): 11, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-worker-type-wntp4'): 6, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-worker-type-nh2ms'): 6, ('ray-cluster-ray-worker-type-wntp4', 'ray-cluster-ray-worker-type-wntp4'): 3, ('ray-cluster-ray-worker-type-wntp4', 'ray-cluster-ray-worker-type-nh2ms'): 2})
Iteration 6
Counter({('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-head-type-bhpwg'): 25, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-head-type-bhpwg'): 20, ('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-worker-type-nh2ms'): 18, ('ray-cluster-ray-worker-type-wntp4', 'ray-cluster-ray-head-type-bhpwg'): 10, ('ray-cluster-ray-head-type-bhpwg', 'ray-cluster-ray-worker-type-wntp4'): 10, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-worker-type-wntp4'): 7, ('ray-cluster-ray-worker-type-wntp4', 'ray-cluster-ray-worker-type-nh2ms'): 5, ('ray-cluster-ray-worker-type-wntp4', 'ray-cluster-ray-worker-type-wntp4'): 3, ('ray-cluster-ray-worker-type-nh2ms', 'ray-cluster-ray-worker-type-nh2ms'): 2})
.....
```

DONE!

Bonus, you can also run ray_burst on the cluster (Assume the remote port is 10001).
If OOM is experienced, you can adjust `deploy/charts/values.yaml` where you satrted the 

```bash
./pants run ray_demo:: -- -p 10001
```

## Uninstall

```bash
> helm -n ray uninstall ray-cluster
release "ray-cluster" uninstalled
```
