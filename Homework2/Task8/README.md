## Multistage Docker Build

I created a simple Java 25 application with a compact `main` method to try out a multistage Docker build.

The Dockerfile is split into two stages:

1. **Build stage:**  
   I used a JDK-based image to compile the application with `javac`.
2. **Runtime stage:**  
   I switched to a lightweight JRE-based image, copied the compiled `.class` file from the first stage, and set it as the entrypoint.

This way, the final image is smaller and contains only what’s needed to run the application.

### The app
- Source code: [MultiStageApp.java](./sample-app/MultiStageApp.java)
- Dockerfile: [Dockerfile](./sample-app/Dockerfile)

### Build Result
I pushed the resulting image to Docker Hub:  
[Image on Docker Hub](https://hub.docker.com/repository/docker/intatl/ucu-dev-data-ops-hw2-t8/general)

---

### Running the Container
The container can be run with:

```bash
docker run intatl/ucu-dev-data-ops-hw2-t8:n8
```
