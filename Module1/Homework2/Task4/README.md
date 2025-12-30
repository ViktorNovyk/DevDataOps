## Run Sample Application in docker container

### Attempt with `Dockerfile-cmd-shell`
Initially, I tried to build and run the Docker image using [Dockerfile-cmd-shell](sample-app/Dockerfile-cmd-shell) but encountered the following issue:

![Build Failure](screenshots/Dockerfile-cmd-shell-failure.png)

---

### Successful Build with `Dockerfile`
I switched to using the standard [Dockerfile](sample-app/Dockerfile), which worked successfully.

#### Build Process
Below are the screenshots capturing the build process:

- ![Build – Part 1](screenshots/docker_build_1.png)
- ![Build – Part 2](screenshots/docker_build_2.png)
- ![Build – Part 3](screenshots/docker_build_3.png)

---

### Running the App
After successfully building the image, I proceeded to run the container.

#### Run Process
- ![Docker Run](screenshots/docker_run.png)

#### Webpage Access
- ![Webpage View](screenshots/webpage.png)
