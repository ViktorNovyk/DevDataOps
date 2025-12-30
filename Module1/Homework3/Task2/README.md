# Convert a chatbot from docker-compose to Kubernetes


## Overview

This project demonstrates the conversion of the chatbot created on the previous homework but run on Kubernetes.

## Screenshots

- Running k8s objects
![screenshot1](screenshots/screenshot1.png)

- Running application
![screenshot2](screenshots/screenshot2.png)

## Deployment Files

The Kubernetes deployment consists of **2 main configuration files**:

| File                             | Description                       |
|----------------------------------|-----------------------------------|
| [ollama.yaml](k8s/ollama.yaml) | Ollama deployment configuration   |
| [app.yaml](k8s/app.yaml)       | Chatbot application configuration |

 After the deployment is complete, it's necessary to run the following command to pull smollm2 model.
```shell
curl -fsS -X POST http://localhost:30001/api/pull -H Content-Type: application/json -d "{\"name\":\"smollm2:135m\"}"
```
30001 is used as a static port for the ollama service.

---

## Ollama Deployment (`ollama.yaml`)

- **Deployment**
    - Persistent volume claim included to cache-loaded models
- **Service Exposure**
    - NodePort service type for localhost access with a static port 30001

---

## Spring Boot Application (`app.yaml`)

- **ConfigMap**
    - Ollama connection URL configuration
- **Application Deployment**
    - Uses ConfigMap 
- **Service Exposure**
    - NodePort service type for localhost access and static port 30002

