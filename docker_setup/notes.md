
## Understood the role of Docker in creating reproducible ROS2 environments


## Docker Setup

Docker was installed on Ubuntu 22.04 using the official Docker documentation.

Reference:
https://docs.docker.com/engine/install/ubuntu/

### Steps followed
- Added Docker official GPG key
- Added Docker APT repository
- Installed Docker Engine and Docker CLI
- Verified installation using `docker run hello-world`
- Configured Docker to run without sudo

## Docker + ROS2

- Installed Docker using official documentation
- Pulled official ROS2 Humble Docker image
- Ran ROS2 inside a Docker container
- Verified ROS2 commands inside container

## Docker Notes

- Learned basic Docker image and container commands
- Faced Docker socket permission issue
- Resolved by adding user to docker group
- Verified Docker commands without sudo

## Docker Commands (Practiced)

### Image Management
docker image ls  
docker image pull ros:humble  
docker image rm  

### Container Management
docker run -it ros:humble bash  
docker container ls  
docker container stop  
docker container start  
docker container rm  

### Container Interaction
docker exec -it <container_name> bash  

### File Sharing
docker run -it -v ~/ros2_ws:/ros2_ws ros:humble bash  

### Dockerfile
FROM ros:humble  
RUN apt update && apt install -y <package>  
COPY . /workspace  
