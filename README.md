# Intelligent Translations System

# Local Setup for development
  - Clone the repository from the github.
  - Create python env for the project.
  - Create Env outside of this repo, since this is specific to your system.
  - Creating Env one folder back of this repository.

      `cd ..`

      `python3 -m venv .`

      `source bin/activate`

  - Install all the packages, navigate to your clone repo.

      `pip3 install -r ./src/requirements.txt`

  - Run the python application

      `python3 src/app.py`

  - Test

    `GET http://localhost:8080/translate?text=Hello&source_lang=en&target_lang=hi`

  - To stop and deactive the Env

      `use ctrl + c`

      `deactive`


# Use of docker for local setup
  - Use below command to create docker image

    `docker build -t flask-translate-app .`

  - Run the docker container

    `docker run -p 8080:8080 flask-translate-app`

  - Test

    `GET http://localhost:8080/translate?text=Hello&source_lang=en&target_lang=hi`