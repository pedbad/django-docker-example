# django-docker-example
A starter project using Django, Docker and PostgreSQL
See the full tutorial here:
[https://pedbad.hashnode.dev/django-docker-and-postgresql](https://pedbad.hashnode.dev/django-docker-and-postgresql).

After cloning or downloading the repository to your local machine:

1. Install Docker: Ensure that Docker is installed on your machine. You can download and install Docker from the official Docker website: [https://www.docker.com/get-started](https://www.docker.com/get-started).

2. Navigate to the project directory: Open a terminal or command prompt and navigate to the directory where you have cloned or downloaded the project.

3. Build the Docker image: Run the following command to build the Docker image for the Django app:

   ```
   docker build -t django-docker-example .
   ```

   This command builds the Docker image using the provided Dockerfile in the project directory.

4. Run the Docker container: Execute the following command to run the Docker container:

   ```
   docker run -p 8000:8000 django-docker-example
   ```

   This command starts the Docker container and maps port 8000 of the container to port 8000 of the local machine.

5. Access the Django app: Open a web browser and navigate to `http://localhost:8000` to access the Django app running inside the Docker container.

Additionally, in the README file of the repository, you can include the following instructions:



- Docker Hub image: If you prefer to use the pre-built Docker image from Docker Hub, you can pull it using the following command:

   ```
   docker pull pedbad/django-docker-example
   ```

   This command pulls the Docker image for the Django app from the Docker Hub repository.

- Docker Compose: If you want to use Docker Compose for managing the app and the database, a `docker-compose.yml` file is provided in the repository. You can run the app and the database together using the following command:

   ```
   docker-compose up
   ```

   This command starts the containers defined in the `docker-compose.yml` file.


