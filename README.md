# case-study-1


## Task 1

#### Application

There is a Flask app under the app folder that works on port 8080.

You can find the image on this dockerhub repo.
erkanderon/basic-flask-8080-app:v1

We are dockerizing the app and then push it to the repo.

```javascript
docker build -t erkanderon/basic-flask-app:v1 .

docker push
```

#### IaC Cluster Setup

On GCP terminal we are setting up **kubectl** and **terraform** cli tools.

```javascript
gcloud components install kubectl
gcloud components install terraform
```

[Cluster Setup Reference](https://github.com/terraform-google-modules/terraform-docs-samples/tree/main/gke/quickstart/autopilot)

We will configure cluster.tf ve app.tf files taken from the reference.

I dont want to enable ipv6 so i configure it to use just ipv4.

**cluster.tf**
```javascript
enable_ula_internal_ipv6 = false
stack_type = "IPV4_ONLY"
location = "europe-west3"
```

For application part we added replica count and changed the image reference. Also we have another configuration for disabling ipv6.

**app.tf**
```javascript
image = "erkanderon/basic-flask-8080-app:v1"
replicas = "2"
ip_family_policy = "SingleStack"
```

After the configuration we can upload tf files to terminal. Then we will run terraform to apply it.

```javascript
terraform init
terraform apply
```



## Task 2

For this task, I choosed a project which is have an test in it.

[Project](https://github.com/ubc/flask-sample-app/tree/main)

Jenkinsfile is tested under a Jenkins machine and succesfully finished.



## Task 3

In this task I developed a python script that can handle stop or start actions on the compute instance.

Here you can find the usage

```javascript
python up-or-down-compute-instance.py 
    --project project_id 
    --zone zone 
    --instance instanceid 
    --operation (start|stop)
```

  