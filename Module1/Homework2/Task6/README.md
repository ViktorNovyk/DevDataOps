### Run 2 containers with volume and prove data sharing

This example demonstrates sharing a file between two containers using a Docker volume.

I used an Alpine Docker image to run a minimal container with a mounted volume.  
Inside that container, I created a file named `sharing_file.txt` in the volume.

Next, I ran another instance of the same image and mounted the same volume to it.  
The second container was able to access the file created by the first container, confirming that the volume works as intended.

You can see the outcome in the screenshot below:

![Sharing a file](screenshots/file-sharing-flow.png)