# Kubernetes-Orchestrated Flask Application

A REST API built with Flask, containerized with a secure multi-stage Docker build, and orchestrated on Kubernetes. The project demonstrates CI/CD readiness with health checks, unit tests, and Kubernetes manifests for deployment, internal networking, and external routing.

## Features
* **Secure containerization:** Multi-stage Docker build on `python:3.12-slim` that minimizes image size, applies OS-level security patches, and runs as a non-root user.
* **Kubernetes orchestration:** Deployment with resource requests/limits and multiple replicas for availability.
* **Traffic routing:** Internal networking via ClusterIP and external routing through an NGINX Ingress controller.
* **Reliability:** API unit tests (`pytest`), Docker health checks, and Kubernetes readiness/liveness probes.

## Technologies Used
* **Application:** Python, Flask, Gunicorn
* **Containerization:** Docker
* **Orchestration:** Kubernetes (Deployment, Service, Ingress)
* **Routing:** NGINX Ingress Controller

## Getting Started

### Prerequisites
* Docker installed locally
* A Kubernetes cluster (Minikube, kind, or a cloud provider) with NGINX Ingress enabled
* `kubectl` configured for your cluster

### Local Testing
1. Install dependencies:
```bash
   pip install -r requirements.txt
```
2. Run the tests:
```bash
   pytest test_main.py
```
3. Run the application:
```bash
   python main.py
```
   The API will be available at http://localhost:5000.

### Kubernetes Deployment
1. Build the Docker image:
```bash
   docker build -t shrrut/flask-cicd-demo:latest .
```
2. Make the image available to your cluster:
```bash
   # Cloud cluster: push to a registry
   docker push shrrut/flask-cicd-demo:latest
   # Minikube: load it directly
   minikube image load shrrut/flask-cicd-demo:latest
   # kind: load it directly
   kind load docker-image shrrut/flask-cicd-demo:latest
```
3. Apply the manifests:
```bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   kubectl apply -f ingress.yaml
```
4. Map the Ingress host to your cluster's IP in `/etc/hosts`:
```text
   127.0.0.1 flask-demo.local
```
   On Minikube, use the output of `minikube ip` instead of `127.0.0.1` (or run `minikube tunnel` with the Docker driver).
5. Open http://flask-demo.local in a browser, or use `curl http://flask-demo.local`.
