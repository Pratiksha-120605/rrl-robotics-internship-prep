
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
