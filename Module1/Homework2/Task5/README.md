### Visualize another data file with Sample application (use bind mounts & entrypoint & cmd combination)

#### Building the Docker Image
Below are the screenshots capturing the build process:

- ![Docker Build Part 1](screenshots/docker_build_1.png)

- ![Docker Build Part 2](screenshots/docker_build_2.png)

---

#### Running the Docker Container with a Custom CSV
Running the container using a bind-mounted [CSV file](new_obj_dependency_data.csv)

1. **Running the Container**  
   ![Running Container with Custom CSV](screenshots/docker_run_new.png)

2. **Webpage with the Custom CSV**  
   ![Webpage with Custom CSV](screenshots/webpage_new.png)

---

#### Running with the Default CSV
If no bind volume is provided, the container will use the default CSV file.

1. **Running the Container (Default CSV)**  
   ![Running Container with Default CSV](screenshots/docker_run_default.png)

2. **Webpage with the Default CSV**  
   ![Webpage with Default CSV](screenshots/webpage_default.png)
