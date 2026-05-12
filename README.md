# Birthday Reminder Application Deployment on DigitalOcean Kubernetes

## Project Overview

This project demonstrates the deployment of a scalable and cost-optimized web application using Docker and Kubernetes on DigitalOcean Kubernetes Service (DOKS).

The application is a Flask-based Birthday Reminder web application connected to a managed PostgreSQL database hosted on DigitalOcean.

The deployment includes:

Docker containerization
Kubernetes deployment
Load balancing using DigitalOcean Load Balancer
Horizontal Pod Autoscaling (HPA)
Managed PostgreSQL database
Resource optimization for cost efficiency

---

# Architecture

## High-Level Architecture

User Request
↓
DigitalOcean Load Balancer
↓
Kubernetes Service
↓
Flask Application Pods (Replicas)
↓
Managed PostgreSQL Database

---

# Technologies Used

| Technology                     | Purpose                    |
| ------------------------------ | -------------------------- |
| Flask                          | Web Application            |
| Docker                         | Containerization           |
| Kubernetes                     | Container Orchestration    |
| DigitalOcean Kubernetes        | Managed Kubernetes Cluster |
| PostgreSQL                     | Managed Database           |
| Docker Hub                     | Container Image Registry   |
| kubectl                        | Kubernetes CLI             |
| doctl                          | DigitalOcean CLI           |

---

# Project Structure

```bash
birthday-reminder-app/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── templates/
│   └── index.html
│
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── hpa.yaml
│
└── README.md
```

---

# Step-by-Step Setup Guide

## Step 1 — Clone Repository

```bash
git clone <your-github-repository-url>
cd birthday-reminder-app
```

---

# Step 2 — Create DigitalOcean PostgreSQL Database

1. Login to DigitalOcean Dashboard
2. Navigate to Databases
3. Create PostgreSQL Database Cluster
4. Select smallest available plan for cost optimization
5. Save the following credentials:

Host
Database Name
Username
Password
Port

---

# Step 3 — Create Contacts Table

Connect using DBeaver or PostgreSQL client and run:

```sql
CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birthday DATE
);
```

Insert sample data:

```sql
INSERT INTO contacts (first_name, last_name, birthday)
VALUES ('Alice', 'Smith', '1990-05-15');

INSERT INTO contacts (first_name, last_name, birthday)
VALUES ('Bob', 'Johnson', '1985-11-23');

INSERT INTO contacts (first_name, last_name, birthday)
VALUES ('Charlie', 'Brown', '2000-01-10');
```

---

# Step 4 — Build Docker Image

```bash
docker build -t birthday-app .
```

---

# Step 5 — Push Docker Image to Docker Hub

Login to Docker:

```bash
docker login
```

Tag image:

```bash
docker tag birthday-app kajalkanchan/birthday-app:v1
```

Push image:

```bash
docker push kajalkanchan/birthday-app:v1
```

---

# Step 6 — Create Kubernetes Cluster

1. Open DigitalOcean Dashboard
2. Navigate to Kubernetes
3. Create Cluster
4. Configuration Used:

| Configuration | Value  |
| ------------- | ------ |
| Nodes         | 1      |
| CPU           | 1 vCPU |
| RAM           | 2 GB   |
| Storage       | 50 GB  |

This setup was intentionally selected to optimize infrastructure cost for a lightweight application workload.

---

# Step 7 — Install Kubernetes Tools

Install:

kubectl
doctl

Verify installation:

```bash
kubectl version --client
```

```bash
doctl version
```

---

# Step 8 — Authenticate DigitalOcean CLI

Generate API token from DigitalOcean Dashboard.

Authenticate:

```bash
doctl auth init
```

Connect Kubernetes cluster:

```bash
doctl kubernetes cluster kubeconfig save <cluster-name>
```

Verify:

```bash
kubectl get nodes
```

---

# Step 9 — Kubernetes Deployment Files

## deployment.yaml

Responsible for:

Creating application pods
Managing replicas
Injecting database environment variables
Defining resource requests and limits

## service.yaml

Responsible for:

Exposing application publicly
Creating DigitalOcean Load Balancer
Routing traffic to application pods

## hpa.yaml

Responsible for:

Horizontal Pod Autoscaling
Scaling pods based on CPU usage

---

# Step 10 — Deploy Application to Kubernetes

Apply Kubernetes manifests:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml
```

Verify deployment:

```bash
kubectl get pods
kubectl get svc
kubectl get hpa
```

---

# Accessing the Application

Retrieve external IP:

```bash
kubectl get svc
```

Open browser:

```bash
http://<external-ip>
```

---

# Horizontal Pod Autoscaling

The application uses Kubernetes Horizontal Pod Autoscaler (HPA).

Configuration:

| Setting       | Value |
| ------------- | ----- |
| Minimum Pods  | 2     |
| Maximum Pods  | 5     |
| CPU Threshold | 50%   |

Benefits:

Automatically scales during increased traffic
Improves application performance
Prevents unnecessary resource consumption
Reduces operational cost

---

# Cost Optimization Strategy

The following optimizations were implemented:

## Minimal Cluster Size

Used a small Kubernetes node configuration:

1 Node
1 vCPU
2 GB RAM

This avoids unnecessary infrastructure costs.

## Horizontal Pod Autoscaling

Pods scale dynamically based on CPU utilization instead of keeping large static infrastructure.

## Managed PostgreSQL

Used smallest managed PostgreSQL instance suitable for current workload.

## Resource Limits

CPU and memory limits were configured in deployment.yaml to prevent resource overconsumption.

---

# Reliability and High Availability

The deployment improves reliability using:

Multiple application pod replicas
Kubernetes self-healing capabilities
Load balancing across pods
Managed PostgreSQL database
Automatic pod restarts on failure



# Cleanup

To avoid ongoing cloud charges:

Delete Kubernetes resources:

```bash
kubectl delete -f k8s/
```

Delete:

* Kubernetes Cluster
* PostgreSQL Database
* Load Balancer

from DigitalOcean Dashboard.

---

# Conclusion

This project demonstrates a scalable, reliable, and cost-efficient Kubernetes deployment using DigitalOcean managed services.

Key outcomes:

* Successfully containerized and deployed a web application
* Implemented Kubernetes orchestration
* Enabled autoscaling and load balancing
* Optimized infrastructure cost
* Built a production-style cloud-native deployment architecture
