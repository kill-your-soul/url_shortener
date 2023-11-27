# URL Shortener
POC for a URL shortener service

## Prerequisites
1. [Git](https://git-scm.com/)
2. [Python 3.8+](https://www.python.org/downloads/)
3. [Poetry](https://python-poetry.org/docs/#installation)

## Installation

1. Clone the repo
   ```shell
   git clone https://github.com/kill-your-soul/url-shortener.git
   ```

2. Install dependencies
   ```shell
   poetry install
   ```

3. Setting environment variables
   - For Windows:
        
        + Powershell:
            ```powershell
            $env:SECRET_KEY="your_secret_key"
            ```

        + cmd:
            ```cmd
            set SECRET_KEY="your_secret_key"
            ```

    - for Linux, MacOS:

        + Bash

            ```shell
            export SECRET_KEY="your_secret_key"
            ```

4. Run the app
    ```shell
    poetry run python manage.py makemigrations
    poetry run python manage.py migrate
    poetry run python manage.py createsuperuser
    poetry run python manage.py runserver
    ```